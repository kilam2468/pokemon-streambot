import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useParams, useNavigate, useLocation } from 'react-router-dom';
import Pokedex from './components/Pokedex';
import Inventory from './components/Inventory';
import Stats from './components/Stats';
import './index.css';

function UserProfile({ view }) {
  const { username: urlUsername } = useParams();
  const navigate = useNavigate();
  const [username, setUsername] = useState(localStorage.getItem('pokemon_username') || '');

  useEffect(() => {
    if (urlUsername) {
      const normalizedUsername = urlUsername.trim().toLowerCase();
      setUsername(normalizedUsername);
      localStorage.setItem('pokemon_username', normalizedUsername);
    }
  }, [urlUsername]);

  const currentUsername = urlUsername ? urlUsername.trim().toLowerCase() : username;

  if (!currentUsername) {
    return null;
  }

  const components = {
    pokedex: <Pokedex username={currentUsername} />,
    inventory: <Inventory username={currentUsername} />,
    stats: <Stats username={currentUsername} />
  };

  return components[view];
}

function AppContent() {
  const location = useLocation();
  const [username, setUsername] = useState(localStorage.getItem('pokemon_username') || '');
  const [tempUsername, setTempUsername] = useState(username);
  const [isLive, setIsLive] = useState(false);

  // Check Twitch live status
  useEffect(() => {
    const checkLiveStatus = async () => {
      try {
        // Using Twitch API requires client ID and token, so we'll use a proxy or public endpoint
        // For now, we'll check periodically
        const response = await fetch('https://decapi.me/twitch/uptime/justasuspect');
        const text = await response.text();
        // If the channel is offline, the response will contain "offline" or error message
        setIsLive(!text.toLowerCase().includes('offline') && !text.toLowerCase().includes('error'));
      } catch (error) {
        console.error('Error checking live status:', error);
        setIsLive(false);
      }
    };

    checkLiveStatus();
    // Check every 60 seconds
    const interval = setInterval(checkLiveStatus, 60000);
    return () => clearInterval(interval);
  }, []);

  // Check if URL contains a username parameter
  useEffect(() => {
    const pathParts = location.pathname.split('/').filter(Boolean);
    if (pathParts.length > 0 && !['inventory', 'stats'].includes(pathParts[0])) {
      const urlUsername = pathParts[0];
      const normalizedUsername = urlUsername.trim().toLowerCase();
      setUsername(normalizedUsername);
      localStorage.setItem('pokemon_username', normalizedUsername);
    }
  }, [location.pathname]);

  const handleSetUsername = (e) => {
    e.preventDefault();
    if (tempUsername.trim()) {
      const normalizedUsername = tempUsername.trim().toLowerCase();
      setUsername(normalizedUsername);
      localStorage.setItem('pokemon_username', normalizedUsername);
    }
  };

  // Check if we're on a user profile route
  const isUserProfileRoute = location.pathname.split('/').filter(Boolean).length > 0 && 
                             location.pathname !== '/' && 
                             !location.pathname.startsWith('/inventory') && 
                             !location.pathname.startsWith('/stats');

  return (
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
              <div className="flex items-center gap-3">
                {/* Twitch Button */}
                <a
                  href="https://www.twitch.tv/justasuspect"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 px-4 py-2 rounded-full font-medium text-sm transition-all duration-300 hover:scale-105"
                  style={{
                    background: isLive 
                      ? 'linear-gradient(135deg, #9146FF 0%, #772CE8 100%)'
                      : 'rgba(145, 70, 255, 0.2)',
                    border: isLive ? '1px solid rgba(145, 70, 255, 0.5)' : '1px solid rgba(145, 70, 255, 0.3)',
                    boxShadow: isLive ? '0 0 20px rgba(145, 70, 255, 0.6), 0 0 40px rgba(145, 70, 255, 0.3)' : 'none'
                  }}
                >
                  <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M11.571 4.714h1.715v5.143H11.57zm4.715 0H18v5.143h-1.714zM6 0L1.714 4.286v15.428h5.143V24l4.286-4.286h3.428L22.286 12V0zm14.571 11.143l-3.428 3.428h-3.429l-3 3v-3H6.857V1.714h13.714z"/>
                  </svg>
                  {isLive ? (
                    <span className="font-bold animate-pulse">LIVE</span>
                  ) : (
                    <span>Twitch</span>
                  )}
                </a>
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

        {!username && !isUserProfileRoute ? (
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
            <Route path="/:username" element={<UserProfile view="pokedex" />} />
            <Route path="/:username/inventory" element={<UserProfile view="inventory" />} />
            <Route path="/:username/stats" element={<UserProfile view="stats" />} />
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
  );
}

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}


export default App;
