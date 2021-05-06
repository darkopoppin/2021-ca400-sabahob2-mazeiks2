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
  props: ["begin", "end", "userLocation"],
  created() {
    // const timeAllocated = this.end.slice(0, 2) - this.begin.slice(0, 2);
    // for (let i = 0; i <= timeAllocated; i++) {
    //   this.selectedBusinesses[i] = this.businesses["b".concat(i.toString())];
    //   delete this.businesses["b".concat(i.toString())];
    // }
    // this.lastSelected = timeAllocated + 1;
    for (const key in this.businesses) {
      this.selectedBusinesses[
        this.businesses[key]["position"]
      ] = this.businesses[key];
    }
    console.log(this.begin)
    console.log(this.userLocation)
    console.log(this.selectedBusinesses[0]);
  },
  data() {
    return {
      markers: {},
      selectedBusinesses: {},
      secondaryBusinesses: {
        b0: {
          categories: ["British", "Coffee & Tea"],
          id: "7-jSaf5DJ7iEQlwpCRuL_A",
          location: {
            address1: "2 Merchants Arch",
          },
          name: "Hanley's Cornish Pasties",
          position: 2,
          url: "https://www.google.com",
          rating: 4,
        },
        b1: {
          categories: ["Breakfast & Brunch", "Wine Bars", "British"],
          id: "Q6-jNElzY4DtsZW9R3_eRw",
          location: {
            address1: "13-17 Dawson St",
          },
          name: "The Ivy",
          position: 0,
          url: "https://www.google.com",
          rating: 3.5,
        },
        b2: {
          categories: ["British"],
          id: "kebeBhbjQyQEZwGnFkD4hQ",
          location: {
            address1: "Marks and Spencers",
          },
          name: "The Restaurant",
          position: 3,
          url: "https://www.google.com",
          rating: 3.5,
        },
        b3: {
          categories: ["Bars", "British"],
          id: "_tl10basdVmlfrWtAjuIuQ",
          location: {
            address1: "South William Street South William Street",
          },
          name: "Bar Mizu",
          position: 3,
          url: "https://www.google.com",
          rating: 3.5,
        },
        b4: {
          categories: ["British"],
          id: "pSJTbfyvcqsqonuTZVg4PQ",
          location: {
            address1: "37 Parnell Street",
          },
          name: "Bennys",
          position: 2,
          url: "https://www.google.com",
          rating: 4,
        },
        b5: {
          categories: ["British"],
          id: "gxp6HHsebumrbsg2NjhuYA",
          location: {
            address1: "3a Clanbrassil St",
          },
          name: "Favourite Fried Chicken",
          position: 4,
          url: "https://www.google.com",
          rating: 3,
        },
        b6: {
          categories: ["British"],
          id: "JFYBkTYbqURQ8V86CbRuRg",
          location: {
            address1: "Unit 4 Malpas St Lower clanbrassil St",
          },
          name: "Chicken Hut D8",
          position: 1,
          url: "https://www.google.com",
          rating: 4,
        },
        b7: {
          categories: ["British"],
          id: "GRaEBT71rtLshWnwR4WU0w",
          location: {
            address1: "40 S Richmond St",
          },
          name: "K O Kebabish",
          position: 1,
          url: "https://www.google.com",
          rating: 3,
        },
        b8: {
          categories: ["British"],
          id: "wq6UQ4JSMl-nSHyspD8JDQ",
          location: {
            address1: "Lower Mercer Street",
          },
          name: "Cusack's Restaurant",
          position: 4,
          url: "https://www.google.com",
          rating: 2,
        },
      },
      businesses: {
        b1: {
          name: "test",
          address1: "Baltimore park",
          categories: ["Bus Tours"],
          coordinates: [53.3444366, -6.2604351],
          distance: 1.095,
          id: "-7gq19hmemQzrqVLfwe0sg",
          parents: ["Tours"],
          position: 0,
          rating: 4.0,
          time: 13.15,
          url:
            "https://www.yelp.com/biz/hidden-dublin-gravediggers-ghost-bus-tour-dublin-2?adjust_creative=m3FleKsUG-1UNqJsJZid9A&utm_campaign=yelp_api_v3&utm_medium=api_v3_graphql&utm_source=m3FleKsUG-1UNqJsJZid9A",
        },
        b11: {
          name: "test",
          address1: "Baltimore park",
          categories: ["Bike tours", "Walking Tours", "Bus Tours"],
          coordinates: [53.3374334371297, -6.29585266113281],
          distance: 2.745,
          id: "6cVqoG_bmcuRCnIKlwlFhw",
          parents: ["Tours"],
          position: 1,
          rating: 4.5,
          time: 32.93333333333333,
          url:
            "https://www.yelp.com/biz/irish-day-tours-christchuch?adjust_creative=m3FleKsUG-1UNqJsJZid9A&utm_campaign=yelp_api_v3&utm_medium=api_v3_graphql&utm_source=m3FleKsUG-1UNqJsJZid9A",
        },
        b19: {
          name: "test",
          address1: "Baltimore park",
          categories: ["Architectural Tours"],
          coordinates: [53.34157, -6.23901],
          distance: 4.123,
          id: "DV7XKwQtF-3TqVcVBHCnRA",
          parents: ["Tours"],
          position: 3,
          rating: 5.0,
          time: 49.56666666666667,
          url:
            "https://www.yelp.com/biz/grayline-dublin-city-tours-dublin?adjust_creative=m3FleKsUG-1UNqJsJZid9A&utm_campaign=yelp_api_v3&utm_medium=api_v3_graphql&utm_source=m3FleKsUG-1UNqJsJZid9A",
        },
        b5: {
          name: "test",
          address1: "Baltimore park",
          categories: ["Mexican"],
          coordinates: [53.3651312, -6.2717154],
          distance: 4.247,
          id: "03U0yOXlz8ut6rO1bZc18Q",
          parents: ["Restaurants"],
          position: 2,
          rating: 2.0,
          time: 51.05,
          url:
            "https://www.yelp.com/biz/hola-amigo-dublin?adjust_creative=m3FleKsUG-1UNqJsJZid9A&utm_campaign=yelp_api_v3&utm_medium=api_v3_graphql&utm_source=m3FleKsUG-1UNqJsJZid9A",
        },
        b64: {
          name: "test",
          address1: "Baltimore park",
          categories: ["Beaches"],
          coordinates: [53.3480682373047, -6.24827003479004],
          distance: 1.332,
          id: "k9ltvySRAKivJvEzBZZzxg",
          parents: ["Active Life"],
          position: 4,
          rating: 3.0,
          time: 16.083333333333332,
          url:
            "https://www.yelp.com/biz/dollymount-strand-dublin-2?adjust_creative=m3FleKsUG-1UNqJsJZid9A&utm_campaign=yelp_api_v3&utm_medium=api_v3_graphql&utm_source=m3FleKsUG-1UNqJsJZid9A",
        },
      },
      user: "",
    };
  },
  methods: {
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
      console.log(this.userLocation)
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