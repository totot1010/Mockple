<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }

  .grey.darken-1 {
    background-color: #757575 !important;
    border-color: "757575" !important;
  }

  .pa-4 {
    padding: 16px !important;
  }

  .username {
    padding-top: 10px;
  }
}
</style>

<script>
export default {
  data: () => ({
    drawer: null,
    links: [
      ["mdi-inbox-arrow-down", "Inbox", "/"],
      ["mdi-send", "Send", "/about"],
      ["mdi-delete", "Trash", "/about"],
      ["mdi-alert-octagon", "Spam", "/about"],
    ],
  }),
};
</script>
