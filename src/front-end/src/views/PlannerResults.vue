<template>
  <ion-page>
    <ion-header>
      <ion-title class="component-title"> Planner results </ion-title>
    </ion-header>
    <ion-content>
      <ion-item-sliding v-for="(item, id) in selectedBusinesses" :key="item">
        <ion-item-options side="end">
          <ion-item-option @click="favorite(item)">Favorite</ion-item-option>
          <ion-item-option color="danger" @click="loadOther(id)"
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
                item.location.address1
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
        <div class="line line0" :style="{ marginLeft: '50%' }"></div>
      </ion-item-sliding>
      <ion-button>
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
  props: ["begin", "end"],
  created() {
    const start = new Date(this.begin);
    const finish = new Date(this.end);
    const timeAllocated = finish.getHours() - start.getHours();
    console.log(timeAllocated);
    for (let i = 0; i <= timeAllocated; i++) {
      this.selectedBusinesses[i] = this.businesses["b".concat(i.toString())];
      delete this.businesses["b".concat(i.toString())];
    }
    this.lastSelected = timeAllocated + 1;
  },
  data() {
    return {
      selectedBusinesses: {},
      businesses: {
        b0: {
          categories: ["British", "Coffee & Tea"],
          id: "7-jSaf5DJ7iEQlwpCRuL_A",
          location: {
            address1: "2 Merchants Arch",
          },
          name: "Hanley's Cornish Pasties",
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
          url: "https://www.google.com",
          rating: 2,
        },
      },
      user: "",
    };
  },
  methods: {
    loadOther(i) {
      console.log(this.selectedBusinesses);
      console.log(this.businesses);
      this.selectedBusinesses[i] = this.businesses[
        "b".concat(this.lastSelected.toString())
      ];
      this.lastSelected++;
    },
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
}

ion-card-title {
  color: black;
}
</style>