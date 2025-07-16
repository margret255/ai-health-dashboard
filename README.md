# 💓 AI-Powered Health Monitor

An end-to-end machine learning project that detects abnormal health conditions using real-time data from fitness trackers or wearable devices.

This project is part of my machine learning journey in building real-worl AI systems.

---

##  Features

✅ Detect heart rate anomalies  
✅ Multi-feature prediction using:
- Total Steps
- Very Active Minutes
- Sedentary Minutes
- Calories Burned  

✅ User-friendly Streamlit dashboard  
✅ Secure login system with session management  
✅ Deployed to the web for public access  

---

## Dataset

Source: [FitBit Fitness Tracker Dataset (Kaggle)](https://www.kaggle.com/datasets/arashnic/fitbit)

Data was cleaned, preprocessed, and transformed using StandardScaler. The following features were selected for model training:

- `TotalSteps`
- `VeryActiveMinutes`
- `SedentaryMinutes`
- `Calories`

---

## Model Training

The model was trained using Scikit-learn. Key steps included:

- Feature scaling with `StandardScaler`
- Binary classification model for anomaly detection
- Saved using `joblib` as:
  - `model.pkl`
  - `scaler.pkl`

Training was done in Google Colab, and the notebook is included in the repository.

---

##  Project Structure
dashboard_project/
├── dashboard.py
├── model.pkl 
├── scaler.pkl 
├── ai_health_model_training.ipynb 
├── requirements.txt
└── README.md 


---

##  How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/ai-health-dashboard.git

# Navigate into the project folder
cd ai-health-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run dashboard.py



## 🌐 Live Demo

🔗 [Click here to try the app online](https://ai-health-dashboardgit-kuaqyppwitgu8knuhobxlo.streamlit.app/)
