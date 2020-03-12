# Insulin-Calculator
## Objective
Create an api for people with diabetes. The functionality implies:
- The user takes a picture of each meal 
- the meal is recognized -- Convolutional neural network (CNN) (to startwith only usefull for pasta, pizza, egg, cheese, hamburger, meat, rice and vegetables)
- The CHO is calculated -- Using USDA api
- The recommended dose of insulin is calculated  
### Model of neural network 
The obtained correlation matrix
![alt text](https://github.com/E2811/Insulin-Calulator/blob/master/img/correlation.png "Logo Title Text 1")

### API endpoints 
- (POST) `/signUp`
  - **Purpose:** Create a new user and save into DB
![alt text](https://github.com/E2811/Insulin-Calulator/blob/master/img/signUp.png "Logo Title Text 1")

- (POST) `/logIn`
  - **Purpose:** logIn as an existed user and enter the desired food to analyzed
  - **Result:** Recommended dose of insulin 
  
- (POST) `/fileUpload
  - **Purpose:** Upload the image you want to analyze

- (GET) `/graph/<username>`
  - **Purpose:** Obtain a graph of doses/time for a given user 

![alt text](https://github.com/E2811/Insulin-Calulator/blob/master/img/graph.png "Logo Title Text 1")

### Future Work 
- Display in heroku
- Increase dataset 
- improve neural network 
- Conect to glucose meter
