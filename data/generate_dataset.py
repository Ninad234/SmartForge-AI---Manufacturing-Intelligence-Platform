import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate 1000 samples
n_samples = 1000

# Generate base features
data = {
    'Timestamp': [datetime(2024, 1, 1) + timedelta(hours=i) for i in range(n_samples)],
    'Injection_Temperature': np.random.normal(220, 15, n_samples),  # Celsius
    'Injection_Pressure': np.random.normal(80, 10, n_samples),  # MPa
    'Cycle_Time': np.random.normal(45, 8, n_samples),  # seconds
    'Cooling_Time': np.random.normal(20, 4, n_samples),  # seconds
    'Material_Viscosity': np.random.normal(500, 50, n_samples),  # Pa·s
    'Ambient_Temperature': np.random.normal(25, 3, n_samples),  # Celsius
    'Machine_Age': np.random.randint(1, 15, n_samples),  # years
    'Operator_Experience': np.random.randint(1, 20, n_samples),  # years
    'Maintenance_Hours': np.random.normal(5, 2, n_samples),  # hours per month
    'Shift': np.random.choice(['Day', 'Night', 'Evening'], n_samples, p=[0.4, 0.35, 0.25]),
    'Machine_Type': np.random.choice(['Type_A', 'Type_B'], n_samples, p=[0.6, 0.4]),
    'Material_Grade': np.random.choice(['Economy', 'Standard', 'Premium'], n_samples, p=[0.3, 0.5, 0.2]),
    'Day_of_Week': np.random.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], n_samples)
}

df = pd.DataFrame(data)

# Create engineered features
df['Temperature_Pressure_Ratio'] = df['Injection_Temperature'] / df['Injection_Pressure']
df['Total_Cycle_Time'] = df['Cycle_Time'] + df['Cooling_Time']
df['Efficiency_Score'] = (100 - df['Machine_Age'] * 2) + (df['Maintenance_Hours'] * 3) + (df['Operator_Experience'] * 1.5)
df['Machine_Utilization'] = np.random.normal(85, 10, n_samples)

# Generate target variable (Parts_Per_Hour) with realistic relationships
base_output = 80

# Positive influences
output = base_output + \
         (df['Injection_Temperature'] - 220) * 0.3 + \
         (df['Injection_Pressure'] - 80) * 0.5 + \
         (df['Operator_Experience'] - 10) * 0.8 + \
         (df['Maintenance_Hours'] - 5) * 2 + \
         (df['Machine_Utilization'] - 85) * 0.2

# Negative influences
output -= (df['Cycle_Time'] - 45) * 0.4
output -= (df['Machine_Age'] - 7) * 1.2
output -= (df['Material_Viscosity'] - 500) * 0.01

# Shift effects
shift_effect = {'Day': 5, 'Night': -3, 'Evening': 0}
output += df['Shift'].map(shift_effect)

# Machine type effects
machine_effect = {'Type_A': 3, 'Type_B': -2}
output += df['Machine_Type'].map(machine_effect)

# Material grade effects
material_effect = {'Economy': -5, 'Standard': 0, 'Premium': 7}
output += df['Material_Grade'].map(material_effect)

# Add some random noise
output += np.random.normal(0, 3, n_samples)

# Ensure reasonable bounds (50-120 parts per hour)
df['Parts_Per_Hour'] = np.clip(output, 50, 120)

# Introduce missing values strategically (20 each)
missing_indices = np.random.choice(df.index, 20, replace=False)
df.loc[missing_indices, 'Material_Viscosity'] = np.nan

missing_indices = np.random.choice(df.index, 20, replace=False)
df.loc[missing_indices, 'Ambient_Temperature'] = np.nan

missing_indices = np.random.choice(df.index, 20, replace=False)
df.loc[missing_indices, 'Operator_Experience'] = np.nan

# Save dataset
df.to_csv('/home/claude/manufacturing_project/data/manufacturing_dataset_1000_samples.csv', index=False)
print(f"Dataset generated successfully with {len(df)} samples!")
print(f"\nDataset shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nMissing values:")
print(df.isnull().sum())
print(f"\nBasic statistics:")
print(df.describe())
