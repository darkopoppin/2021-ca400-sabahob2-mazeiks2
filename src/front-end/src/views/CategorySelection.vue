<template>
  <ion-page>
      <ion-header>
      <ion-title size="small" class="component-title">Please select some preferences for CiteC to know you better! </ion-title>
    </ion-header>
  <ion-content>
  <ion-card class="card">
    <ion-grid>
      <ion-row>
      <ion-col class= "columns">
        <ion-button class='category' v-for="(item,key) in categories" v-bind:key="item"
          @click="openModal(key)"> {{key}}
        </ion-button>
      </ion-col>
      </ion-row>
    </ion-grid>
  </ion-card>
  </ion-content>
  </ion-page>
</template>


<script>
import {
  IonPage,
  IonButton,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
  IonCard,
  modalController
} from "@ionic/vue";
import Modal from "./Modal.vue";
import { defineComponent } from "vue";
import categories from "../../categories";


export default defineComponent({
  components: { IonPage, IonButton, IonCard, IonGrid, IonRow, IonCol, IonContent },
  data() {
    return { 
      categories: categories,
      currentModal: null };
  },
  methods: {
    async openModal(category) {
      const modal = await modalController
        .create({
          component: Modal,
          cssClass: "my-modal",
          componentProps: {
            values: categories[category],
            title: "Category selection",
            close: () => this.closeModal(),
          },
        })
      this.currentModal = modal;
      return modal.present();
    },
    closeModal() {
      if (this.currentModal) {
        this.currentModal.dismiss().then(() => {
          this.currentModal = null;
        });
      }
    },
  },
});
</script>

<style scoped>
.component-title{
  text-align: center;
  font-size: x-large;
}
.card {
  position: relative;
  --background: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
  padding: 40px 55px 45px 55px;
  border-radius: 15px;
  transition: all .3s;
}
.columns {
  text-align: center;
}
.category {
  width: 40%;
  min-width: fit-content;
  margin-top: 5%;
  margin-left: 5%;
  margin-right: 5%;
}

.homeButton {
  width: 40%;
  min-width: fit-content;
  margin-left: 30%;
  margin-right: 30%;
  margin-top: 10%;
  --background: black;
}

</style>