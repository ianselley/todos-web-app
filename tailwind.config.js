const colors = require("tailwindcss/colors");

module.exports = {
  mode: "jit",
  purge: ["./website/**/*.{js,html}"],
  darkMode: "class", // or 'media' or 'class' or 'false'
  theme: {
    extend: {
      transitionDuration: {
        400: "400ms",
      },
      gridTemplateColumns: {
        "auto-min": "auto min-content",
      },
    },
    fontFamily: {
      rubik: "Rubik",
      montserrat: "Montserrat",
      pacifico: "Pacifico",
    },
    colors: {
      transparent: "transparent",
      current: "currentColor",
      white: colors.white,
      black: colors.black,
      rose: colors.rose,
      pink: colors.pink,
      fuchsia: colors.fuchsia,
      purple: colors.purple,
      violet: colors.violet,
      indigo: colors.indigo,
      blue: colors.blue,
      sky: colors.sky,
      cyan: colors.cyan,
      teal: colors.teal,
      emerald: colors.emerald,
      green: colors.green,
      lime: colors.lime,
      yellow: colors.yellow,
      amber: colors.amber,
      orange: colors.orange,
      red: colors.red,
      warmGray: colors.warmGray,
      trueGray: colors.trueGray,
      gray: colors.gray,
      coolGray: colors.coolGray,
      blueGray: colors.blueGray,
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
