<template>
  <ion-page>
      <ion-header>
        <ion-title size="small" class="component-title"> User Settings </ion-title>
      </ion-header>
    <ion-content>
      <ion-card class="card">
    <ion-grid>
      <ion-row>
      <ion-col class= "columns">
        <ion-button type="submit" v-on:click="logOut()"> Log out </ion-button>
        <ion-button type="submit" v-on:click="categoryScreen()"> Change categories </ion-button>
        <ion-button type="submit" v-on:click="alreadyVisited()"> Already Visited </ion-button>
        <ion-button type="submit" v-on:click="savedInterests()"> Saved </ion-button>
      </ion-col>
      </ion-row>
    </ion-grid>
  </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonContent,
  IonHeader,
  IonPage,
  IonButton,
  IonTitle,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth } from "../firebase";

export default defineComponent({
  name: "Settings",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonButton,
    IonTitle,
  },
  methods: {
    logOut() {
      auth.signOut().then(() => {
        auth.onAuthStateChanged(() => {
          this.$router.push("/SignIn");
        });
      });
    },
    categoryScreen(){
      this.$router.push({
          path: "/categories"}
      )},
  }
});
</script>

<style>
.component-title {
  background-color: white;
  color: black;
  text-align: center;
  font-size: x-large;
}
</style>