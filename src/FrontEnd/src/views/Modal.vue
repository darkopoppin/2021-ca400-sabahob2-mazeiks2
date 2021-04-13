<template>
  <ion-content >
      <button @click="dismiss"> Cancel</button>
    <ion-list>
      <ion-item v-for="(value) in values" v-bind:key="value">
        <ion-chip v-on:click="selected(value)" v-bind:class="{selected: selectedCategories[value]}">{{ value }}</ion-chip>
      </ion-item>
    </ion-list>

    <ion-button v-on:click= "submit()"> Submit</ion-button>
  </ion-content>
</template>

<script>
import {
  IonContent,
  IonList,
  IonItem,
  // IonLabel,
  IonButton,
  IonChip
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
import firebase from "firebase";

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
    created() {
      // let alreadySelected = []
      //axios.get('http://127.0.0.1:5000/categorySelection', {params: user.uid}).then(response => console.log(response)).catch(error => console.log(error))
      // alreadySelected = response
    },
    selected(value) {
      this.selectedCategories[value] = !this.selectedCategories[value];
    },
    submit() {
      const finalCategories = Object.keys(this.selectedCategories).filter(k => this.selectedCategories[k] === true)
      console.log(finalCategories)
      const user = firebase.auth().currentUser;
      axios.post('http://127.0.0.1:5000/categorySelection', { params: [finalCategories, user.uid]}).then(response => console.log(response)).catch(error => console.log(error))
    },
    dismiss() {
      this.close()
    },
  },
  components: { IonContent, IonList, IonButton, IonItem, IonChip },
});
</script>

<style scoped>

.selected {
  color: red;
}

.Button {
  display: block;
  height: 100px;
  width: 100px;
  border-radius: 50%;
  border: 1px solid red;
}

.myModal {
background-color: cornflowerblue !important;
color: Black;
position: absolute !important;
width: 600px !important;
height: 570px !important;
top: 0 !important;
bottom: 0 !important;
left: 0 !important;
right: 0 !important;
margin: auto !important;
border-style: solid;
border-width: 1px;
border-radius: 10px !important;
border-color: black;
}

</style>