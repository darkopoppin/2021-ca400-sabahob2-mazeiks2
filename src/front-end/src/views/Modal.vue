<template>
  <ion-page >
      <button @click="dismiss"> Cancel</button>
    <ion-list>
      <ion-item v-for="item in categories" v-bind:key="item">
        <ion-label>{{ item.val }}</ion-label>
        <ion-checkbox
          @update:modelValue="item.isChecked = $event"
          :modelValue="item.isChecked"
        >
        </ion-checkbox>
      </ion-item>
    </ion-list>

    <ion-button v-on:click= "submit()"> Submit</ion-button>
  </ion-page>
</template>

<script>
import {
  IonPage,
  IonList,
  IonItem,
  IonCheckbox,
  IonLabel,
  IonButton,
} from "@ionic/vue";
import { defineComponent } from "vue";
import axios from "axios";
import firebase from "firebase";

export default defineComponent({
  name: "Modal",
  props: {
    title: { type: String, default: "Super Modal" },
    close: { type: Function }
  },
  data() {
    return {
      categories : [ { val: 'Acai Bowls', isChecked: true }, { val: 'Aerial Tours', isChecked: false }, { val: 'Afghan', isChecked: false }, ],
      content: "Content",
      items : ['Acai Bowls', 'Aerial Tours','Afghan','African','Airsoft','Amateur Sports Teams','Amusement Parks','Andalusian','Aquariums','Arabian','Arcades','Archery','Architectural Tours'],
    };
  },
  methods: {
    submit() {
      const user = firebase.auth().currentUser;
      console.log(user)
      axios.post('http://127.0.0.1:5000/categorySelection', {params: [this.categories, user.uid]}).then(response => console.log(response)).catch(error => console.log(error))
    },
    dismiss() {
      this.close()
    },
  },
  components: { IonPage, IonList, IonButton, IonItem, IonCheckbox, IonLabel },
});
</script>

<style scoped>
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
overflow: hidden !important;
}
</style>