import { useState } from 'react';
import { analyzeJob } from '../api/analysis';
import type { AnalysisResponse, JobInput } from '../types/analysis';

export const useAnalysis = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<AnalysisResponse | null>(null);

  const analyze = async (jobData: JobInput) => {
    setLoading(true);
    setError(null);

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

  const reset = () => {
    setResult(null);
    setError(null);
  };

  return { analyze, loading, error, result, reset };
};
