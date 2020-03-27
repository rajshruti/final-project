import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def predict(x):
    # Read the file containing dataset
    
    file = pd.read_csv("Data/MLdataset.csv")
    file["TotalTime"] = file["TotalTime"].round(1)
    
    # Applying One-Hot Encoding
    
    data = file.values
    X = data[:, 0]
    y = data[:, 3]
    label_encoder = LabelEncoder()
    label_encoder.fit(y)
    encoded_y = label_encoder.transform(y)
    
    #  Split our data into training and testing
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
    
    X_train = X_train.reshape(-1,1)
    X_test = X_test.reshape(-1,1)
    
    # Create a Logistic Regression Model
    
    classifier = LogisticRegression()
    
    classifier.fit(X_train, y_train)
    
    
    # Predict the class of the new data point
    user_input = np.array([[x]])
    prediction = classifier.predict(user_input)
    
    return prediction