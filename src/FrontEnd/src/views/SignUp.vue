<template>
  <ion-page>
    <ion-content>
      <ion-card class="card">
        <form @submit.prevent="userRegistration">
          <h3 class="header">Sign Up</h3>

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

          <ion-button type="submit" class="submit-button"> Sign Up </ion-button>

          <p class="SignIn">
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
  IonPage,
  IonButton,
  IonCard,
  IonInput,
  IonItem,
} from "@ionic/vue";
import { defineComponent } from "vue";
import firebase from "firebase/app";
import { auth } from "../firebase";

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
        auth
        .setPersistence(firebase.auth.Auth.Persistence.LOCAL)
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

<style scoped>
.submit-button{
  margin-top: 5%;
}

.SignIn{
  text-align: center;
  text-decoration: none;
  font-size: 15px;
  padding-bottom: 1%;
  padding-top: 10%;
  color: #7a7a7a;
  margin: 0;
}
</style>