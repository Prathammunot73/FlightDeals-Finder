# ✈️ Flight Deals Finder

A Python application that searches for cheap flight deals using Google Flights (SerpAPI), compares them with stored prices, and sends SMS and WhatsApp notifications when a lower price is found.

## 🚀 Features

- Search flight prices using Google Flights (SerpAPI)
- Find direct and indirect flights
- Compare flight prices with stored lowest prices
- Send SMS notifications using Twilio
- Send WhatsApp notifications using Twilio WhatsApp Sandbox
- Store API keys securely using environment variables (`.env`)
- Cache API responses to reduce API requests

## 🛠️ Tech Stack

- Python
- SerpAPI
- Sheety API
- Twilio API
- Requests
- Python Dotenv

## 📂 Project Structure

```
FlightDeals-Finder/
│── main.py
│── data_manager.py
│── flight_search.py
│── flight_data.py
│── notification_manager.py
│── .gitignore
│── .env.example
```

## ⚙️ Installation

1. Clone the repository

```bash
git clone https://github.com/Prathammunot73/FlightDeals-Finder.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your credentials:

- SerpAPI Key
- Sheety API Token
- Twilio Account SID
- Twilio Auth Token
- Twilio Phone Number
- Twilio WhatsApp Sandbox Number

4. Run the project

```bash
python main.py
```

## 📱 Notifications

When a cheaper flight is found, the application sends:

- 📩 SMS Notification
- 💬 WhatsApp Notification

including:

- Destination
- Flight Price
- Departure Date
- Return Date

## 🔮 Future Improvements

- Email Notifications
- Web Dashboard
- Automatic Daily Flight Checks
- Support for Multiple Users
