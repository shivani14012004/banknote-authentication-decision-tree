# 🌳 Banknote Authentication using Decision Tree

## 📌 Project Overview

This project uses a **Decision Tree Classification** algorithm to predict whether a banknote belongs to **Class 0 or Class 1**.

Two Decision Tree criteria were compared:

* **Gini**
* **Entropy**

After comparing their test accuracies, **Entropy performed better** with an accuracy of **98.5%**.

The trained Entropy Decision Tree model is saved as a pickle file and used in a **Streamlit web application** for prediction.

---

## 📊 Dataset

The dataset used in this project is:

```text
banknotes (1).csv
```

The dataset contains information about banknotes with the following columns:

| Feature  | Description                    |
| -------- | ------------------------------ |
| Variance | Variance of the banknote image |
| Skewness | Skewness of the banknote image |
| Curtosis | Curtosis of the banknote image |
| Entropy  | Entropy of the banknote image  |
| Class    | Target variable                |

### Features

The model uses these four input features:

```text
Variance
Skewness
Curtosis
Entropy
```

### Target

```text
Class
```

---

## 🤖 Algorithm Used

The main algorithm used in this project is:

**Decision Tree Classifier**

Two criteria were tested:

```python
criterion='gini'
```

and

```python
criterion='entropy'
```

Both models were trained using the same train-test split:

```python
train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
```

Using the same `random_state=42` makes the comparison fair and repeatable.

---

## 📈 Model Comparison

| Model                   |  Accuracy |
| ----------------------- | --------: |
| Decision Tree - Gini    | **98.1%** |
| Decision Tree - Entropy | **98.5%** |

### 🏆 Best Model

The **Entropy Decision Tree** was selected because it achieved the higher test accuracy:

```text
Entropy Accuracy = 98.5%
```

Therefore, the final model was created using:

```python
DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)
```

---

## 💾 Model Saving

The trained model was saved using Python's `pickle` library.

```python
import pickle

with open('decision_tree_entropy.pkl', 'wb') as file:
    pickle.dump(dt_entropy, file)
```

The saved model file is:

```text
decision_tree_entropy.pkl
```

---

## 🌐 Streamlit Application

The trained model is integrated into a **Streamlit web application**.

The user enters:

```text
Variance
Skewness
Curtosis
Entropy
```

The application sends these values to the trained Decision Tree model and predicts the class.

### Application Flow

```text
User Input
    ↓
Variance
Skewness
Curtosis
Entropy
    ↓
Entropy Decision Tree
    ↓
Prediction
    ↓
Class 0 / Class 1
```

---

## 📁 Project Structure

The recommended GitHub project structure is:

```text
Decision_Tree_Project/
│
├── app.py
├── decision_tree_entropy.pkl
├── banknotes (1).csv
├── requirements.txt
├── README.md
├── .gitignore
│
└── venv/
```

### ⚠️ Important

The `venv/` folder should **not be uploaded to GitHub**.

The virtual environment is created locally on your computer. Other users can recreate it using the `requirements.txt` file.

Therefore, add this to `.gitignore`:

```text
venv/
__pycache__/
*.pyc
```

Your GitHub repository should contain:

```text
app.py
decision_tree_entropy.pkl
banknotes (1).csv
requirements.txt
README.md
.gitignore
```

---

## 🐍 Virtual Environment Setup

Using a virtual environment keeps the project dependencies separate from other Python projects.

### Step 1 — Create Virtual Environment

Open the VS Code terminal inside the project folder:

```bash
python -m venv venv
```

---

### Step 2 — Activate Virtual Environment

For Windows Command Prompt:

```bash
venv\Scripts\activate
```

For Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

After successful activation, you should see:

```text
(venv)
```

at the beginning of the terminal line.

Example:

```text
(venv) C:\Users\YourName\Decision_Tree_Project>
```

---

### Step 3 — Install Required Libraries

Run:

```bash
pip install pandas numpy scikit-learn matplotlib streamlit
```

---

## 📦 requirements.txt

After installing the required libraries, create the `requirements.txt` file using:

```bash
pip freeze > requirements.txt
```

This saves the installed Python packages and their versions.

The file will look similar to:

```text
numpy==...
pandas==...
scikit-learn==...
matplotlib==...
streamlit==...
```

