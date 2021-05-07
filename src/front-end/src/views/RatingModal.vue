<template>
  <ion-page>
      <ion-header>
    <ion-title class="component-title"> Please rate your visit!</ion-title>
      </ion-header>
    <p> Your ratings help us determine what you enjoy and recommend more relevant interests to you!</p>
    <ion-content>
      <star-rating class="stars"
                :star-size="50"
                @update:rating="setRating"
                :show-rating="false"
              ></star-rating>
    </ion-content>
    
      <ion-button class="return" @click="dismiss">Cancel</ion-button>
  </ion-page>
</template>

<script>
import { IonContent, IonPage, IonTitle, IonHeader, IonButton } from "@ionic/vue";
import { defineComponent } from "vue";
import StarRating from "vue-star-rating";
import { auth, db } from "../firebase";

export default defineComponent({
  name: "RatingModal",
  props: {
    title: { type: String, default: "Super Modal" },
    business: { type: Array },
    close: { type: Function },
  },
  methods: {
    setRating(rating){
      const user = auth.currentUser;
      const businessId = this.business["id"]
      const businessCategories = this.business["categories"]
      db.collection("users").doc(user.uid).set({
            visited :
              {[businessId] : {
                categories: businessCategories,
                rating: rating
              }
            }
          },
    { merge: true })
    this.close();
    },
    dismiss() {
      this.close();
    },
  },
  components: { IonContent, IonPage, IonTitle, IonHeader, IonButton , StarRating },
});
</script>

<style scoped>
ion-title {
    text-align: center;
}
ion-content {
    text-align: center;
    padding-top: 50%
}
.stars{
    margin-top: 40%;
    justify-content: center;
    }
.return{
    border: none;
}
.my-modal {
        height: 10px;
        width: 20px;
}
</style>