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
        <div className="flex flex-col items-center space-y-4">
          <div className="w-16 h-16 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
          <div className="text-white text-xl font-medium">Loading Stats...</div>
        </div>
      </div>
    );
  }

  if (!stats) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-4">
        <div className="text-6xl opacity-50">📊</div>
        <div className="text-center text-white text-xl">No stats available</div>
        <p className="text-gray-400">Start catching Pokémon!</p>
      </div>
    );
  }

  const rarityColors = {
    common: 'from-gray-400 to-gray-500',
    uncommon: 'from-green-400 to-green-500',
    rare: 'from-blue-400 to-blue-500',
    epic: 'from-purple-400 to-purple-500',
    legendary: 'from-yellow-400 to-yellow-500',
  };

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 animate-fadeIn">
      <div className="glass-strong rounded-3xl shadow-2xl p-8 border border-white/10">
        <div className="mb-8">
          <h2 className="text-4xl font-bold mb-2 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">Statistics</h2>
          <p className="text-gray-400 text-lg">@{stats.username}</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">
          <div className="glass rounded-2xl p-8 border border-white/10 hover:border-blue-400/50 card-hover group">
            <div className="flex items-center justify-between mb-3">
              <div className="text-sm font-medium text-gray-400">Total Caught</div>
              <div className="text-3xl opacity-50 group-hover:scale-110 transition-transform">🎯</div>
            </div>
            <div className="text-5xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">{stats.total_caught}</div>
          </div>
          <div className="glass rounded-2xl p-8 border border-white/10 hover:border-green-400/50 card-hover group">
            <div className="flex items-center justify-between mb-3">
              <div className="text-sm font-medium text-gray-400">Unique Pokémon</div>
              <div className="text-3xl opacity-50 group-hover:scale-110 transition-transform">✨</div>
            </div>
            <div className="text-5xl font-bold bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent">{stats.unique_pokemon}</div>
          </div>
          <div className="glass rounded-2xl p-8 border border-white/10 hover:border-yellow-400/50 card-hover group">
            <div className="flex items-center justify-between mb-3">
              <div className="text-sm font-medium text-gray-400">Coins</div>
              <div className="text-3xl opacity-50 group-hover:scale-110 transition-transform">🪙</div>
            </div>
            <div className="text-5xl font-bold bg-gradient-to-r from-yellow-400 to-orange-400 bg-clip-text text-transparent">{stats.coins}</div>
          </div>
        </div>

        <h3 className="text-3xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">Pokémon by Rarity</h3>
        <div className="space-y-4">
          {Object.entries(stats.rarity_counts || {}).map(([rarity, count], index) => (
            <div key={rarity} className="animate-slideInLeft" style={{ animationDelay: `${index * 0.1}s` }}>
              <div className="flex items-center mb-2">
                <div className="w-32 font-semibold text-white capitalize text-sm">{rarity}</div>
                <div className="flex-1 glass rounded-full h-10 relative overflow-hidden border border-white/10">
                  <div
                    className={`bg-gradient-to-r ${rarityColors[rarity]} h-full flex items-center justify-end px-4 transition-all duration-1000 ease-out shadow-lg`}
                    style={{ 
                      width: `${(count / stats.total_caught) * 100}%`,
                      transitionDelay: `${index * 0.1}s`
                    }}
                  >
                    <span className="text-white font-bold text-sm drop-shadow-lg">{count}</span>
                  </div>
                </div>
                <div className="w-20 text-right">
                  <span className="text-gray-400 text-sm font-medium">
                    {Math.round((count / stats.total_caught) * 100)}%
                  </span>
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
