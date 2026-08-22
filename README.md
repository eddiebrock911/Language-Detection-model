# 🌍 Language Detection Model

<p align="center">
  <strong>Natural Language Processing • Machine Learning • NLP • Streamlit</strong>
</p>

<p align="center">
  An NLP-powered Machine Learning application that automatically identifies the language of a given text.
</p>

<p align="center">
  <a href="https://whatkit.onrender.com">🚀 Live Demo</a> •
  <a href="https://github.com/eddiebrock911/Language-Detection-model">💻 Source Code</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Machine%20Learning-NLP-F7931E?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/NLP-Language%20Detection-6A5ACD?style=for-the-badge">
  <img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=for-the-badge&logo=render&logoColor=black">
</p>

---

## 📌 Overview

**Language Detection Model** is a Natural Language Processing application that predicts the language of an input text using a trained Machine Learning model.

The project demonstrates how raw text can be transformed into numerical features using a vectorizer and then classified using a trained language-detection model.

The complete workflow is:

```text
Input Text
    ↓
Text Preprocessing
    ↓
Vectorization
    ↓
Machine Learning Model
    ↓
Language Prediction
    ↓
Result
```

This project focuses on practical NLP concepts such as text preprocessing, feature extraction, vectorization, supervised classification, model serialization, and deployment.

---

## 🚀 Live Demo

### 🌐 Try the Application

**Live Application:**
https://whatkit.onrender.com

Enter a sentence or paragraph into the application and the trained model will predict its language.

---

## ✨ Features

* 🌍 Automatic language detection
* 🧠 Machine Learning-based NLP classification
* 📝 Text input interface
* ⚡ Fast prediction
* 🔤 Text vectorization
* 💾 Serialized ML model
* 💾 Serialized vectorizer
* 🎨 Interactive Streamlit interface
* ☁️ Render deployment
* 📊 Dataset-based supervised learning
* 🧪 Jupyter Notebook for experimentation

---

## 🧠 How It Works

The application uses two important serialized components:

```text
language_detection_model.pkl
```

and

```text
vectorizer.pkl
```

The vectorizer converts text into numerical features that can be understood by the Machine Learning model.

### Prediction Pipeline

```text
                  User Text
                     │
                     ▼
             ┌───────────────┐
             │ Preprocessing │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │  Vectorizer   │
             └───────┬───────┘
                     │
                     ▼
          Numerical Text Features
                     │
                     ▼
             ┌───────────────┐
             │  ML Classifier│
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   Language    │
             │   Prediction  │
             └───────────────┘
```

---

## 🔬 NLP Pipeline

The project follows a standard text-classification workflow:

```text
Raw Dataset
     ↓
Text Cleaning
     ↓
Feature Extraction
     ↓
Vectorization
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
Application Deployment
```

---

## 📚 Natural Language Processing

Language detection is a text classification problem.

Given an input:

```text
"This is an example sentence."
```

the model converts the text into numerical features and predicts the most likely language class.

A simplified representation is:

```text
Text
 ↓
Tokenizer / Vectorizer
 ↓
Feature Vector
 ↓
Classifier
 ↓
Language Label
```

---

## 🧮 Text Vectorization

Machine Learning algorithms cannot directly understand raw text.

The `vectorizer.pkl` file contains the fitted text vectorization component used by the application.

Conceptually:

```text
"Hello, how are you?"
          ↓
      Vectorizer
          ↓
[0.00, 0.21, 0.00, 0.74, ...]
          ↓
      ML Model
          ↓
      Prediction
```

This allows textual information to be represented numerically.

---

## 🤖 Machine Learning Model

The trained classifier is stored in:

```text
language_detection_model.pkl
```

The model was trained using the language dataset and corresponding text features.

The serialized model allows the deployed application to perform inference without retraining every time the application starts.

---

## 📊 Dataset

The project includes:

```text
language.csv
```

This dataset is used as the source data for developing the language classification model.

The general dataset workflow is:

```text
Dataset
  ↓
Text Samples
  ↓
Language Labels
  ↓
Preprocessing
  ↓
Vectorization
  ↓
Model Training
```

---

## 📂 Project Structure

```text
Language-Detection-model/
│
├── Myenv/
│
├── app.py
│
├── detectionLan.ipynb
│
├── language.csv
│
├── language_detection_model.pkl
│
├── vectorizer.pkl
│
├── render.yaml
│
├── requirements.txt
│
└── README.md
```

The repository currently contains the application, training notebook, dataset, serialized model/vectorizer, dependency file, and Render configuration.

### 📄 File Description

| File                           | Purpose                               |
| ------------------------------ | ------------------------------------- |
| `app.py`                       | Main Streamlit application            |
| `detectionLan.ipynb`           | Model development and experimentation |
| `language.csv`                 | Training dataset                      |
| `language_detection_model.pkl` | Trained ML classifier                 |
| `vectorizer.pkl`               | Fitted text vectorizer                |
| `render.yaml`                  | Render deployment configuration       |
| `requirements.txt`             | Python dependencies                   |
| `README.md`                    | Project documentation                 |

---

## 🛠️ Tech Stack

### Programming

* Python

### Machine Learning

* Scikit-learn
* Supervised Classification
* Model Serialization

### NLP

* Text preprocessing
* Text vectorization
* Language classification

### Application

* Streamlit

### Data Processing

* Pandas
* NumPy

### Development

* Jupyter Notebook
* Git
* GitHub

### Deployment

