import React, { useState, useEffect } from 'react';
import { getUserPokedex, getAllPokemon } from '../api/pokemonApi';

const Pokedex = ({ username }) => {
  const [caughtPokemon, setCaughtPokemon] = useState([]);
  const [allPokemon, setAllPokemon] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filterRarity, setFilterRarity] = useState('all');
  const [sortBy, setSortBy] = useState('recent');

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const [caught, all] = await Promise.all([
          getUserPokedex(username),
          getAllPokemon()
        ]);
        setCaughtPokemon(caught);
        setAllPokemon(all);
      } catch (error) {
        console.error('Error fetching pokedex:', error);
      } finally {
        setLoading(false);
      }
    };

    if (username) {
      fetchData();
    }
  }, [username]);

  const getRarityColor = (rarity) => {
    const colors = {
      common: 'bg-gray-400',
      uncommon: 'bg-green-500',
      rare: 'bg-blue-500',
      epic: 'bg-purple-600',
      legendary: 'bg-yellow-500'
    };
    return colors[rarity] || 'bg-gray-400';
  };

  const getBallImage = (ballType) => {
    const balls = {
      pokeball: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/poke-ball.png',
      greatball: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/great-ball.png',
      ultraball: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/ultra-ball.png',
      masterball: 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/items/master-ball.png'
    };
    return balls[ballType] || balls.pokeball;
  };

  const getBallName = (ballType) => {
    const names = {
      pokeball: 'Poké Ball',
      greatball: 'Great Ball',
      ultraball: 'Ultra Ball',
      masterball: 'Master Ball'
    };
    return names[ballType] || ballType;
  };

  const filteredPokemon = caughtPokemon
    .filter(p => filterRarity === 'all' || p.rarity === filterRarity)
    .sort((a, b) => {
      if (sortBy === 'recent') {
        return new Date(b.caught_at) - new Date(a.caught_at);
      } else if (sortBy === 'name') {
        return a.pokemon_name.localeCompare(b.pokemon_name);
      } else if (sortBy === 'rarity') {
        const rarityOrder = { legendary: 5, epic: 4, rare: 3, uncommon: 2, common: 1 };
        return rarityOrder[b.rarity] - rarityOrder[a.rarity];
      }
      return 0;
    });

  const caughtNames = new Set(caughtPokemon.map(p => p.pokemon_name));
  const uniqueCaught = caughtNames.size;
  const totalPokemon = allPokemon.length;

  if (loading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="text-white text-xl">Loading Pokedex...</div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-3xl font-bold text-gray-800 mb-4">Pokedex Progress</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="bg-blue-100 rounded-lg p-4">
            <div className="text-sm text-gray-600">Unique Pokemon</div>
            <div className="text-3xl font-bold text-blue-600">{uniqueCaught}/{totalPokemon}</div>
          </div>
          <div className="bg-green-100 rounded-lg p-4">
            <div className="text-sm text-gray-600">Total Caught</div>
            <div className="text-3xl font-bold text-green-600">{caughtPokemon.length}</div>
          </div>
          <div className="bg-purple-100 rounded-lg p-4">
            <div className="text-sm text-gray-600">Completion</div>
            <div className="text-3xl font-bold text-purple-600">
              {totalPokemon > 0 ? Math.round((uniqueCaught / totalPokemon) * 100) : 0}%
            </div>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
        <div className="flex flex-wrap gap-4 mb-6">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Filter by Rarity</label>
            <select
              value={filterRarity}
              onChange={(e) => setFilterRarity(e.target.value)}
              className="px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              <option value="all">All</option>
              <option value="common">Common</option>
              <option value="uncommon">Uncommon</option>
              <option value="rare">Rare</option>
              <option value="epic">Epic</option>
              <option value="legendary">Legendary</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">Sort By</label>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"
            >
              <option value="recent">Most Recent</option>
              <option value="name">Name</option>
              <option value="rarity">Rarity</option>
            </select>
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          {filteredPokemon.map((pokemon) => (
            <div
              key={pokemon.id}
              className="bg-gradient-to-b from-gray-50 to-gray-100 rounded-lg p-4 shadow hover:shadow-lg transition-shadow"
            >
              <div className="relative">
                <img
                  src={pokemon.sprite_url}
                  alt={pokemon.pokemon_name}
                  className="w-full h-24 object-contain mb-2 pixelated"
                  style={{ imageRendering: 'pixelated' }}
                />
                <span className={`absolute top-0 right-0 ${getRarityColor(pokemon.rarity)} text-white text-xs px-2 py-1 rounded-bl-lg`}>
                  {pokemon.rarity.toUpperCase()}
                </span>
              </div>
              <h3 className="font-bold text-center text-gray-800 text-sm">{pokemon.pokemon_name}</h3>
              <p className="text-xs text-center text-gray-600">{pokemon.pokemon_type}</p>
              <div className="flex items-center justify-center gap-1 mt-1">
                <img 
                  src={getBallImage(pokemon.caught_with)} 
                  alt={getBallName(pokemon.caught_with)}
                  className="w-4 h-4 pixelated"
                  style={{ imageRendering: 'pixelated' }}
                />
                <p className="text-xs text-gray-500">{getBallName(pokemon.caught_with)}</p>
              </div>
              <p className="text-xs text-center text-gray-500">
                {new Date(pokemon.caught_at).toLocaleDateString()}
              </p>
            </div>
          ))}
        </div>

        {filteredPokemon.length === 0 && (
          <div className="text-center py-12 text-gray-500">
            No Pokemon found. Start catching in the Twitch chat!
          </div>
        )}
      </div>
    </div>
  );
};

export default Pokedex;
