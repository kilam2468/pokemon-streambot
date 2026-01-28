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
      color: 'from-red-500 to-red-600',
      description: 'Standard catching ball',
    },
    greatball: {
      name: 'Great Ball',
      color: 'from-blue-500 to-blue-600',
      description: 'Better catch rate',
    },
    ultraball: {
      name: 'Ultra Ball',
      color: 'from-yellow-400 to-yellow-500',
      description: 'High catch rate',
    },
    masterball: {
      name: 'Master Ball',
      color: 'from-purple-500 to-purple-600',
      description: '100% catch rate!',
    },
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-white text-xl">Loading Inventory...</div>
      </div>
    );
  }

  if (!inventory) {
    return (
      <div className="text-center text-white text-xl">
        User not found. Make sure you've joined the stream!
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-3xl font-bold text-gray-800 mb-2">Inventory</h2>
        <p className="text-gray-600 mb-6">@{inventory.username}</p>
        
        <div className="bg-gradient-to-r from-yellow-400 to-yellow-500 rounded-lg p-6 mb-6">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-sm font-medium text-yellow-900">Your Coins</div>
              <div className="text-4xl font-bold text-white">{inventory.coins}</div>
            </div>
            <div className="text-6xl">🪙</div>
          </div>
        </div>

        <h3 className="text-2xl font-bold text-gray-800 mb-4">Poke Balls</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {Object.entries(ballData).map(([key, ball]) => (
            <div
              key={key}
              className={`bg-gradient-to-r ${ball.color} rounded-lg p-6 text-white shadow-lg`}
            >
              <div className="flex justify-between items-start mb-2">
                <div>
                  <h4 className="text-xl font-bold">{ball.name}</h4>
                  <p className="text-sm opacity-90">{ball.description}</p>
                </div>
                <div className="text-3xl font-bold">{inventory[key]}</div>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-6 p-4 bg-blue-50 rounded-lg">
          <h4 className="font-bold text-gray-800 mb-2">💡 How to get more:</h4>
          <ul className="text-sm text-gray-700 space-y-1">
            <li>• Catch Pokemon to earn coins</li>
            <li>• Use !shop in Twitch chat to buy more balls</li>
            <li>• Watch the stream to earn coins over time</li>
            <li>• Claim daily bonus with !daily command</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Inventory;