* Render

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/eddiebrock911/Language-Detection-model.git
```

### 2. Navigate to the Project

```bash
cd Language-Detection-model
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

After starting, Streamlit will provide a local URL in the terminal.

Typically:

```text
http://localhost:8501
```

---

## 🧪 Model Development

The Machine Learning experimentation is available in:

```text
detectionLan.ipynb
```

The notebook can be used to understand the development process:

```text
Load Dataset
     ↓
Explore Dataset
     ↓
Clean Text
     ↓
Prepare Features
     ↓
Vectorize Text
     ↓
Train Classifier
     ↓
Evaluate Model
     ↓
Save Model
     ↓
Save Vectorizer
```

---

## 💾 Model Serialization

After training, the important ML components are stored as `.pkl` files:

```text
language_detection_model.pkl
vectorizer.pkl
```

This makes the deployment workflow efficient because the application can load the already-trained components.

```python
import pickle

model = pickle.load(
    open("language_detection_model.pkl", "rb")
)

vectorizer = pickle.load(
    open("vectorizer.pkl", "rb")
)
```

The exact loading implementation should follow the logic used in `app.py`.

---

## 🔄 Prediction Workflow

The application performs prediction approximately as follows:

```text
User enters text
        ↓
Input validation
        ↓
Text preprocessing
        ↓
Vectorizer transforms text
        ↓
ML model receives vector
        ↓
Model predicts language
        ↓
Prediction displayed
```

---

## 🎯 Use Cases

Language detection can be useful as a preprocessing step for many NLP systems.

Potential applications include:

* 🌐 Multilingual websites
* 💬 Chat applications
* 🔎 Search systems
* 🌍 Translation pipelines
* 📰 Content classification
* 🤖 NLP applications
* 📚 Educational applications
* 🧩 Multilingual AI systems

Language detection is commonly used as an early stage before tasks such as translation or other language-specific NLP processing.

---

## 🧠 What This Project Demonstrates

This project demonstrates practical knowledge of:

* Natural Language Processing
* Text classification
* Feature extraction
* Text vectorization
* Supervised Machine Learning
* Model persistence
* Streamlit application development
* Deployment
* Git/GitHub workflow

The project moves beyond notebook-only ML by connecting a trained model to a user-facing application.

---

## ☁️ Deployment

The repository contains:

```text
render.yaml
```

for Render deployment configuration.

Deployment architecture:

```text
GitHub Repository
       ↓
     Render
       ↓
Python Environment
       ↓
Streamlit Application
       ↓
Public Web App
```

### Live Deployment

🌐 **https://whatkit.onrender.com**

The GitHub repository currently lists the deployed application under its About section.

---

## ⚠️ Limitations

Language detection performance can depend on:

* Input length
* Text quality
* Spelling errors
* Mixed-language sentences
* Similar languages
* Transliteration
* Very short text
* Unseen vocabulary
* Dataset coverage

For example, extremely short text may not contain enough linguistic information for reliable classification.

---

## 🔮 Future Improvements

Possible upgrades:

* [ ] Display prediction confidence
* [ ] Support more languages
* [ ] Add multilingual examples
* [ ] Improve preprocessing
* [ ] Add confusion matrix
* [ ] Add model accuracy dashboard
* [ ] Add probability distribution
* [ ] Add batch text prediction
* [ ] Add CSV upload for bulk detection
* [ ] Add API endpoint
* [ ] Add REST API using FastAPI
* [ ] Add language statistics
* [ ] Add prediction history
* [ ] Add automated tests
* [ ] Add GitHub Actions CI/CD
* [ ] Experiment with Transformer-based models

---

## 🚀 Advanced Version Roadmap

A future architecture could combine language detection with translation:

```text
             User Text
                 │
                 ▼
        ┌─────────────────┐
        │ Language Detect │
        └────────┬────────┘
                 │
                 ▼
          Detected Language
                 │
                 ▼
        ┌─────────────────┐
        │ Translation NLP │
        └────────┬────────┘
                 │
                 ▼
          Translated Text
```

This would turn the current classifier into a more complete multilingual NLP system.

---

## 📈 Future Model Experiments

The project can also be extended by comparing multiple approaches:

| Approach            | Category      |
| ------------------- | ------------- |
| TF-IDF + Classifier | Classical NLP |
| Character N-grams   | NLP           |
| Word N-grams        | NLP           |
| Logistic Regression | ML            |
| Naive Bayes         | ML            |
| Linear SVM          | ML            |
| Random Forest       | ML            |
| Transformer Model   | Deep Learning |

Character-level features can be especially useful for language identification because languages often have distinctive character and character-sequence patterns.

---

## 👨‍💻 Author

### Ankit

**AI / Machine Learning Developer**

**GitHub:**
https://github.com/eddiebrock911

**Repository:**
https://github.com/eddiebrock911/Language-Detection-model

**Live Demo:**
https://whatkit.onrender.com

---

## ⭐ Support

If this project helped you learn something:

⭐ Star the repository
🍴 Fork the project
🐛 Report issues
💡 Suggest improvements

---

## 📜 License

This project is intended for educational and experimental purposes.

Before redistributing the project or dataset, verify the applicable licenses for all third-party resources.

---

<p align="center">

<strong>🌍 Text → NLP → Machine Learning → Language</strong>

<br><br>

Built with <strong>Python • NLP • Scikit-learn • Streamlit</strong>

<br><br>

Made by <strong>Ankit</strong> 🚀

</p>

