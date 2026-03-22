from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import json
import numpy as np
import pandas as pd
from typing import List, Optional, Dict, Any
import os

# Initialize FastAPI app
app = FastAPI(
    title="Manufacturing Output Prediction API",
    description="AI-powered API for predicting manufacturing equipment output with intelligent insights",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load models and artifacts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR,"models","best_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR,"models","scaler.pkl")
FEATURE_NAMES_PATH = os.path.join(BASE_DIR,"models","feature_names.json")
METADATA_PATH = os.path.join(BASE_DIR,"models","model_metadata.json")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    with open(FEATURE_NAMES_PATH, 'r') as f:
        feature_names = json.load(f)
    with open(METADATA_PATH, 'r') as f:
        metadata = json.load(f)
    print("✓ Models and artifacts loaded successfully!")
except Exception as e:
    print(f"⚠ Error loading models: {e}")
    model, scaler, feature_names, metadata = None, None, None, None


# Pydantic models for request/response
class MachineParameters(BaseModel):
    """Input parameters for prediction"""
    Injection_Temperature: float = Field(..., description="Injection temperature in Celsius", ge=180, le=260)
    Injection_Pressure: float = Field(..., description="Injection pressure in MPa", ge=50, le=120)
    Cycle_Time: float = Field(..., description="Cycle time in seconds", ge=20, le=80)
    Cooling_Time: float = Field(..., description="Cooling time in seconds", ge=10, le=40)
    Material_Viscosity: float = Field(..., description="Material viscosity in Pa·s", ge=300, le=700)
    Ambient_Temperature: float = Field(..., description="Ambient temperature in Celsius", ge=15, le=35)
    Machine_Age: int = Field(..., description="Machine age in years", ge=0, le=20)
    Operator_Experience: int = Field(..., description="Operator experience in years", ge=0, le=30)
    Maintenance_Hours: float = Field(..., description="Maintenance hours per month", ge=0, le=15)
    Shift: str = Field(..., description="Shift: Day, Night, or Evening")
    Machine_Type: str = Field(..., description="Machine type: Type_A or Type_B")
    Material_Grade: str = Field(..., description="Material grade: Economy, Standard, or Premium")
    Day_of_Week: str = Field(..., description="Day of week")
    Temperature_Pressure_Ratio: Optional[float] = Field(None, description="Auto-calculated if not provided")
    Total_Cycle_Time: Optional[float] = Field(None, description="Auto-calculated if not provided")
    Efficiency_Score: Optional[float] = Field(None, description="Auto-calculated if not provided")
    Machine_Utilization: float = Field(85.0, description="Machine utilization percentage")

    class Config:
        json_schema_extra = {
            "example": {
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
            }
        }


class PredictionResponse(BaseModel):
    """Response with prediction and insights"""
    predicted_output: float
    confidence_interval: Dict[str, float]
    performance_category: str
    ai_insights: List[str]
    optimization_suggestions: List[str]
    risk_alerts: List[str]
    model_info: Dict[str, Any]


class BatchPredictionRequest(BaseModel):
    """Batch prediction request"""
    scenarios: List[MachineParameters]


class OptimizationRequest(BaseModel):
    """Request for optimization recommendations"""
    current_parameters: MachineParameters
    target_output: float
    constraints: Optional[Dict[str, Any]] = None


# Helper functions
def calculate_engineered_features(params: MachineParameters) -> MachineParameters:
    """Calculate engineered features if not provided"""
    if params.Temperature_Pressure_Ratio is None:
        params.Temperature_Pressure_Ratio = params.Injection_Temperature / params.Injection_Pressure
    
    if params.Total_Cycle_Time is None:
        params.Total_Cycle_Time = params.Cycle_Time + params.Cooling_Time
    
    if params.Efficiency_Score is None:
        params.Efficiency_Score = (
            (100 - params.Machine_Age * 2) + 
            (params.Maintenance_Hours * 3) + 
            (params.Operator_Experience * 1.5)
        )
    
    return params


def prepare_features(params: MachineParameters) -> np.ndarray:
    """Convert parameters to feature array matching model's expected format"""
    # Calculate engineered features
    params = calculate_engineered_features(params)
    
    # Create dataframe with raw features
    data = {
        'Injection_Temperature': [params.Injection_Temperature],
        'Injection_Pressure': [params.Injection_Pressure],
        'Cycle_Time': [params.Cycle_Time],
        'Cooling_Time': [params.Cooling_Time],
        'Material_Viscosity': [params.Material_Viscosity],
        'Ambient_Temperature': [params.Ambient_Temperature],
        'Machine_Age': [params.Machine_Age],
        'Operator_Experience': [params.Operator_Experience],
        'Maintenance_Hours': [params.Maintenance_Hours],
        'Temperature_Pressure_Ratio': [params.Temperature_Pressure_Ratio],
        'Total_Cycle_Time': [params.Total_Cycle_Time],
        'Efficiency_Score': [params.Efficiency_Score],
        'Machine_Utilization': [params.Machine_Utilization],
        'Shift': [params.Shift],
        'Machine_Type': [params.Machine_Type],
        'Material_Grade': [params.Material_Grade],
        'Day_of_Week': [params.Day_of_Week]
    }
    
    df = pd.DataFrame(data)
    
    # One-hot encode categorical variables
    df = pd.get_dummies(df, columns=['Shift', 'Machine_Type', 'Material_Grade', 'Day_of_Week'], drop_first=True)
    
    # Ensure all expected features are present
    for feature in feature_names:
        if feature not in df.columns:
            df[feature] = 0
    
    # Reorder columns to match training
    df = df[feature_names]
    
    return df.values


def generate_ai_insights(params: MachineParameters, prediction: float) -> List[str]:
    """Generate AI-powered insights using GenAI-style analysis"""
    insights = []
    
    # Performance insight
    if prediction >= 90:
        insights.append(f"🎯 Excellent performance predicted: {prediction:.1f} parts/hour - operating at high efficiency")
    elif prediction >= 75:
        insights.append(f"✓ Good performance predicted: {prediction:.1f} parts/hour - within optimal range")
    else:
        insights.append(f"⚠ Below-average performance predicted: {prediction:.1f} parts/hour - optimization recommended")
    
    # Temperature analysis
    if params.Injection_Temperature > 230:
        insights.append("🌡️ High injection temperature detected - may increase energy costs but improve material flow")
    elif params.Injection_Temperature < 210:
        insights.append("🌡️ Low injection temperature - may reduce energy costs but affect part quality")
    
    # Cycle time analysis
    if params.Cycle_Time < 35:
        insights.append("⚡ Fast cycle time - maximizing throughput but monitor for quality issues")
    elif params.Cycle_Time > 55:
        insights.append("🐌 Slow cycle time - quality-focused but reducing overall output")
    
    # Machine age impact
    if params.Machine_Age > 10:
        insights.append(f"⚙️ Aging equipment ({params.Machine_Age} years) - regular maintenance critical")
    
    # Operator experience
    if params.Operator_Experience > 15:
        insights.append("👨‍🔧 Highly experienced operator - leverage expertise for process optimization")
    elif params.Operator_Experience < 5:
        insights.append("📚 Less experienced operator - consider additional training for efficiency gains")
    
    # Shift analysis
    if params.Shift == "Night":
        insights.append("🌙 Night shift - monitor for fatigue-related quality variations")
    elif params.Shift == "Day":
        insights.append("☀️ Day shift - typically highest productivity period")
    
    # Material grade
    if params.Material_Grade == "Premium":
        insights.append("💎 Premium material grade - higher output potential with optimized settings")
    elif params.Material_Grade == "Economy":
        insights.append("💰 Economy material grade - cost-effective but may limit maximum output")
    
    return insights


def generate_optimization_suggestions(params: MachineParameters, prediction: float) -> List[str]:
    """Generate actionable optimization suggestions"""
    suggestions = []
    
    # Temperature optimization
    optimal_temp_range = (215, 225)
    if params.Injection_Temperature < optimal_temp_range[0]:
        suggestions.append(f"📈 Increase injection temperature to {optimal_temp_range[0]}-{optimal_temp_range[1]}°C for improved output (+3-5 parts/hour)")
    elif params.Injection_Temperature > optimal_temp_range[1]:
        suggestions.append(f"📉 Reduce injection temperature to {optimal_temp_range[0]}-{optimal_temp_range[1]}°C to balance output and energy efficiency")
    
    # Pressure optimization
    optimal_pressure_range = (75, 85)
    if params.Injection_Pressure < optimal_pressure_range[0]:
        suggestions.append(f"📈 Increase injection pressure to {optimal_pressure_range[0]}-{optimal_pressure_range[1]} MPa (+2-4 parts/hour)")
    
    # Cycle time optimization
    if params.Cycle_Time > 50:
        suggestions.append("⚡ Reduce cycle time by optimizing cooling efficiency (potential +5-8 parts/hour)")
    
    # Maintenance suggestions
    if params.Maintenance_Hours < 4:
        suggestions.append("🔧 Increase preventive maintenance to 5-6 hours/month (potential +3-6 parts/hour)")
    
    # Machine utilization
    if params.Machine_Utilization < 80:
        suggestions.append(f"📊 Improve machine utilization from {params.Machine_Utilization:.1f}% to 85%+ through better scheduling")
    
    # Material-specific
    if params.Material_Grade == "Economy" and prediction < 75:
        suggestions.append("💡 Consider upgrading to Standard grade material for +5-8 parts/hour boost")
    
    return suggestions[:5]  # Return top 5 suggestions


def generate_risk_alerts(params: MachineParameters, prediction: float) -> List[str]:
    """Generate risk alerts based on parameters"""
    alerts = []
    
    # Performance risk
    if prediction < 60:
        alerts.append("🚨 CRITICAL: Predicted output significantly below target - immediate intervention required")
    elif prediction < 70:
        alerts.append("⚠️ WARNING: Below-optimal output predicted - review settings")
    
    # Equipment risk
    if params.Machine_Age > 12 and params.Maintenance_Hours < 5:
        alerts.append("⚠️ WARNING: Old equipment with insufficient maintenance - failure risk elevated")
    
    # Quality risk
    if params.Cycle_Time < 30:
        alerts.append("⚠️ CAUTION: Very fast cycle time may compromise part quality")
    
    # Operator risk
    if params.Operator_Experience < 3 and params.Shift == "Night":
        alerts.append("⚠️ CAUTION: Inexperienced operator on night shift - increased error probability")
    
    # Temperature risk
    if params.Injection_Temperature > 240 or params.Injection_Temperature < 200:
        alerts.append("⚠️ WARNING: Extreme temperature setting - material degradation or incomplete filling risk")
    
    return alerts


# API Endpoints
@app.get("/")
def root():
    """Root endpoint with API information"""
    return {
        "message": "Manufacturing Output Prediction API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "predict": "/predict",
            "batch_predict": "/batch-predict",
            "optimize": "/optimize",
            "health": "/health",
            "model_info": "/model-info"
        }
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if model is not None else "unhealthy",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None,
        "features_loaded": feature_names is not None
    }


