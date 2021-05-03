<template>
  <ion-page>
  <button class="return" @click="dismiss"> Cancel</button>
  <ion-content >
    <ion-list style="display: inline-block;">
      <ion-item style="display: inline-block; width:50%;" lines="none" v-for="(value) in values" v-bind:key="value">
        <ion-chip v-on:click="selected(value)" v-bind:class="{selected: selectedCategories[value]}">{{ value }}</ion-chip>
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
  // IonLabel,
  IonPage,
  IonButton,
  IonChip
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
import { auth } from "../firebase";

export default defineComponent({
  name: "Modal",
  props: {
    title: { type: String, default: "Super Modal" },
    values: {type: Array},
    close: { type: Function }
  },
  data () {
    return { selectedCategories: {}}
  },
  methods: {
    selected(value) {
      this.selectedCategories[value] = !this.selectedCategories[value];
    },
    submit() {
      const finalCategories = Object.keys(this.selectedCategories).filter(k => this.selectedCategories[k] === true)
      const user = auth.currentUser;
      axios.post('http://127.0.0.1:5000/categorySelection', { params: [finalCategories, user.uid]}).then(response => console.log(response)).catch(error => console.log(error))
    },
    dismiss() {
      this.close()
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
  color: green;
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