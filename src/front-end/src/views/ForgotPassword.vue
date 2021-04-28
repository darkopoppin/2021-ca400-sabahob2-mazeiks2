<template>
  <ion-page>
    <ion-content>
      <ion-card>
          <form @submit.prevent="forgetPassword">
            <h3>Forgot Password</h3>

            
              <ion-item>
                <ion-input
                  type="email"
                  placeholder="Email"
                  v-model="user.email"
                />
              </ion-item>

            <ion-button type="submit">Reset password</ion-button>

            <p class="SignUp">
              <router-link to="/">Back to Sign In</router-link>
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
  name: "ForgotPassword",
  components: {
    IonContent,
    // IonHeader,
    IonInput,
    IonCard,
    IonItem,
    IonButton,
    IonPage,
    // IonTitle,
    // IonToolbar
  },
  data() {
    return {
      user: {
        email: "",
      },
    };
  },
  methods: {
    forgetPassword() {
      firebase
        .auth()
        .sendPasswordResetEmail(this.user.email)
        .then(() => {
          alert("Check your registered email to reset the password!");
          this.user = {
            email: "",
          };
          this.$router.push({ path: "/" });
        })
        .catch((error) => {
          alert(error);
        });
    },
  },
});
</script>