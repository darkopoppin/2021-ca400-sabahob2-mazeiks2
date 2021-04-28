<template>
  <ion-page>
      <ion-header>
        <ion-title class="component-title">Planner! </ion-title>
      </ion-header>
    <ion-content>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
} from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "planner",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
  }
});
</script>