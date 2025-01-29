import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

# Load the terrain dataset
features_train, labels_train, features_test, labels_test = makeTerrainData()

########################## SVM #################################
from sklearn.svm import SVC

# Create an SVM classifier with a linear kernel
clf = SVC(kernel="linear")

# Train the classifier on the training data
clf.fit(features_train, labels_train)

# Make predictions on the test data
pred = clf.predict(features_test)

# Debugging: Print dataset shapes
print("Training features shape:", np.shape(features_train))
print("Training labels shape:", np.shape(labels_train))
print("Test features shape:", np.shape(features_test))
print("Test labels shape:", np.shape(labels_test))

# Compute accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)

# Function to return accuracy
def submitAccuracy():
    return acc

# Print the accuracy for verification
print("Model Accuracy:", submitAccuracy())

# Generate and display the decision boundary image
try:
    prettyPicture(clf, features_test, labels_test)
    plt.show()  # Show the image
except NameError:
    print("Error: prettyPicture function not found.")
