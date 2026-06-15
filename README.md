# Forest Fire Weather Index (FWI) Prediction

A Machine Learning-powered web application that predicts the **Fire Weather Index (FWI)** based on weather and environmental conditions. The application is built using **Flask**, **Scikit-Learn**, and a modern SaaS-style user interface.

## Features

* Predict Fire Weather Index (FWI) in real time
* Clean and responsive SaaS-inspired UI
* Machine Learning model trained using Scikit-Learn
* Input validation through HTML forms
* Detailed prediction results page
* Displays selected class and region information

## Input Features

The model uses the following features:

* Temperature
* Relative Humidity (RH)
* Wind Speed (Ws)
* Rain
* FFMC
* DMC
* ISI
* Classes (Fire / Not Fire)
* Region (Bejaia / Sidi-Bel Abbes)

## Tech Stack

### Backend

* Python
* Flask
* NumPy
* Scikit-Learn
* Pickle

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── project_cycle_03_model.pkl
│   └── project_cycle_03_scaler.pkl
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd project-folder
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

The application will be available at:

```text
http://localhost:6006
```

## Workflow

```text
User Input
     ↓
Flask Form Submission
     ↓
Data Preprocessing
     ↓
Feature Scaling
     ↓
Machine Learning Model
     ↓
FWI Prediction
     ↓
Results Page
```

## Screenshots

Add screenshots of:

* Home Page
* Prediction Result Page

## Future Improvements

* Prediction history
* Interactive charts and analytics
* Model monitoring dashboard
* User authentication
* Cloud deployment

## Author

Kapil Yadav

First-Year Engineering Student | Full Stack & DevOps Learner
