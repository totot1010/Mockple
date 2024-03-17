<template>
  <v-app>
    <div class="login-box">
      <v-card class="login-form">
        <v-card-title class="login-title">Login</v-card-title>
        <v-card-subtitle>ユーザー情報をご入力ください</v-card-subtitle>
        <form @submit.prevent="submit">
          <v-text-field :counter="10" label="Name"></v-text-field>

          <v-text-field label="E-mail"></v-text-field>

          <v-select :items="items" label="Select"></v-select>

          <v-checkbox label="Option" type="checkbox" value="1"></v-checkbox>

          <v-btn class="me-4" type="submit"> submit </v-btn>

          <v-btn @click="handleReset"> clear </v-btn>
        </form>
      </v-card>
    </div>
  </v-app>
</template>

<script setup>
import { ref } from "vue";

const items = ref(["Item 1", "Item 2", "Item 3", "Item 4"]);
</script>

<style scoped>
.login-form {
  margin: 150px;
  padding: 30px;
}

.login-box {
  width: 50%;
  margin: 0px auto;
  padding: 30px;
}

.login-title {
  display: inline-block;
}
</style>
