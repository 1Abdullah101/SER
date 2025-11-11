/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class', // Add this to enable dark mode with the 'dark' class
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      animation: {
        draw: 'draw 8s ease infinite',
        drawDelay: 'draw 8s 3s ease infinite',
      },
      keyframes: {
        draw: {
          '0%': { strokeDashoffset: '1500', opacity: '0.8' },
          '50%': { strokeDashoffset: '0' },
          '100%': { strokeDashoffset: '-1500', opacity: '0.8' },
        },
      },
    },
  },
  plugins: [],
}
