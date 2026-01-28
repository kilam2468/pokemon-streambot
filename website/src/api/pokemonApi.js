import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getUserStats = async (username) => {
  const response = await api.get(`/api/user/${username}/stats`);
  return response.data;
};

export const getUserPokedex = async (username) => {
  const response = await api.get(`/api/user/${username}/pokedex`);
  return response.data;
};

export const getUserInventory = async (username) => {
  const response = await api.get(`/api/user/${username}/inventory`);
  return response.data;
};

export const getAllPokemon = async () => {
  const response = await api.get('/api/pokemon');
  return response.data;
};

export const getLeaderboard = async () => {
  const response = await api.get('/api/leaderboard');
  return response.data;
};
