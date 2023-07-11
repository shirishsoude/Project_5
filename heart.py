import tkinter as tk
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
heart_data = pd.read_csv('heart.csv')

# Separate the features and target variable
X = heart_data.drop('target', axis=1)
y = heart_data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Function to make the prediction
def predict_heart_disease():
    age = int(age_entry.get())
    sex = int(sex_entry.get())
    cp = int(cp_entry.get())
    trestbps = int(trestbps_entry.get())
    chol = int(chol_entry.get())
    fbs = int(fbs_entry.get())
    restecg = int(restecg_entry.get())
    thalach = int(thalach_entry.get())
    exang = int(exang_entry.get())
    oldpeak = float(oldpeak_entry.get())
    slope = int(slope_entry.get())
    ca = int(ca_entry.get())
    thal = int(thal_entry.get())

    # Create a new input data instance
    new_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                            columns=X.columns)

    # Make prediction on the new data
    prediction = rf_classifier.predict(new_data)

    if prediction[0] == 0:
        result = "No heart disease"
    else:
        result = "Heart disease detected"

    result_label.config(text="Prediction Result: " + result)

# Create the GUI window
window = tk.Tk()
window.title("Heart Disease Prediction")

# Create labels and entry fields for user input
tk.Label(window, text="Age:").grid(row=0, column=0, sticky=tk.W)
age_entry = tk.Entry(window)
age_entry.grid(row=0, column=1)

tk.Label(window, text="Sex (0 for female, 1 for male):").grid(row=1, column=0, sticky=tk.W)
sex_entry = tk.Entry(window)
sex_entry.grid(row=1, column=1)

tk.Label(window, text="Chest Pain Type (0-3):").grid(row=2, column=0, sticky=tk.W)
cp_entry = tk.Entry(window)
cp_entry.grid(row=2, column=1)

tk.Label(window, text="Resting Blood Pressure:").grid(row=3, column=0, sticky=tk.W)
trestbps_entry = tk.Entry(window)
trestbps_entry.grid(row=3, column=1)

tk.Label(window, text="Serum Cholesterol Level:").grid(row=4, column=0, sticky=tk.W)
chol_entry = tk.Entry(window)
chol_entry.grid(row=4, column=1)

tk.Label(window, text="Fasting Blood Sugar (0 for <120mg/dl, 1 for >120mg/dl):").grid(row=5, column=0, sticky=tk.W)
fbs_entry = tk.Entry(window)
fbs_entry.grid(row=5, column=1)

tk.Label(window, text="Resting Electrocardiographic Results (0-2):").grid(row=6, column=0, sticky=tk.W)
restecg_entry = tk.Entry(window)
restecg_entry.grid(row=6, column=1)

tk.Label(window, text="Maximum Heart Rate Achieved:").grid(row=7, column=0, sticky=tk.W)
thalach_entry = tk.Entry(window)
thalach_entry.grid(row=7, column=1)

tk.Label(window, text="Exercise Induced Angina (0 for No, 1 for Yes):").grid(row=8, column=0, sticky=tk.W)
exang_entry = tk.Entry(window)
exang_entry.grid(row=8, column=1)

tk.Label(window, text="ST Depression Induced by Exercise Relative to Rest:").grid(row=9, column=0, sticky=tk.W)
oldpeak_entry = tk.Entry(window)
oldpeak_entry.grid(row=9, column=1)

tk.Label(window, text="Slope of the Peak Exercise ST Segment (0-2):").grid(row=10, column=0, sticky=tk.W)
slope_entry = tk.Entry(window)
slope_entry.grid(row=10, column=1)

tk.Label(window, text="Number of Major Vessels (0-3) Colored by Fluoroscopy:").grid(row=11, column=0, sticky=tk.W)
ca_entry = tk.Entry(window)
ca_entry.grid(row=11, column=1)

tk.Label(window, text="Thalassemia (0-3):").grid(row=12, column=0, sticky=tk.W)
thal_entry = tk.Entry(window)
thal_entry.grid(row=12, column=1)

# Create a button for prediction
predict_button = tk.Button(window, text="Predict", command=predict_heart_disease)
predict_button.grid(row=13, column=0, columnspan=2)

# Create a label to display the prediction result
result_label = tk.Label(window, text="Prediction Result:")
result_label.grid(row=14, column=0, columnspan=2)

# Start the GUI event loop
window.mainloop()
