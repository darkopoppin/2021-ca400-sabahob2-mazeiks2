<template>
  <ion-page>
    <ion-content>
      <ion-card class="card">
        <form @submit.prevent="forgetPassword">
          <h3 class="header">Forgot Password</h3>

            
              <ion-item class="input">
                <ion-input
                  type="email"
                  placeholder="Email"
                  v-model="user.email"
                />
              </ion-item>

          <ion-button type="submit" class="submit-button" >Reset password</ion-button>

          <p class="link-back">
            Back to
            <router-link to="/SignIn">Sign In</router-link>
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
import { auth } from "../firebase";

export default defineComponent({
  name: "ForgotPassword",
  components: {
    IonContent,
    IonInput,
    IonCard,
    IonItem,
    IonButton,
    IonPage,
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
        auth
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