import React, { useState, useEffect } from 'react';
import { getUserStats } from '../api/pokemonApi';

const Stats = ({ username }) => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        setLoading(true);
        const data = await getUserStats(username);
        setStats(data);
      } catch (error) {
        console.error('Error fetching stats:', error);
      } finally {
        setLoading(false);
      }
    };

    if (username) {
      fetchStats();
    }
  }, [username]);

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-white text-xl">Loading Stats...</div>
      </div>
    );
  }

  if (!stats) {
    return (
      <div className="text-center text-white text-xl">
        No stats available. Start catching Pokemon!
      </div>
    );
  }

  const rarityColors = {
    common: 'bg-gray-400',
    uncommon: 'bg-green-500',
    rare: 'bg-blue-500',
    epic: 'bg-purple-600',
    legendary: 'bg-yellow-500',
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-lg p-6">
        <h2 className="text-3xl font-bold text-gray-800 mb-2">Statistics</h2>
        <p className="text-gray-600 mb-6">@{stats.username}</p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-6 text-white">
            <div className="text-sm font-medium opacity-90">Total Caught</div>
            <div className="text-4xl font-bold">{stats.total_caught}</div>
          </div>
          <div className="bg-gradient-to-r from-green-500 to-green-600 rounded-lg p-6 text-white">
            <div className="text-sm font-medium opacity-90">Unique Pokemon</div>
            <div className="text-4xl font-bold">{stats.unique_pokemon}</div>
          </div>
          <div className="bg-gradient-to-r from-yellow-500 to-yellow-600 rounded-lg p-6 text-white">
            <div className="text-sm font-medium opacity-90">Coins</div>
            <div className="text-4xl font-bold">{stats.coins}</div>
          </div>
        </div>

        <h3 className="text-2xl font-bold text-gray-800 mb-4">Pokemon by Rarity</h3>
        <div className="space-y-3">
          {Object.entries(stats.rarity_counts || {}).map(([rarity, count]) => (
            <div key={rarity} className="flex items-center">
              <div className="w-32 font-medium text-gray-700 capitalize">{rarity}</div>
              <div className="flex-1 bg-gray-200 rounded-full h-8 relative overflow-hidden">
                <div
                  className={`${rarityColors[rarity]} h-full flex items-center justify-end px-3 transition-all duration-500`}
                  style={{ width: `${(count / stats.total_caught) * 100}%` }}
                >
                  <span className="text-white font-bold text-sm">{count}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Stats;
