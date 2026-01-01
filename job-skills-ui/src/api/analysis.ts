import { apiClient } from './client';
import type { AnalysisResponse, JobInput, BatchAnalysisResponse, FetchJobResponse } from '../types/analysis';

export const analyzeJob = async (jobData: JobInput): Promise<AnalysisResponse> => {
  const response = await apiClient.post<AnalysisResponse>(
    '/api/v1/analysis/analyze',
    jobData
  );
  return response.data;
};

export const analyzeBatch = async (jobs: JobInput[]): Promise<BatchAnalysisResponse> => {
  const response = await apiClient.post<BatchAnalysisResponse>(
    '/api/v1/analysis/batch',
    { jobs }
  );
  return response.data;
};

export const fetchJobFromUrl = async (url: string): Promise<FetchJobResponse> => {
  const response = await apiClient.post<FetchJobResponse>(
    '/api/v1/analysis/fetch-job',
    { url }
  );
  return response.data;
};
