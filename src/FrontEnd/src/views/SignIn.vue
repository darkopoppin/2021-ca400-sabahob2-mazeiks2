<template>
  <ion-page>
    <ion-content>
      <ion-card class="card">
          <h3 class="header">Login</h3>
          <form @submit.prevent="userLogin">
            <div class = "email-form">
            <ion-item class ="input">
              <ion-input 
                class="input"
                type="email"
                placeholder="email"
                v-model="user.email">

              <ion-icon :icon="personOutline" slot="start" class="icon"/> 
              </ion-input>
            </ion-item>
            </div>

            <div class = "password-form">
            <ion-item class ="input"> 
              <ion-input
                class="input"
                type="password"
                placeholder="password"
                v-model="user.password">

              <ion-icon :icon="lockClosedOutline" slot="start" class="icon"/>
              </ion-input>
            </ion-item>
            </div>
            <ion-item class="checkbox">
              <ion-checkbox @update:modelValue="rememberMe = $event"></ion-checkbox>
              <ion-label class="checkbox-label">Remember me</ion-label>
            </ion-item>
            <ion-button type="submit" class="submit-button">Sign In </ion-button>

            <p class="forgot-password-link">
              <router-link to="/ForgotPassword">Forgot password</router-link>
            </p>
            <p class="sign-up-field">
              Ready to explore? <router-link to="/SignUp"> Sign Up!</router-link>
            </p>
          </form>
      </ion-card>
    </ion-content>
  </ion-page>
</template>


<script>
import {
  IonContent,
  IonHeader,
  IonTitle,
  IonToolbar,
  IonCheckbox,
  IonPage,
  IonIcon,
  IonButton,
  IonCard,
  IonInput,
  IonItem,
  IonLabel
} from "@ionic/vue";
import { defineComponent } from "vue";
import firebase from "firebase/app";
import { auth } from "../firebase";
import { personOutline, lockClosedOutline } from 'ionicons/icons';

export default defineComponent({
  name: "SignIn",
  components: {
    IonContent,
    IonCard,
    IonInput,
    IonItem,
    IonIcon,
    IonCheckbox,
    IonButton,
    IonPage,
    IonLabel,
  },
  setup() {
    return {
      personOutline, lockClosedOutline
    }
  },
  data() {
    return {
      rememberMe : {val: "checkBox", isChecked: true},
      user: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    userLogin() {
        if (this.rememberMe){
          auth
          .setPersistence(firebase.auth.Auth.Persistence.LOCAL)
          .then(() => {
            return auth
              .signInWithEmailAndPassword(this.user.email, this.user.password)
              .then((res) => {
                res.user
                  .updateProfile({
                    displayName: this.user.name,
                  })
                  .then(() => {
                    this.$router.push("/");
                  });
              })
              .catch((error) => {
                alert(error.message);
              });
          });
        }
        else {
          auth
          .signInWithEmailAndPassword(this.user.email, this.user.password)
              .then((res) => {
                  res
                  .user
                  .updateProfile({
                    displayName: this.user.name,
                  })
                  .then(() => {
                    this.$router.push("/");
                  });
              })
              .catch((error) => {
                alert(error.message);
              });
          }
    },
  },
});
</script>

<style>
.card {
  position: relative;
  width: 450px;
  margin: auto;
  margin-top: 10%;
  background: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
  padding: 40px 55px 45px 55px;
  border-radius: 15px;
  transition: all .3s;
}

.submit-button {
  --border-radius: 900px;
  width: 40%;
  margin-left: 30%;
  margin-right: 30%;
}
label {
  font-weight: 500;
}

.forgot-password-link {

  text-align: center;
  text-decoration: none;
  font-size: 13px;
  padding-bottom: 30px;
  padding-top: 10px;
  color: #7a7a7a;
  margin: 0;
}


.sign-up-field {
  width: 40%;
  margin-left: 20%;
  margin-right: 20%;
  position: absolute;
  bottom: 0%;
}

.input {
  position: relative;
  --min-height: 0px;
  --padding-start: 0px;
  --inner-padding-end:0px;
  --border-radius: 100px;
  background-color: lightgray;
  text-indent: 10px;
}

.icon {
  padding-left: 2%;
  bottom: 30%;
  font-size: 20px;
}

.password-form {
  margin-top: 10px;
  overflow: hidden;
  border-radius: 100px;
}

.email-form {
  overflow: hidden;
  border-radius: 100px;
}

.header{
  text-align:center;
  font-size: 300%;
  font-style: bold;
  color: black;
  font-weight: 600;
  padding-bottom: 10%; 
}

.checkbox {
  --border-style: none;
  
}
.checkbox-label {
padding-left: 4%;
}
</style>