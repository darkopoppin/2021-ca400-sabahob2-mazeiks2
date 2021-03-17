<template>
  <ion-page>
    <ion-content>
      <ion-card>
          <form @submit.prevent="userLogin">
            <h3>Sign In</h3>

            <ion-item>
              <ion-input
                type="email"
                placeholder="email"
                v-model="user.email"
              />
            </ion-item>

            <ion-item>
              <ion-input
                type="password"
                placeholder="password"
                v-model="user.password"
              />
            </ion-item>

            <ion-button type="submit">Sign In </ion-button>

            <p>
              <router-link to="/ForgotPassword">Forgot password?</router-link>
            </p>
            <p>
              <router-link to="/SignUp">Sign Up instead?</router-link>
            </p>
          </form>
      </ion-card>
    </ion-content>
  </ion-page>
</template>


<script>
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
  IonButton,
  IonCard,
  IonInput,
  IonItem,
} from "@ionic/vue";
import { defineComponent } from "vue";
import firebase from "firebase";

export default defineComponent({
  name: "SignIn",
  components: {
    IonContent,
    IonCard,
    IonInput,
    IonItem,
    // IonHeader,
    IonButton,
    IonPage,
    // IonTitle,
    // IonToolbar
  },
  data() {
    return {
      user: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    userLogin() {
      firebase
        .auth()
        .setPersistence(firebase.auth.Auth.Persistence.LOCAL)
        .then(() => {
          return firebase
            .auth()
            .signInWithEmailAndPassword(this.user.email, this.user.password)
            .then((res) => {
              res.user
                .updateProfile({
                  displayName: this.user.name,
                })
                .then(() => {
                  this.$router.push("/home");
                });
            })
            .catch((error) => {
              alert(error.message);
            });
        });
    },
  },
});
</script>