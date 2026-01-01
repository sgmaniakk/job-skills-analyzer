import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import { Skill } from '../../types/analysis';

interface Props {
  skills: Skill[];
  limit?: number;
}

const CATEGORY_COLORS: Record<string, string> = {
  programming_languages: '#3b82f6',
  frameworks: '#10b981',
  databases: '#f59e0b',
  cloud_platforms: '#8b5cf6',
  devops_tools: '#ef4444',
  web_technologies: '#06b6d4',
  data_science: '#ec4899',
  mobile_development: '#14b8a6',
  design_tools: '#f97316',
  methodologies: '#6366f1',
  security: '#84cc16',
  blockchain: '#a855f7',
  game_development: '#eab308',
  business_intelligence: '#22c55e',
  soft_skills: '#64748b',
  other: '#9ca3af',
};

export const SkillsBarChart = ({ skills, limit = 20 }: Props) => {
  // Sort by count and take top N
  const topSkills = [...skills]
    .sort((a, b) => b.count - a.count)
    .slice(0, limit);

  const data = topSkills.map(skill => ({
    name: skill.name,
    count: skill.count,
    fill: CATEGORY_COLORS[skill.category] || CATEGORY_COLORS.other,
    category: skill.category.replace(/_/g, ' '),
    confidence: Math.round(skill.confidence * 100),
  }));

  return (
    <div className="w-full bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-xl font-bold text-gray-800 mb-4">
        Top {limit} Skills by Frequency
      </h3>
      <div className="w-full h-96">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart
            data={data}
            margin={{ top: 20, right: 30, left: 20, bottom: 100 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              dataKey="name"
              angle={-45}
              textAnchor="end"
              height={100}
              interval={0}
              tick={{ fontSize: 12 }}
            />
            <YAxis
              label={{ value: 'Count', angle: -90, position: 'insideLeft' }}
            />
            <Tooltip
              content={({ active, payload }) => {
                if (active && payload && payload.length) {
                  const data = payload[0].payload;
                  return (
                    <div className="bg-white p-3 border border-gray-200 rounded-md shadow-lg">
                      <p className="font-semibold text-gray-800">{data.name}</p>
                      <p className="text-sm text-gray-600">
                        Count: <span className="font-medium">{data.count}</span>
                      </p>
                      <p className="text-sm text-gray-600">
                        Category: <span className="font-medium capitalize">{data.category}</span>
                      </p>
                      <p className="text-sm text-gray-600">
                        Confidence: <span className="font-medium">{data.confidence}%</span>
                      </p>
                    </div>
                  );
                }
                return null;
              }}
            />
            <Legend />
            <Bar dataKey="count" fill="#3b82f6" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};
