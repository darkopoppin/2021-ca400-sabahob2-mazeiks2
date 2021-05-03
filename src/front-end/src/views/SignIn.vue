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
                placeholder="Email"
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
                placeholder="Password"
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

            <p class="link-back">
              <router-link to="/ForgotPassword">Forgot password?</router-link>
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
import { auth, persistence } from "../firebase";
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
          .setPersistence(persistence.LOCAL)
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
ion-content {
  --ion-background-color: white;
}

.card {
  text-align: center;
  width: 40%;
  margin: auto;
  margin-top: 10%;
  background: #ffffff;
  box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
  padding: 40px 55px 45px 55px;
  border-radius: 15px;
  transition: all .3s;
}

@media only screen and (max-width: 850px) {
  .card {
  width: 100%;
}
}


.submit-button {
  --border-radius: 100px;
  min-width: fit-content;
  width: 40%;
}

.link-back {
  text-align: center;
  text-decoration: none;
  font-size: 16px;
  padding-top: 20px;
  color: #7a7a7a;
  margin: 0;
}

.sign-up-field {
  font-size: 18px;
  padding-top: 30px;
  text-align: center;
  margin: 0;
  color: black;
}

.input {
  --highlight-background: none;
  position: relative;
  --min-height: 0px;
  --padding-start: 0px;
  --inner-padding-end:0px;
  --border-radius: 100px;
  --background: lightgray;
  --ion-text-color: black;
  padding-bottom: 10px;
  text-indent: 10px;
  --border-width: 0px;
}

.icon {
  padding-left: 2%;
  bottom: 30%;
  font-size: 20px;
}

.header{
  text-align:center;
  font-size: 400%;
  font-style: bold;
  color: black;
  font-weight: 600;
  padding-bottom: 10%; 
}

.checkbox {
  --border-style: none;
  --color: black;
  --background: white;
  
}

.checkbox-label {
  padding-left: 3%;
}

</style>