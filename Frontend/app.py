

import streamlit as st
import requests

st.title("House Price Prediction")

st.write("Enter the house details below")

income = st.number_input("Income", min_value=0.0)
age = st.number_input("House Age", min_value=0.0)
rooms = st.number_input("Total Rooms", min_value=0.0)
bedrooms = st.number_input("Total Bedrooms", min_value=1)
population = st.number_input("Population", min_value=0)

if st.button("Predict House Price"):

    data = {
        "income": income,
        "age": age,
        "rooms": rooms,
        "bedrooms": bedrooms,
        "population": population
    }

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json=data
        )

        if response.status_code == 200:
            result = response.json()

            st.success(
                f"Predicted House Price: {result['predicted_price']:.2f}"
            )

        else:
            st.error(response.json().get("error", "Prediction failed"))

    except requests.exceptions.ConnectionError:
        st.error("Flask backend is not running. Please start the backend.")

    except Exception as e:
        st.error(f"Error: {e}")
