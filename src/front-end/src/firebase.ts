import firebase from 'firebase/app';
import 'firebase/auth';
import 'firebase/firestore';

// firebase config from CiteCy
const firebaseConfig = {
    apiKey : "AIzaSyBO0wRTtvrYhE6V6ublQmb7bNmQf7NVEsU",
    authDomain : "citecy.firebaseapp.com",
    databaseURL : "https://citecy-default-rtdb.europe-west1.firebasedatabase.app",
    projectId : "citecy",
    storageBucket : "citecy.appspot.com",
    messagingSenderId : "908044652058",
    appId : "1:908044652058:web:cad032412cb5bdaf430ba3",
    measurementId : "G-BN9SW7SVVB"
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