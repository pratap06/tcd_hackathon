import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "Ireland": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        "Waste": 0.1  # kgCO2/kg
    }
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Food Retail Carbon Calculator")

# Streamlit app code
st.title("Retail Store Carbon Calculator App 🛒")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select Country", ["Ireland"])  # Add more countries as needed

# User inputs for store names
stores = {
    "Ireland": ["Dublin Store 1", "Cork Store 2", "Galway Store 3"],  # Add stores for other countries if needed
}
store_name = st.selectbox("Select Store Name", stores[country])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚛 Monthly transportation distance (in km)")
    distance_monthly = st.slider("Distance", 0.0, 1000.0, key="distance_input")

    st.subheader("🗑️ Monthly waste generated (in kg)")
    waste_monthly = st.slider("Waste", 0.0, 1000.0, key="waste_input")

with col2:
    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity_monthly = st.slider("Electricity", 0.0, 10000.0, key="electricity_input")

    st.subheader("🍲 Monthly items sold")
    meals_monthly = st.slider("Items Sold", 0, 10000, key="meals_input")

# Normalize inputs
distance_yearly = distance_monthly * 12
electricity_yearly = electricity_monthly * 12
meals_yearly = meals_monthly * 12

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance_yearly
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity_yearly
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals_yearly
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste_monthly

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

# Calculate daily emissions
daily_transportation_emissions = round(transportation_emissions / 365, 4)
daily_electricity_emissions = round(electricity_emissions / 365, 4)
daily_diet_emissions = round(diet_emissions / 365, 4)
daily_waste_emissions = round(waste_emissions / 365, 4)
daily_total_emissions = round(total_emissions / 365, 4)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Your Carbon Emission Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions per Year")
        st.info(f"🚛 Delivery: {transportation_emissions} tonnes CO2")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2")
        st.info(f"🍽️ Meals: {diet_emissions} tonnes CO2")
        st.info(f"🍽️ Food Waste: {waste_emissions} tonnes CO2")
        st.success(f"🌍 Total Carbon Footprint: {total_emissions} tonnes CO2")

    with col4:
        st.subheader("Carbon Emissions per Day")
        st.info(f"🚛 Delivery: {daily_transportation_emissions} tonnes CO2")
        st.info(f"💡 Electricity: {daily_electricity_emissions} tonnes CO2")
        st.info(f"🍽️ Meals: {daily_diet_emissions} tonnes CO2")
        st.info(f"🍽️ Food Waste: {daily_waste_emissions} tonnes CO2")
        st.success(f"🌍 Total Carbon Footprint: {daily_total_emissions} tonnes CO2 per day")
