<template>
  <ion-page>
    <button class="return" @click="dismiss">Cancel</button>
    <ion-content>
      <ion-list style="display: inline-block">
        <ion-item
          style="display: inline-block; width: 50%"
          lines="none"
          v-for="value in values"
          v-bind:key="value">
          <ion-chip
            v-on:click="selected(value)"
            v-bind:class="{ selected: selectedCategories[value] }"
            >{{ value }}
            </ion-chip>
        </ion-item>
      </ion-list>

      <ion-button class="button" v-on:click="submit()"> Submit</ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import {
  IonContent,
  IonList,
  IonItem,
  IonPage,
  IonButton,
  IonChip,
} from "@ionic/vue";
import { defineComponent } from "vue";
import { auth, db } from "../firebase";

export default defineComponent({
  name: "Modal",
  props: {
    title: { type: String, default: "Super Modal" },
    values: { type: Array },
    close: { type: Function },
  },
  data() {
    return { selectedCategories: {} };
  },
  created() {
    const user = auth.currentUser;
    db.collection("users")
      .doc(user.uid)
      .get()
      .then((doc) => {
        if (doc.exists) {
          doc.data()["liked_categories"].forEach(category => {
            this.selectedCategories[category] = true;
          });
        } else {
          // doc.data() will be undefined in this case
          console.log("No such document!");
        }
      })
      .catch((error) => {
        console.log("Error getting document:", error);
      });
  },
  methods: {
    selected(value) {
      this.selectedCategories[value] = !this.selectedCategories[value];
    },
    submit() {
      const selectedCategories = Object.keys(this.selectedCategories).filter(
        (k) => this.selectedCategories[k] === true
      );
      const user = auth.currentUser;
      db.collection("users").doc(user.uid).set(
        {
          "liked_categories": selectedCategories,
        },
        { merge: true }
      );
      this.close();
    },
    dismiss() {
      this.close();
    },
  },
  components: { IonContent, IonList, IonButton, IonItem, IonChip, IonPage },
});
</script>

<style scoped>
ion-content {
  --ion-item-background: white;
  --ion-text-color: black;
}

.selected {
  color: white;
  background-color: green;
}

.return {
  height: 5%;
  color: white;
  background-color: blue;
  font-weight: 15px;
}

.button {
  width: 40%;
  min-width: fit-content;
  margin-left: 30%;
  margin-right: 30%;
  --background: blue;
}
</style>