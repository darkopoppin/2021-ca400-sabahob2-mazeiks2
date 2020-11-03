# School of Computing &mdash; Year 4 Project Proposal Form

## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title:       | CityCy            |
|Student 1 Name:      | Bozhidar Sabahov            |
|Student 1 ID:        | 17703831        |
|Student 2 Name:      | Salvijus Mazeikis            |
|Student 2 ID:        | 17320181            |
|Project Supervisor:  | Annalina Caputo            |


## SECTION B

### Introduction

The objective of our project is to create a progressive web application which would aid the users in the planning of their holiday or leisure day. It would be done by creating a planned day with activities ranging from sightseeing, dining, escape rooms to visiting museums. The activities would be suitable to the user and the plan would fit in their available free time.

### Outline

A Machine Learning algorithm would predict what activities the user would like to do based on their interests, hobbies, age, etc. Then, given the user’s time available, the type of transport and budget, it would create a plan of activities.
 
In addition, if the user is visiting another city, the activities would be chosen in such a way that the user can discover interesting/famous parts of the city. On the other hand, when the user would like to spend their leisure time, the planned activities would not include sightseeing, museums, etc

To be on track with the plan, the estimated time that the user can spend on each activity will be included. Furthermore, the plan could be updated in real-time if the user is behind the provided schedule. For example, if they decide to spend more time than it is suggested on an activity or they are in traffic.


### Background

The motivation behind this project is that we have often found ourselves struggling to decide what to do on weekends. The reason is that there is a huge variety of activities to choose from in Dublin.

### Achievements

The main goal of this project is to have a web-app, with working front-end and back-end, offering the following functionalities:
- Algorithm that will be able to create a plan from the list of activities that will match the user’s budget, available time, transportation, location
- Machine learning algorithm (classification model/collaborative filtering or hybrid) that would be able to improve the choice of activities for each user
- Real-time updates of the planned activities if the user is behind schedule

Customer base:
- Tourists
- Young people

### Justification

The application will be useful when a big city is visited for a short duration of time. For instance, when a person has a long layover at an airport. Then, the app can create a plan of activities for the duration of their layover. Another example is if they are visiting a city on their own or they just want to simply enjoy a day out.

### Programming language(s)

Python, JavaScript

### Programming tools / Tech stack

The final choice of web frameworks and database will be made once we decide the architectural approach to the web application. 
- Database - Firebase/SQL
- UI design - Adobe XD
- Front-end - React/Cordova/Vue.js
- Back-end - Django/Node.js
- MachineLearning - PyTorch/TF

### Hardware

None

### Learning Challenges

- Machine Learning
- Dealing with the cold start problem for recommendation systems
- Collecting preferences about the user that would aid us in selecting suitable activities
- Integrating the recommendation algorithm/model
- Creating and optimizing an algorithm to plan activities given time, budget, transportation, location
- Updating the scheduled activities in real time using user’s location 


### Breakdown of work

#### Bozhidar Sabahov

- UI design
- Frontend API implementation
- Design the web app architecture
- Server-side implementation
- Algorithm to pick the activities that would fit the user’s available time, budget, transportation, location (something like the Knapsack problem)
- Real-time updates of the planned activities
- Ui testing, Unit testing


#### Salvijus Mazeikis

- User study
- Database design and implementation
- Server-side implementation
- Backend API implementation
- Train a recommender system using machine learning
- End-to-end testing, machine learning testing
