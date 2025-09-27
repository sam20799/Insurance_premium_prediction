import streamlit as st
from prediction_helper import predict

# --------- Configuration ---------
st.set_page_config(
    page_title="Health Insurance Cost Predictor",
    layout="wide",
    page_icon="🏥"
)

# Header
st.title("🏥 Health Insurance Cost Predictor")
st.markdown("### Get accurate premium estimates powered by advanced machine learning")
st.divider()

# App Information in Expandable Section
with st.expander("🧠 How This App Works", expanded=False):
    st.markdown("""
    This app predicts **insurance premium costs** based on your personal information using trained machine learning models.  
    To ensure higher accuracy across different age groups, we use **two specialized models**:
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        **🚀 Age > 25: XGBoost Regressor**
        - Accuracy: **99%**
        - Only **3%** predictions show extreme error
        """)

    with col2:
        st.info("""
        **📈 Age ≤ 25: Linear Regression**
        - Accuracy: **98%**
        - Only **2%** extreme error
        """)

    st.success("""
    **🧮 Features Considered:** Age, Income, Number of Dependents, Insurance Plan Type, 
    Risk Score, BMI Category, Smoking Status, Employment Status, Region, Gender, and Medical History
    """)

st.markdown("## 📋 Enter Your Information")

# Form inputs organized in tabs for better UX
tab1, tab2, tab3, tab4 = st.tabs(
    ["👤 Personal Info", "💰 Financial & Family", "🏥 Health & Risk", "📍 Insurance & Location"])

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

with tab1:
    st.markdown("#### Personal Details")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('🎂 Age', min_value=18, step=1, max_value=100, value=25)
    with col2:
        gender = st.selectbox('⚧ Gender', categorical_options['Gender'])
    with col3:
        marital_status = st.selectbox('💍 Marital Status', categorical_options['Marital Status'])

with tab2:
    st.markdown("#### Financial & Family Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        income_lakhs = st.number_input('💵 Annual Income (Lakhs)', step=1, min_value=0, max_value=200, value=5)
    with col2:
        number_of_dependants = st.number_input('👨‍👩‍👧‍👦 Number of Dependants', min_value=0, step=1, max_value=20,
                                               value=0)
    with col3:
        employment_status = st.selectbox('💼 Employment Status', categorical_options['Employment Status'])

with tab3:
    st.markdown("#### Health & Risk Assessment")
    col1, col2, col3 = st.columns(3)

    with col1:
        bmi_category = st.selectbox('⚖️ BMI Category', categorical_options['BMI Category'])
    with col2:
        smoking_status = st.selectbox('🚬 Smoking Status', categorical_options['Smoking Status'])
    with col3:
        genetical_risk = st.number_input('🧬 Genetical Risk Score (0-5)', step=1, min_value=0, max_value=5, value=0)

    st.markdown("#### Medical History")
    medical_history = st.selectbox('🏥 Select your medical condition', categorical_options['Medical History'])

with tab4:
    st.markdown("#### Insurance & Location Details")
    col1, col2 = st.columns(2)

    with col1:
        region = st.selectbox('📍 Region', categorical_options['Region'])
    with col2:
        insurance_plan = st.selectbox('🏛️ Insurance Plan Type', categorical_options['Insurance Plan'])

# Create input dictionary
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

st.divider()

# Prediction Section
st.markdown("## 🔮 Get Your Prediction")

# Display current selections in a nice format
with st.expander("📋 Review Your Information", expanded=False):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Personal Info:**")
        st.write(f"• Age: {age}")
        st.write(f"• Gender: {gender}")
        st.write(f"• Marital Status: {marital_status}")
        st.write(f"• Employment: {employment_status}")

    with col2:
        st.markdown("**Health & Risk:**")
        st.write(f"• BMI Category: {bmi_category}")
        st.write(f"• Smoking: {smoking_status}")
        st.write(f"• Genetical Risk: {genetical_risk}")
        st.write(f"• Medical History: {medical_history}")

    with col3:
        st.markdown("**Financial & Insurance:**")
        st.write(f"• Income: ₹{income_lakhs} Lakhs")
        st.write(f"• Dependants: {number_of_dependants}")
        st.write(f"• Insurance Plan: {insurance_plan}")
        st.write(f"• Region: {region}")

# Prediction Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('🎯 **Predict Insurance Cost**', type="primary", use_container_width=True):
        with st.spinner('🔄 Calculating your insurance cost...'):
            try:
                prediction = predict(input_dict)
                st.snow()
                st.success(f'### 🎉 Predicted Health Insurance Cost: ₹{prediction:,.2f}')

                # Additional insights
                if age > 25:
                    st.info("📊 Prediction made using **XGBoost Regressor** (99% accuracy)")
                else:
                    st.info("📊 Prediction made using **Linear Regression** (98% accuracy)")

            except Exception as e:
                st.error(f"❌ Error making prediction: {str(e)}")

st.divider()

# Feature Importance Section
st.markdown("## 🔍 Model Feature Importance")
st.markdown("Understanding what factors influence insurance costs the most:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🚀 Age > 25 Model (XGBoost)")
    try:
        st.image("feature_importance_over_25.jpeg", use_container_width=True)
    except:
        st.warning("📊 Feature importance chart for Age > 25 will be displayed here when available")

with col2:
    st.markdown("#### 📈 Age ≤ 25 Model (Linear Regression)")
    try:
        st.image("feature_importance_under_25.jpeg", use_container_width=True)
    except:
        st.warning("📊 Feature importance chart for Age ≤ 25 will be displayed here when available")

# Key Insights
st.markdown("### 💡 Key Insights")
insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.info("""
    **🚀 For Older Individuals (>25):**
    - Top drivers: Insurance plan, Age, and Risk Score.
    - Health risks: Obesity, Smoking, and Overweight BMI strongly increase predictions.
    - Moderate impact: Self-employment, Gender, Genetic risk, and Region.
    - Negative impact: More Dependents, Higher Income, and Unmarried status lower predictions.
    - Model is mainly driven by insurance, age, and health risk factors.
    """)

with insight_col2:

    st.info("""
    **📈 For Younger Individuals (≤25):**
    - Top drivers: Insurance plan, Genetic risk, and Risk score.
    - Health risks: Obesity, Regular smoking, and Overweight BMI increase predictions.
    - Moderate impact: Occasional smoking, Underweight BMI, Dependents, and Marital status.
    - Minimal effect: Gender, Region, Employment, Income, and Age.
    - Model is mainly driven by insurance type and genetic/health risk factors.
    """)
st.divider()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style='text-align: center'>
    <p>© SHUBHAM KR 2025 All rights reserved | Powered by Machine Learning & Streamlit</p>
    </div>
    """, unsafe_allow_html=True)