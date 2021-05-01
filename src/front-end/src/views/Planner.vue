<template>
  <ion-page>
      <h3>Output screen!</h3>
      <ion-back-button></ion-back-button>
      <p>{{ user.displayName }}</p>


  </ion-page>
</template>

<script>
import {
  // IonContent,
  // IonHeader,
  IonPage,
  // IonTitle,
  // IonToolbar,
  IonBackButton,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth } from "../firebase";

export default defineComponent({
  name: "planner",
  components: {
    // IonContent,
    // IonHeader, pipeline test
    IonPage,
    IonBackButton,
    // IonTitle,
    // IonToolbar
  },
  data() {
    return {
      user: {},
    };
  },
  created() {
    auth.onAuthStateChanged((user) => {
      if (user) {
        this.user = user;
      } else {
        this.user = null;
      }
    });
  },
  methods: {
    return() {
      this.$router.push("/home")
    },
    recommender() {
      this.$router.push("/planner")
    },
  },
});
</script>