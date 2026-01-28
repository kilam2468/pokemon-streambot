/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        pokemon: {
          red: '#FF0000',
          blue: '#0066CC',
          yellow: '#FFD700',
          common: '#9E9E9E',
          uncommon: '#4CAF50',
          rare: '#2196F3',
          epic: '#9C27B0',
          legendary: '#FF9800'
        }
      }
    },
  },
  plugins: [],
}
