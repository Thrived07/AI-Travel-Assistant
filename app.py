import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langchain.schema.runnable import RunnablePassthrough

# ✅ Set Up API Key
os.environ["GOOGLE_API_KEY"] = "Your-API-KEY"

# ✅ Initialize LangChain Model
llm = GoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=os.environ["GOOGLE_API_KEY"])

# ✅ Define Prompt Template
travel_prompt = PromptTemplate(
    input_variables=["from_location", "to_location"],
    template="""
    You are an AI-powered travel assistant. Plan a journey from {from_location} to {to_location}.
    Provide details about:
    - Available travel options (flight/train/bus) with estimated costs
    - Recommended hotels and price ranges
    - Top attractions and activities
    - Overall budget estimation

    Present the response in a clear and organized format.
    """
)

# ✅ Create LangChain Travel Chain Using RunnableSequence
travel_chain = travel_prompt | llm | RunnablePassthrough()

# ✅ Streamlit UI Setup
st.set_page_config(page_title="AI Travel Assistant", layout="wide")
st.markdown("<h1 style='text-align: center; color: #0078D7;'>🌍 AI Travel Assistant</h1>", unsafe_allow_html=True)

# ✅ Input Fields
col1, col2 = st.columns(2)
with col1:
    from_location = st.text_input("🏠 Departure Location:", placeholder="Enter your starting location")
with col2:
    to_location = st.text_input("📍 Destination:", placeholder="Enter your destination")

# ✅ Predict Button
if st.button("🚀 Generate Travel Plan"):
    if from_location and to_location:
        result = travel_chain.invoke({"from_location": from_location, "to_location": to_location})
        st.success("✅ Your Travel Plan:")
        st.write(result)
    else:
        st.warning("⚠ Please enter both departure and destination locations!")
