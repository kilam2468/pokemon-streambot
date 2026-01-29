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
        <div className="flex flex-col items-center space-y-4">
          <div className="w-16 h-16 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
          <div className="text-white text-xl font-medium">Loading Pokédex...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 py-8 animate-fadeIn">
      <div className="glass-strong rounded-3xl p-8 mb-8 border border-white/10" style={{ boxShadow: 'none' }}>
        <h2 className="text-4xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">Pokédex Progress</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="glass rounded-2xl p-6 border border-white/10 hover:border-purple-400/50 transition-colors duration-200" style={{ boxShadow: 'none' }}>
            <div className="text-sm text-gray-400 mb-2">Unique Pokémon</div>
            <div className="text-4xl font-bold bg-gradient-to-r from-blue-400 to-cyan-400 bg-clip-text text-transparent">{uniqueCaught}/{totalPokemon}</div>
          </div>
          <div className="glass rounded-2xl p-6 border border-white/10 hover:border-green-400/50 transition-colors duration-200" style={{ boxShadow: 'none' }}>
            <div className="text-sm text-gray-400 mb-2">Total Caught</div>
            <div className="text-4xl font-bold bg-gradient-to-r from-green-400 to-emerald-400 bg-clip-text text-transparent">{caughtPokemon.length}</div>
          </div>
          <div className="glass rounded-2xl p-6 border border-white/10 hover:border-purple-400/50 transition-colors duration-200" style={{ boxShadow: 'none' }}>
            <div className="text-sm text-gray-400 mb-2">Completion</div>
            <div className="text-4xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
              {totalPokemon > 0 ? Math.round((uniqueCaught / totalPokemon) * 100) : 0}%
            </div>
          </div>
        </div>
      </div>

      <div className="glass-strong rounded-3xl p-8 border border-white/10" style={{ boxShadow: 'none' }}>
        <div className="flex flex-wrap gap-4 mb-8">
          <div className="flex-1 min-w-[200px]">
            <label className="block text-sm font-medium text-gray-300 mb-3">Filter by Rarity</label>
            <select
              value={filterRarity}
              onChange={(e) => setFilterRarity(e.target.value)}
              className="w-full px-5 py-3 glass rounded-xl border border-white/20 focus:border-purple-400 focus:outline-none transition-all duration-300 text-white"
            >
              <option value="all" className="bg-gray-800">All Rarities</option>
              <option value="common" className="bg-gray-800">Common</option>
              <option value="uncommon" className="bg-gray-800">Uncommon</option>
              <option value="rare" className="bg-gray-800">Rare</option>
              <option value="epic" className="bg-gray-800">Epic</option>
              <option value="legendary" className="bg-gray-800">Legendary</option>
            </select>
          </div>
          <div className="flex-1 min-w-[200px]">
            <label className="block text-sm font-medium text-gray-300 mb-3">Sort By</label>
            <select
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
              className="w-full px-5 py-3 glass rounded-xl border border-white/20 focus:border-purple-400 focus:outline-none transition-all duration-300 text-white"
            >
              <option value="recent" className="bg-gray-800">Most Recent</option>
              <option value="name" className="bg-gray-800">Name</option>
              <option value="rarity" className="bg-gray-800">Rarity</option>
            </select>
          </div>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4">
          {filteredPokemon.map((pokemon, index) => (
            <div
              key={pokemon.id}
              className="glass rounded-2xl p-4 border border-white/10 hover:border-purple-400/50 group animate-scaleIn transition-all duration-200"
              style={{ animationDelay: `${index * 0.05}s`, boxShadow: 'none' }}
            >
              <div className="relative">
                <div className="absolute inset-0 bg-gradient-to-br from-purple-500/20 to-pink-500/20 rounded-xl opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                <img
                  src={pokemon.sprite_url}
                  alt={pokemon.pokemon_name}
                  className="w-full h-24 object-contain mb-3 pixelated relative z-10 transform group-hover:scale-110 transition-transform duration-300"
                  style={{ imageRendering: 'pixelated' }}
                />
                <span className={`absolute top-0 right-0 ${getRarityColor(pokemon.rarity)} text-white text-[10px] px-2 py-1 rounded-bl-xl rounded-tr-xl font-bold shadow-lg`}>
                  {pokemon.rarity.toUpperCase()}
                </span>
              </div>
              <h3 className="font-bold text-center text-white text-sm mb-1">{pokemon.pokemon_name}</h3>
              <p className="text-xs text-center text-gray-400 mb-2">{pokemon.pokemon_type}</p>
              <div className="flex items-center justify-center gap-1 mb-1">
                <img 
                  src={getBallImage(pokemon.caught_with)} 
                  alt={getBallName(pokemon.caught_with)}
                  className="w-4 h-4 pixelated"
                  style={{ imageRendering: 'pixelated' }}
                />
                <p className="text-xs text-gray-400">{getBallName(pokemon.caught_with)}</p>
              </div>
              <p className="text-xs text-center text-gray-300">
                {new Date(pokemon.caught_at).toLocaleDateString()}
              </p>
            </div>
          ))}
        </div>

        {filteredPokemon.length === 0 && (
          <div className="text-center py-20">
            <div className="text-6xl mb-4 opacity-50">🎮</div>
            <div className="text-gray-400 text-lg">No Pokémon found</div>
            <p className="text-gray-500 text-sm mt-2">Start catching in the Twitch chat!</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default Pokedex;
