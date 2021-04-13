<template>
  <ion-page>
    <ion-list>
      <ion-item v-for="(item,key) in categories" v-bind:key="item">
        <ion-button
          @click="openModal(key)">
        <ion-label>{{ key }}</ion-label>
        </ion-button>
      </ion-item>
    </ion-list>
    <ion-button @click="() => this.$router.push('/Home')"> Home  </ion-button>
  </ion-page>
</template>


<script>
import {
  IonButton,
  IonPage,
  modalController,
  IonList,
  IonItem,
  IonLabel
} from "@ionic/vue";
import Modal from "./Modal.vue";
import { useRouter } from "vue-router";
import { defineComponent } from "vue";
import categories from "../../categories";


export default defineComponent({
  components: { IonButton, IonPage, IonList, IonItem, IonLabel },
  data() {
    return { 
      categories: categories,
      currentModal: null };
  },
  methods: {
    setup() {
      const router = useRouter();
      return { router };
    },
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