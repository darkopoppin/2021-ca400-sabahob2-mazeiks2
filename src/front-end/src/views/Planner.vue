<template>
  <ion-page>
    <ion-header>
      <ion-title class="component-title">Planner! </ion-title>
    </ion-header>
    <ion-content>
      <ion-card class="card">
        <form>
          <ion-item>
            <vue-google-autocomplete
              id="map"
              ref="address"
              classname="form-control"
              placeholder="Start typing"
              v-on:placechanged="getAddressData"
            >
            </vue-google-autocomplete>
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
import { NativeGeocoder } from "@ionic-native/native-geocoder/";
import VueGoogleAutocomplete from "vue-google-autocomplete";
import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonButton,
  IonCard,
  IonDatetime,
  IonLabel,
  IonItem,
  onIonViewWillEnter,
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
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
    IonLabel,
    IonItem,
    VueGoogleAutocomplete,
  },
  data() {
    return {
      isLoading: true,
      lat: 0,
      lng: 0,
      address: "default",
      startTime: "00:00",
      endTime: "02:00",
    };
  },
  created() {
    onIonViewWillEnter(() => {
      const time = new Date()
      this.startTime = time.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit', hour12: false })
      let futureTime = time.setTime(time.getHours() + 2);
      if (futureTime > 24){
        futureTime = futureTime - 24;
        if (futureTime < 10){
          futureTime = "0" + futureTime
        }
      }
      this.endTime = futureTime.toString() + this.startTime.slice(2)
      const options = {
        useLocale: true,
        maxResults: 5,
      };
      // gets user location using ionic geolocation
      Geolocation.getCurrentPosition(this.options)
        .then((geoPosition) => {
          this.lat = geoPosition.coords.latitude;
          this.lng = geoPosition.coords.longitude;
          // if mobile is used ionic native reverse geocoder otherwise browsers use google maps API
          if (screen.width <= 760) {
            NativeGeocoder.reverseGeocode(this.lat, this.lng, options)
              .then((result) => console.log(JSON.stringify(result[0])))
              .catch((error) => console.log(error));
          } else {
            axios
              .get(`https://maps.google.com/maps/api/geocode/json?latlng=${this.lat},${this.lng}&key=${""}`)
              .then((response) => {
                this.address = response.data.results[0]["formatted_address"];
              })
              .catch((error) => {
                console.log(error);
              })
              .finally(() => (this.isLoading = false));
          }
        })
        .catch((err) => {
          console.log(err);
          this.isLoading = false;
          this.showErrorAlert();
        });
    });
  },
  methods: {
    getAddressData: function (addressData) {
      this.address = addressData;
    },
    submitPlan() {
      console.log(this.address, this.startTime, this.endTime);
      // const userUid = auth.currentUser.uid;
      // axios.get('http://127.0.0.1:5144/planner', 
      // { params: {'user_id': userUid, 'start_time': this.startTime, 'end_time': this.endTime, 'latitude': '53.3471', 'longitude': '-6.2719'} })
      // .then(response => {
      //   const data = response.data;
      //   console.log(data);
      // }).catch(error => console.log(error))
      this.$router.push({name:"PlannerResults" , params:{begin: this.startTime, end:this.endTime}});
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