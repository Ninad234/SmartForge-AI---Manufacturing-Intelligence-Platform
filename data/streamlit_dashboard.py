import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import joblib
import json
import os
import statsmodels.api as sm
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="🏭 Manufacturing AI Dashboard",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {padding: 0rem 1rem;}
    .stMetric {
        background-color: #0000;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .insight-box {
        background-color: #fff3cd;
        color:black;
        border-left: 5px solid #ffc107;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .recommendation-box {
        background-color: #d1ecf1;
        color:black;
        border-left: 5px solid #17a2b8;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    .risk-box {
        background-color: #f8d7da;
        color:black;
        border-left: 5px solid #dc3545;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    h1 {color: #1f4e78;}
    h2 {color: #2e75b6;}
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD MODEL AND DATA
# ============================================================================

@st.cache_resource
def load_model_artifacts():
    """Load trained model, scaler, and metadata - FIXED PATHS!"""
    try:
        # Your folder structure
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # model = joblib.load('models/best_model.pkl')
        # scaler = joblib.load('models/scaler.pkl')
        
        model = joblib.load(os.path.join(BASE_DIR, "models", "best_model.pkl"))
        scaler = joblib.load(os.path.join(BASE_DIR, "models", "scaler.pkl"))

        with open(os.path.join(BASE_DIR, "models", "feature_names.json"), "r") as f:
            feature_names = json.load(f)

        with open(os.path.join(BASE_DIR, "models", "model_metadata.json"), "r") as f:
            metadata = json.load(f)
        
        return model, scaler, feature_names, metadata, None
    except Exception as e:
        return None, None, None, None, str(e)

@st.cache_data
def load_dataset():
    """Load the manufacturing dataset"""
    try:
        df = pd.read_csv('manufacturing_dataset_1000_samples.csv')
        return df, None
    except Exception as e:
        try:
            df = pd.read_csv('data/manufacturing_dataset_1000_samples.csv')
            return df, None
        except:
            return None, str(e)

# ============================================================================
# GENAI FUNCTIONS - ENHANCED & FIXED
# ============================================================================

def generate_personalized_insights(params, prediction, dataset_stats):
    """GenAI: Generate intelligent insights"""
    insights = []
    
    avg_cycle = dataset_stats['Cycle_Time']['mean']
    if params['Cycle_Time'] > avg_cycle + 5:
        insights.append({
            'icon': '⏱️',
            'title': 'High Cycle Time Detected',
            'message': f"Your cycle time ({params['Cycle_Time']:.1f}s) is {params['Cycle_Time'] - avg_cycle:.1f}s above average. This is reducing output significantly.",
            'impact': 'HIGH'
        })
    elif params['Cycle_Time'] < avg_cycle - 5:
        insights.append({
            'icon': '⚡',
            'title': 'Optimized Cycle Time',
            'message': f"Excellent! Your cycle time ({params['Cycle_Time']:.1f}s) is faster than average.",
            'impact': 'POSITIVE'
        })
    
    avg_exp = dataset_stats['Operator_Experience']['mean']
    if params['Operator_Experience'] < 10:
        insights.append({
            'icon': '👨‍🔧',
            'title': 'Operator Experience Gap',
            'message': f"Operator has {params['Operator_Experience']} years (avg: {avg_exp:.0f}). Training could improve efficiency.",
            'impact': 'MEDIUM'
        })
    elif params['Operator_Experience'] > 20:
        insights.append({
            'icon': '🌟',
            'title': 'Expert Operator',
            'message': f"Highly experienced operator ({params['Operator_Experience']} years). Great asset!",
            'impact': 'POSITIVE'
        })
    
    if params['Machine_Age'] > 10:
        insights.append({
            'icon': '⚙️',
            'title': 'Aging Equipment',
            'message': f"Machine is {params['Machine_Age']} years old. Increased maintenance recommended.",
            'impact': 'MEDIUM'
        })
    
    if params['Shift'] == 'Night':
        insights.append({
            'icon': '🌙',
            'title': 'Night Shift Operation',
            'message': "Night shift shows 5-8% lower output historically. Ensure adequate supervision.",
            'impact': 'LOW'
        })
    elif params['Shift'] == 'Day':
        insights.append({
            'icon': '☀️',
            'title': 'Day Shift - Peak Performance',
            'message': "Day shift typically achieves highest productivity.",
            'impact': 'POSITIVE'
        })
    
    return insights

def generate_optimization_recommendations(params, prediction, target_output=None):
    """GenAI: Generate optimization recommendations"""
    recommendations = []
    
    if target_output is None:
        target_output = prediction * 1.15
    
    if params['Cycle_Time'] > 40:
        potential_gain = (params['Cycle_Time'] - 38) * 0.4
        recommendations.append({
            'priority': '🔴 HIGH',
            'action': 'Reduce Cycle Time',
            'current': f"{params['Cycle_Time']:.1f}s",
            'target': '35-38s',
            'how': 'Optimize cooling efficiency, check mold temperature',
            'gain': f"+{potential_gain:.1f} parts/hour"
        })
    
    if params['Injection_Pressure'] < 110:
        potential_gain = (115 - params['Injection_Pressure']) * 0.05
        recommendations.append({
            'priority': '🟡 MEDIUM',
            'action': 'Increase Injection Pressure',
            'current': f"{params['Injection_Pressure']:.0f} MPa",
            'target': '110-120 MPa',
            'how': 'Gradually increase in 5 MPa increments',
            'gain': f"+{potential_gain:.1f} parts/hour"
        })
    
    if params['Maintenance_Hours'] < 45:
        recommendations.append({
            'priority': '🟢 LOW',
            'action': 'Increase Preventive Maintenance',
            'current': f"{params['Maintenance_Hours']:.0f} hrs/month",
            'target': '50-55 hrs/month',
            'how': 'Schedule weekly inspections and calibration',
            'gain': '+2.0 parts/hour'
        })
    
    return recommendations

def generate_risk_alerts(params, prediction, dataset_stats):
    """GenAI: Risk detection"""
    alerts = []
    
    if params['Cycle_Time'] < 30:
        alerts.append({
            'level': 'WARNING',
            'icon': '⚠️',
            'title': 'Quality Risk: Cycle Time Too Fast',
            'message': 'Very short cycle may compromise quality.',
            'action': 'Increase quality checks'
        })
    
    if params['Machine_Age'] > 12 and params['Maintenance_Hours'] < 40:
        alerts.append({
            'level': 'CRITICAL',
            'icon': '🚨',
            'title': 'Equipment Failure Risk',
            'message': f"Old machine ({params['Machine_Age']} years) + low maintenance",
            'action': 'Schedule immediate inspection'
        })
    
    if prediction < dataset_stats['Parts_Per_Hour']['mean'] * 0.7:
        alerts.append({
            'level': 'CRITICAL',
            'icon': '🚨',
            'title': 'Severe Underperformance',
            'message': f"Output ({prediction:.1f}) is very low",
            'action': 'Investigate immediately'
        })
    
    return alerts

def make_prediction(params, model, scaler, feature_names):
    """Make prediction - FIXED!"""
    try:
        input_data = {
            'Injection_Temperature': params['Injection_Temperature'],
            'Injection_Pressure': params['Injection_Pressure'],
            'Cycle_Time': params['Cycle_Time'],
            'Cooling_Time': params['Cooling_Time'],
            'Material_Viscosity': params['Material_Viscosity'],
            'Ambient_Temperature': params['Ambient_Temperature'],
            'Machine_Age': params['Machine_Age'],
            'Operator_Experience': params['Operator_Experience'],
            'Maintenance_Hours': params['Maintenance_Hours'],
            'Temperature_Pressure_Ratio': params['Injection_Temperature'] / max(params['Injection_Pressure'], 0.1),
            'Total_Cycle_Time': params['Cycle_Time'] + params['Cooling_Time'],
            'Efficiency_Score': (100 - params['Machine_Age'] * 2) + (params['Maintenance_Hours'] / 10 * 3) + (params['Operator_Experience'] * 1.5),
            'Machine_Utilization': params['Machine_Utilization'],
            'Shift': params['Shift'],
            'Machine_Type': params['Machine_Type'],
            'Material_Grade': params['Material_Grade'],
            'Day_of_Week': params['Day_of_Week']
        }
        
        df = pd.DataFrame([input_data])
        df = pd.get_dummies(df, columns=['Shift', 'Machine_Type', 'Material_Grade', 'Day_of_Week'], drop_first=True)
        
        for feature in feature_names:
            if feature not in df.columns:
                df[feature] = 0
        
        df = df[feature_names]
        scaled = scaler.transform(df)
        prediction = model.predict(scaled)[0]
        
        return max(5, min(70, prediction))
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return 30.0

# ============================================================================
# LOAD EVERYTHING
# ============================================================================

model, scaler, feature_names, metadata, model_error = load_model_artifacts()
df, data_error = load_dataset()

if model_error or data_error:
    st.error("⚠️ **Error Loading Files**")
    if model_error:
        st.error(f"Model Error: {model_error}")
    if data_error:
        st.error(f"Data Error: {data_error}")
    st.info("📁 **Expected folder structure:**\n```\nmanufacturing_project/\n├── streamlit_dashboard.py\n├── manufacturing_dataset_1000_samples.xlsx\n└── models/\n    ├── best_model.pkl\n    ├── scaler.pkl\n    ├── feature_names.json\n    └── model_metadata.json\n```")
    st.stop()

# Calculate dataset stats
dataset_stats = {
    'Parts_Per_Hour': {
        'mean': df['Parts_Per_Hour'].mean(),
        'std': df['Parts_Per_Hour'].std(),
        'min': df['Parts_Per_Hour'].min(),
        'max': df['Parts_Per_Hour'].max()
    },
    'Cycle_Time': {
        'mean': df['Cycle_Time'].mean(),
        'std': df['Cycle_Time'].std()
    },
    'Operator_Experience': {
        'mean': df['Operator_Experience'].mean(),
        'std': df['Operator_Experience'].std()
    }
}

# ============================================================================
# HEADER
# ============================================================================

st.title("🏭 Manufacturing Output Prediction Dashboard")
st.markdown("### AI-Powered Production Optimization System")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Model Accuracy", f"{metadata['test_r2']*100:.1f}%", "Excellent")
with col2:
    st.metric("Avg Error", f"±{metadata['test_rmse']:.1f}", "parts/hour")
with col3:
    st.metric("Model Type", metadata['best_model'])
with col4:
    st.metric("Features", metadata['n_features'])

st.markdown("---")

# ============================================================================
# SIDEBAR - FIXED SLIDERS!
# ============================================================================

st.sidebar.header("🎛️ Machine Parameters")

tab_mode = st.sidebar.radio("Input Mode", ["🖐️ Manual Entry", "📊 Quick Presets"])

if tab_mode == "🖐️ Manual Entry":
    st.sidebar.subheader("Process Parameters")
    
    # FIXED: Adjusted max values based on dataset
    injection_temp = st.sidebar.slider(
        "Injection Temperature (°C)",
        min_value=180.0,
        max_value=300.0,  # ✅ FIXED: Increased from 260
        value=215.0,
        step=1.0,
        help="Barrel temperature for material melting",
        key="temp_slider"
    )
    
    injection_pressure = st.sidebar.slider(
        "Injection Pressure (MPa)",
        min_value=80.0,
        max_value=150.0,
        value=115.0,
        step=1.0,
        help="Pressure applied during injection",
        key="pressure_slider"
    )
    
    cycle_time = st.sidebar.slider(
        "Cycle Time (seconds)",
        min_value=16.0,
        max_value=60.0,
        value=36.0,
        step=1.0,
        help="Total time per production cycle",
        key="cycle_slider"
    )
    
    cooling_time = st.sidebar.slider(
        "Cooling Time (seconds)",
        min_value=8.0,
        max_value=20.0,
        value=12.0,
        step=0.5,
        help="Time allowed for part cooling",
        key="cooling_slider"
    )
    
    st.sidebar.subheader("Material & Environment")
    
    material_viscosity = st.sidebar.slider(
        "Material Viscosity (Pa·s)",
        min_value=100.0,
        max_value=1000.0,  # ✅ FIXED: Increased from 500
        value=240.0,
        step=10.0,
        key="viscosity_slider"
    )
    
    ambient_temp = st.sidebar.slider(
        "Ambient Temperature (°C)",
        min_value=18.0,
        max_value=28.0,
        value=23.0,
        step=0.5,
        key="ambient_slider"
    )
    
    material_grade = st.sidebar.selectbox(
        "Material Grade",
        ["Economy", "Standard", "Premium"],
        index=1,
        key="grade_select"
    )
    
    st.sidebar.subheader("Equipment & Personnel")
    
    machine_age = st.sidebar.slider(
        "Machine Age (years)",
        min_value=1,
        max_value=15,
        value=8,
        step=1,
        key="age_slider"
    )
    
    operator_exp = st.sidebar.slider(
        "Operator Experience (years)",
        min_value=1,
        max_value=120,  # ✅ FIXED: Increased from 30
        value=15,
        step=1,
        key="exp_slider"
    )
    
    maintenance_hours = st.sidebar.slider(
        "Monthly Maintenance (hours)",
        min_value=26,
        max_value=500,  # ✅ FIXED: Increased from 100
        value=50,
        step=1,
        key="maint_slider"
    )
    
    machine_utilization = st.sidebar.slider(
        "Machine Utilization",
        min_value=0.0,
        max_value=1.0,  # ✅ FIXED: Changed to 0-1 range
        value=0.36,
        step=0.01,
        format="%.2f",
        key="util_slider"
    )
    
    st.sidebar.subheader("Operational Context")
    
    shift = st.sidebar.selectbox(
        "Shift",
        ["Day", "Evening", "Night"],
        index=0,
        key="shift_select"
    )
    
    machine_type = st.sidebar.selectbox(
        "Machine Type",
        ["Type_A", "Type_B", "Type_C"],
        index=0,
        key="type_select"
    )
    
    day_of_week = st.sidebar.selectbox(
        "Day of Week",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        index=0,
        key="day_select"
    )

else:  # Quick Presets
    preset = st.sidebar.selectbox(
        "Select Preset Scenario",
        [
            "🎯 Optimal Settings",
            "⚡ Speed Focus",
            "💎 Quality Focus",
            "🔧 Old Machine",
            "👨‍🎓 New Operator"
        ],
        key="preset_select"
    )
    
    if preset == "🎯 Optimal Settings":
        injection_temp, injection_pressure = 220.0, 115.0
        cycle_time, cooling_time = 36.0, 12.0
        material_viscosity, ambient_temp = 240.0, 23.0
        machine_age, operator_exp = 5, 20
        maintenance_hours, machine_utilization = 55, 0.45
        shift, machine_type, material_grade = "Day", "Type_A", "Standard"
        day_of_week = "Wednesday"
        
    elif preset == "⚡ Speed Focus":
        injection_temp, injection_pressure = 230.0, 125.0
        cycle_time, cooling_time = 25.0, 9.0
        material_viscosity, ambient_temp = 200.0, 23.0
        machine_age, operator_exp = 3, 15
        maintenance_hours, machine_utilization = 50, 0.55
        shift, machine_type, material_grade = "Day", "Type_A", "Premium"
        day_of_week = "Tuesday"
        
    elif preset == "💎 Quality Focus":
        injection_temp, injection_pressure = 215.0, 105.0
        cycle_time, cooling_time = 50.0, 18.0
        material_viscosity, ambient_temp = 300.0, 22.0
        machine_age, operator_exp = 4, 25
        maintenance_hours, machine_utilization = 60, 0.35
        shift, machine_type, material_grade = "Day", "Type_B", "Premium"
        day_of_week = "Wednesday"
        
    elif preset == "🔧 Old Machine":
        injection_temp, injection_pressure = 210.0, 100.0
        cycle_time, cooling_time = 45.0, 15.0
        material_viscosity, ambient_temp = 250.0, 24.0
        machine_age, operator_exp = 13, 18
        maintenance_hours, machine_utilization = 35, 0.28
        shift, machine_type, material_grade = "Evening", "Type_C", "Standard"
        day_of_week = "Thursday"
        
    else:  # New Operator
        injection_temp, injection_pressure = 215.0, 110.0
        cycle_time, cooling_time = 42.0, 13.0
        material_viscosity, ambient_temp = 240.0, 23.0
        machine_age, operator_exp = 6, 3
        maintenance_hours, machine_utilization = 48, 0.32
        shift, machine_type, material_grade = "Day", "Type_A", "Standard"
        day_of_week = "Monday"

# ============================================================================
# BUILD PARAMS & MAKE PREDICTION
# ============================================================================

params = {
    'Injection_Temperature': injection_temp,
    'Injection_Pressure': injection_pressure,
    'Cycle_Time': cycle_time,
    'Cooling_Time': cooling_time,
    'Material_Viscosity': material_viscosity,
    'Ambient_Temperature': ambient_temp,
    'Machine_Age': machine_age,
    'Operator_Experience': operator_exp,
    'Maintenance_Hours': maintenance_hours,
    'Machine_Utilization': machine_utilization,
    'Shift': shift,
    'Machine_Type': machine_type,
    'Material_Grade': material_grade,
    'Day_of_Week': day_of_week
}

# REAL-TIME PREDICTION - Updates automatically when sliders change!
prediction = make_prediction(params, model, scaler, feature_names)

# ============================================================================
# MAIN DISPLAY - AUTO-UPDATES!
# ============================================================================

st.markdown(f"""
    <div class="prediction-box">
        <h1 style="margin:0; color:white;">🎯 Predicted Output</h1>
        <h1 style="font-size: 72px; margin:10px 0; color:white;">{prediction:.1f}</h1>
        <h3 style="margin:0; color:white;">Parts Per Hour</h3>
        <p style="margin-top:15px; opacity:0.9;">Confidence: ±{metadata['test_rmse']:.1f} parts/hour</p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

avg_output = dataset_stats['Parts_Per_Hour']['mean']
max_output = dataset_stats['Parts_Per_Hour']['max']

with col1:
    diff_avg = prediction - avg_output
    st.metric(
        "vs Average",
        f"{prediction:.1f}",
        f"{diff_avg:+.1f} parts/hour"
    )

with col2:
    percentile = (df['Parts_Per_Hour'] < prediction).mean() * 100
    st.metric(
        "Performance Percentile",
        f"{percentile:.0f}%",
        "of all scenarios"
    )

with col3:
    potential = max_output - prediction
    st.metric(
        "Improvement Potential",
        f"+{potential:.1f}",
        "to max observed"
    )

st.markdown("---")

# ============================================================================
# GENAI INSIGHTS - AUTO-UPDATE!
# ============================================================================

st.header("🤖 AI-Powered Insights & Recommendations")

tab1, tab2, tab3 = st.tabs([
    "💡 Intelligent Insights",
    "⚡ Optimization Tips",
    "🚨 Risk Alerts"
])

with tab1:
    st.subheader("Why This Prediction?")
    insights = generate_personalized_insights(params, prediction, dataset_stats)
    
    if insights:
        for insight in insights:
            impact_color = {
                'HIGH': '#dc3545',
                'MEDIUM': '#ffc107',
                'LOW': '#17a2b8',
                'POSITIVE': '#28a745'
            }.get(insight['impact'], '#6c757d')
            
            st.markdown(f"""
                <div class="insight-box">
                    <h4>{insight['icon']} {insight['title']} <span style="color:{impact_color}">({insight['impact']} IMPACT)</span></h4>
                    <p>{insight['message']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("✅ All parameters well-optimized!")

with tab2:
    st.subheader("How to Improve")
    recommendations = generate_optimization_recommendations(params, prediction)
    
    if recommendations:
        for rec in recommendations:
            st.markdown(f"""
                <div class="recommendation-box">
                    <h4>{rec['priority']} {rec['action']}</h4>
                    <p><strong>Current:</strong> {rec['current']} → <strong>Target:</strong> {rec['target']}</p>
                    <p><strong>How:</strong> {rec['how']}</p>
                    <p><strong>Expected Gain:</strong> {rec['gain']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.success("🎉 Already optimized!")

with tab3:
    st.subheader("Risk Detection")
    alerts = generate_risk_alerts(params, prediction, dataset_stats)
    
    if alerts:
        for alert in alerts:
            st.markdown(f"""
                <div class="risk-box">
                    <h4>{alert['icon']} {alert['level']}: {alert['title']}</h4>
                    <p><strong>Issue:</strong> {alert['message']}</p>
                    <p><strong>Action:</strong> {alert['action']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.success("✅ No risks detected!")

st.markdown("---")

# ============================================================================
# VISUALIZATIONS - AUTO-UPDATE!
# ============================================================================

st.header("📊 Data Analysis")

viz_tab1, viz_tab2 = st.tabs(["📈 Your Position", "🔗 Key Relationships"])

with viz_tab1:
    fig = px.histogram(
        df,
        x='Parts_Per_Hour',
        nbins=30,
        title="Where You Stand",
        color_discrete_sequence=['#667eea']
    )
    
    fig.add_vline(
        x=prediction,
        line_dash="dash",
        line_color="red",
        annotation_text=f"You: {prediction:.1f}",
        annotation_position="top"
    )
    
    fig.add_vline(
        x=avg_output,
        line_dash="dot",
        line_color="green",
        annotation_text=f"Avg: {avg_output:.1f}",
        annotation_position="bottom"
    )
    
    st.plotly_chart(fig, use_container_width=True)

with viz_tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.scatter(
            df,
            x='Cycle_Time',
            y='Parts_Per_Hour',
            color='Machine_Type',
            title="Cycle Time Impact",
            trendline="ols"
        )
        
        fig.add_scatter(
            x=[cycle_time],
            y=[prediction],
            mode='markers',
            marker=dict(size=15, color='red', symbol='star'),
            name='Your Setting',
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.box(
            df,
            x='Shift',
            y='Parts_Per_Hour',
            color='Shift',
            title="Output by Shift"
        )
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("""
    <div style="text-align:center; padding:20px;">
        <p style="color:#666;">
            🏭 Manufacturing AI Dashboard | Model: {model} | Accuracy: {acc}%
        </p>
    </div>
""".format(model=metadata['best_model'], acc=f"{metadata['test_r2']*100:.1f}"), unsafe_allow_html=True)