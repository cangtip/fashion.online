import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ======================

# DATA HISTORIS

# ======================

X_train = np.array([
[5, 10],
[10, 20],
[15, 5],
[20, 25],
[25, 15]
])

y_train = np.array([
50,
80,
110,
90,
150
])

# ======================

# TRAINING MODEL

# ======================

model = LinearRegression().fit(
X_train,
y_train
)

# ======================

# BASELINE

# ======================

baseline_input = np.array([[10, 10]])

baseline_pred = model.predict(
baseline_input
)[0]

# ======================

# FUNGSI SIMULASI

# ======================

def run_simulation(new_iklan, new_diskon):


    intervention_input = np.array([
    [new_iklan, new_diskon]
])

    prediction = model.predict(
    intervention_input
)[0]

    delta_y = prediction - baseline_pred

    return prediction, delta_y

# ======================

# HEADER

# ======================

st.markdown("""

<div style="
background: linear-gradient(90deg, #87CEEB, #B0E0E6);
padding: 20px;
border-radius: 15px;
text-align: center;
margin-bottom: 20px;
">
<h1 style="color:white;">
🛍️ Smart Fashion Strategy Simulator
</h1>
<p style="color:white;font-size:18px;">
What-If Analysis untuk Strategi Promosi Fashion Online
</p>
</div>
""", unsafe_allow_html=True)

st.write(
"Ubah anggaran iklan dan diskon untuk melihat dampaknya terhadap keuntungan yang diprediksi."
)

# ======================

# SIDEBAR

# ======================

st.sidebar.header("📢 Strategi Promosi")

iklan_slider = st.sidebar.slider(
"Anggaran Iklan Digital (Juta)",
0,
50,
10
)

diskon_slider = st.sidebar.slider(
"Diskon Produk Fashion (%)",
0,
50,
10
)

# ======================

# ENGINE

# ======================

hasil_pred, delta = run_simulation(
iklan_slider,
diskon_slider
)

# ======================

# METRIC

# ======================

col1, col2 = st.columns(2)

col1.metric(
"Prediksi Keuntungan",
f"Rp {hasil_pred:.2f} Jt",
f"{delta:.2f} Jt"
)

if delta > 0:
    status = "Optimal"
elif delta < 0:
    status = "Kurang Optimal"
else:
    status = "Stabil"

col2.metric(
"Status Strategi",
status
)

# ======================

# GRAFIK

# ======================

st.subheader("📊 Perbandingan Skenario")

data_plot = pd.DataFrame({
"Skenario": ["Baseline", "Intervensi"],
"Keuntungan": [baseline_pred, hasil_pred]
})

st.bar_chart(
data=data_plot,
x="Skenario",
y="Keuntungan"
)

# ======================

# INSIGHT

# ======================

st.subheader("💡 Insight")

if delta > 0:
    st.success(
"Strategi promosi saat ini diprediksi memberikan hasil yang lebih baik dibandingkan kondisi awal."
)

elif delta < 0:
    st.warning(
"Strategi promosi saat ini belum mampu melampaui performa kondisi awal."
)

else:
    st.info(
"Belum terdapat perubahan dibandingkan kondisi baseline."
)

# ======================

# RINGKASAN

# ======================

st.subheader("📋 Ringkasan Simulasi")

st.write(f"""
• Anggaran Iklan Digital : {iklan_slider} Juta

• Diskon Produk Fashion : {diskon_slider}%

• Prediksi Keuntungan : Rp {hasil_pred:.2f} Juta

• Perubahan dari Baseline : {delta:.2f} Juta
""")
