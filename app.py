import streamlit as st
import pandas as pd
import numpy as np
import joblib
import xgboost as xgb

# Page Config
st.set_page_config(page_title="Revenue Radar | KRA", page_icon="📉", layout="centered")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .big-font { font-size:24px !important; font-weight: bold; }
    .risk-high { color: #d9534f; font-weight: bold; }
    .risk-med { color: #f0ad4e; font-weight: bold; }
    .risk-low { color: #5cb85c; font-weight: bold; }
    div[data-testid="stMetricValue"] { font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.image("https://github.com/user-attachments/assets/093ba018-e048-479e-9959-274aeffcb24b", use_column_width=True)
st.title("📉 Revenue Radar: CIT Risk Engine")
st.markdown(" **Corporate Income Tax Compliance & Audit Intelligence System**")

# --- LOAD MODEL (Dynamic Version) ---
@st.cache_resource
def load_model():
    model_path = 'kra_cit_risk_model_v1.pkl'
    try:
        loaded = joblib.load(model_path)
        if isinstance(loaded, dict) and 'model' in loaded:
            return loaded['model']
        return loaded
    except:
        return None

model = load_model()

if model is None:
    st.error("⚠️ Model file 'kra_cit_risk_model_v1.pkl' not found.")
    st.stop()

# --- INPUT FORM ---
with st.form("risk_form"):
    st.subheader("📋 Firm Financial Profile")
    col1, col2 = st.columns(2)
    
    with col1:
        turnover = st.number_input("Gross Turnover (KES)", min_value=0.0, value=15000000.0, step=1000.0)
        cost_of_sales = st.number_input("Cost of Sales (KES)", min_value=0.0, value=12500000.0, step=1000.0)
    
    with col2:
        admin_expenses = st.number_input("Admin/Operating Expenses (KES)", min_value=0.0, value=3500000.0, step=1000.0)
        sector = st.selectbox("Industry Sector", ["Manufacturing", "Service", "Construction", "Agriculture", "Other"])

    submit = st.form_submit_button("🔍 Run Compliance Audit")

# --- ANALYSIS ENGINE ---
if submit:
    st.divider()
    
    # 1. Feature Engineering
    cost_ratio = cost_of_sales / turnover if turnover > 0 else 0
    admin_ratio = admin_expenses / turnover if turnover > 0 else 0
    profit_margin = (turnover - cost_of_sales - admin_expenses) / turnover if turnover > 0 else 0
    
    # 2. Prepare Data (Dynamic Bridge)
    input_data = {
        'num__grossturnover': turnover,
        'num__cost_of_sales': cost_of_sales,
        'num__total_administrative_exp': admin_expenses,
        'num__cost_to_turnover': cost_ratio,
        'num__admin_cost_ratio': admin_ratio,
        'cat__business_type_Company': 1,
        'cat__return_type_Original': 1
    }
    
    # Sector Mapping
    if sector == "Manufacturing": input_data['cat__sector_MANUFACTURING'] = 1
    elif sector == "Service": input_data['cat__sector_SERVICE ACTIVITIES'] = 1
    elif sector == "Construction": input_data['cat__sector_CONSTRUCTION'] = 1
    elif sector == "Agriculture": input_data['cat__sector_AGRICULTURE, FORESTRY AND FISHING'] = 1
    else: input_data['cat__sector_Other'] = 1

    # 3. Predict
    try:
        df_user = pd.DataFrame([input_data])
        
        # Auto-detect required columns
        req_cols = None
        if hasattr(model, "feature_names"): req_cols = model.feature_names
        elif hasattr(model, "feature_names_in_"): req_cols = model.feature_names_in_
        elif hasattr(model, "get_booster"): req_cols = model.get_booster().feature_names
            
        if req_cols is not None:
            df_final = df_user.reindex(columns=req_cols, fill_value=0)
        else:
            df_final = df_user

        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(df_final)[0][1]
        else:
            probability = model.predict(xgb.DMatrix(df_final))
            if isinstance(probability, np.ndarray): probability = probability[0]

        # --- DETAILED OUTPUT DASHBOARD ---
        
        # A. Score Header
        st.subheader("🛡️ Compliance Risk Assessment")
        
        col_score, col_gauge = st.columns([1, 2])
        
        with col_score:
            score_pct = probability * 100
            if probability > 0.65:
                st.markdown(f"<span class='big-font risk-high'>{score_pct:.1f}%</span>", unsafe_allow_html=True)
                st.markdown("**Status:** :red[High Risk]")
            elif probability > 0.35:
                st.markdown(f"<span class='big-font risk-med'>{score_pct:.1f}%</span>", unsafe_allow_html=True)
                st.markdown("**Status:** :orange[Medium Risk]")
            else:
                st.markdown(f"<span class='big-font risk-low'>{score_pct:.1f}%</span>", unsafe_allow_html=True)
                st.markdown("**Status:** :green[Low Risk]")

        with col_gauge:
            st.write("Risk Probability Gauge")
            st.progress(probability)
            if probability > 0.65:
                st.caption("This firm exhibits strong patterns associated with artificial loss reporting.")

        st.divider()

        # B. Financial Health Indicators
        st.subheader("📊 Financial Health Indicators")
        kpi1, kpi2, kpi3 = st.columns(3)
        
        kpi1.metric("Cost of Sales Ratio", f"{cost_ratio:.1%}", 
                    delta="High" if cost_ratio > 0.7 else "Normal", delta_color="inverse")
        
        kpi2.metric("Net Profit Margin", f"{profit_margin:.1%}", 
                    delta="Loss" if profit_margin < 0 else "Healthy", delta_color="normal")
        
        kpi3.metric("Admin Expense Ratio", f"{admin_ratio:.1%}", 
                    delta="High" if admin_ratio > 0.4 else "Normal", delta_color="inverse")

        # C. Audit Intelligence (Why is it high risk?)
        st.subheader("🚩 Audit Intelligence Reports")
        
        flags = []
        if cost_ratio > 0.75:
            flags.append(f"** inflated Cost Structure:** Cost of Sales is consuming {cost_ratio:.0%} of turnover, significantly reducing taxable income.")
        if profit_margin < 0:
            flags.append(f"**Perpetual Loss Position:** The firm is reporting a loss of {abs(profit_margin*turnover):,.0f} KES. Verify if this aligns with business expansion or artificial evasion.")
        if admin_ratio > 0.5:
            flags.append("**Excessive Admin Expenses:** Operating expenses are unusually high compared to revenue.")
        
        if not flags and probability > 0.5:
             flags.append("**Pattern Anomaly:** While individual ratios seem normal, the combination of features matches known non-compliant profiles (e.g., sector-specific anomalies).")
        
        if flags:
            for flag in flags:
                st.error(flag, icon="🚨")
        else:
            st.success("No major financial anomalies detected in the provided inputs.", icon="✅")

        # D. Recommended Actions
        if probability > 0.5:
            with st.expander("📂 Recommended Audit Steps", expanded=True):
                st.write("""
                1. **Request General Ledger:** Verify 'Other Direct Costs' and 'Admin Expenses' for non-allowable deductions.
                2. **Supplier Validation:** Check if major cost components correspond to ETR receipts or valid invoices.
                3. **Related Party Checks:** Investigate if high costs are payments to related entities (Transfer Pricing risk).
                """)

    except Exception as e:
        st.error(f"Analysis failed: {e}")