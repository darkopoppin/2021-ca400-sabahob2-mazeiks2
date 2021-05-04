<template>
  <ion-page>
    <ion-tabs>
      <ion-tab-bar v-if="isMobile()" slot="bottom">
        <ion-tab-button tab="planner" href="/Planner">
          <ion-icon :icon="calendar"></ion-icon>
          <ion-label>Planner</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="Recommender" href="/Recommender">
          <ion-icon :icon="bulb"></ion-icon>
          <ion-label>Recommendations</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="settings" href="/Settings">
          <ion-icon :icon="settings"></ion-icon>
          <ion-label>Settings</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="category" href="/Categories">
          <ion-icon :icon="list"></ion-icon>
          <ion-label>Categories</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
      <ion-tab-bar v-else slot="top">
        <ion-title class="title">Welcome to CiteCy!</ion-title>
        <ion-tab-button tab="planner" href="/Planner">
          <ion-icon :icon="calendar"></ion-icon>
          <ion-label>Planner</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="Recommender" href="/Recommender">
          <ion-icon :icon="bulb"></ion-icon>
          <ion-label>Recommendations</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="settings" href="/Settings">
          <ion-icon :icon="settings"></ion-icon>
          <ion-label>Settings</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="category" href="/Categories">
          <ion-icon :icon="list"></ion-icon>
          <ion-label>Categories</ion-label>
        </ion-tab-button>
      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonTabBar,
  IonTabButton,
  IonTabs,
  IonIcon,
  IonLabel,
  IonTitle,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { list, calendar, settings, bulb } from "ionicons/icons";

export default defineComponent({
  name: "Home",
  components: {
    IonPage,
    IonTabBar,
    IonTabButton,
    IonTabs,
    IonIcon,
    IonLabel,
    IonTitle,
  },
  setup() {
    return {
      list,
      calendar,
      settings,
      bulb,
    };
  },
  data() {
    return {
      user: null,
      loggedIn: false,
    };
  },
  methods: {
    isMobile() {
      if (screen.width <= 760) {
        return true;
      } else {
        return false;
      }
    },
  },
});
</script>

<style scoped>
.title {
  text-align: left;
}
</style>