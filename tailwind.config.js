module.exports = {
  purge: [
    "./source/js/**/*.{js,jsx}",
    "./network-api/networkapi/wagtailpages/templates/**/*.html",
  ],
  mode: "jit",
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    screen: {
      sm: "576px",
      md: "768px",
      lg: "992px",
      xl: "1200px",
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
  prefix: "tw-",
};
