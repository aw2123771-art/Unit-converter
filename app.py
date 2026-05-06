import streamlit as st

st.title("⚙️ Engineering Unit Converter App")

st.write("Convert common engineering units easily.")

# Conversion type
option = st.selectbox(
    "Choose conversion type",
    ["Length (m ↔ cm ↔ km)", "Temperature (C ↔ F)", "Pressure (Pa ↔ kPa)"]
)

# LENGTH
if option == "Length (m ↔ cm ↔ km)":
    value = st.number_input("Enter value in meters (m):", min_value=0.0)

    if st.button("Convert Length"):
        cm = value * 100
        km = value / 1000

        st.success(f"{value} m = {cm} cm")
        st.success(f"{value} m = {km} km")

# TEMPERATURE
elif option == "Temperature (C ↔ F)":
    c = st.number_input("Enter temperature in Celsius:")

    if st.button("Convert Temperature"):
        f = (c * 9/5) + 32
        st.success(f"{c} °C = {f} °F")

# PRESSURE
elif option == "Pressure (Pa ↔ kPa)":
    pa = st.number_input("Enter pressure in Pascal (Pa):")

    if st.button("Convert Pressure"):
        kpa = pa / 1000
        st.success(f"{pa} Pa = {kpa} kPa")
