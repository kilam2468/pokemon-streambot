import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Pokedex from './components/Pokedex';
import Inventory from './components/Inventory';
import Stats from './components/Stats';
import './index.css';

function App() {
  const [username, setUsername] = useState(localStorage.getItem('pokemon_username') || '');
  const [tempUsername, setTempUsername] = useState(username);

  const handleSetUsername = (e) => {
    e.preventDefault();
    if (tempUsername.trim()) {
      const normalizedUsername = tempUsername.trim().toLowerCase();
      setUsername(normalizedUsername);
      localStorage.setItem('pokemon_username', normalizedUsername);
    }
  };

  return (
    <Router>
      <div className="min-h-screen">
        <nav 
          className="sticky top-0 z-50 border-b border-white/10"
          style={{
            background: 'rgba(17, 24, 39, 0.85)',
            backdropFilter: 'blur(12px)',
            WebkitBackdropFilter: 'blur(12px)',
            boxShadow: 'none'
          }}
        >
          <div className="max-w-7xl mx-auto px-6 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-8">
                <h1 className="text-2xl font-bold bg-gradient-to-r from-purple-400 to-pink-400 bg-clip-text text-transparent">
                  🎮 Pokémon Collector
                </h1>
                <div className="hidden md:flex space-x-1">
                  <Link 
                    to="/" 
                    className="nav-link"
                  >
                    Pokédex
                  </Link>
                  <Link 
                    to="/inventory" 
                    className="nav-link"
                  >
                    Inventory
                  </Link>
                  <Link 
                    to="/stats" 
                    className="nav-link"
                  >
                    Stats
                  </Link>
                </div>
              </div>
              <div className="flex items-center">
                {username ? (
                  <div 
                    className="flex items-center space-x-3 rounded-full px-4 py-2"
                    style={{
                      background: 'rgba(255, 255, 255, 0.05)',
                      border: '1px solid rgba(255, 255, 255, 0.1)'
                    }}
                  >
                    <span className="text-sm font-medium">@{username}</span>
                    <button
                      onClick={() => {
                        setUsername('');
                        setTempUsername('');
                        localStorage.removeItem('pokemon_username');
                      }}
                      className="bg-gradient-to-r from-purple-500 to-pink-500 hover:from-purple-600 hover:to-pink-600 px-4 py-1.5 rounded-full text-sm font-medium"
                      style={{ transition: 'all 0.2s', boxShadow: 'none' }}
                    >
                      Change
                    </button>
                  </div>
                ) : null}
              </div>
            </div>
          </div>
        </nav>

        {!username ? (
          <div className="flex items-center justify-center min-h-[80vh] px-4">
            <div className="glass-strong rounded-3xl shadow-2xl p-10 max-w-md w-full mx-4 animate-scaleIn">
              <div className="text-center mb-8">
                <div className="text-6xl mb-4 animate-float">🎮</div>
                <h2 className="text-4xl font-bold bg-gradient-to-r from-purple-400 via-pink-400 to-purple-400 bg-clip-text text-transparent mb-3">
                  Welcome, Trainer!
                </h2>
                <p className="text-gray-300 text-sm">
                  Enter your Twitch username to view your Pokémon collection
                </p>
              </div>
              <form onSubmit={handleSetUsername} className="space-y-5">
                <div className="relative">
                  <input
                    type="text"
                    value={tempUsername}
                    onChange={(e) => setTempUsername(e.target.value)}
                    placeholder="Your Twitch username"
                    className="w-full px-6 py-4 glass rounded-2xl border border-white/20 focus:border-purple-400 focus:outline-none focus:ring-2 focus:ring-purple-400/50 transition-all duration-300 text-white placeholder-gray-400"
                    required
                  />
                </div>
                <button
                  type="submit"
                  className="w-full bg-gradient-to-r from-purple-500 via-pink-500 to-purple-500 text-white py-4 rounded-2xl font-semibold hover:shadow-2xl hover:scale-[1.02] transition-all duration-300 shadow-lg"
                >
                  View Collection
                </button>
              </form>
              <div className="mt-6 p-5 glass rounded-2xl border border-white/10">
                <p className="text-sm text-gray-300 leading-relaxed">
                  💡 Don't have any Pokémon yet? Join the stream and use <code className="px-2 py-1 bg-white/10 rounded">!p catch</code> when a Pokémon spawns!
                </p>
              </div>
            </div>
          </div>
        ) : (
          <Routes>
            <Route path="/" element={<Pokedex username={username} />} />
            <Route path="/inventory" element={<Inventory username={username} />} />
            <Route path="/stats" element={<Stats username={username} />} />
          </Routes>
        )}

        <footer className="bg-gray-800 text-white py-6 mt-12">
          <div className="max-w-7xl mx-auto px-4 text-center">
            <p className="text-sm">Pokemon Stream Bot - Catch 'em all on Twitch!</p>
            <p className="text-xs text-gray-400 mt-2">
              Pokemon sprites from PokeAPI | Not affiliated with Nintendo/Game Freak
            </p>
          </div>
        </footer>
      </div>
    </Router>
  );
}


export default App;
