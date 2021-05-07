<template>
  <ion-page>
    <ion-header>
      <ion-title size="small" class="component-title"
        >Plan your adventure!
      </ion-title>
    </ion-header>
    <ion-content>
      <ion-card class="card">
        <form>
          <ion-item>
            <ion-label> {{ address }}</ion-label>
            <ion-button @click="openModal()"
              ><ion-icon :icon="locateOutline" />
            </ion-button>
          </ion-item>
          <ion-item>
            <ion-label>Start time:</ion-label>
            <ion-datetime
              display-format="HH:mm"
              minute-values="0,15,30,45"
              v-model="startTime"
              @ionChange="updateStartTime(startTime)"
            ></ion-datetime>
          </ion-item>
          <ion-item>
            <ion-label>End time:</ion-label>
            <ion-datetime
              display-format="HH:mm"
              minute-values="0,15,30,45"
              v-model="endTime"
              @ionChange="updateEndTime(endTime)"
            ></ion-datetime>
          </ion-item>
          <ion-button v-on:click="submitPlan()"> Plan it! </ion-button>
        </form>
      </ion-card>
    </ion-content>
  </ion-page>
</template>

<script>
import { Geolocation } from "@ionic-native/geolocation";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonButton,
  IonCard,
  IonDatetime,
  IonIcon,
  IonLabel,
  IonItem,
  onIonViewWillEnter,
  modalController,
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
import MapModal from "./MapModal.vue";
import { locateOutline } from "ionicons/icons";
import { auth } from "../firebase";

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
    IonIcon,
    IonLabel,
    IonItem,
  },
  setup() {
    return {
      locateOutline,
    };
  },
  data() {
    return {
      isLoading: true,
      lat: 0,
      lng: 0,
      address: "loading",
      coOrdinates: { lat: 0, lng: 0 },
      startTime: "00:00",
      endTime: "02:00",
    };
  },
  created() {
    onIonViewWillEnter(() => {
      const time = new Date();
      this.startTime = time.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
      });
      let futureTime = time.setTime(time.getHours() + 5);
      if (futureTime > 24) {
        futureTime = futureTime - 24;
        if (futureTime < 10) {
          futureTime = "0" + futureTime;
        }
      } else if (futureTime < 10) {
        futureTime = "0" + futureTime;
      }
      this.endTime = futureTime.toString() + this.startTime.slice(2);
      const options = {
        useLocale: true,
        maxResults: 5,
      };
      // gets user location using ionic geolocation
      Geolocation.getCurrentPosition(options)
        .then((geoPosition) => {
          this.lat = geoPosition.coords.latitude;
          this.lng = geoPosition.coords.longitude;
          this.coOrdinates["lat"] = this.lat;
          this.coOrdinates["lng"] = this.lng;
          this.getAddressData(this.lat, this.lng);
        })
        .catch((err) => {
          console.log(err);
          this.isLoading = false;
          this.showErrorAlert();
        });
    });
  },
  methods: {
    getAddressData(lat, lng) {
      axios
        .get(
          `https://maps.google.com/maps/api/geocode/json?latlng=${lat},${lng}&key=${"AIzaSyAidt7QaA1ZsyKRK23PDYWas-Y2heHZkAQ"}`
        )
        .then((response) => {
          this.address = response.data.results[0]["formatted_address"];
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async openModal() {
      const modal = await modalController.create({
        component: MapModal,
        cssClass: "my-modal",
        componentProps: {
          location: this.coOrdinates,
          close: (data) => this.closeModal(data),
        },
      });
      this.currentModal = modal;
      return modal.present();
    },
    closeModal(data) {
      this.coOrdinates = data;
      this.getAddressData(data["lat"], data["lng"]);
      if (this.currentModal) {
        this.currentModal.dismiss().then(() => {
          this.currentModal = null;
        });
      }
    },
    submitPlan() {
      const userUid = auth.currentUser.uid;
      axios
        .get("http://127.0.0.1:5144/planner", {
          params: {
            "user_id": userUid,
            "start_time": this.startTime,
            "end_time": this.endTime,
            latitude: this.lat,
            longitude: this.lng,
          },
        })
        .then((response) => {
          this.$router.push({
            name: "PlannerResults",
            params: {
              begin: this.startTime,
              end: this.endTime,
              userLocation: JSON.stringify(this.coOrdinates),
              businesses: JSON.stringify(response.data),
            },
          });
        })
        .catch((error) => console.log(error));
    },
    updateStartTime(newTime) {
      this.startTime = newTime;
    },
    updateEndTime(newTime) {
      this.endTime = newTime;
    },
  },
});
</script>
