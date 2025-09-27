# 🏥 Health Insurance Cost Predictor

A machine learning-powered web application that predicts health insurance premium costs based on personal and demographic information. Built with Streamlit and powered by advanced ML models for accurate cost estimation.

## 🚀 Features

- **Dual Model Architecture**: Uses specialized models for different age groups
  - **Age ≤ 25**: Linear Regression (98% accuracy)
  - **Age > 25**: XGBoost Regressor (99% accuracy)
- **Interactive Web Interface**: User-friendly Streamlit dashboard
- **Comprehensive Risk Assessment**: Considers 12+ factors including health, demographics, and lifestyle
- **Real-time Predictions**: Instant cost estimates with detailed insights
- **Feature Importance Visualization**: Understand what drives your insurance costs

## 🎯 Model Performance

- **Overall Accuracy**: 98-99% across both models
- **Low Error Rate**: Only 2-3% predictions show extreme error
- **Specialized Training**: Age-specific models for optimal accuracy

## 📋 Input Features

The predictor considers the following factors:

### Personal Information
- Age (18-100)
- Gender (Male/Female)
- Marital Status (Married/Unmarried)
- Number of Dependents (0-20)

### Financial & Employment
- Annual Income (in Lakhs)
- Employment Status (Salaried/Self-Employed/Freelancer)

### Health & Risk Factors
- BMI Category (Normal/Overweight/Obesity/Underweight)
- Smoking Status (No Smoking/Occasional/Regular)
- Genetic Risk Score (0-5)
- Medical History (9 different conditions including diabetes, heart disease, etc.)

### Insurance & Location
- Insurance Plan Type (Bronze/Silver/Gold)
- Region (Northwest/Northeast/Southeast/Southwest)

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/sam20799/health-insurance-predictor.git
cd health-insurance-predictor
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Required Files Structure
Ensure you have the following model artifacts in the `artifacts/` directory:
```
artifacts/
├── model_young.joblib      # Linear Regression model for age ≤ 25
├── model_rest.joblib       # XGBoost model for age > 25
├── scaler_young.joblib     # Scaler for young age group
└── scaler_rest.joblib      # Scaler for older age group
```

### Feature Importance Images (Optional)
Place these images in the root directory for visualization:
- `feature_importance_over_25.jpeg`
- `feature_importance_under_25.jpeg`

## 🚀 Running the Application

### Local Development
```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

### Production Deployment

#### Deploy to Streamlit Cloud
1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy with one click

#### Deploy to Heroku
1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run main.py
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
```

## 📊 How It Works

### 1. Data Preprocessing
- Categorical variables are one-hot encoded
- Numerical features are scaled using saved scalers
- Medical history is converted to normalized risk scores

### 2. Model Selection
- **Age ≤ 25**: Linear Regression optimized for younger demographics
- **Age > 25**: XGBoost Regressor for complex non-linear patterns

### 3. Risk Score Calculation
Medical conditions are weighted by severity:
- Heart Disease: 8 points
- Diabetes: 6 points  
- High Blood Pressure: 6 points
- Thyroid: 5 points
- Combined conditions are additive

### 4. Prediction Output
- Cost estimate in Indian Rupees (₹)
- Model accuracy information
- Feature importance insights

## 🔧 Technical Details

### Dependencies
- **streamlit**: Web application framework
- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning algorithms
- **xgboost**: Gradient boosting framework
- **joblib**: Model serialization
- **numpy**: Numerical computing

### Model Architecture
- **Linear Regression**: For younger users (≤25 years)
  - Features: Insurance plan, genetic risk, risk score
  - Accuracy: 98%
- **XGBoost Regressor**: For older users (>25 years)  
  - Features: Insurance plan, age, risk score, BMI, smoking
  - Accuracy: 99%

## 📈 Key Insights

### For Younger Individuals (≤25):
- **Primary Drivers**: Insurance plan type, genetic risk, health risk score
- **Health Impact**: Obesity and smoking significantly increase costs
- **Minimal Effect**: Age, income, and regional differences

### For Older Individuals (>25):
- **Primary Drivers**: Insurance plan, age, comprehensive risk assessment
- **Major Factors**: BMI category, smoking status, employment type
- **Cost Reducers**: Higher income, more dependents, unmarried status

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**SHUBHAM KR**  
*Machine Learning & Data Science Enthusiast*

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Machine learning models trained using [scikit-learn](https://scikit-learn.org/) and [XGBoost](https://xgboost.readthedocs.io/)
- UI icons from various emoji sets

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/health-insurance-predictor/issues) section
2. Create a new issue with detailed description
3. Contact the maintainer

---

**⭐ Star this repository if you find it helpful!**