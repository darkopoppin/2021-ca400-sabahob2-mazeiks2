<template>
  <ion-page>
    <ion-content>
      <ion-card>
        <form @submit.prevent="userRegistration">
          <h3>Sign Up</h3>

          <ion-item>
            <ion-input type="text" v-model="user.name" placeholder="Name" />
          </ion-item>

          <ion-item>
            <ion-input type="email" v-model="user.email" placeholder="Email" />
          </ion-item>

          <ion-item>
            <ion-input
              type="password"
              v-model="user.password"
              placeholder="Password"
            />
          </ion-item>

          <ion-button type="submit"> Sign Up </ion-button>

          <p>
            Already registered
            <router-link to="/">sign in?</router-link>
          </p>
        </form>
      </ion-card>
    </ion-content>
  </ion-page>
</template>


<script>
import {
  IonContent,
  IonPage,
  IonButton,
  IonCard,
  IonInput,
  IonItem,
} from "@ionic/vue";
import { defineComponent } from "vue";
import firebase from "firebase/app";

export default defineComponent({
  name: "SignUp",
  components: {
    IonContent,
    IonPage,
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
      firebase
        .auth()
        .createUserWithEmailAndPassword(this.user.email, this.user.password)
        .then((res) => {
          res.user
            .updateProfile({
              displayName: this.user.name,
            })
            .then(() => {
              this.$router.push("/Home");
            });
        })
        .catch((error) => {
          alert(error.message);
        });
    },
  },
});
</script>