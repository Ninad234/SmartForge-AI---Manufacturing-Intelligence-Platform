# 🏭 Manufacturing Equipment Output Prediction

## AI-Powered Production Optimization System

[![Python 3.10+](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/MIT-green?style=for-the-badge)](https://opensource.org/license/MIT)

### 📋 Project Overview


This project was developed as a Data Science and Machine Learning capstone project to help manufacturing teams predict hourly equipment output and improve operational efficiency.

The system analyzes machine parameters, environmental conditions, maintenance information, and operator-related factors to estimate production output in real time.

## Key Features

📈 Production output prediction<br>
🤖 Machine Learning model training and evaluation<br>
⚡ FastAPI REST API for real-time predictions<br>
🐳 Dockerized deployment<br>
📊 Exploratory Data Analysis (EDA)<br>
🎯 Feature engineering and preprocessing pipeline<br>
💡 AI-generated optimization recommendations


## 🚀 Quick Start

### Option 1: Docker Deployment (Recommended)

```bash
# Clone or navigate to project directory
cd manufacturing_project

# Build and run with Docker Compose
docker-compose up --build

# API will be available at: http://localhost:8000
# Interactive docs: http://localhost:8000/docs
```

### Option 2: Local Development

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate the environment
# On Windows:
.\venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run Jupyter notebook for EDA
jupyter notebook notebooks/manufacturing_analysis.ipynb

# Start FastAPI server
cd api
python main.py

# Or use uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Data Science** | Python, Pandas, NumPy, Scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **API Framework** | FastAPI, Pydantic |
| **Deployment** | Docker, Docker Compose, Uvicorn |
| **ML Models** | Linear Regression, Random Forest, Gradient Boosting |
| **DevOps** | Git, GitHub Actions (optional) |

---

### 🎯 Key Outcomes

- Built an end-to-end Machine Learning workflow
- Compared multiple regression algorithms
- Achieved high prediction accuracy using ensemble learning
- Deployed the model through a production-ready REST API
- Containerized the application using Docker

---

### 📊 Dataset

Synthetic manufacturing dataset containing 1,000 production records.

Target Variable
Parts_Per_Hour
Feature Categories
Process Parameters
Material Properties
Equipment Information
Environmental Factors
Operator Information
Maintenance Metrics

### Feature Categories

| Category | Features |
|----------|----------|
| **Process Parameters** | Injection_Temperature, Injection_Pressure, Cycle_Time, Cooling_Time |
| **Material Properties** | Material_Viscosity, Material_Grade |
| **Equipment** | Machine_Age, Machine_Type, Machine_Utilization |
| **Environmental** | Ambient_Temperature |
| **Human Factors** | Operator_Experience, Shift |
| **Maintenance** | Maintenance_Hours |

---

## 🔬 machine Learning Pipeline 

### 1. Data Preprocessing
- ✅ Missing value imputation (median strategy)
- ✅ One-hot encoding for categorical variables
- ✅ Feature scaling (StandardScaler)
- ✅ Feature engineering
- ✅ Outlier detection and analysis

### 2. Model Development
Trained and evaluated 5 models:
- **Linear Regression** (Baseline)
- **Ridge Regression** (L2 regularization)
- **Lasso Regression** (L1 regularization)
- **Random Forest** (Ensemble)
- **Gradient Boosting** (Advanced ensemble)

---

## 📈 Model Performance

| Model | Test RMSE | Test MAE | Test R² | Status |
|-------|-----------|----------|---------|--------|
| Linear Regression | ~3.2 | ~2.4 | ~0.93 | ✅ Production |
| Ridge Regression | ~3.3 | ~2.5 | ~0.92 | ✅ Backup |
| Lasso Regression | ~3.5 | ~2.6 | ~0.91 | ✅ Alternative |
| Random Forest | ~2.1 | ~1.6 | ~0.97 | 🎯 Best Model |
| Gradient Boosting | ~2.3 | ~1.7 | ~0.96 | ✅ Strong |

**Best Model**: Random Forest (97% variance explained, ±2.1 parts/hour error)

---

## 🌟 GenAI-Powered Features

### 1. **Intelligent Insights**
```python
# Automatic analysis of:
- Performance predictions with context
- Temperature and pressure optimization
- Machine age impact assessment
- Operator experience evaluation
- Shift-based productivity patterns
```

### 2. **Optimization Suggestions**
```python
# AI-generated recommendations:
- Parameter adjustments for target output
- Energy efficiency improvements
- Maintenance scheduling
- Material grade recommendations
```

### 3. **Risk Alerts**
```python
# Proactive warnings for:
- Below-target performance
- Equipment failure risks
- Quality compromise scenarios
- Operator safety considerations
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
| :--- | :---: | :--- |
| `/predict` | **POST** | Predict production output |
| `/batch-predict` | **POST** | Predict multiple scenarios |
| `/optimize` | **POST** | Generate optimization suggestions |
| `/model-info` | **GET** | Model information |
| `/health` | **GET** | Health check |


## 📁 Project Structure

```
manufacturing_project/
│
├── data/
│   ├── generate_dataset.py          # Dataset generation script
│   └── manufacturing_dataset_1000_samples.csv
│
├── notebooks/
│   └── manufacturing_analysis.ipynb  # Complete EDA & modeling notebook
│
├── src/
│   ├── preprocessing.py              # Data preprocessing utilities
│   └── model_training.py             # Model training scripts
│
├── models/
│   ├── best_model.pkl                # Trained model
│   ├── scaler.pkl                    # Feature scaler
│   ├── feature_names.json            # Feature list
│   └── model_metadata.json           # Model metrics
│
├── api/
│   └── main.py                       # FastAPI application
│
├── docker/
│   └── Dockerfile                    # Docker configuration
│
├── reports/
│   ├── *.png                         # EDA visualizations
│   ├── model_comparison.csv          # Model results
│   └── final_report.pdf              # Complete analysis report
│
├── presentation/
│   └── capstone_presentation.pptx    # Project presentation
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### 👨‍💻 Author

Ninad Gawade

GitHub: https://github.com/Ninad234

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Dataset inspired by real manufacturing processes
- Built with modern data science best practices
- GenAI insights powered by intelligent heuristics
- API design following REST principles

---

## 📞 Contact & Support

For questions, issues, or contributions:
- **Email**: ninadgawade149@gmail.com
- **GitHub**: github.com/SmartForge-AI---Manufacturing-Intelligence-Platform
- **Documentation**: Full docs in `/docs` folder

---

## 🎉 Quick Test

```bash
# Test the API
curl http://localhost:8000/health

# View interactive docs
open http://localhost:8000/docs

# Make a test prediction
python -m api.test_client
```

---

**Built with ❤️ for Manufacturing Excellence**

*Last Updated: 2024*
