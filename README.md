# 🥗 Diet WhatsApp Chatbot

A simple WhatsApp chatbot built using **Flask** and **Twilio** that provides **diet recommendations** for common health conditions like **diabetes**, **hypertension**, and **heart disease**.  

---

## 💡 Problem It Solves

Many people with chronic conditions struggle to find clear, accessible, and personalized dietary guidance.  
This chatbot:

- Simplifies nutrition recommendations for common conditions.  
- Provides quick food suggestions directly on WhatsApp, easy to access and widely used.  
- Helps users make informed food choices.  

---

## 🧰 Prerequisites

Before you begin, make sure you have:

- 🐍 **Python 3.8+**  
- 📱 A **Twilio account** (with WhatsApp sandbox setup)  
- 🔑 **Twilio credentials** (Account SID, Auth Token)  
- 📦 **pip** (Python package manager)

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/diet-whatsapp-chatbot.git
cd diet-whatsapp-chatbot
```

### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv venv
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install flask twilio
```

### 4. Configure Twilio Sandbox for WhatsApp
1. Go to Twilio Console → Messaging → Try it Out → WhatsApp Sandbox.
2. Follow the steps to join the sandbox (you’ll get a join code to send via WhatsApp).
3. Copy your Twilio Account SID and Auth Token.
4. Set up a webhook URL (you’ll get it in the next step).

---

## 🚀 How to Run
### 1. Start the Flask app
```bash
python app.py
```

By default, it runs at:
👉 http://127.0.0.1:5000

### 2. Expose your local server using ngrok
```bash
ngrok http 5000
```

Copy the https URL from the ngrok output (e.g., https://xxxx.ngrok.io).

### 3. Connect to Twilio
In Twilio Sandbox Settings, set the “WHEN A MESSAGE COMES IN” field to: https://xxxx.ngrok.io/whatsapp

---

## 💬 Usage Examples

### Example 1: Greeting
```bash
You:
Hi

Bot:

👋 Hello! I'm your Diet Chat Assistant.
Tell me your health conditions and I'll suggest foods that are safe, should be limited, or avoided.
💡 Example: diabetes, hypertension

### Example 2: Condition Input
You:
diabetes, heart

Bot:

🍽️ Diet Suggestions for Diabetes, Heart

✅ Safe Foods:
• Oats  
• Quinoa  
• Salmon  

⚠️ Foods to Limit:
• Carrots  

❌ Foods to Avoid:
• White Bread  

💬 Type another condition or 'exit' to end the chat.
```

---

## 👩‍💻 Contributing

I welcome contributions! Follow these steps:

### 🧾 Guidelines
1. Fork the repository
2. Create a new branch
```bash
git checkout -b feature/my-feature
```
4. Commit your changes
```bash git commit -m "Add new feature"
```
6. Push your branch
```bash
git push origin feature/my-feature
```
8. Open a Pull Request

---

## 📚 Libraries & Resources
1. Flask – Web framework
2. Twilio – WhatsApp API
3. ngrok – Localhost tunneling
4. American Heart Association (AHA) – Dietary references
5. American Diabetes Association (ADA) – Dietary sources
6. diet_kb.json – Nutritional knowledge base

---

## 📞 Contact
Author: Karen Morais
Email: karenfm.2310@gmail.com
GitHub: [@Codeshock123](https://github.com/Codeshock123)

---

## 🚧 Limitations & Future Plans

### Current Limitations
1. Supports only three conditions: diabetes, hypertension, and heart disease
2. Limited food database stored locally (diet_kb.json)
3. No machine learning or NLP-based understanding yet

### Future Enhancements
1. 🧠 Integrate with an AI model for better conversation handling
2. 📈 Expand food database and include more health conditions
3. 💬 Support for multiple languages
4. 🌍 Deploy on a public cloud with persistent storage

---

⭐ If you like this project, consider giving it a star on GitHub!
