import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

@st.cache_resource
def load_data():
    data = pd.read_csv('hour.csv')

    return data

data = load_data()

st.title("Bike Share Dashboard :bike:")

fig_hist = px.histogram(
    data, x="cnt", y="cnt", title="Distribution of Bike Share Count per Season", color = "season")
st.plotly_chart(fig_hist, use_container_width=True,
                height=400, width=600)

monthly_count = data.groupby("mnth")["cnt"].sum().reset_index()
fig_monthly_count = px.line(
    monthly_count, x="mnth", y="cnt", title="monthly Bike Share Count")
st.plotly_chart(fig_monthly_count, use_container_width=True,
                height=400, width=600)


col1, col2 = st.columns(2)

with col1:
    fig_hum = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
    st.plotly_chart(fig_hum,
    use_container_width=True, height=400, width=600)

with col2:
    fig_wind = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
    st.plotly_chart(fig_wind,use_container_width=True,height=400, width=800)


fig_temp = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp, use_container_width=True,
                height=400, width=800)


avg_rentals_by_season = data.groupby('season')['cnt'].mean().reset_index()
fig_avg = px.bar(
    avg_rentals_by_season, x="season", y="cnt", title="Season Bike Share Count")
st.plotly_chart(fig_avg, use_container_width=True,
                height=400, width=600)



hourly_rentals = data.groupby('hr')['cnt'].sum().reset_index()
fig_hourly = px.bar(
    hourly_rentals, x="hr", y="cnt", title="Hourly Bike Share Count", color_discrete_sequence=['skyblue'] * len(hourly_rentals))
st.plotly_chart(fig_hourly, use_container_width=True,
                height=400, width=600)


st.sidebar.title("Information:")
st.sidebar.markdown("**• Nama: Ilham Nurrahman**")
st.sidebar.markdown(
    "**• Email: ilhamnurahman34@gmail.com**")
st.sidebar.markdown(
    "**• Dicoding: mysterieuxman**")


st.sidebar.title("About")
st.sidebar.info("Dashboard ini menampilkan representasi visual dari kumpulan data mengenai layanan Bike Share. Informasi dalam dataset ini mencakup detail tentang penyewaan sepeda, yang dipengaruhi oleh beberapa faktor seperti musim, suhu, kelembaban, dan variabel lainnya.")
