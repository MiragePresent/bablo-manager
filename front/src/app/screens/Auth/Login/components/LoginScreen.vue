<template>
    <v-layout row wrap>
        <v-flex
            md4
            sm6
            xs12
            offset-md4
            offset-sm3
            >
            <login-form/>
        </v-flex>
    </v-layout>
</template>

<script>
import LoginForm from './LoginForm'
export default {
  components: {
    LoginForm
  }
}
</script>

<style lang="css">
</style>
