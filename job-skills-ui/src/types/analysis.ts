export interface Skill {
  id: string;
  name: string;
  count: number;
  category: string;
  confidence: number;
}

export interface AnalysisResponse {
  id: string;
  title?: string;
  analyzed_at: string;
  skills: Skill[];
  total_skills_found: number;
  categories: Record<string, number>;
}

export interface JobInput {
  job_description: string;
  title?: string;
}

export interface AggregatedSkill {
  name: string;
  total_count: number;
  appeared_in_jobs: number;
  percentage: number;
  category: string;
}

export interface BatchAnalysisResponse {
  id: string;
  analyzed_at: string;
  total_jobs: number;
  aggregated_skills: AggregatedSkill[];
  individual_analyses: AnalysisResponse[];
  top_skills: AggregatedSkill[];
  category_breakdown: Record<string, number>;
}
