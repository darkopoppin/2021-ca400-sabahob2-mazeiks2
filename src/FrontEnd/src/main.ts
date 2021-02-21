import { createApp } from 'vue'
import App from './App.vue'
import router from './router';
import firebase from 'firebase';

import { IonicVue } from '@ionic/vue';

/* Core CSS required for Ionic components to work properly */
import '@ionic/vue/css/core.css';

/* Basic CSS for apps built with Ionic */
import '@ionic/vue/css/normalize.css';
import '@ionic/vue/css/structure.css';
import '@ionic/vue/css/typography.css';

/* Optional CSS utils that can be commented out */
import '@ionic/vue/css/padding.css';
import '@ionic/vue/css/float-elements.css';
import '@ionic/vue/css/text-alignment.css';
import '@ionic/vue/css/text-transformation.css';
import '@ionic/vue/css/flex-utils.css';
import '@ionic/vue/css/display.css';

/* Theme variables */
import './theme/variables.css';

const firebaseConfig = {
  apiKey: "AIzaSyBO0wRTtvrYhE6V6ublQmb7bNmQf7NVEsU",
  authDomain: "citecy.firebaseapp.com",
  databaseURL: "https://citecy-default-rtdb.europe-west1.firebasedatabase.app",
  projectId: "citecy",
  storageBucket: "citecy.appspot.com",
  messagingSenderId: "908044652058",
  appId: "1:908044652058:web:cad032412cb5bdaf430ba3",
  measurementId: "G-BN9SW7SVVB"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const app = createApp(App)
  .use(IonicVue)
  .use(router);
  
router.isReady().then(() => {
  app.mount('#app');
});