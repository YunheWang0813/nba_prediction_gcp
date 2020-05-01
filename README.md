# ECE 590 Final Project: NBA Prediction

Team: Yunhe Wang, Gavin Jin, Jingyu Su, Jia Rong Chua

## Backend Machine Learning Model
1. Download input data (team statistics data) from NBA.com and upload file to S3 bucket
2. Create a new notebook instance of AWS Sagemaker 
3. Load data from the S3 bucket
4. Data exploratory analysis: plot distribution of variables, missing value, normalize dataset, outlier analysis, feature correlation analysis 
5. Modeling: test different baseline models i.e. logistic regression, random forest, navie bayes, xgboost with model tunning using cross-validation based on evaluation by accuracy score
6. Predict probability of teams winning for all combinations of team matchups
7. Predicted values stored as csv file and uploaded to S3 bucket

## Backend-Frontend Integration 
ML output to DynamoDB:
1. Create a Lambda function 
2. upload the zipped version of ’S3toDynamoDB.py’ to the lambda function created or copy it directly to the Lambda function IDE
3. Modify the IAM role of this function to allow access authority for S3 and DynamoDB 
4. Add S3 object trigger to the function

DynamoDB to API:
1. Create a Lambda function 
2. upload the zipped version of ‘DynamoDB_API.py’ to the lambda function created or copy it directly to the Lambda function IDE
3. Modify the IAM role of this function to allow access authority for DynamoDB 
4. Add API gateway trigger to the function

API Gateway:
1. Start a resource for the project
2. Create a method to host request
3. Create GET method to form a API
4. Forward the GET method to Lambda function 
5. Test the created API with a built-in test function

## Frontend Web Application Development (Yunhe Wang)
* Framework: Flask
* Frontend: Javascript, JQuery, HTML/CSS, Bootstrap 4
* Backend: Python

To start the application:
1. Access virtual environment: ```source venv/bin/activate```
2. Install requests explicitly: ```pip install requests```
3. Install packages: ```make install ```
4. Test locally: ```python main.py```

## Locust Load Testing
The application is tested locally
1. run the main.py file in the virtual environment
2. If using AWS (which we did for load testing), ensure pots 8080 and 8089 are provided with public access
3. create ```locustfile.py``` to test the main page access, fixed team predictions and randomized team predictions
4. in a separate shell environment, run ```locust``` in the directory where the ```locustfile.py``` resides
5. access the locust dashboard on port 8089 and create swarm of 1000 users

### Demo Video Link
https://youtu.be/bCiO7xc37Uc

