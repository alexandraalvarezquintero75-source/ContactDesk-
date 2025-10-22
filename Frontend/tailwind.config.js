// /** @type {import('tailwindcss').Config} */
// export default {
//   content: [
//     "./index.html",
//     "./src/**/*.{vue,js,ts,jsx,tsx}"
//   ],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }
// /** @type {import('tailwindcss').Config} */
// const primeui = require('tailwindcss-primeui')

// export default {
//   content: ['./index.html', './src/**/*.{vue,js,ts}'],
//   darkMode: ['selector', '[class="p-dark"]'],
//   plugins: [primeui],
// };

/**  @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#f97316',   // tu naranja principal
        secondary: '#ea580c', // naranja oscuro para hover
      },
    },
  },
  plugins: [],
}
