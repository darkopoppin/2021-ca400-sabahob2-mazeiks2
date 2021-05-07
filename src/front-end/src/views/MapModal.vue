<template>
  <ion-page>
    <ion-title class="map-title"> Drag marker to select new location </ion-title>
    <ion-content>
      <div id="map"></div>
      <ion-button class="submit-button" v-on:click="submit()"> Save location</ion-button>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonContent, IonPage, IonTitle, IonButton } from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "MapModal",
  props: {
    title: { type: String, default: "Super Modal" },
    values: { type: Array },
    location: {type : Object},
    close: { type: Function },
  },
  mounted() {
    this.mapCenter = this.location
    this.initMap();
  },
  methods: {
    initMap() {
      const myLatlng = new google.maps.LatLng(this.mapCenter); // eslint-disable-line
        const mapOptions = {
          zoom: 12,
          center: myLatlng
        }
      this.map = new google.maps.Map(document.getElementById("map"), mapOptions); // eslint-disable-line
      const marker = new google.maps.Marker({ // eslint-disable-line
        position: myLatlng,
        map: this.map,
        draggable:true,
        title:"Drag me!"
    });
    let that = this // eslint-disable-line
    function updated(location, that) {
      that.marker = location.getPosition().toJSON()
    }
    google.maps.event.addListener(marker, 'dragend', function(){ // eslint-disable-line
      updated(marker, that);
    });
    },
    submit() {
      this.close(this.marker);
    },
    dismiss() {
      this.close();
    },
  },
  components: { IonContent, IonPage, IonTitle, IonButton },
});
</script>

<style scoped>
#map {
  position: unset !important;
}
.map-title {
  display: contents;
  text-align: center;
}
.submit-button {
  bottom: 10px;
  position: fixed;
  left: 30%;
}
</style>