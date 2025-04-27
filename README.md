# 🔥 Smart Calories Tracker - Predict Your Burn with AI 🔥

Welcome to the **Calories Burnt Prediction App**! This project uses a RandomForest Regressor model to predict calories burnt based on user input. It features full **MLflow tracking**, a **Streamlit frontend**, **Docker containerization**, and a complete **CI/CD pipeline** with GitHub Actions 🚀.

---

## 📂 Project Structure

```
.github/workflows/deploy.yml    # GitHub Actions CI/CD pipeline
├── data/                       # Data collection
├── mlartifacts/                # Model artifacts
├── mlruns/                     # MLflow tracking logs
├── Research/                   # Research and experiments
├── src/
│   └── train.py                # Model training code
├── tests/
│   ├── model.joblib            # Saved model
│   └── test_model.py           # Unit tests
├── app.py                      # Streamlit app
├── Dockerfile                  # Docker container config
├── requirements.txt            # Python dependencies
├── README.md                   # Project README
├── .gitignore                  # Files to ignore in Git
├── .dockerignore               # Files to ignore in Docker
└── venv/                       # Virtual environment (local only)
```

---

## 🚀 Features

- **Data Collection & Preprocessing** 🗂️
- **Model Training** (RandomForest Regressor)
- **High Accuracy** ✅ (R2 Score: **98%**, MSE: **7**)
- **MLflow Tracking** 📈 (Runs on **port 5000**)
- **Streamlit App** 🎨 (Runs on **port 2003**)
- **Dockerized Deployment** 🐳
- **CI/CD Pipeline** with GitHub Actions 💻

---

## 🛠️ Setup Instructions

### 1. Clone the Repository 📥
```bash
git clone https://github.com/ka1817/Smart-Calories-Tracker-Predict-Your-Burn-with-AI.git
cd Smart-Calories-Tracker-Predict-Your-Burn-with-AI
```

### 2. Build Docker Image Locally 🐳
```bash
docker build -t pranavreddy123/calories-burnt-app:latest .
```

### 3. Run Docker Container 🚀
```bash
docker run -d -p 2003:8501 pranavreddy123/calories-burnt-app:latest
```

Then, open your browser at:
```
http://localhost:2003
```

---

## 🐳 Dockerfile

```Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```


---

## 🔄 CI/CD Pipeline (GitHub Actions)

- On every push to `main` branch:
  - Checkout code 📥
  - Setup Python environment 🐍
  - Install dependencies 📦
  - Start MLflow UI for tracking 📊
  - Run tests ✅
  - Build Docker image without cache 🛠️
  - Push Docker image to Docker Hub 📤
  - Deploy to AWS EC2 instance ☁️

---

## 📈 MLflow Tracking

- Tracking server will run on:
```
http://localhost:5000
```
- You can view and compare experiments!

---

## 🙌 Contributors

- **Pranav Reddy** ([@pranavreddy123](https://github.com/ka1817))

---

## 📜 License

This project is licensed under the **MIT License**.

---
Thank you for checking out the **Smart Calories Tracker** project! ✨

Developed By Pranav Reddy