The exact versions depend on your virtual environment.

---

## 🔄 Install Dependencies from requirements.txt

If someone downloads or clones this project from GitHub, they can create a virtual environment and install all required packages using:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Then run:

```bash
pip install -r requirements.txt
```

This installs the dependencies required for the project.

---

## ▶️ Run the Streamlit Application

Open the project folder in VS Code.

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Then run:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually, Streamlit runs at:

```text
http://localhost:8501
```

---

## 🖥️ Streamlit Application

The application provides input fields for:

```text
Variance
Skewness
Curtosis
Entropy
```

After entering the values, click:

```text
Predict
```

The application displays the predicted class.

---

## 🔍 Example Prediction

Example input:

```text
Variance = 3.62
Skewness = 8.66
Curtosis = -2.80
Entropy = -0.44
```

The model receives:

```python
[[3.62, 8.66, -2.80, -0.44]]
```

and returns the predicted class:

```text
Class 0
```

or:

```text
Class 1
```

---

## 📊 Feature Importance

The Decision Tree model can provide feature importance values using:

```python
model.feature_importances_
```

These values help identify which features contributed more to the model's decisions.

The project can also visualize these values using a Matplotlib/Pyplot graph in Streamlit.

---

## 🎯 Project Objective

The main objectives of this project are:

1. Load and explore the banknote dataset.
2. Separate features and target.
3. Split the dataset into training and testing data.
4. Build a Decision Tree using Gini.
5. Build a Decision Tree using Entropy.
6. Compare both model accuracies.
7. Select the better-performing model.
8. Save the selected model using Pickle.
9. Create a Streamlit application.
10. Use the trained model to make predictions.

---

## 🏆 Result

The two Decision Tree models produced the following results:

```text
Gini    → 98.1%
Entropy → 98.5%
```

Therefore, **Entropy was selected as the final model**.

### Final Model

```python
DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)
```

### Final Accuracy

```text
98.5%
```

---

## 🚀 Future Improvements

The project can be further improved by:

* Adding a confusion matrix.
* Adding precision, recall, and F1-score.
* Adding a classification report.
* Improving the Streamlit user interface.
* Deploying the Streamlit application online.
* Comparing Decision Tree with Random Forest, KNN, SVM, and Logistic Regression.
* Adding feature-importance visualization.
* Adding input validation in the Streamlit application.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Pickle
* Google Colab
* VS Code
* Git
* GitHub

---

## 📄 Files Description

| File                        | Description                                   |
| --------------------------- | --------------------------------------------- |
| `app.py`                    | Streamlit application                         |
| `decision_tree_entropy.pkl` | Trained Entropy Decision Tree model           |
| `banknotes (1).csv`         | Banknote Authentication dataset               |
| `requirements.txt`          | Python dependencies                           |
| `README.md`                 | Project documentation                         |
| `.gitignore`                | Files/folders excluded from GitHub            |
| `venv/`                     | Local virtual environment — **do not upload** |

---

## 📌 GitHub Upload

After creating all project files, check the project folder:

```text
Decision_Tree_Project/
│
├── app.py
├── decision_tree_entropy.pkl
├── banknotes (1).csv
├── requirements.txt
├── README.md
└── .gitignore
```

Make sure `venv/` is excluded using `.gitignore`.

Then initialize Git:

```bash
git init
```

Add the project files:

```bash
git add .
```

Commit the project:

```bash
git commit -m "Banknote Authentication Decision Tree project"
```

Connect your GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Rename the branch to `main`:

```bash
git branch -M main
```

Push the project:

```bash
git push -u origin main
```

---

## 👩‍💻 Author

**Shivani Patil**

### Machine Learning Project

**Banknote Authentication using Decision Tree Classification**

---

## ⭐ Conclusion

This project demonstrates how a **Decision Tree Classifier** can be used for banknote authentication.

Both **Gini** and **Entropy** criteria were evaluated using the same train-test split.

The results were:

```text
Gini    → 98.1%
Entropy → 98.5%
```

Since Entropy achieved the higher accuracy, the **Entropy Decision Tree** was selected as the final model.

The model was saved using Pickle and integrated with a **Streamlit web application** for real-time banknote classification.


