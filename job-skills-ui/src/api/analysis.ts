import { apiClient } from './client';
import { AnalysisResponse, JobInput, BatchAnalysisResponse } from '../types/analysis';

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
