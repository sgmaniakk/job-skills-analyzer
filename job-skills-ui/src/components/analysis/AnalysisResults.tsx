import { AnalysisResponse } from '../../types/analysis';
import { SkillsBarChart } from './SkillsBarChart';
import { SkillsPieChart } from './SkillsPieChart';
import { SkillsTable } from './SkillsTable';

interface Props {
  analysis: AnalysisResponse;
  onReset: () => void;
}

export const AnalysisResults = ({ analysis, onReset }: Props) => {
  const downloadJSON = () => {
    const dataStr = JSON.stringify(analysis, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `skills-analysis-${analysis.id}.json`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="w-full max-w-7xl mx-auto space-y-6">
      {/* Header */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex justify-between items-start">
          <div>
            <h2 className="text-2xl font-bold text-gray-800">
              {analysis.title || 'Job Analysis Results'}
            </h2>
            <p className="text-gray-600 mt-1">
              Analyzed on {new Date(analysis.analyzed_at).toLocaleString()}
            </p>
            <div className="mt-4 flex gap-4">
              <div className="bg-blue-50 px-4 py-2 rounded-md">
                <p className="text-sm text-gray-600">Total Skills Found</p>
                <p className="text-2xl font-bold text-blue-600">
                  {analysis.total_skills_found}
                </p>
              </div>
              <div className="bg-green-50 px-4 py-2 rounded-md">
                <p className="text-sm text-gray-600">Categories</p>
                <p className="text-2xl font-bold text-green-600">
                  {Object.keys(analysis.categories).length}
                </p>
              </div>
            </div>
          </div>
          <div className="flex gap-2">
            <button
              onClick={downloadJSON}
              className="px-4 py-2 border border-gray-300 text-gray-700 rounded-md font-medium hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 transition-colors"
            >
              Download JSON
            </button>
            <button
              onClick={onReset}
              className="px-4 py-2 bg-blue-600 text-white rounded-md font-medium hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 transition-colors"
            >
              Analyze Another Job
            </button>
          </div>
        </div>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <SkillsBarChart skills={analysis.skills} limit={15} />
        <SkillsPieChart categories={analysis.categories} />
      </div>

      {/* Table Section */}
      <SkillsTable skills={analysis.skills} />
    </div>
  );
};
