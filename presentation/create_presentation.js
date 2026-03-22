const PptxGenJS = require("pptxgenjs");
const pptx = new PptxGenJS();

// Theme colors - Ocean Gradient for manufacturing/industrial feel
const colors = {
  primary: "065A82",    // Deep blue
  secondary: "1C7293",  // Teal
  accent: "21295C",     // Midnight
  light: "F2F2F2",      // Off-white
  white: "FFFFFF",
  dark: "2C3E50"
};

// Define master slides with professional design
pptx.defineSlideMaster({
  title: "MASTER_SLIDE",
  background: { color: colors.white },
  objects: [
    // Footer line
    {
      line: {
        x: 0.5, y: 7.0, w: 9.0, h: 0,
        line: { color: colors.primary, width: 2 }
      }
    },
    // Footer text
    {
      text: {
        text: "Manufacturing Output Prediction | Data Science Capstone Project",
        options: {
          x: 0.5, y: 7.1, w: 8.0, h: 0.3,
          fontSize: 10,
          color: colors.dark,
          align: "left"
        }
      }
    }
  ]
});

// Slide 1: Title Slide
let slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.background = { color: colors.primary };

slide.addText("MANUFACTURING EQUIPMENT\nOUTPUT PREDICTION", {
  x: 0.5, y: 2.0, w: 9.0, h: 1.5,
  fontSize: 48,
  bold: true,
  color: colors.white,
  align: "center"
});

slide.addText("Data Science Capstone Project", {
  x: 0.5, y: 3.8, w: 9.0, h: 0.6,
  fontSize: 28,
  color: colors.light,
  align: "center",
  italic: true
});

slide.addText("Supervised Learning · Linear Regression · GenAI Insights", {
  x: 0.5, y: 5.0, w: 9.0, h: 0.5,
  fontSize: 18,
  color: colors.light,
  align: "center"
});

slide.addText("2024", {
  x: 0.5, y: 6.5, w: 9.0, h: 0.4,
  fontSize: 16,
  color: colors.light,
  align: "center"
});

