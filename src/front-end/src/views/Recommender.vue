<template>
  <ion-page>
      <div class="main-page">
        <ion-header>
          <ion-segment @ionChange="segmentChanged($event)" style="background: #3880ff;">
            <ion-item>
              <ion-label>Pets</ion-label>
              <ion-select multiple="true">
                <ion-select-option value="bird">Bird</ion-select-option>
                <ion-select-option value="cat">Cat</ion-select-option>
                <ion-select-option value="dog">Dog</ion-select-option>
                <ion-select-option value="honeybadger">Honey Badger</ion-select-option>
              </ion-select>
            </ion-item>
          </ion-segment>
        </ion-header>
      <ion-content>
        <div class="content">
        <ion-list>
          <ion-card v-for="item in items" :key="item">
            <ion-grid>
              <ion-row>
                <ion-col>
                  <ion-card-header style="padding: 0%;">
                  <ion-card-title>{{item.name}}</ion-card-title>
                  <ion-card-subtitle>{{item.categories}}</ion-card-subtitle>
                  </ion-card-header>
                  <ion-list>
                    <ion-item>Address: {{item.location.address1}}</ion-item>
                    <ion-item>Rating: {{item.rating}}</ion-item>
                  </ion-list>
                </ion-col>
                  <ion-list>
                    <ion-thumbnail>
                      <img :src="item.photos[0]">
                    </ion-thumbnail>
                  </ion-list>
                <ion-col>
                </ion-col>
              </ion-row>
            </ion-grid>
            <ion-card-content>

            </ion-card-content>
          </ion-card>
        </ion-list>
        <ion-infinite-scroll
          @ionInfinite="loadData($event)" 
          threshold="100px" 
          id="infinite-scroll"
          :disabled="isDisabled">
        
          <ion-infinite-scroll-content
            loading-spinner="bubbles"
            loading-text="Loading more data...">
          </ion-infinite-scroll-content>
        </ion-infinite-scroll>
      </div>
      </ion-content>
      </div>
  </ion-page>
</template>

<script>
import {
  IonHeader,
  IonContent, 
  IonInfiniteScroll, 
  IonInfiniteScrollContent,
  IonList,
  IonItem,
  IonPage,
  onIonViewWillEnter,
  IonCard, 
  IonCardContent, 
  IonCardTitle,
  IonCardSubtitle,
  IonCardHeader,
  IonSegment,
  IonSelectOption,
  IonSelect,
  IonLabel,
  IonGrid,
  IonRow,
  IonCol,
  IonThumbnail
} from "@ionic/vue";

import { defineComponent, ref } from "vue";
import { auth } from "../firebase";
import axios from "axios";

export default defineComponent({
  name: "Recommender",
  components: {
    IonContent,
    IonHeader,
    IonPage,
    IonInfiniteScroll, 
    IonInfiniteScrollContent,
    IonList,
    IonItem,
    IonCard,
    IonCardContent,
    IonCardTitle,
    IonCardSubtitle,
    IonCardHeader,
    IonSegment,
    IonLabel,
    IonSelectOption,
    IonSelect,
    IonGrid,
    IonRow,
    IonCol,
    IonThumbnail,
  },
  setup() {
    const isDisabled = ref(false);
    const recommendations = [];
    const items = ref([]);
    const images = ref([]);
    console.log('Setup');
    
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
        images.value.push(recommendations[i]['photos'][0])
      }
    }

    const loadData = (ev) => {
      setTimeout(() => {
        pushData();
        console.log('Loaded data');
        ev.target.complete();

        // App logic to determine if all data is loaded
        // and disable the infinite scroll
        if (items.value.length == recommendations.length) {
          console.log('disable')
          ev.target.disabled = true;
        }
      }, 500);
    }

    let loggedIn = false;
    let userProfile = null;
    const recommend = () => {
      const userUid = userProfile.uid;
      axios.get('http://127.0.0.1:5000/recommender', 
      { params: {'user_id': userUid} })
      .then(response => {
        const data = response.data;
        for (const key in data){
          recommendations.push(data[key]);
        }
        console.log(recommendations);
        pushData();
      }).catch(error => console.log(error))
    }

    onIonViewWillEnter(() => {
      auth.onAuthStateChanged((user) => {
        if (user) {
          userProfile = user;
          loggedIn = true;
          console.log('Logged in');
          recommend();
        } else {
          user = null;
        }
      });
    });

    return {
      isDisabled,
      loadData,
      items,
      images,
      loggedIn
    }
  }
})
</script>
<style scoped>
  .main-page   {
    width: 100%;
    height: 100%;
    display: flex;
    margin-top:3%
  }
  .content {
    width: 70%;
  }
  ion-header {
    position:fixed;
    top:0;
  }

  ion-segment-button{
    display: flex;
  }
</style>
