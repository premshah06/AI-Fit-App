# **Fit-AI-Coach**

## **Introduction**
Fit-AI-Coach is a cutting-edge web application designed to deliver **personalized fitness and diet plans** using Google's Gemini Pro Model. With its user-friendly interface and intelligent recommendations, Fit-AI-Coach is perfect for anyone aiming to achieve specific fitness goals, enhance their health, or maintain a healthy lifestyle.

---

## **Features**
- **Personalized Plans**: Tailored recommendations based on user inputs like age, BMI, daily activity, and fitness goals.
- **AI-Powered Insights**: Uses Google's Gemini Pro Model to dynamically generate fitness and diet recommendations.
- **Localized Suggestions**: Recommends diets and exercises based on the availability in the user's country.
- **User-Friendly Design**: Interactive forms, intuitive layout, and instant feedback.
- **Security Measures**: Built-in safety configurations to ensure reliable AI-generated responses.

---

## **Technologies Used**
- **Languages**: Python
- **Libraries**:
  - **Streamlit**: For creating the web-based interactive user interface.
  - **Pandas**: For managing and processing user input data.
  - **Google Generative AI (Gemini)**: For generating personalized recommendations.
- **APIs**:
  - Integrated Google MakerSuite API for AI-powered content generation.

---

## **Setup**
Follow these steps to set up and run Fit-AI-Coach on your local machine:

### **1. Clone the Repository**
Fork and clone this repository to your machine:
```bash
git clone https://github.com/username/Fit-AI-Coach.git
cd Fit-AI-Coach
```

### **2. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **3. Get API Key**
- Obtain a Gemini API key from [Google MakerSuite](https://makersuite.google.com/app/apikey).
- Add the API key to the Streamlit secrets file:
  1. Create a `.streamlit/secrets.toml` file:
     ```toml
     [api_key]
     key = "your_gemini_api_key"
     ```

### **4. Run the Application**
Start the Streamlit app:
```bash
streamlit run app.py
```
