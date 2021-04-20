# Website
## Docker
    - docker build -t NAME .
    - docker run -dp 8100:8100 NAME

## Manually
    - npm install -g @ionic/cli
    - npm install

It should now be accessable at http://localhost:8100

# Android
- Ensure you have [Android Studio](https://developer.android.com/studio)

        - npm install -g @ionic/cli
        - npm install
        - npm run build
        - ionic capacitor run android

# Apple
    - npm install -g @ionic/cli
    - npm install
    - npm run build
    - ionic cordova run ios
    Deployment NOT TESTED