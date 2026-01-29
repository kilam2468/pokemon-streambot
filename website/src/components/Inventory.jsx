import React, { useState, useEffect } from 'react';
import { getUserInventory } from '../api/pokemonApi';

const Inventory = ({ username }) => {
  const [inventory, setInventory] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchInventory = async () => {
      try {
        setLoading(true);
        const data = await getUserInventory(username);
        setInventory(data);
      } catch (error) {
        console.error('Error fetching inventory:', error);
      } finally {
        setLoading(false);
      }
    };

    if (username) {
      fetchInventory();
    }
  }, [username]);

  const ballData = {
    pokeball: {
      name: 'Poké Ball',
      gradient: 'from-red-500 via-red-400 to-pink-500',
      description: 'Standard catching ball',
      icon: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png',
    },
    greatball: {
      name: 'Great Ball',
      gradient: 'from-blue-500 via-blue-400 to-cyan-500',
      description: 'Better catch rate',
      icon: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/great-ball.png',
    },
    ultraball: {
      name: 'Ultra Ball',
      gradient: 'from-yellow-400 via-yellow-300 to-orange-400',
      description: 'High catch rate',
      icon: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png',
    },
    masterball: {
      name: 'Master Ball',
      gradient: 'from-purple-500 via-purple-400 to-pink-500',
      description: '100% catch rate!',
      icon: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png',
    },
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="flex flex-col items-center space-y-4">
          <div className="w-16 h-16 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
          <div className="text-white text-xl font-medium">Loading Inventory...</div>
        </div>
      </div>
    );
  }

  if (!inventory) {
    return (
      <div className="flex flex-col items-center justify-center h-64 space-y-4">
        <div className="text-6xl opacity-50">🎒</div>
        <div className="text-center text-white text-xl">User not found</div>
        <p className="text-gray-400">Make sure you've joined the stream!</p>
      </div>
    );
  }

  return (
    <div className="max-w-5xl mx-auto px-4 py-8 animate-fadeIn">
      <div className="glass-strong rounded-3xl shadow-2xl p-8 mb-8 border border-white/10">
        <div className="mb-8">
          <h2 className="text-4xl font-bold mb-2 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">Inventory</h2>
          <p className="text-gray-400 text-lg">@{inventory.username}</p>
        </div>
        
        <div className="glass rounded-2xl p-8 mb-8 border border-white/10 hover:border-yellow-400/50 card-hover group overflow-hidden relative">
          <div className="absolute inset-0 bg-gradient-to-br from-yellow-500/10 to-orange-500/10 opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
          <div className="flex items-center justify-between relative z-10">
            <div>
              <div className="text-sm font-medium text-gray-400 mb-2">Your Coins</div>
              <div className="text-6xl font-bold bg-gradient-to-r from-yellow-400 to-orange-400 bg-clip-text text-transparent">{inventory.coins}</div>
            </div>
            <div className="text-7xl animate-float">🪙</div>
          </div>
        </div>

        <h3 className="text-3xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">Poké Balls</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {Object.entries(ballData).map(([key, ball], index) => (
            <div
              key={key}
              className="glass rounded-2xl p-6 border border-white/10 hover:border-purple-400/50 card-hover group overflow-hidden relative animate-scaleIn"
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              <div className={`absolute inset-0 bg-gradient-to-br ${ball.gradient} opacity-0 group-hover:opacity-20 transition-all duration-500`}></div>
              <div className="flex justify-between items-start mb-4 relative z-10">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-2">
                    <img 
                      src={ball.icon} 
                      alt={ball.name}
                      className="w-8 h-8 pixelated"
                      style={{ imageRendering: 'pixelated' }}
                    />
                    <h4 className="text-xl font-bold text-white">{ball.name}</h4>
                  </div>
                  <p className="text-sm text-gray-400">{ball.description}</p>
                </div>
                <div className={`text-5xl font-bold bg-gradient-to-r ${ball.gradient} bg-clip-text text-transparent group-hover:scale-110 transition-transform duration-300`}>
                  {inventory[key]}
                </div>
              </div>
              <div className="h-2 glass rounded-full overflow-hidden relative z-10">
                <div 
                  className={`h-full bg-gradient-to-r ${ball.gradient} transition-all duration-1000`}
                  style={{ 
                    width: `${Math.min((inventory[key] / 10) * 100, 100)}%`,
                    transitionDelay: `${index * 0.1}s`
                  }}
                ></div>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-8 p-6 glass rounded-2xl border border-white/10">
          <h4 className="font-bold text-white mb-3 flex items-center gap-2">
            <span>💡</span>
            <span>How to get more:</span>
          </h4>
          <ul className="space-y-2 text-sm text-gray-300">
            <li className="flex items-start gap-2">
              <span className="text-purple-400">•</span>
              <span><strong className="text-white">Earn coins</strong> by catching Pokémon (10 coins each)</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-purple-400">•</span>
              <span>Claim your <strong className="text-white">daily bonus</strong> with <code className="px-2 py-1 bg-white/10 rounded text-purple-300">!pdaily</code> (50 coins)</span>
            </li>
            <li className="flex items-start gap-2">
              <span className="text-purple-400">•</span>
              <span>Use <code className="px-2 py-1 bg-white/10 rounded text-purple-300">!pbuy pokeball</code> in Twitch chat to purchase items</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Inventory;
