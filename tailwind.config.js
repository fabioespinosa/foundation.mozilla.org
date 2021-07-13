module.exports = {
  purge: [
    "./source/js/**/*.{js,jsx}",
    "./maintenance/maintenance.html",
    "./network-api/networkapi/wagtailpages/templates/**/*.html",
  ],
  mode: "jit",
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
  prefix: "tw-",
};
