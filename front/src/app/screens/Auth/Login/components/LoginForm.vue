<template>
    <v-card>
        <v-card-title primary-title>
            <h3 class="headline mb-0">Login</h3>
        </v-card-title>
        <v-container>
            <v-form>
                <v-text-field
                  v-model="login"
                  label="Username"
                  required
                ></v-text-field>
                <v-text-field
                  v-model="password"
                  label="Password"
                  required
                  type="password"
                ></v-text-field>
            </v-form>
        </v-container>
        <v-card-actions class="login-form__actons">
            <a href="">Forgot the password?</a>
            <v-spacer></v-spacer>
            <v-btn
                class="blue"
                dark
                >
                Enter <v-icon>keyboard_arrow_right</v-icon>
            </v-btn>
        </v-card-actions>
    </v-card>
</template>
<script>
  export default{
      data() {
          return {
              login: '',
              password: '',
          };
      }
  }
</script>
<style>
    .card__actions.login-form__actons{
        padding: 16px
    }
</style>
