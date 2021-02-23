<template>
  <ion-page>
    <ion-list>
      <ion-item>
      <ion-button @click="openModal">Active Life</ion-button>
      </ion-item>
      <ion-item>
      <ion-button @click="openModal">Local Flavor</ion-button>
      </ion-item>
      <ion-item>
      <ion-button @click="openModal">NightLife</ion-button>
      </ion-item>
      <ion-item>
      <ion-button @click="openModal">Restaurants</ion-button>
      </ion-item>
      <ion-item>
      <ion-button @click="openModal">Arts & Entertainment</ion-button>
      </ion-item>
    </ion-list>
    <ion-button @click="() => this.$router.push('/Home')"> Home  </ion-button>
  </ion-page>
</template>


<script>
import { IonButton, IonPage, modalController, IonList, IonItem } from '@ionic/vue';
import Modal from './Modal.vue'
import { useRouter } from 'vue-router';


export default {
  components: { IonButton, IonPage, IonList, IonItem },
  methods: {
    setup() {
      const router = useRouter();
      return { router };
    },
    async openModal() {
      const modal = await modalController
        .create({
          component: Modal,
          cssClass: 'my-custom-class',
          componentProps: {
            title: 'New Title'
          },
        })
      return modal.present();
    },
  },
}
</script>