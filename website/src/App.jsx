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
      setUsername(tempUsername.trim());
      localStorage.setItem('pokemon_username', tempUsername.trim());
    }
  };

  return (
    <Router>
      <div className="min-h-screen">
        <nav className="bg-gradient-to-r from-red-600 to-red-700 text-white shadow-lg">
          <div className="max-w-7xl mx-auto px-4 py-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-8">
                <h1 className="text-2xl font-bold">🎮 Pokemon Stream Bot</h1>
                <div className="hidden md:flex space-x-4">
                  <Link to="/" className="hover:bg-red-800 px-4 py-2 rounded transition">
                    Pokedex
                  </Link>
                  <Link to="/inventory" className="hover:bg-red-800 px-4 py-2 rounded transition">
                    Inventory
                  </Link>
                  <Link to="/stats" className="hover:bg-red-800 px-4 py-2 rounded transition">
                    Stats
                  </Link>
                </div>
              </div>
              <div className="flex items-center">
                {username ? (
                  <div className="flex items-center space-x-2">
                    <span className="text-sm">@{username}</span>
                    <button
                      onClick={() => {
                        setUsername('');
                        setTempUsername('');
                        localStorage.removeItem('pokemon_username');
                      }}
                      className="bg-red-800 hover:bg-red-900 px-3 py-1 rounded text-sm transition"
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
          <div className="flex items-center justify-center min-h-[80vh]">
            <div className="bg-white rounded-lg shadow-xl p-8 max-w-md w-full mx-4">
              <h2 className="text-3xl font-bold text-gray-800 mb-4 text-center">
                Welcome, Trainer!
              </h2>
              <p className="text-gray-600 mb-6 text-center">
                Enter your Twitch username to view your Pokemon collection
              </p>
              <form onSubmit={handleSetUsername} className="space-y-4">
                <input
                  type="text"
                  value={tempUsername}
                  onChange={(e) => setTempUsername(e.target.value)}
                  placeholder="Your Twitch username"
                  className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-transparent"
                  required
                />
                <button
                  type="submit"
                  className="w-full bg-gradient-to-r from-red-600 to-red-700 text-white py-3 rounded-lg font-bold hover:from-red-700 hover:to-red-800 transition"
                >
                  View Collection
                </button>
              </form>
              <div className="mt-6 p-4 bg-blue-50 rounded-lg">
                <p className="text-sm text-gray-700">
                  💡 Don't have any Pokemon yet? Join the stream and use !catch when a Pokemon spawns!
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
