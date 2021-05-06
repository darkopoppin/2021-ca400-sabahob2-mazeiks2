<template>
  <ion-page>
    <ion-content>
      <div id="map"></div>
    </ion-content>
  </ion-page>
</template>

<script>
import { IonContent, IonPage } from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Map",
  props: ["markers", "userLocation"],
  data() {
    return {
      isMounted: false,
      map: null,
      mapCenter: { lat: 0, lng: 0 },
    };
  },
  mounted() {
    const places = JSON.parse(this.markers);
    const userLocation = JSON.parse(this.userLocation);
    this.initMap(userLocation);
    this.directions(userLocation, places["0"])
    for (let i = 0; i < Object.keys(places).length - 1; i++) {
        this.directions(places[i.toString()], places[(i + 1).toString()]);
    }
  },
  methods: {
    directions(startPoint, endPoint) {
      let directionsService = new google.maps.DirectionsService(); // eslint-disable-line
      let directionsRenderer = new google.maps.DirectionsRenderer(); // eslint-disable-line
      const request = {
        origin: startPoint,
        destination: endPoint,
        travelMode: "WALKING",
      };
      directionsRenderer.setMap(this.map);
      directionsService.route(request, function (result, status) {
        if (status == "OK") {
          const steps = result.routes[0].legs[0].steps;
          steps.forEach((res, key) => {
            const marker = new google.maps.Marker({ // eslint-disable-line
              position: {
                lat: res.start_location.lat(),
                lng: res.start_location.lng(),
              },
              map: this.map,
              label: {
                text: key,
                color: "#FFF",
              },
            });
          });
          directionsRenderer.setDirections(result);
        } else {
          console.log(status);
        }
      });
    },
    initMap() {
      this.map = new google.maps.Map(document.getElementById("map"), { // eslint-disable-line
        center: this.userLocation,
        zoom: 12,
      });
    },
  },
  components: { IonContent, IonPage },
});
</script>

<style scoped>
#map {
  position: unset !important;
}
</style>