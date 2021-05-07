<template>
  <ion-page>
    <ion-content>
      <ion-item-sliding v-for="(item, id) in selectedBusinesses" :key="item">
        <ion-item-options side="end">
          <ion-item-option color="secondary" @click="loadOther(id)"
            >Load new</ion-item-option
          >
          <ion-item-option color="primary" @click="openModal(id)">Visited!</ion-item-option>
        </ion-item-options>
        <ion-item>
          <ion-card>
            <ion-card-header>
              <ion-card-title class="ion-text-center">{{
                item.name
              }}</ion-card-title>
              <ion-card-subtitle class="ion-text-center">{{
                item.address1
              }}</ion-card-subtitle>
            </ion-card-header>
            <ion-card-content>
              <ion-item
                v-for="tag in item.categories"
                v-bind:key="tag"
                class="tags"
              >
                {{ tag }}</ion-item
              >
              <star-rating
                :star-size="20"
                :increment="0.5"
                :rating="item.rating"
                :read-only="true"
                :show-rating="false"
              ></star-rating>
              <ion-button class="yelp" @Click="redirect(item.url)">
                <ion-icon :icon="globeOutline" />
                <ion-label>Yelp</ion-label>
              </ion-button>
            </ion-card-content>
          </ion-card>
        </ion-item>
        <div class="line line0" :style="{ marginLeft: '50%' }"> 
        <ion-chip class="information">  {{Math.round(item.distance)}}km or {{Math.round(item.time)}} minutes! </ion-chip></div>
      </ion-item-sliding>
      <ion-list class="mapButtons">
      <ion-button v-on:click="googleMaps()">
        <ion-label> Open in Google Maps </ion-label>
      </ion-button>
      <ion-button v-on:click="openTheMap()">
        <ion-label> Open Preview Map! </ion-label>
      </ion-button>
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonContent,
  // IonHeader,
  IonPage,
  IonButton,
  IonCard,
  IonCardTitle,
  IonCardHeader,
  IonCardContent,
  IonCardSubtitle,
  IonIcon,
  IonItem,
  IonItemSliding,
  IonItemOption,
  IonItemOptions,
  IonLabel,
  // IonTitle,
  IonChip,
  modalController,
} from "@ionic/vue";
import StarRating from "vue-star-rating";
import { globeOutline } from "ionicons/icons";
import { defineComponent } from "vue";
import RatingModal from "../views/RatingModal.vue";

export default defineComponent({
  name: "PlannerResults",
  components: {
    IonContent,
    // IonHeader,
    IonPage,
    IonCard,
    IonItem,
    IonItemSliding,
    IonItemOption,
    IonItemOptions,
    IonCardTitle,
    IonCardHeader,
    IonCardContent,
    IonCardSubtitle,
    IonIcon,
    IonLabel,
    IonButton,
    // IonTitle,
    IonChip,
    StarRating,
  },
  setup() {
    return {globeOutline}
  },
  props: {
    begin: {
    default: "10:00",
    type: String
  },
   end: {
     default: "15:00",
     type: String
   }, userLocation: {
     default: "{lat: 53.213, lng: -6.5332}",
     type: String
   }, 
   businesses: {
     default: "{}",
     type: String
   }},
  created() {
    const jsonBusinesses = JSON.parse(this.businesses)
    for (const key in jsonBusinesses) {
      this.selectedBusinesses[
        jsonBusinesses[key]["position"]
      ] = jsonBusinesses[key];
    }
  },
  data() {
    return {
      rating: 0,
      markers: {},
      selectedBusinesses: {},
      user: "",
    };
  },
  methods: {
    redirect(url){
      window.open(url, '_blank');
    },
    async openModal(id) {
      const selected = this.selectedBusinesses[id]
      const modal = await modalController.create({
        component: RatingModal,
        cssClass: "my-modal",
        componentProps: {
          business: selected,
          close: (data) => this.closeModal(data),
        },
      });
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
    loadOther(i) {
      for (const key in this.secondaryBusinesses) {
      if (this.secondaryBusinesses[key]["position"] == i){
        this.selectedBusinesses[i] = this.secondaryBusinesses[key]
        delete this.secondaryBusinesses[key]
        break;
        }
      }
    },
    openTheMap() {
      for (const key in this.selectedBusinesses){
        const formatedCoords = {}
        formatedCoords["lat"] = this.selectedBusinesses[key]["coordinates"][0]
        formatedCoords["lng"] = this.selectedBusinesses[key]["coordinates"][1]
        this.markers[key] = formatedCoords
      }
      this.$router.push({name:"Map" , params:{markers : JSON.stringify(this.markers), userLocation : this.userLocation}});
    },
    googleMaps(){
      const userLocation = JSON.parse(this.userLocation)
      let mapsUrl = 'https://www.google.com/maps/dir/'
      mapsUrl += userLocation["lat"] + "," + userLocation["lng"] + "/"
      for (const key in this.selectedBusinesses){
        let formatedString = ""
        formatedString += this.selectedBusinesses[key]["coordinates"][0] + ","
        formatedString += this.selectedBusinesses[key]["coordinates"][1] + "/"
        mapsUrl += formatedString
      }
    this.redirect(mapsUrl)
    }
  },
});
</script>
<style scoped>
.component-title {
  background-color:lightblue;
  color: black;
}
@media only screen and (max-width: 800px) {
  ion-card {
    width:100%;
    display:block;
    margin: 0 auto;
    text-align: center;
    min-width: fit-content;
    border-radius: 4px;
    background: linear-gradient(to bottom right, #666699 -16%, #99ccff 73%);
  }
}
@media only screen and (min-width: 801px) {
  ion-card {
    display: inline-block;
    margin-left: 35%;
    width: 30% !important;
    text-align: center;
    border-radius: 4px;
    background: linear-gradient(to bottom right, #666699 -16%, #99ccff 73%);
  }
}
.tags {
  display: inline-block;
}
.information{
  display: inline-table;
  width: 150px;
}
.mapButtons{
  background-color: rgb(246, 241, 242);
  text-align: center;
}
.yelp {
  color: white;
  --background: darkred;
}
ion-content{
  --ion-background-color: rgb(246, 241, 242);
}
ion-item {
  --background: transparent;
  --border-style: none;
}
vue-star-rating{
  display: block;
  text-align: center;
}
ion-card-header {
  --background: #c9efef;
}
.line {
  margin-left: 1.6%;
  height: 75px;
  width: 1px;
  border: 0.5px solid #c1bfbf;
  color: black;
  display: flex;
}

ion-card-title {
  color: black;
}
</style>