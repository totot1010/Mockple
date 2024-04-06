<template>
  <v-app>
    <div class="login-box">
      <v-card class="login-form">
        <v-card-title class="login-title">SignUp</v-card-title>
        <v-card-subtitle>ユーザー情報をご入力ください</v-card-subtitle>
        <v-form @submit.prevent="submit" v-model="valid" lazy-validation>
          <v-text-field
            v-model="name"
            :rules="nameRules"
            label="UserName"
            required
          ></v-text-field>

          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            type="password"
            label="Password"
          ></v-text-field>

          <v-btn
            class="login-button"
            type="submit"
            color="success"
            :disabled="isValid"
          >
            SignUp
          </v-btn>

          <v-btn> CLEAR </v-btn>
        </v-form>
      </v-card>
    </div>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    name: "",
    nameRules: [
      (v) => !!v || "Name is required",
      (v) => (v && v.length <= 10) || "Name must be less 10 characters",
    ],
    // password:
    valid: true,
    // email: "";
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be",
    ],
  }),
  computed: {
    isValid() {
      return !this.valid;
    },
  },
};
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

.login-button {
  margin-right: 20px;
}
</style>
