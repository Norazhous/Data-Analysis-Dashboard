# Data analysis UI for compression refrigeration experiment.

The server is developed in Python; Flask is used for web communication; and the Coolprop library is used for R134a property calculation.

The client is developed in Vue.js.

# Client

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

cd the path to /dataAnalysis

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

# Server

This template should help running the program.

## project running 

run app.py

## libraries included

Flask(https://flask.palletsprojects.com/en/3.0.x/): 

```
pip install Flask
```

CoolProp(http://www.coolprop.org/index.html#):

```
pip install coolprop
```