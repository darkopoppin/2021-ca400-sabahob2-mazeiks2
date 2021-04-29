<template>
  <ion-page>
    <ion-header>
      <ion-title class="component-title">Planner! </ion-title>
    </ion-header>
    <ion-content>
      <ion-card class="card">
        <form>
          <ion-item>
            <ion-input placeholder="Location"></ion-input>
          </ion-item>
          <ion-item>
            <ion-label>Start time:</ion-label>
            <ion-datetime display-format="HH:mm" minute-values="0,15,30,45"></ion-datetime>
          </ion-item>
          <ion-item>
            <ion-label>End time:</ion-label>
            <ion-datetime display-format="HH:mm" minute-values="0,15,30,45"></ion-datetime>
          </ion-item>
          <ion-button v-on:click="getLocation()"> Sign In </ion-button>
        </form>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import { Geolocation } from '@ionic-native/geolocation';
import { IonContent, IonHeader, IonPage, IonTitle, IonButton, IonCard, IonDatetime, IonLabel, IonItem, IonInput } from "@ionic/vue";
import { defineComponent } from "vue";



export default defineComponent({
  name: "planner",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonTitle,
    IonButton,
    IonCard,
    IonDatetime,
    IonLabel,
    IonItem,
    IonInput,
  },
  methods:{  
    getLocation() {
      Geolocation.getCurrentPosition(this.options)
        .then(geoPosition => {
          const coordinates = {
            lat: geoPosition.coords.latitude,
            lng: geoPosition.coords.longitude
          };

          console.log(coordinates.lat , coordinates.lng); // Always prints the old coordinate even if the device is in a different location
        })
        .catch(err => {
          this.isLoading = false;
          this.showErrorAlert();
        });

  },
  },
});
</script>