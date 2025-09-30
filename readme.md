# 🩺 Healthcare Backend API

A Python backend that provides REST APIs for **disease prediction**, **clinical notes generation**, and **doctor recommendation** based on prescriptions.  
Built with **FastAPI**, **ML models**, and industry-standard best practices.


Disclaimer: These apis were used alongside with the main node-js backend for our health application (FYP)for reference you can visit marham.pk or oladoc.

---

## 🚀 Features

- **Disease Prediction** – Predicts possible diseases from patient symptoms.
- **Clinical Notes Generation** – Generates structured clinical notes from patient history.
- **Doctor Recommendation** – Suggests specialized doctors based on prescription image.

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Machine Learning**: Scikit-learn / TensorFlow / huggingface 
- **Environment Management**: `python-dotenv`
- **API Documentation**: Swagger

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend
```

### 2️⃣ Make an environment to isolate dependencies

```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the backend

```bash
uvicorn app.main:app --reload
```

## Note:

Both the disease predition and clinical notes models are trained separately in google colab. Training notebooks will be attached soon..
The dataset used for training both models was open source and does not guarantee authenticity, use with caution and if possible use authentic data for production use.
