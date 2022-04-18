import sklearn
import os
import tensorflow as tf
from sklearn.decomposition import PCA
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.svm import SVC

# Read in the images and perform PCA on each color dim and then concatenate to get a 1 d vecotor I guess
old_location = "raw"
inputs = []
outputs = []
for dir in os.walk(old_location):
    print(dir[0])
    for idx, i in enumerate(os.listdir(dir[0])):
        if dir[0] == old_location:
            continue
        im = cv2.imread(os.path.join(dir[0], i))
        r, g, b = cv2.split(im)
        r, g, b = r / 255, g / 255, b / 255
        pca = PCA(n_components=1)
        r = pca.fit_transform(r)
        g = pca.fit_transform(g)
        b = pca.fit_transform(b)
        vec = np.concatenate([np.array(r), np.array(g), np.array(b)], axis=0)
        inputs.append(vec.flatten())
        outputs.append(dir[0])

inputs = np.array(inputs)
outputs = np.array(outputs)
train, val, train_labels, val_labels = train_test_split(
    inputs, outputs, test_size=0.2, random_state=1
)
rf = RandomForestClassifier(n_estimators=1000, random_state=1, class_weight="balanced")
# Train the model on training data
rf.fit(train, train_labels)
predictions = rf.predict(val)

print(classification_report(val_labels, predictions))

print("-" * 100)
svclassifier = SVC(kernel="linear")
svclassifier.fit(train, train_labels)
predictions = svclassifier.predict(val)
print(classification_report(val_labels, predictions))
