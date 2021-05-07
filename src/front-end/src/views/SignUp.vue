<template>
  <ion-page>
    <ion-content>
      <ion-card class="card">
        <form @submit.prevent="userRegistration">
          <h3 class="header">Sign Up</h3>

          <ion-item class="input">
            <ion-input type="number" v-model="user.age" placeholder="age" />
          </ion-item>

          <ion-item class="input">
            <ion-label>Gender</ion-label>
            <ion-select placeholder="Select" v-model="user.gender">
              <ion-select-option value="Female">Female</ion-select-option>
              <ion-select-option value="Male">Male</ion-select-option>
            </ion-select>
          </ion-item>

          <ion-item class="input">
            <ion-input type="text" v-model="user.location" placeholder="Primary city" />
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
  IonPage,
  IonSelect,
  IonSelectOption,
  IonLabel,
  IonButton,
  IonCard,
  IonInput,
  IonItem,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth, persistence, db } from "../firebase";

export default defineComponent({
  name: "SignUp",
  components: {
    IonContent,
    IonPage,
    IonSelect,
    IonSelectOption,
    IonLabel,
    IonButton,
    IonCard,
    IonInput,
    IonItem,
  },
  data() {
    return {
      user: {
        age: Number,
        gender: "",
        location: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    userRegistration() {
      if (this.user.age == "" || this.user.gender == "" || this.user.location == ""){
        alert("fill in all inputs!")
      }
      else{
      auth.setPersistence(persistence.LOCAL).then(() => {
        return auth
          .createUserWithEmailAndPassword(this.user.email, this.user.password)
          .then((res) => {
            db.collection("users").doc(res.user.uid).set({
              age: parseInt(this.user.age),
              gender: this.user.gender,
              location: this.user.location,
              "liked_categories": {},
              visited: {}
            })
            this.$router.push("/home/categories");
          })
          .catch((error) => {
            alert(error.message);
          })
      });
    }
  },
  },
});
</script>