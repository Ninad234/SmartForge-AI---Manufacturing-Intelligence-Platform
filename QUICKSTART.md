# 🚀 QUICK START GUIDE
## Manufacturing Output Prediction Project

## ⚡ 5-Minute Setup

### Option 1: Docker (Recommended - Fastest)

```bash
# Navigate to project
cd manufacturing_project

# Start everything with one command
docker-compose up --build

# Access API at: http://localhost:8000
# Interactive docs: http://localhost:8000/docs
```

### Option 2: Local Python

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Jupyter notebook
jupyter notebook notebooks/manufacturing_analysis.ipynb

# Or start the API server
cd api
python main.py
```

## 📊 Run the Complete Analysis

```bash
# Install Jupyter
pip install jupyter notebook

# Launch and run all cells
jupyter notebook notebooks/manufacturing_analysis.ipynb

# This will:
# - Load and analyze the dataset
# - Create 10+ visualizations
# - Train 5 models
# - Save best model and results
# - Generate comprehensive report
```

## 🧪 Test the API

### Make a prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Injection_Temperature": 220.0,
    "Injection_Pressure": 80.0,
    "Cycle_Time": 45.0,
    "Cooling_Time": 20.0,
    "Material_Viscosity": 500.0,
    "Ambient_Temperature": 25.0,
    "Machine_Age": 5,
    "Operator_Experience": 10,
    "Maintenance_Hours": 5.0,
    "Shift": "Day",
    "Machine_Type": "Type_A",
    "Material_Grade": "Standard",
    "Day_of_Week": "Monday",
    "Machine_Utilization": 85.0
  }'
```

### Check health

```bash
curl http://localhost:8000/health
```

### Get model info

```bash
curl http://localhost:8000/model-info
```

## 📁 Project Structure

```
manufacturing_project/
├── data/                  # Dataset and generation script
├── notebooks/            # Jupyter analysis notebook
├── models/               # Trained models and metadata
├── api/                  # FastAPI application
├── reports/              # Visualizations and analysis
├── presentation/         # PowerPoint slides
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
└── README.md            # Full documentation
```

## 🎯 Key Files

1. **Dataset**: `data/manufacturing_dataset_1000_samples.csv`
2. **Analysis**: `notebooks/manufacturing_analysis.ipynb`
3. **API**: `api/main.py`
4. **Models**: `models/best_model.pkl`
5. **Report**: Output document
6. **Slides**: Output presentation (20 slides)

## 📈 Expected Results

- **Model Accuracy**: 97% (Random Forest)
- **RMSE**: ±2.1 parts/hour
- **API Response Time**: <50ms
- **Visualizations**: 10+ charts saved

## 🔧 Troubleshooting

### Docker issues
```bash
# Stop and remove containers
docker-compose down

# Rebuild fresh
docker-compose up --build --force-recreate
```

### Python dependency issues
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Port already in use
```bash
# Change port in docker-compose.yml or use:
docker-compose up -p 8001:8000
```

## 📚 Next Steps

1. **Review the analysis**: Open Jupyter notebook
2. **Test the API**: Use Swagger UI at `/docs`
3. **Read the report**: Check output documents
4. **Review presentation**: 20 comprehensive slides
5. **Deploy to production**: Use Docker compose

## 💡 Pro Tips

- Use Swagger UI (`/docs`) for interactive API testing
- Check `reports/` folder for all visualizations
- Model artifacts in `models/` can be loaded anywhere
- API supports batch predictions for efficiency
- GenAI insights automatically generated with each prediction

## 🎓 Learning Outcomes Demonstrated

✅ Data preprocessing and EDA
✅ Multiple ML model comparison
✅ Model evaluation and selection
✅ REST API development
✅ Docker containerization
✅ GenAI integration
✅ Production-ready deployment
✅ Comprehensive documentation

---

**Questions? Check README.md for full documentation!**