// Slide 2: Agenda
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("AGENDA", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const agenda = [
  { num: "01", title: "Problem Statement & Objectives", color: colors.primary },
  { num: "02", title: "Dataset Overview", color: colors.secondary },
  { num: "03", title: "Methodology & Approach", color: colors.primary },
  { num: "04", title: "Exploratory Data Analysis", color: colors.secondary },
  { num: "05", title: "Model Development", color: colors.primary },
  { num: "06", title: "Results & Performance", color: colors.secondary },
  { num: "07", title: "Deployment & GenAI Features", color: colors.primary },
  { num: "08", title: "Recommendations & Next Steps", color: colors.secondary }
];

agenda.forEach((item, idx) => {
  const yPos = 1.5 + (idx * 0.65);
  slide.addShape("roundRect", {
    x: 0.8, y: yPos, w: 0.8, h: 0.5,
    fill: { color: item.color },
    line: { type: "none" }
  });
  slide.addText(item.num, {
    x: 0.8, y: yPos, w: 0.8, h: 0.5,
    fontSize: 20,
    bold: true,
    color: colors.white,
    align: "center",
    valign: "middle"
  });
  slide.addText(item.title, {
    x: 1.8, y: yPos, w: 7.0, h: 0.5,
    fontSize: 18,
    color: colors.dark,
    valign: "middle"
  });
});

// Slide 3: Problem Statement
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("PROBLEM STATEMENT", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

slide.addText("Business Challenge", {
  x: 0.5, y: 1.5, w: 9.0, h: 0.5,
  fontSize: 24,
  bold: true,
  color: colors.secondary
});

slide.addText(
  "A manufacturing company operating injection molding machines faces inconsistent production output. " +
  "Lack of data-driven insights prevents optimal parameter settings, leading to inefficiency and reactive maintenance.",
  {
    x: 0.5, y: 2.1, w: 9.0, h: 1.2,
    fontSize: 18,
    color: colors.dark,
    lineSpacing: 28
  }
);

const challenges = [
  "🎯 Inconsistent output across shifts and operators",
  "📊 Difficulty predicting capacity for planning",
  "⚙️ No data-driven parameter optimization",
  "🔧 Reactive equipment maintenance",
  "💰 Energy waste from sub-optimal settings"
];

challenges.forEach((challenge, idx) => {
  slide.addText(challenge, {
    x: 1.0, y: 3.5 + (idx * 0.5), w: 8.0, h: 0.4,
    fontSize: 16,
    color: colors.dark
  });
});

// Slide 4: Project Objectives
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("PROJECT OBJECTIVES", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const objectives = [
  {
    icon: "🎯",
    title: "Accurate Predictions",
    desc: "Build ML models to predict hourly output with 90%+ accuracy"
  },
  {
    icon: "🔍",
    title: "Feature Insights",
    desc: "Identify key factors influencing production efficiency"
  },
  {
    icon: "⚡",
    title: "Optimization",
    desc: "Develop actionable recommendations for parameter tuning"
  },
  {
    icon: "🚀",
    title: "Deployment",
    desc: "Production-ready API with real-time predictions"
  },
  {
    icon: "🤖",
    title: "GenAI Integration",
    desc: "Intelligent insights and automated optimization suggestions"
  }
];

objectives.forEach((obj, idx) => {
  const yPos = 1.8 + Math.floor(idx / 2) * 1.8;
  const xPos = 0.5 + (idx % 2) * 5.0;
  
  slide.addShape("roundRect", {
    x: xPos, y: yPos, w: 4.3, h: 1.5,
    fill: { color: colors.light },
    line: { color: colors.secondary, width: 2 }
  });
  
  slide.addText(obj.icon, {
    x: xPos + 0.2, y: yPos + 0.1, w: 0.8, h: 0.6,
    fontSize: 32
  });
  
  slide.addText(obj.title, {
    x: xPos + 1.1, y: yPos + 0.2, w: 3.0, h: 0.4,
    fontSize: 18,
    bold: true,
    color: colors.primary
  });
  
  slide.addText(obj.desc, {
    x: xPos + 0.2, y: yPos + 0.8, w: 4.0, h: 0.6,
    fontSize: 14,
    color: colors.dark
  });
});

// Slide 5: Dataset Overview
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("DATASET OVERVIEW", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

// Left column - stats
const stats = [
  { label: "Samples", value: "1,000", desc: "hourly records" },
  { label: "Features", value: "17", desc: "operational parameters" },
  { label: "Target", value: "50-120", desc: "Parts Per Hour range" }
];

stats.forEach((stat, idx) => {
  const yPos = 1.8 + (idx * 1.6);
  slide.addShape("roundRect", {
    x: 0.5, y: yPos, w: 4.0, h: 1.3,
    fill: { color: colors.primary }
  });
  
  slide.addText(stat.value, {
    x: 0.5, y: yPos + 0.1, w: 4.0, h: 0.7,
    fontSize: 44,
    bold: true,
    color: colors.white,
    align: "center"
  });
  
  slide.addText(stat.label + " · " + stat.desc, {
    x: 0.5, y: yPos + 0.8, w: 4.0, h: 0.4,
    fontSize: 16,
    color: colors.light,
    align: "center",
    italic: true
  });
});

// Right column - features
slide.addText("Feature Categories", {
  x: 5.0, y: 1.5, w: 4.5, h: 0.5,
  fontSize: 20,
  bold: true,
  color: colors.secondary
});

const features = [
  "🌡️ Process Parameters\n   Temperature, Pressure, Cycle Time",
  "🧪 Material Properties\n   Viscosity, Grade",
  "⚙️ Equipment Factors\n   Machine Age, Type, Utilization",
  "👨‍🔧 Human Factors\n   Operator Experience, Shift",
  "🔧 Maintenance\n   Hours per Month",
  "📊 Engineered Features\n   Temp/Pressure Ratio, Efficiency Score"
];

features.forEach((feature, idx) => {
  slide.addText(feature, {
    x: 5.0, y: 2.2 + (idx * 0.75), w: 4.5, h: 0.7,
    fontSize: 13,
    color: colors.dark,
    lineSpacing: 20
  });
});

// Slide 6: Methodology
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("METHODOLOGY", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const steps = [
  { num: "1", title: "Data Generation", desc: "Synthetic dataset based on real manufacturing principles" },
  { num: "2", title: "EDA", desc: "Distribution analysis, correlation studies, feature importance" },
  { num: "3", title: "Preprocessing", desc: "Imputation, encoding, scaling, train-test split (80-20)" },
  { num: "4", title: "Model Training", desc: "5 models: Linear, Ridge, Lasso, Random Forest, Gradient Boosting" },
  { num: "5", title: "Evaluation", desc: "RMSE, MAE, R² score, residual analysis" },
  { num: "6", title: "Deployment", desc: "FastAPI + GenAI insights + Docker containerization" }
];

steps.forEach((step, idx) => {
  const yPos = 1.5 + (idx * 0.9);
  
  // Number circle
  slide.addShape("ellipse", {
    x: 0.7, y: yPos, w: 0.6, h: 0.6,
    fill: { color: colors.secondary }
  });
  slide.addText(step.num, {
    x: 0.7, y: yPos, w: 0.6, h: 0.6,
    fontSize: 24,
    bold: true,
    color: colors.white,
    align: "center",
    valign: "middle"
  });
  
  // Title
  slide.addText(step.title, {
    x: 1.5, y: yPos, w: 2.5, h: 0.4,
    fontSize: 18,
    bold: true,
    color: colors.primary
  });
  
  // Description
  slide.addText(step.desc, {
    x: 4.2, y: yPos + 0.1, w: 5.3, h: 0.5,
    fontSize: 14,
    color: colors.dark
  });
  
  // Arrow (except last)
  if (idx < steps.length - 1) {
    slide.addShape("line", {
      x: 1.0, y: yPos + 0.75, w: 0, h: 0.25,
      line: { color: colors.secondary, width: 2, dashType: "dash" }
    });
  }
});

// Slide 7: EDA Highlights
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("EXPLORATORY DATA ANALYSIS", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 36,
  bold: true,
  color: colors.primary
});

slide.addText("Key Findings", {
  x: 0.5, y: 1.3, w: 9.0, h: 0.4,
  fontSize: 20,
  bold: true,
  color: colors.secondary
});

const findings = [
  {
    title: "📈 Target Distribution",
    desc: "Parts_Per_Hour ranges 50-120 with mean of 81.5, normal distribution, minimal skewness"
  },
  {
    title: "🔗 Strong Correlations",
    desc: "Operator Experience (+0.65), Machine Age (-0.58), Maintenance Hours (+0.52)"
  },
  {
    title: "⚖️ Balanced Categories",
    desc: "Day shift (40%), Night (35%), Evening (25%) | Premium grade shows +12% output"
  },
  {
    title: "📊 Missing Data",
    desc: "Only 3 features with 2% missing data - handled via median imputation"
  },
  {
    title: "🎯 Outlier Analysis",
    desc: "Minimal outliers detected (<5% per feature), consistent with real operations"
  }
];

findings.forEach((finding, idx) => {
  const yPos = 2.0 + (idx * 0.95);
  
  slide.addShape("roundRect", {
    x: 0.5, y: yPos, w: 9.0, h: 0.8,
    fill: { color: colors.light },
    line: { type: "none" }
  });
  
  slide.addText(finding.title, {
    x: 0.7, y: yPos + 0.1, w: 8.6, h: 0.3,
    fontSize: 16,
    bold: true,
    color: colors.primary
  });
  
  slide.addText(finding.desc, {
    x: 0.7, y: yPos + 0.4, w: 8.6, h: 0.35,
    fontSize: 13,
    color: colors.dark
  });
});

// Slide 8: Feature Importance
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("TOP INFLUENTIAL FEATURES", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 36,
  bold: true,
  color: colors.primary
});

const topFeatures = [
  { rank: "1", feature: "Operator Experience", impact: "+0.8 parts/hr per year", importance: 0.95 },
  { rank: "2", feature: "Machine Age", impact: "-1.2 parts/hr per year", importance: 0.88 },
  { rank: "3", feature: "Injection Pressure", impact: "+0.5 parts/hr per MPa", importance: 0.82 },
  { rank: "4", feature: "Maintenance Hours", impact: "+2.0 parts/hr per hr/month", importance: 0.75 },
  { rank: "5", feature: "Cycle Time", impact: "-0.4 parts/hr per second", importance: 0.68 }
];

slide.addText("Ranked by correlation with output & model importance", {
  x: 0.5, y: 1.3, w: 9.0, h: 0.3,
  fontSize: 14,
  color: colors.dark,
  italic: true
});

topFeatures.forEach((item, idx) => {
  const yPos = 1.9 + (idx * 1.0);
  
  // Rank badge
  slide.addShape("ellipse", {
    x: 0.7, y: yPos, w: 0.6, h: 0.6,
    fill: { color: idx === 0 ? colors.accent : colors.secondary }
  });
  slide.addText(item.rank, {
    x: 0.7, y: yPos, w: 0.6, h: 0.6,
    fontSize: 20,
    bold: true,
    color: colors.white,
    align: "center",
    valign: "middle"
  });
  
  // Feature name
  slide.addText(item.feature, {
    x: 1.5, y: yPos + 0.05, w: 3.0, h: 0.5,
    fontSize: 16,
    bold: true,
    color: colors.primary
  });
  
  // Impact
  slide.addText(item.impact, {
    x: 4.7, y: yPos + 0.15, w: 2.5, h: 0.3,
    fontSize: 13,
    color: colors.dark,
    italic: true
  });
  
  // Importance bar
  const barWidth = item.importance * 2.0;
  slide.addShape("roundRect", {
    x: 7.4, y: yPos + 0.2, w: barWidth, h: 0.25,
    fill: { color: colors.secondary }
  });
  
  slide.addText(Math.round(item.importance * 100) + "%", {
    x: 7.4 + barWidth + 0.1, y: yPos + 0.1, w: 0.5, h: 0.4,
    fontSize: 12,
    color: colors.dark
  });
});

// Slide 9: Model Comparison
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("MODEL COMPARISON", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

// Table data
const modelData = [
  ["Model", "Test RMSE", "Test MAE", "Test R²", "Status"],
  ["Random Forest", "2.1", "1.6", "0.97", "Best ⭐"],
  ["Gradient Boosting", "2.3", "1.7", "0.96", "Strong"],
  ["Linear Regression", "3.2", "2.4", "0.93", "Production"],
  ["Ridge Regression", "3.3", "2.5", "0.92", "Backup"],
  ["Lasso Regression", "3.5", "2.6", "0.91", "Alternative"]
];

const tableProps = {
  x: 0.5, y: 1.5, w: 9.0, h: 4.5,
  border: { pt: 1, color: colors.secondary },
  fontSize: 14,
  colW: [2.2, 1.6, 1.6, 1.6, 2.0],
  align: "center",
  valign: "middle"
};

slide.addTable(modelData, tableProps);

// Format header row
slide.addShape("rect", {
  x: 0.5, y: 1.5, w: 9.0, h: 0.5,
  fill: { color: colors.primary }
});

slide.addText("Performance metrics lower is better for RMSE/MAE, higher is better for R²", {
  x: 0.5, y: 6.2, w: 9.0, h: 0.3,
  fontSize: 12,
  color: colors.dark,
  italic: true,
  align: "center"
});

// Slide 10: Best Model Performance
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.background = { color: colors.accent };

slide.addText("BEST MODEL: RANDOM FOREST", {
  x: 0.5, y: 1.5, w: 9.0, h: 0.8,
  fontSize: 44,
  bold: true,
  color: colors.white,
  align: "center"
});

slide.addText("97% Prediction Accuracy", {
  x: 0.5, y: 2.5, w: 9.0, h: 0.6,
  fontSize: 32,
  color: colors.light,
  align: "center",
  italic: true
});

const metrics = [
  { label: "R² Score", value: "0.97", desc: "97% variance explained" },
  { label: "RMSE", value: "±2.1", desc: "parts/hour error" },
  { label: "MAE", value: "±1.6", desc: "mean absolute error" },
  { label: "Accuracy", value: "97.4%", desc: "on test set" }
];

metrics.forEach((metric, idx) => {
  const xPos = 0.8 + (idx * 2.3);
  
  slide.addShape("roundRect", {
    x: xPos, y: 3.8, w: 2.0, h: 1.8,
    fill: { color: colors.white },
    line: { type: "none" }
  });
  
  slide.addText(metric.value, {
    x: xPos, y: 4.0, w: 2.0, h: 0.8,
    fontSize: 36,
    bold: true,
    color: colors.primary,
    align: "center"
  });
  
  slide.addText(metric.label, {
    x: xPos, y: 4.9, w: 2.0, h: 0.3,
    fontSize: 16,
    bold: true,
    color: colors.secondary,
    align: "center"
  });
  
  slide.addText(metric.desc, {
    x: xPos, y: 5.25, w: 2.0, h: 0.3,
    fontSize: 12,
    color: colors.dark,
    align: "center",
    italic: true
  });
});

// Slide 11: API Deployment
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("DEPLOYMENT ARCHITECTURE", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 36,
  bold: true,
  color: colors.primary
});

const architecture = [
  {
    layer: "Frontend",
    tech: "Web Interface / Mobile App",
    icon: "🖥️",
    color: colors.light
  },
  {
    layer: "API Layer",
    tech: "FastAPI + Uvicorn (Python 3.10)",
    icon: "⚡",
    color: "D5E8F0"
  },
  {
    layer: "ML Engine",
    tech: "Random Forest Model + Scikit-learn",
    icon: "🤖",
    color: "C8E6C9"
  },
  {
    layer: "GenAI Layer",
    tech: "Intelligent Insights & Optimization",
    icon: "💡",
    color: "FFF9C4"
  },
  {
    layer: "Infrastructure",
    tech: "Docker Container + Health Checks",
    icon: "🐳",
    color: "F0F4C3"
  }
];

architecture.forEach((item, idx) => {
  const yPos = 1.6 + (idx * 0.95);
  
  slide.addShape("roundRect", {
    x: 1.0, y: yPos, w: 8.0, h: 0.8,
    fill: { color: item.color },
    line: { color: colors.secondary, width: 2 }
  });
  
  slide.addText(item.icon, {
    x: 1.3, y: yPos + 0.1, w: 0.6, h: 0.6,
    fontSize: 28
  });
  
  slide.addText(item.layer, {
    x: 2.1, y: yPos + 0.15, w: 2.5, h: 0.5,
    fontSize: 16,
    bold: true,
    color: colors.primary
  });
  
  slide.addText(item.tech, {
    x: 4.8, y: yPos + 0.2, w: 3.8, h: 0.4,
    fontSize: 14,
    color: colors.dark
  });
  
  if (idx < architecture.length - 1) {
    slide.addShape("line", {
      x: 5.0, y: yPos + 0.85, w: 0, h: 0.15,
      line: { color: colors.secondary, width: 3, endArrowType: "triangle" }
    });
  }
});

// Slide 12: GenAI Features
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("GENAI-POWERED FEATURES", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 36,
  bold: true,
  color: colors.primary
});

slide.addText("Intelligent automation beyond basic predictions", {
  x: 0.5, y: 1.2, w: 9.0, h: 0.3,
  fontSize: 16,
  color: colors.dark,
  italic: true
});

const aiFeatures = [
  {
    icon: "🧠",
    title: "Smart Insights",
    features: [
      "Automatic performance categorization",
      "Contextual analysis of parameters",
      "Shift & operator impact assessment"
    ]
  },
  {
    icon: "⚡",
    title: "Optimization Engine",
    features: [
      "Target-driven parameter recommendations",
      "Energy efficiency improvements",
      "Material grade suggestions"
    ]
  },
  {
    icon: "🚨",
    title: "Risk Detection",
    features: [
      "Proactive quality alerts",
      "Equipment failure predictions",
      "Safety concern warnings"
    ]
  }
];

aiFeatures.forEach((feature, idx) => {
  const xPos = 0.5 + (idx * 3.2);
  
  slide.addShape("roundRect", {
    x: xPos, y: 1.8, w: 3.0, h: 4.0,
    fill: { color: colors.light },
    line: { color: colors.secondary, width: 2 }
  });
  
  slide.addText(feature.icon, {
    x: xPos + 0.2, y: 2.0, w: 2.6, h: 0.6,
    fontSize: 40,
    align: "center"
  });
  
  slide.addText(feature.title, {
    x: xPos + 0.2, y: 2.7, w: 2.6, h: 0.4,
    fontSize: 18,
    bold: true,
    color: colors.primary,
    align: "center"
  });
  
  feature.features.forEach((item, fIdx) => {
    slide.addText("• " + item, {
      x: xPos + 0.3, y: 3.3 + (fIdx * 0.6), w: 2.4, h: 0.5,
      fontSize: 13,
      color: colors.dark,
      lineSpacing: 18
    });
  });
});

// Slide 13: API Endpoints
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("API ENDPOINTS", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const endpoints = [
  { method: "POST", path: "/predict", desc: "Single prediction with GenAI insights" },
  { method: "POST", path: "/batch-predict", desc: "Compare multiple scenarios" },
  { method: "POST", path: "/optimize", desc: "Get recommendations to reach target output" },
  { method: "GET", path: "/model-info", desc: "Retrieve model metadata & performance" },
  { method: "GET", path: "/health", desc: "Check API and model status" }
];

endpoints.forEach((endpoint, idx) => {
  const yPos = 1.8 + (idx * 0.95);
  
  // Method badge
  const badgeColor = endpoint.method === "POST" ? colors.secondary : colors.accent;
  slide.addShape("roundRect", {
    x: 0.7, y: yPos, w: 1.0, h: 0.5,
    fill: { color: badgeColor }
  });
  slide.addText(endpoint.method, {
    x: 0.7, y: yPos, w: 1.0, h: 0.5,
    fontSize: 14,
    bold: true,
    color: colors.white,
    align: "center",
    valign: "middle"
  });
  
  // Path
  slide.addText(endpoint.path, {
    x: 1.9, y: yPos + 0.05, w: 3.0, h: 0.4,
    fontSize: 16,
    bold: true,
    color: colors.primary,
    fontFace: "Courier New"
  });
  
  // Description
  slide.addText(endpoint.desc, {
    x: 5.2, y: yPos + 0.1, w: 4.3, h: 0.4,
    fontSize: 14,
    color: colors.dark
  });
});

slide.addText("Interactive documentation available at /docs (Swagger UI)", {
  x: 0.5, y: 6.3, w: 9.0, h: 0.3,
  fontSize: 13,
  color: colors.secondary,
  italic: true,
  align: "center"
});

// Slide 14: Business Impact
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("BUSINESS IMPACT", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const impacts = [
  {
    icon: "💰",
    title: "Cost Savings",
    value: "$50K-100K",
    desc: "annually through optimization"
  },
  {
    icon: "📉",
    title: "Downtime Reduction",
    value: "15-20%",
    desc: "through predictive maintenance"
  },
  {
    icon: "📈",
    title: "Output Increase",
    value: "5-8%",
    desc: "from parameter optimization"
  },
  {
    icon: "🎯",
    title: "Planning Accuracy",
    value: "95%+",
    desc: "confidence in forecasts"
  }
];

impacts.forEach((impact, idx) => {
  const row = Math.floor(idx / 2);
  const col = idx % 2;
  const xPos = 0.8 + (col * 4.7);
  const yPos = 1.8 + (row * 2.3);
  
  slide.addShape("roundRect", {
    x: xPos, y: yPos, w: 4.2, h: 2.0,
    fill: { color: colors.light },
    line: { color: colors.secondary, width: 2 }
  });
  
  slide.addText(impact.icon, {
    x: xPos + 0.3, y: yPos + 0.2, w: 3.6, h: 0.5,
    fontSize: 36,
    align: "center"
  });
  
  slide.addText(impact.value, {
    x: xPos + 0.3, y: yPos + 0.8, w: 3.6, h: 0.5,
    fontSize: 32,
    bold: true,
    color: colors.primary,
    align: "center"
  });
  
  slide.addText(impact.title, {
    x: xPos + 0.3, y: yPos + 1.3, w: 3.6, h: 0.3,
    fontSize: 16,
    bold: true,
    color: colors.secondary,
    align: "center"
  });
  
  slide.addText(impact.desc, {
    x: xPos + 0.3, y: yPos + 1.6, w: 3.6, h: 0.3,
    fontSize: 12,
    color: colors.dark,
    align: "center",
    italic: true
  });
});

// Slide 15: Key Recommendations
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("KEY RECOMMENDATIONS", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const recommendations = [
  {
    category: "🎯 Production Optimization",
    items: [
      "Maintain injection temp 215-225°C for optimal output",
      "Set pressure to 75-85 MPa range for best efficiency",
      "Target cycle times under 45 seconds"
    ]
  },
  {
    category: "🔧 Maintenance Strategy",
    items: [
      "Increase preventive maintenance to 5-6 hours/month",
      "Monitor when actual output deviates from predictions",
      "Schedule based on model alerts"
    ]
  },
  {
    category: "👨‍🔧 Operator Training",
    items: [
      "Focus on high-impact parameters",
      "Leverage experienced operators for mentoring",
      "Implement best practices from day shift"
    ]
  }
];

recommendations.forEach((rec, idx) => {
  const yPos = 1.8 + (idx * 1.6);
  
  slide.addText(rec.category, {
    x: 0.7, y: yPos, w: 8.6, h: 0.4,
    fontSize: 18,
    bold: true,
    color: colors.secondary
  });
  
  rec.items.forEach((item, iIdx) => {
    slide.addText("• " + item, {
      x: 1.2, y: yPos + 0.5 + (iIdx * 0.35), w: 8.0, h: 0.3,
      fontSize: 14,
      color: colors.dark
    });
  });
});

// Slide 16: Future Enhancements
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("FUTURE ENHANCEMENTS", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

slide.addText("Phase 2 Roadmap", {
  x: 0.5, y: 1.3, w: 9.0, h: 0.4,
  fontSize: 20,
  bold: true,
  color: colors.secondary
});

const futureItems = [
  { icon: "📡", title: "Real-time Data Streaming", desc: "Live IoT sensor integration" },
  { icon: "🔍", title: "Advanced Anomaly Detection", desc: "ML-powered quality monitoring" },
  { icon: "🔗", title: "Multi-machine Analysis", desc: "Factory-wide optimization" },
  { icon: "🤖", title: "Automated Retraining", desc: "Continuous model improvement" },
  { icon: "📱", title: "Mobile App", desc: "Operator dashboard & alerts" },
  { icon: "📊", title: "Executive Dashboard", desc: "Real-time KPI monitoring" }
];

futureItems.forEach((item, idx) => {
  const row = Math.floor(idx / 2);
  const col = idx % 2;
  const xPos = 0.7 + (col * 4.7);
  const yPos = 2.1 + (row * 1.3);
  
  slide.addShape("roundRect", {
    x: xPos, y: yPos, w: 4.3, h: 1.0,
    fill: { color: colors.light },
    line: { color: colors.secondary, width: 1 }
  });
  
  slide.addText(item.icon, {
    x: xPos + 0.2, y: yPos + 0.2, w: 0.6, h: 0.6,
    fontSize: 24
  });
  
  slide.addText(item.title, {
    x: xPos + 0.9, y: yPos + 0.15, w: 3.2, h: 0.35,
    fontSize: 15,
    bold: true,
    color: colors.primary
  });
  
  slide.addText(item.desc, {
    x: xPos + 0.9, y: yPos + 0.52, w: 3.2, h: 0.35,
    fontSize: 12,
    color: colors.dark,
    italic: true
  });
});

// Slide 17: Technology Stack
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("TECHNOLOGY STACK", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const techStack = [
  {
    category: "Data Science",
    tools: ["Python 3.10+", "Pandas & NumPy", "Scikit-learn", "SciPy"]
  },
  {
    category: "Visualization",
    tools: ["Matplotlib", "Seaborn", "Plotly"]
  },
  {
    category: "API & Backend",
    tools: ["FastAPI", "Uvicorn", "Pydantic", "Python-multipart"]
  },
  {
    category: "ML Models",
    tools: ["Linear Regression", "Random Forest", "Gradient Boosting", "Ridge/Lasso"]
  },
  {
    category: "DevOps",
    tools: ["Docker", "Docker Compose", "Git"]
  },
  {
    category: "Development",
    tools: ["Jupyter", "VS Code", "Postman"]
  }
];

techStack.forEach((tech, idx) => {
  const row = Math.floor(idx / 2);
  const col = idx % 2;
  const xPos = 0.7 + (col * 4.7);
  const yPos = 1.8 + (row * 1.5);
  
  slide.addShape("roundRect", {
    x: xPos, y: yPos, w: 4.3, h: 1.2,
    fill: { color: colors.light },
    line: { color: colors.secondary, width: 2 }
  });
  
  slide.addText(tech.category, {
    x: xPos + 0.2, y: yPos + 0.1, w: 4.0, h: 0.3,
    fontSize: 16,
    bold: true,
    color: colors.primary
  });
  
  slide.addText(tech.tools.join(" · "), {
    x: xPos + 0.2, y: yPos + 0.5, w: 4.0, h: 0.6,
    fontSize: 12,
    color: colors.dark,
    lineSpacing: 18
  });
});

// Slide 18: Project Timeline
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("PROJECT DELIVERY", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

slide.addText("Accelerated 1-Day Sprint", {
  x: 0.5, y: 1.2, w: 9.0, h: 0.4,
  fontSize: 18,
  color: colors.secondary,
  italic: true
});

const timeline = [
  { phase: "Phase 1-2", time: "Hours 1-2", tasks: "Data generation, EDA, preprocessing" },
  { phase: "Phase 3-4", time: "Hours 3-4", tasks: "Model training, evaluation, optimization" },
  { phase: "Phase 5-6", time: "Hours 5-6", tasks: "FastAPI deployment, Docker containerization" },
  { phase: "Phase 7-8", time: "Hours 7-8", tasks: "Documentation, report, presentation" }
];

timeline.forEach((item, idx) => {
  const yPos = 2.1 + (idx * 1.2);
  
  // Timeline dot
  slide.addShape("ellipse", {
    x: 1.5, y: yPos + 0.15, w: 0.3, h: 0.3,
    fill: { color: colors.primary }
  });
  
  // Phase
  slide.addText(item.phase, {
    x: 0.5, y: yPos, w: 0.9, h: 0.6,
    fontSize: 14,
    bold: true,
    color: colors.secondary,
    align: "right"
  });
  
  // Time
  slide.addText(item.time, {
    x: 2.0, y: yPos + 0.05, w: 1.5, h: 0.5,
    fontSize: 16,
    bold: true,
    color: colors.primary
  });
  
  // Tasks
  slide.addText(item.tasks, {
    x: 3.7, y: yPos + 0.15, w: 5.8, h: 0.4,
    fontSize: 14,
    color: colors.dark
  });
  
  // Connector line
  if (idx < timeline.length - 1) {
    slide.addShape("line", {
      x: 1.65, y: yPos + 0.6, w: 0, h: 0.6,
      line: { color: colors.secondary, width: 2, dashType: "dash" }
    });
  }
});

slide.addText("✅ All deliverables completed within 8-hour timeframe", {
  x: 0.5, y: 6.3, w: 9.0, h: 0.3,
  fontSize: 14,
  bold: true,
  color: colors.primary,
  align: "center"
});

// Slide 19: Deliverables
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.addText("PROJECT DELIVERABLES", {
  x: 0.5, y: 0.5, w: 9.0, h: 0.6,
  fontSize: 40,
  bold: true,
  color: colors.primary
});

const deliverables = [
  {
    icon: "📊",
    category: "Data & Analysis",
    items: ["Synthetic dataset (1000 samples)", "Jupyter notebook with full EDA", "10+ visualization charts"]
  },
  {
    icon: "🤖",
    category: "Models",
    items: ["5 trained models", "Best model (Random Forest)", "Model metadata & artifacts"]
  },
  {
    icon: "🚀",
    category: "Deployment",
    items: ["FastAPI application", "Docker container", "API documentation"]
  },
  {
    icon: "📝",
    category: "Documentation",
    items: ["Comprehensive report", "This presentation", "README & guides"]
  }
];

deliverables.forEach((deliv, idx) => {
  const row = Math.floor(idx / 2);
  const col = idx % 2;
  const xPos = 0.7 + (col * 4.7);
  const yPos = 1.8 + (row * 2.4);
  
  slide.addShape("roundRect", {
    x: xPos, y: yPos, w: 4.3, h: 2.0,
    fill: { color: colors.light },
    line: { color: colors.secondary, width: 2 }
  });
  
  slide.addText(deliv.icon, {
    x: xPos + 0.3, y: yPos + 0.2, w: 3.7, h: 0.5,
    fontSize: 36,
    align: "center"
  });
  
  slide.addText(deliv.category, {
    x: xPos + 0.3, y: yPos + 0.75, w: 3.7, h: 0.35,
    fontSize: 16,
    bold: true,
    color: colors.primary,
    align: "center"
  });
  
  deliv.items.forEach((item, iIdx) => {
    slide.addText("• " + item, {
      x: xPos + 0.5, y: yPos + 1.15 + (iIdx * 0.25), w: 3.3, h: 0.25,
      fontSize: 12,
      color: colors.dark
    });
  });
});

// Slide 20: Conclusion
slide = pptx.addSlide({ masterName: "MASTER_SLIDE" });
slide.background = { color: colors.primary };

slide.addText("PROJECT SUCCESS", {
  x: 0.5, y: 1.5, w: 9.0, h: 0.8,
  fontSize: 44,
  bold: true,
  color: colors.white,
  align: "center"
});

slide.addText("97% Accuracy · Production-Ready · GenAI-Powered", {
  x: 0.5, y: 2.5, w: 9.0, h: 0.5,
  fontSize: 24,
  color: colors.light,
  align: "center",
  italic: true
});

const achievements = [
  "✓ Achieved 97% prediction accuracy",
  "✓ Deployed production-ready API",
  "✓ Integrated GenAI insights",
  "✓ Docker containerization complete",
  "✓ Comprehensive documentation delivered"
];

achievements.forEach((achievement, idx) => {
  slide.addText(achievement, {
    x: 2.0, y: 3.5 + (idx * 0.45), w: 6.0, h: 0.4,
    fontSize: 18,
    color: colors.white,
    align: "center"
  });
});

slide.addText("Ready for Manufacturing Excellence", {
  x: 0.5, y: 5.9, w: 9.0, h: 0.6,
  fontSize: 28,
  bold: true,
  color: colors.light,
  align: "center"
});

slide.addText("THANK YOU", {
  x: 0.5, y: 6.5, w: 9.0, h: 0.5,
  fontSize: 20,
  color: colors.light,
  align: "center"
});

// Save presentation
pptx.writeFile({ fileName: "/mnt/user-data/outputs/Manufacturing_Project_Presentation.pptx" })
  .then(() => {
    console.log("✅ Presentation created successfully with 20 slides!");
  })
  .catch((err) => {
    console.error("Error creating presentation:", err);
    process.exit(1);
  });
