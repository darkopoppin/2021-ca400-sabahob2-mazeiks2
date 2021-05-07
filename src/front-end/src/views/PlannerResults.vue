<template>
  <ion-page>
    <ion-header>
      <ion-title class="component-title"> Planner results </ion-title>
    </ion-header>
    <ion-content>
      <ion-item-sliding v-for="(item, id) in selectedBusinesses" :key="item">
        <ion-item-options side="end">
          <ion-item-option color="secondary" @click="loadOther(id)"
            >Load new</ion-item-option
          >
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
        <div class="line line0" :style="{ marginLeft: '50%' }"> {{item.distance}}km {{item.time}} time to walk</div>
      </ion-item-sliding>
      <ion-button v-on:click="openTheMap()">
        <ion-label> Open in Map! </ion-label>
      </ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonContent,
  IonHeader,
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
  IonTitle,
} from "@ionic/vue";
import StarRating from "vue-star-rating";
import { globeOutline } from "ionicons/icons";
import { defineComponent } from "vue";

export default defineComponent({
  name: "PlannerResults",
  components: {
    IonContent,
    IonHeader,
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
    IonTitle,
    StarRating,
  },
  setup() {
    return {
      globeOutline,
    };
  },
  props: ["begin", "end", "userLocation", "businesses"],
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
      markers: {},
      selectedBusinesses: {},
      user: "",
    };
  },
  methods: {
    redirect(url){
      window.open(url, '_blank');
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
    }
  },
});
</script>
<style scoped>
.component-title {
  background-color: white;
  color: black;
}
ion-card {
  background: rgb(34, 193, 195);
  background: linear-gradient(
    0deg,
    rgba(34, 193, 195, 1) 0%,
    rgba(22, 50, 48, 0.7707457983193278) 20%,
    rgba(17, 15, 10, 1) 100%,
    rgba(253, 187, 45, 1) 100%
  );
  box-shadow: 5px 14px 80px rgba(34, 35, 58, 0.2);
  width: 70%;
  margin-left: 15%;
}
.tags {
  display: inline-block;
}
.yelp {
  color: white;
  --background: darkred;
}
ion-item {
  --background: transparent;
  --border-style: none;
}
ion-card-header {
  --background: white;
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