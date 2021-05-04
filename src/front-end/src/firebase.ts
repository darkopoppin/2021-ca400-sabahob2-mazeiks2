import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

// firebase config from CiteCy
const firebaseConfig = {
  apiKey: "AIzaSyCzt8TEXDXmGSPMK_Z0H3obcSb36iceUb4",
  authDomain: "citycydev.firebaseapp.com",
  databaseURL: "https://citycydev-default-rtdb.firebaseio.com",
  projectId: "citycydev",
  storageBucket: "citycydev.appspot.com",
  messagingSenderId: "153875323476",
  appId: "1:153875323476:web:c27b38b118f60168f7ebc1"
}

firebase.initializeApp(firebaseConfig)

// initialise db and auth for later exporting and ease of use
const persistence = firebase.auth.Auth.Persistence
const db = firebase.firestore()
const auth = firebase.auth()

// reference databases collections
// const usersCollection = db.collection('users')

// export utils/refs
export {
  db,
  auth,
  persistence
}