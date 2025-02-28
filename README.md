AI Travel Assistant

📌 Overview

The AI Travel Assistant is a web-based application built using Streamlit and LangChain that helps users generate personalized travel plans. The app leverages the Google Gemini AI model to provide travel recommendations, including transport options, accommodations, attractions, and budget estimates.

🚀 Features

Generates AI-powered travel plans.

Provides travel options (flight/train/bus) with estimated costs.

Suggests recommended hotels and price ranges.

Lists must-visit attractions and activities.

Offers a structured and organized travel budget.

🛠️ Technologies Used

Python

Streamlit (for UI)

LangChain (for prompt handling)

Google Gemini AI (for AI-powered recommendations)

📦 Installation

1️⃣ Clone the Repository

git clone https://github.com/Thrived07/ai-travel-assistant.git
cd ai-travel-assistant

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Set Up Google API Key

Create a .env file and add your Google Gemini API Key:

GOOGLE_API_KEY=your_api_key_here

Or set it directly in the script:

os.environ["GOOGLE_API_KEY"] = "your_api_key_here"

4️⃣ Run the App

streamlit run app.py

📄 Project Structure

/ai-travel-assistant
│── app.py             # Main Streamlit application
│── requirements.txt   # Dependencies
│── README.md          # Project documentation

🌟 Usage

Enter the departure and destination locations.

Click on Generate Travel Plan.

View AI-generated travel suggestions and budget details.

🤝 Contributing

Feel free to fork this repository and contribute improvements!

📜 License

This project is licensed under the MIT License.
