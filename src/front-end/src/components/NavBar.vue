<template>
  <div class="side-menu ion-align-items-center">
    <ion-grid>
      <ion-row>
        <ion-col offset="3">
          <h3>Welcome</h3>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col offset="3">
          <ion-button>Home</ion-button>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col offset="3">
          <ion-button>Create plan</ion-button>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col offset="3">
          <ion-button>Profile</ion-button>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col offset="3">
          <ion-button>Log out</ion-button>
        </ion-col>
      </ion-row>
      <ion-row>
        <ion-col offset="3">
          ion-col
        </ion-col>
      </ion-row>
    </ion-grid>
  </div>
</template>

<script>
import {
    IonCol,
    IonGrid,
    IonRow,
    IonButton
} from "@ionic/vue";

export default {
    name: "NavSideBar",
    props: ['items'],
    components: {
        IonCol,
        IonGrid,
        IonRow,
        IonButton
    }

}
</script>

<style>
  .side-menu {
    display:flex;
    width: 30%;
  }
</style>