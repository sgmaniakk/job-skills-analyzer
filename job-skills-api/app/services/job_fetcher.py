"""
Service for fetching job descriptions from job board URLs.
"""

import httpx
from bs4 import BeautifulSoup
from typing import Dict, Optional
from urllib.parse import urlparse


class JobFetchError(Exception):
    """Custom exception for job fetching errors"""
    pass


class JobFetcher:
    """Fetch job descriptions from various job boards"""

    TIMEOUT = 10.0  # seconds

    @staticmethod
    async def fetch_job(url: str) -> Dict[str, str]:
        """
        Fetch job title and description from a job board URL.

        Args:
            url: URL to the job posting

        Returns:
            Dictionary with 'title' and 'description' keys

        Raises:
            JobFetchError: If fetching fails or URL is invalid
        """
        try:
            # Validate URL
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                raise JobFetchError("Invalid URL format")

            # Determine job board and fetch accordingly
            hostname = parsed.netloc.lower()

            if 'greenhouse.io' in hostname:
                return await JobFetcher._fetch_greenhouse(url)
            elif 'lever.co' in hostname:
                return await JobFetcher._fetch_lever(url)
            elif 'linkedin.com' in hostname:
                return await JobFetcher._fetch_linkedin(url)
            else:
                # Generic fallback
                return await JobFetcher._fetch_generic(url)

        except httpx.RequestError as e:
            raise JobFetchError(f"Network error: {str(e)}")
        except Exception as e:
            raise JobFetchError(f"Failed to fetch job: {str(e)}")

    @staticmethod
    async def _fetch_greenhouse(url: str) -> Dict[str, str]:
        """Fetch from Greenhouse job board"""
        async with httpx.AsyncClient(timeout=JobFetcher.TIMEOUT) as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title = None
            title_elem = soup.find('h1', class_='app-title')
            if title_elem:
                title = title_elem.get_text(strip=True)

            # Extract description
            description = ""
            content_div = soup.find('div', id='content')

            if content_div:
                # Remove application form sections
                for unwanted in content_div.find_all(['form', 'script', 'style']):
                    unwanted.decompose()

                # Get all text content
                description = content_div.get_text(separator='\n', strip=True)

            if not description:
                raise JobFetchError("Could not extract job description from Greenhouse page")

            return {
                'title': title or 'Job Opening',
                'description': description
            }

    @staticmethod
    async def _fetch_lever(url: str) -> Dict[str, str]:
        """Fetch from Lever job board"""
        async with httpx.AsyncClient(timeout=JobFetcher.TIMEOUT) as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract title
            title = None
            title_elem = soup.find('h2', attrs={'data-qa': 'posting-name'})
            if not title_elem:
                title_elem = soup.find('h1')
            if title_elem:
                title = title_elem.get_text(strip=True)

            # Extract description
            description = ""
            content_div = soup.find('div', class_='content')
            if not content_div:
                content_div = soup.find('div', attrs={'data-qa': 'job-description'})

            if content_div:
                # Remove unwanted elements
                for unwanted in content_div.find_all(['form', 'script', 'style', 'footer']):
                    unwanted.decompose()

                description = content_div.get_text(separator='\n', strip=True)

            if not description:
                raise JobFetchError("Could not extract job description from Lever page")

            return {
                'title': title or 'Job Opening',
                'description': description
            }

    @staticmethod
    async def _fetch_linkedin(url: str) -> Dict[str, str]:
        """Fetch from LinkedIn (note: may be restricted)"""
        # LinkedIn often requires authentication and blocks scrapers
        # This is a basic implementation that may not work reliably
        async with httpx.AsyncClient(
            timeout=JobFetcher.TIMEOUT,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
        ) as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # LinkedIn structure varies, this is best-effort
            title_elem = soup.find('h1') or soup.find('h2', class_='topcard__title')
            title = title_elem.get_text(strip=True) if title_elem else 'Job Opening'

            desc_div = soup.find('div', class_='description__text')
            if not desc_div:
                desc_div = soup.find('article')

            description = desc_div.get_text(separator='\n', strip=True) if desc_div else ""

            if not description:
                raise JobFetchError("Could not extract job description from LinkedIn (authentication may be required)")

            return {
                'title': title,
                'description': description
            }

    @staticmethod
    async def _fetch_generic(url: str) -> Dict[str, str]:
        """Generic fetcher for unknown job boards"""
        async with httpx.AsyncClient(
            timeout=JobFetcher.TIMEOUT,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
        ) as client:
            response = await client.get(url, follow_redirects=True)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Try to find title
            title = None
            for tag in ['h1', 'h2']:
                title_elem = soup.find(tag)
                if title_elem:
                    title = title_elem.get_text(strip=True)
                    break

            # Try to find main content
            description = ""
            for selector in ['main', 'article', 'div[role="main"]', 'body']:
                content = soup.select_one(selector)
                if content:
                    # Remove unwanted elements
                    for unwanted in content.find_all(['script', 'style', 'nav', 'header', 'footer']):
                        unwanted.decompose()

                    description = content.get_text(separator='\n', strip=True)
                    if description and len(description) > 100:
                        break

            if not description or len(description) < 50:
                raise JobFetchError("Could not extract sufficient job description content")

            return {
                'title': title or 'Job Opening',
                'description': description
            }
