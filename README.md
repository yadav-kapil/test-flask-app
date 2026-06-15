# Forest Fire Weather Index (FWI) Prediction

A test/demo Flask application that predicts the **Fire Weather Index (FWI)** using a Machine Learning model trained on weather and environmental data.

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