@app.get("/model-info")
def get_model_info():
    """Get model information and metadata"""
    if metadata is None:
        raise HTTPException(status_code=503, detail="Model metadata not loaded")
    
    return {
        "model_name": metadata.get("best_model"),
        "performance_metrics": {
            "test_rmse": metadata.get("test_rmse"),
            "test_mae": metadata.get("test_mae"),
            "test_r2": metadata.get("test_r2"),
            "test_mse": metadata.get("test_mse")
        },
        "model_details": {
            "n_features": metadata.get("n_features"),
            "n_samples_train": metadata.get("n_samples_train"),
            "n_samples_test": metadata.get("n_samples_test")
        },
        "interpretation": {
            "accuracy": f"{metadata.get('test_r2', 0)*100:.1f}% variance explained",
            "average_error": f"±{metadata.get('test_rmse', 0):.2f} parts/hour"
        }
    }


@app.post("/predict", response_model=PredictionResponse)
def predict_output(params: MachineParameters):
    """
    Predict manufacturing output with AI-powered insights
    
    Returns prediction, confidence interval, and intelligent recommendations
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Prepare features
        features = prepare_features(params)
        
        # Scale features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        prediction = max(50, min(120, prediction))  # Clip to realistic range
        
        # Calculate confidence interval (using RMSE from metadata)
        rmse = metadata.get("test_rmse", 5.0)
        confidence_interval = {
            "lower_bound": prediction - 2 * rmse,
            "upper_bound": prediction + 2 * rmse,
            "confidence_level": "95%"
        }
        
        # Categorize performance
        if prediction >= 90:
            performance_category = "Excellent"
        elif prediction >= 75:
            performance_category = "Good"
        elif prediction >= 60:
            performance_category = "Average"
        else:
            performance_category = "Below Average"
        
        # Generate AI insights
        ai_insights = generate_ai_insights(params, prediction)
        optimization_suggestions = generate_optimization_suggestions(params, prediction)
        risk_alerts = generate_risk_alerts(params, prediction)
        
        return PredictionResponse(
            predicted_output=round(prediction, 2),
            confidence_interval=confidence_interval,
            performance_category=performance_category,
            ai_insights=ai_insights,
            optimization_suggestions=optimization_suggestions,
            risk_alerts=risk_alerts,
            model_info={
                "model_type": metadata.get("best_model"),
                "r2_score": metadata.get("test_r2"),
                "rmse": metadata.get("test_rmse")
            }
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


@app.post("/batch-predict")
def batch_predict(request: BatchPredictionRequest):
    """
    Batch prediction for multiple scenarios
    
    Useful for comparing different parameter combinations
    """
    if model is None or scaler is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        results = []
        for i, params in enumerate(request.scenarios):
            features = prepare_features(params)
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]
            prediction = max(50, min(120, prediction))
            
            results.append({
                "scenario_id": i + 1,
                "predicted_output": round(prediction, 2),
                "parameters": params.dict()
            })
        
        # Sort by predicted output
        results_sorted = sorted(results, key=lambda x: x['predicted_output'], reverse=True)
        
        return {
            "total_scenarios": len(results),
            "best_scenario": results_sorted[0],
            "worst_scenario": results_sorted[-1],
            "all_results": results_sorted
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")


@app.post("/optimize")
def optimize_parameters(request: OptimizationRequest):
    """
    AI-powered optimization to reach target output
    
    Provides parameter adjustments to achieve desired production rate
    """
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        current_params = request.current_parameters
        target = request.target_output
        
        # Get current prediction
        current_features = prepare_features(current_params)
        current_scaled = scaler.transform(current_features)
        current_prediction = model.predict(current_scaled)[0]
        
        gap = target - current_prediction
        
        recommendations = []
        
        if abs(gap) < 2:
            recommendations.append("✓ Current settings already near target!")
        else:
            if gap > 0:
                recommendations.append(f"📈 Need to increase output by {gap:.1f} parts/hour")
                
                # Temperature recommendation
                if current_params.Injection_Temperature < 220:
                    temp_increase = min(5, gap * 0.5)
                    recommendations.append(
                        f"• Increase injection temperature by {temp_increase:.1f}°C (potential +{temp_increase*0.3:.1f} parts/hour)"
                    )
                
                # Pressure recommendation
                if current_params.Injection_Pressure < 85:
                    pressure_increase = min(5, gap * 0.3)
                    recommendations.append(
                        f"• Increase injection pressure by {pressure_increase:.1f} MPa (potential +{pressure_increase*0.5:.1f} parts/hour)"
                    )
                
                # Cycle time recommendation
                if current_params.Cycle_Time > 40:
                    cycle_reduction = min(5, gap * 0.4)
                    recommendations.append(
                        f"• Reduce cycle time by {cycle_reduction:.1f} seconds (potential +{cycle_reduction*0.4:.1f} parts/hour)"
                    )
                
                # Maintenance recommendation
                if current_params.Maintenance_Hours < 6:
                    recommendations.append(
                        f"• Increase maintenance to 6 hours/month (potential +{(6-current_params.Maintenance_Hours)*2:.1f} parts/hour)"
                    )
                
            else:
                recommendations.append(f"📉 Current settings exceed target by {abs(gap):.1f} parts/hour")
                recommendations.append("• Consider reducing temperature or pressure to save energy costs")
                recommendations.append("• Current efficiency already optimal for target")
        
        return {
            "current_output": round(current_prediction, 2),
            "target_output": target,
            "gap": round(gap, 2),
            "gap_percentage": round((gap / target) * 100, 1),
            "feasibility": "Achievable" if abs(gap) < 15 else "Challenging",
            "recommendations": recommendations,
            "estimated_timeline": "1-2 hours to implement and stabilize" if abs(gap) < 10 else "4-8 hours for major adjustments"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Optimization error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
