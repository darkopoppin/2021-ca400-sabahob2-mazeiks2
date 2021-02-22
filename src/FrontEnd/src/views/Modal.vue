<template>
  <ion-page>
    <ion-grid>
      <ion-item>
      <ion-button class="Button" >Something</ion-button>
      <ion-button class="Button" >Something</ion-button>
      <ion-button class="Button" >Something</ion-button>
      </ion-item>
      <ion-item>
      <ion-button class="Button" >Something</ion-button>
      <ion-button class="Button" >Something</ion-button>
      </ion-item>
    </ion-grid>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonGrid,
  IonItem,
  IonButton,
} from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Modal",
  props: {
    title: { type: String, default: "Super Modal" },
  },
  data() {
    return {
      content: "Content",
    };
  },
  created() {
    console.log("here")
  },
  components: { IonPage, IonGrid, IonItem, IonButton, },
});
</script>

<style scoped>
.Button {
  display: block;
  height: 100px;
  width: 100px;
  border-radius: 50%;
  border: 1px solid red;
}
</style>