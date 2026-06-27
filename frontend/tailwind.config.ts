import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e6f2ff',
          100: '#bfd9ff',
          200: '#99c0ff',
          300: '#73a7ff',
          400: '#4d8eff',
          500: '#0074C2',
          600: '#0059a0',
          700: '#00427d',
          800: '#002b5a',
          900: '#001437',
        },
        dark: {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#777777',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111111',
        },
      },
      fontFamily: {
        sans: ['var(--font-iran-yekan)', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
export default config
