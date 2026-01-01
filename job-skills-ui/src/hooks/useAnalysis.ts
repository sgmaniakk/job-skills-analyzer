import { useState } from 'react';
import { analyzeJob, analyzeBatch } from '../api/analysis';
import type { AnalysisResponse, JobInput, BatchAnalysisResponse } from '../types/analysis';

export const useAnalysis = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<AnalysisResponse | null>(null);
  const [batchResult, setBatchResult] = useState<BatchAnalysisResponse | null>(null);

  const analyze = async (jobData: JobInput) => {
    setLoading(true);
    setError(null);
    setBatchResult(null);

    try {
      const response = await analyzeJob(jobData);
      setResult(response);
      return response;
    } catch (err) {
      const errorMessage = err instanceof Error
        ? err.message
        : 'Failed to analyze job description';
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const analyzeBatchJobs = async (jobs: JobInput[]) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await analyzeBatch(jobs);
      setBatchResult(response);
      return response;
    } catch (err) {
      const errorMessage = err instanceof Error
        ? err.message
        : 'Failed to analyze job descriptions';
      setError(errorMessage);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const reset = () => {
    setResult(null);
    setBatchResult(null);
    setError(null);
  };

  return { analyze, analyzeBatchJobs, loading, error, result, batchResult, reset };
};
