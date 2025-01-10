# Importing libraries
import google.generativeai as genai
import streamlit as st
import pandas as pd

# Gemini and Streamlit Configuration
genai.configure(api_key=st.secrets["api_key"])
st.set_page_config(page_icon="💪", page_title="AI Fitness Coach", layout='centered')

generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Caching Data to Avoid Re-reading Files
@st.cache_data
def get_countries_name():
    countries = pd.read_csv("countries.csv")
    return countries.name

country_list = get_countries_name()
build_options = ["Thin", "Average", "Broad or Muscular", "Significantly Overweight"]
flexibility_options = ["Very flexible", "Pretty flexible", "Not that good", "I'm not sure"]
diet_preferences = ["Vegan", "Vegetarian", "Jain", "Swaminarayan", "Non-Vegetarian"]
water_intake_options = ["Less than 2 glasses", "About 2 glasses", "2 to 6 glasses", "More than 5 glasses"]
sleep_duration_options = ["Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours"]
preferred_workout_duration = ["10-15 minutes", "15-25 minutes", "25+ minutes", "Don't know"]
workout_frequency_options = ["Almost every day", "Several times per week", "Several times per month", "Never"]
work_schedule_options = ["9 to 5", "Night shifts", "My hours are flexible", "Not working/retired"]
daily_activity_choices = ["I spend most of the day sitting", "I take active breaks", "I'm on my feet all day long"]
body_sensitivity_choices = ["Sensitive back", "Sensitive knees", "None"]
dream_goal_options = ["Build muscle & strength", "Lose weight", "Improve mobility", "Develop flexibility", "Improve overall fitness"]

# Header Section
st.header("🤖 AI Fitness Coach")
st.write(
    "<h4>Let's get started! Fill out the information below to help me design the perfect fitness plan tailored to you.<h4>", 
    unsafe_allow_html=True
)

# User Information Form
with st.container():
    st.subheader("📝 Personal Information")
    age_input = st.number_input("What is your age?", value=18, min_value=16)
    selected_country = st.selectbox("Select Your Country (to provide recommendations):", country_list)
    col1, col2 = st.columns(2)
    with col1:
        height_cm = st.number_input("What is your height (in centimeters)?", value=168, min_value=100)
    with col2:
        weight_kg = st.number_input("What is your weight (in kilograms)?", value=60, min_value=20)
    calculated_bmi = round(weight_kg / ((height_cm / 100) ** 2))

# Card-Like Layout for Preferences
with st.container():
    st.subheader("🏋️‍♂️ Fitness Preferences")
    st.markdown("### Build and Flexibility")
    col1, col2 = st.columns(2)
    with col1:
        selected_build = st.selectbox("Describe your physical build:", build_options)
    with col2:
        selected_flexibility = st.selectbox("How flexible are you?", flexibility_options)

    st.markdown("### Lifestyle and Habits")
    col1, col2 = st.columns(2)
    with col1:
        selected_diet = st.selectbox("Preferred Diet:", diet_preferences)
        selected_water_intake = st.selectbox("Daily Water Intake:", water_intake_options)
    with col2:
        selected_sleep_duration = st.selectbox("Usual Sleep Duration:", sleep_duration_options)
        selected_work_schedule = st.selectbox("Work Schedule:", work_schedule_options)

# Interactive Multi-Select for Activity and Sensitivity
with st.container():
    st.subheader("🏃‍♀️ Activity and Goals")
    selected_workout_time = st.selectbox("Workout Duration:", preferred_workout_duration)
    selected_workout_frequency = st.selectbox("Workout Frequency:", workout_frequency_options)
    selected_daily_activity = st.selectbox("Daily Activity Level:", daily_activity_choices)
    selected_body_sensitivity = st.multiselect("Body Sensitivity Issues:", body_sensitivity_choices, default=["None"])

    # Handle "None" selection
    if "None" in selected_body_sensitivity and len(selected_body_sensitivity) > 1:
        selected_body_sensitivity = ["None"]

    bad_habits_input = st.text_area("Any bad habits? Write them here:", placeholder="For example: Smoking, Watching TV while eating")
    selected_fitness_goal = st.selectbox("Main Fitness Goal:", dream_goal_options)

# Generate Fitness Plan Button
prompt = f"""
You are Jake, an expert fitness coach. Design a personalized fitness and diet plan based on the following user details:
- Age: {age_input}
- Country: {selected_country}
- Height: {height_cm / 100}m
- Weight: {weight_kg}kg
- BMI: {calculated_bmi}
- Build: {selected_build}
- Flexibility: {selected_flexibility}
- Diet Preference: {selected_diet}
- Water Intake: {selected_water_intake}
- Sleep: {selected_sleep_duration}
- Workout Time: {selected_workout_time}
- Frequency: {selected_workout_frequency}
- Activity Level: {selected_daily_activity}
- Sensitivities: {", ".join(selected_body_sensitivity)}
- Bad Habits: {bad_habits_input}
- Goal: {selected_fitness_goal}

Provide separate markdown tables for **Diet Plan**, **Exercise Plan**, and general **Recommendations**.
"""

if st.button("Submit"):
    if not selected_body_sensitivity or selected_body_sensitivity == ["None"]:
        st.error("Please select at least one sensitivity or confirm 'None' before submitting.")
    else:
        response = model.generate_content(prompt)
        st.markdown(response.text)

