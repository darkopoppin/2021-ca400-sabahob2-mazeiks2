<template>
  <ion-page>
    <ion-header>
      <ion-title class="component-title"> your personalised recommendations!</ion-title>
    </ion-header>
    <ion-content>
      <ion-loading
        :is-open="isOpenRef"
        cssClass="my-custom-class"
        message="Loading recommendations...!"
        :duration="timeout"
        @didDismiss="setOpen(false)"
      >
      </ion-loading>
      <ion-grid>
        <ion-row>
          <ion-col size="12">
            <ion-card v-for="item in items" :key="item">
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
                  v-bind:key="tag.title"
                  class="tags"
                >
                  {{ tag.title }}</ion-item
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
          </ion-col>
        </ion-row>
      </ion-grid>
      <ion-infinite-scroll
        @ionInfinite="loadData($event)"
        threshold="100px"
        id="infinite-scroll"
        :disabled="isDisabled"
      >
        <ion-infinite-scroll-content
          loading-spinner="bubbles"
          loading-text="Loading more data..."
        >
        </ion-infinite-scroll-content>
      </ion-infinite-scroll>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonHeader,
  IonContent,
  IonInfiniteScroll,
  IonInfiniteScrollContent,
  IonItem,
  IonPage,
  onIonViewWillEnter,
  IonCard,
  IonIcon,
  IonButton,
  IonCardContent,
  IonCardTitle,
  IonCardSubtitle,
  IonCardHeader,
  IonTitle,
  IonLabel,
  IonGrid,
  IonRow,
  IonCol,
  IonLoading,
} from "@ionic/vue";
import { defineComponent, ref } from "vue";
import StarRating from "vue-star-rating";
import { globeOutline } from "ionicons/icons";
import axios from "axios";
import { auth } from "../firebase";

export default defineComponent({
  name: "Recommender",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonIcon,
    IonButton,
    IonInfiniteScroll,
    IonInfiniteScrollContent,
    IonItem,
    IonCard,
    IonCardContent,
    IonCardTitle,
    IonCardSubtitle,
    IonCardHeader,
    IonTitle,
    IonLabel,
    IonGrid,
    IonRow,
    IonCol,
    StarRating,
    IonLoading,
  },
  props: {
    timeout: { type: Number, default: 10000 },
  },
  setup() {
    const isOpenRef = ref(false);
    const setOpen = (state) => isOpenRef.value = state;

    const isDisabled = ref(false);
    const recommendations = [];
    const items = ref([]);

    const pushData = () => {
      let max = 0;
      let min = 0;
      const left = recommendations.length - items.value.length;
      if (left < 15) {
        max = items.value.length + left;
        min = max - left;
      } else {
        max = items.value.length + 15;
        min = max - 15;
      }
      for (let i = min; i < max; i++) {
        items.value.push(recommendations[i]);
      }
    };

    const loadData = (ev) => {
      setTimeout(() => {
        pushData();
        console.log("Loaded data");
        ev.target.complete();

        // App logic to determine if all data is loaded
        // and disable the infinite scroll
        if (items.value.length == recommendations.length) {
          console.log("disable");
          ev.target.disabled = true;
        }
      }, 500);
    };

    const recommend = () => {
      const userUid = auth.currentUser.uid;
      axios
        .get("http://127.0.0.1:5144/recommender", {
          params: { "user_id": userUid },
        })
        .then((response) => {
          setOpen(false)
          const data = response.data;
          for (const key in data) {
            recommendations.push(data[key]);
          }
          pushData();
        })
        .catch((error) => {
          console.log(error);
          setOpen(false)
        });
    };
    onIonViewWillEnter(() => {
      setOpen(true)
      recommend();
    });

    return {
      isDisabled,
      loadData,
      items,
      globeOutline,
      isOpenRef,
      setOpen,
    };
  },
  methods: {
    redirect(url) {
      window.location.href = url;
    },
  },
});
</script>
<style scoped>
@media only screen and (max-width: 800px) {
  ion-card {
    text-align: center;
    min-width: fit-content;
    border-radius: 4px;
    background: linear-gradient(to bottom right, #666699 -16%, #99ccff 73%);
    box-shadow: 5px 14px 80px rgba(34, 35, 58, 0.2);
  }
}
@media only screen and (min-width: 801px) {
  ion-card {
    display: inline-block;
    width: 30% !important;
    text-align: center;
    border-radius: 4px;
    background: linear-gradient(to bottom right, #666699 -16%, #99ccff 73%);
    box-shadow: 5px 14px 80px rgba(34, 35, 58, 0.2);
  }
}
.tags {
  color: black;
  font-size: large;
  display: inline-block;
}
.yelp {
  color: white;
  --background: darkred;
}
vue-star-rating{
  display: block;
  text-align: center;
}
ion-content{
  --ion-background-color: rgb(246, 241, 242);
}
ion-item {
  --background: transparent;
  --border-style: none;
}
ion-card-header {
  --background: #c9efef;
}
ion-card-title {
  color: black;
}
ion-segment-button {
  display: flex;
}
</style>
