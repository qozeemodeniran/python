import numpy as np 
from sklearn import metrics as mt
import matplotlib.pyplot as plt

# generate numbers for "actual" and "predicted" values
actual = np.random.binomial(1, 0.9, size=1000)
predicted = np.random.binomial(1, 0.9, size=1000)

# use metrics on actual and predcted values
confusion_matrix = mt.confusion_matrix(actual, predicted)

# convert table into confusion matrix display
cm_display = mt.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

# visualise display
cm_display.plot()
# plt.show()

Accuracy = mt.accuracy_score(actual, predicted)
print("Accuracy: ", Accuracy)

Precision = mt.precision_score(actual, predicted)
print("Precision: ", Precision)

Sensitivity = mt.recall_score(actual, predicted) # sometimes called recall
print("Sensitivity: ", Sensitivity)

Specificity = mt.recall_score(actual, predicted, pos_label=0) # deals with negative (opposite of Sensitivity)
print("Specificity: ",Specificity)

F1_score = mt.f1_score(actual, predicted)
print("F1_score: ", F1_score)