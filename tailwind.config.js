const colors = require("tailwindcss/colors");

module.exports = {
  mode: "jit",
  purge: ["./website/**/*.{js,html}"],
  darkMode: "class", // or 'media' or 'class' or 'false'
  theme: {
    extend: {
      inset: {
        "1+1": "calc(100% + 1rem)",
        "1+2.5": "calc(100% + 2.5rem)",
      },
      transitionDuration: {
        400: "400ms",
      },
      gridTemplateColumns: {
        "auto-min": "auto min-content",
        "min-auto": "min-content auto",
        "min-auto-min": "min-content auto min-content",
        "txt-x": "auto 1.5rem",
      },
      lineHeight: {
        16: "4rem",
      },
      spacing: {
        18: "4.5rem",
        120: "30rem",
        160: "40rem",
      },
    },
    fontFamily: {
      rubik: "Rubik",
      montserrat: "Montserrat",
      pacifico: "Pacifico",
      oleoScript: "Oleo Script",
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
