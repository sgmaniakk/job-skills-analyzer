import { useState } from 'react';
import type { JobInput } from '../../types/analysis';

interface UnifiedJobUploaderProps {
  onAnalyze: (jobs: JobInput[]) => void;
  loading: boolean;
}

interface JobEntry {
  id: string;
  title: string;
  jobDescription: string;
}

export const UnifiedJobUploader = ({ onAnalyze, loading }: UnifiedJobUploaderProps) => {
  const [jobs, setJobs] = useState<JobEntry[]>([
    { id: '1', title: '', jobDescription: '' },
  ]);
  const [error, setError] = useState('');

  const addJob = () => {
    const newId = (Math.max(...jobs.map(j => parseInt(j.id))) + 1).toString();
    setJobs([...jobs, { id: newId, title: '', jobDescription: '' }]);
  };

  const removeJob = (id: string) => {
    if (jobs.length > 1) {
      setJobs(jobs.filter(job => job.id !== id));
    }
  };

  const updateJob = (id: string, field: 'title' | 'jobDescription', value: string) => {
    setJobs(jobs.map(job =>
      job.id === id ? { ...job, [field]: value } : job
    ));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Validation
    const validJobs = jobs.filter(job => job.jobDescription.trim().length >= 50);

    if (validJobs.length === 0) {
      setError('Job description must be at least 50 characters long');
      return;
    }

    if (validJobs.length < jobs.length) {
      setError(`${jobs.length - validJobs.length} job description(s) were skipped (too short)`);
    } else {
      setError('');
    }

    // Convert to JobInput format
    const jobInputs: JobInput[] = validJobs.map(job => ({
      job_description: job.jobDescription,
      title: job.title.trim() || undefined,
    }));

    onAnalyze(jobInputs);
  };

  const handleClear = () => {
    setJobs([
      { id: '1', title: '', jobDescription: '' },
    ]);
    setError('');
  };

  const validJobCount = jobs.filter(j => j.jobDescription.trim().length >= 50).length;
  const buttonText = validJobCount === 1 ? 'Analyze Job' : `Analyze ${validJobCount} Jobs`;

  return (
    <div className="w-full max-w-6xl mx-auto">
      <div className="bg-white rounded-lg shadow-md p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-4">
          Analyze Job Description{jobs.length > 1 ? 's' : ''}
        </h2>
        <p className="text-gray-600 mb-6">
          {jobs.length === 1
            ? 'Paste a job description to extract and analyze required technical skills using NLP.'
            : 'Compare multiple job descriptions to find common skills across positions.'}
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          {jobs.map((job, index) => (
            <div key={job.id} className="border border-gray-200 rounded-lg p-4 bg-gray-50">
              <div className="flex justify-between items-center mb-3">
                <h3 className="text-lg font-semibold text-gray-700">
                  {jobs.length === 1 ? 'Job Description' : `Job Description #${index + 1}`}
                </h3>
                {jobs.length > 1 && (
                  <button
                    type="button"
                    onClick={() => removeJob(job.id)}
                    disabled={loading}
                    className="text-red-600 hover:text-red-800 text-sm font-medium disabled:opacity-50"
                  >
                    Remove
                  </button>
                )}
              </div>

              <div className="space-y-3">
                {/* Job Title */}
                <div>
                  <label
                    htmlFor={`title-${job.id}`}
                    className="block text-sm font-medium text-gray-700 mb-1"
                  >
                    Job Title (Optional)
                  </label>
                  <input
                    type="text"
                    id={`title-${job.id}`}
                    value={job.title}
                    onChange={(e) => updateJob(job.id, 'title', e.target.value)}
                    placeholder="e.g., Senior Full Stack Developer"
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent text-sm"
                    disabled={loading}
                  />
                </div>

                {/* Job Description */}
                <div>
                  <label
                    htmlFor={`description-${job.id}`}
                    className="block text-sm font-medium text-gray-700 mb-1"
                  >
                    Job Description <span className="text-red-500">*</span>
                  </label>
                  <textarea
                    id={`description-${job.id}`}
                    value={job.jobDescription}
                    onChange={(e) => updateJob(job.id, 'jobDescription', e.target.value)}
                    placeholder="Paste the full job description here..."
                    rows={jobs.length === 1 ? 12 : 8}
                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none text-sm"
                    disabled={loading}
                  />
                  <p className="text-xs text-gray-500 mt-1">
                    {job.jobDescription.length} characters (minimum 50 required)
                  </p>
                </div>
              </div>
            </div>
          ))}

          {/* Add Job Button */}
          <button
            type="button"
            onClick={addJob}
            disabled={loading || jobs.length >= 10}
            className="w-full py-3 border-2 border-dashed border-gray-300 text-gray-600 rounded-md font-medium hover:border-blue-500 hover:text-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            + Add Another Job to Compare {jobs.length >= 10 && '(Max 10)'}
          </button>

          {/* Error Message */}
          {error && (
            <div className="bg-yellow-50 border border-yellow-200 text-yellow-800 px-4 py-3 rounded-md text-sm">
              {error}
            </div>
          )}

          {/* Buttons */}
          <div className="flex gap-3">
            <button
              type="submit"
              disabled={loading || validJobCount === 0}
              className="flex-1 bg-blue-600 text-white px-6 py-3 rounded-md font-medium hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
            >
              {loading ? (
                <span className="flex items-center justify-center gap-2">
                  <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                    <circle
                      className="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      strokeWidth="4"
                      fill="none"
                    />
                    <path
                      className="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                    />
                  </svg>
                  Analyzing...
                </span>
              ) : (
                buttonText
              )}
            </button>

            <button
              type="button"
              onClick={handleClear}
              disabled={loading}
              className="px-6 py-3 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 disabled:bg-gray-100 disabled:cursor-not-allowed transition-colors"
            >
              Clear
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
