import { useState } from 'react';
import { UnifiedJobUploader } from './components/upload/UnifiedJobUploader';
import { AnalysisResults } from './components/analysis/AnalysisResults';
import { BatchAnalysisResults } from './components/analysis/BatchAnalysisResults';
import { useAnalysis } from './hooks/useAnalysis';
import type { JobInput } from './types/analysis';

function App() {
  const { analyze, analyzeBatchJobs, loading, error, result, batchResult, reset } = useAnalysis();
  const [showResults, setShowResults] = useState(false);

  const handleAnalyze = async (jobs: JobInput[]) => {
    try {
      // If only one job, use single analysis endpoint
      if (jobs.length === 1) {
        await analyze(jobs[0]);
      } else {
        // If multiple jobs, use batch analysis endpoint
        await analyzeBatchJobs(jobs);
      }
      setShowResults(true);
    } catch (err) {
      console.error('Analysis failed:', err);
    }
  };

  const handleReset = () => {
    reset();
    setShowResults(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                Job Skills Analyzer
              </h1>
              <p className="mt-1 text-sm text-gray-600">
                Extract and analyze technical skills from job descriptions using NLP
              </p>
            </div>
            <div className="flex items-center gap-2">
              <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
                Powered by spaCy NLP
              </span>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8 sm:px-6 lg:px-8">
        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-md">
            <p className="font-medium">Error</p>
            <p className="text-sm">{error}</p>
          </div>
        )}

        {!showResults ? (
          <UnifiedJobUploader onAnalyze={handleAnalyze} loading={loading} />
        ) : result ? (
          <AnalysisResults analysis={result} onReset={handleReset} />
        ) : batchResult ? (
          <BatchAnalysisResults result={batchResult} onReset={handleReset} />
        ) : null}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 mt-12">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <p className="text-center text-sm text-gray-500">
            Built with FastAPI, spaCy, React, and TypeScript
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
