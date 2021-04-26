<template>
  <ion-page>
    <ion-content>
      <ion-card class="card">
        <form @submit.prevent="userRegistration">
          <h3 class="header">Sign Up</h3>

          <ion-item class="input">
            <ion-input type="text" v-model="user.name" placeholder="Name" />
          </ion-item>

          <ion-item class="input">
            <ion-input type="email" v-model="user.email" placeholder="Email" />
          </ion-item>

          <ion-item class="input">
            <ion-input
              type="password"
              v-model="user.password"
              placeholder="Password"
            />
          </ion-item>

          <ion-button type="submit" class="submit-button"> Sign Up </ion-button>

          <p class="link-back">
            Already registered
            <router-link to="/SignIn">sign in?</router-link>
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
import { auth, persistence } from "../firebase";

export default defineComponent({
  name: "SignUp",
  components: {
    IonContent,
    // IonHeader,
    IonPage,
    // IonTitle,
    // IonToolbar,
    IonButton,
    IonCard,
    IonInput,
    IonItem,
  },
  data() {
    return {
      user: {
        name: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    userRegistration() {
        auth
        .setPersistence(persistence.LOCAL)
        .then(() => {
          return auth
            .createUserWithEmailAndPassword(this.user.email, this.user.password)
            .then((res) => {
              res.user
                .updateProfile({
                  displayName: this.user.name,
                })
                .then(() => {
                  this.$router.push("/categorySelection");
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