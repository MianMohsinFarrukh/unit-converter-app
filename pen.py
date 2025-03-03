import streamlit as st

# Set the page title
st.set_page_config(
    page_title="Unit Converter App",
    page_icon="🔣",
    layout="wide"
)

# App content
st.title("🔣 Unit Converter App!")
st.markdown("### Convert Length, Weight, Time, Mass, Temperature & Energy Instantly.")
st.write("Welcome! Please select a category, enter a value & get the converted result in real time.")

# Function to convert units
def convert_units(category, value, unit):
    if category == "Length":
        conversions = {
            "Meters to Kilometers": value / 1000,
            "Kilometers to Meters": value * 1000,
            "Feet to Meters": value * 0.3048,
            "Meters to Feet": value / 0.3048
        }
    elif category == "Weight":
        conversions = {
            "Grams to Kilograms": value / 1000,
            "Kilograms to Grams": value * 1000,
            "Pounds to Kilograms": value * 0.453592,
            "Kilograms to Pounds": value / 0.453592
        }
    elif category == "Time":
        conversions = {
            "Seconds to Minutes": value / 60,
            "Minutes to Seconds": value * 60,
            "Hours to Minutes": value * 60,
            "Minutes to Hours": value / 60
        }
    elif category == "Mass":
        conversions = {
            "Milligrams to Grams": value / 1000,
            "Grams to Milligrams": value * 1000,
            "Grams to Kilograms": value / 1000,
            "Kilograms to Grams": value * 1000
        }
    elif category == "Temperature":
        conversions = {
            "Celsius to Fahrenheit": (value * 9/5) + 32,
            "Fahrenheit to Celsius": (value - 32) * 5/9,
            "Celsius to Kelvin": value + 273.15,
            "Kelvin to Celsius": value - 273.15
        }
    elif category == "Energy":
        conversions = {
            "Joules to Kilojoules": value / 1000,
            "Kilojoules to Joules": value * 1000,
            "Calories to Joules": value * 4.184,
            "Joules to Calories": value / 4.184
        }
    else:
        conversions = {}

    return conversions.get(unit, "Invalid conversion")

# UI components
category = st.selectbox("Select a category:", ["Length", "Weight", "Time", "Mass", "Temperature", "Energy"])
value = st.number_input("Enter the value to convert:", min_value=0.0, format="%.2f")
unit = st.selectbox(
    "Select a conversion:",
    {
        "Length": [
            "Meters to Kilometers",
            "Kilometers to Meters",
            "Feet to Meters",
            "Meters to Feet"
        ],
        "Weight": [
            "Grams to Kilograms",
            "Kilograms to Grams",
            "Pounds to Kilograms",
            "Kilograms to Pounds"
        ],
        "Time": [
            "Seconds to Minutes",
            "Minutes to Seconds",
            "Hours to Minutes",
            "Minutes to Hours"
        ],
        "Mass": [
            "Milligrams to Grams",
            "Grams to Milligrams",
            "Grams to Kilograms",
            "Kilograms to Grams"
        ],
        "Temperature": [
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius",
            "Celsius to Kelvin",
            "Kelvin to Celsius"
        ],
        "Energy": [
            "Joules to Kilojoules",
            "Kilojoules to Joules",
            "Calories to Joules",
            "Joules to Calories"
        ]
    }[category]
)

# Conversion and display
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The converted value is: {result}")
