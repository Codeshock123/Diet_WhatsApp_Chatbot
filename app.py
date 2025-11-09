from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json

# Load your knowledge base
with open("diet_kb.json", "r") as f:
    kb = json.load(f)

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.form.get("Body").lower().strip()
    resp = MessagingResponse()
    msg = resp.message()

    valid_conditions = ["diabetes", "hypertension", "heart"]

    # --- GREETING ---
    if incoming_msg in ["hi", "hello", "hey", "start"]:
        msg.body(
            "👋 Hello! I'm your *Diet Chat Assistant*.\n\n"
            "Tell me your health conditions and I'll suggest foods that are safe, "
            "should be limited, or avoided.\n\n"
            "💡 Example: `diabetes, hypertension`\n\n"
            "Type `help` to see more options or `exit` to end the chat."
        )
        return str(resp)

    # --- HELP ---
    if incoming_msg == "help":
        msg.body(
            "📘 *How to use:*\n"
            "• Type one or more conditions separated by commas.\n"
            "• Example: `diabetes`, `heart`, or `diabetes, hypertension`\n\n"
            "👉 Available conditions: diabetes, hypertension, heart\n"
            "Type `exit` to stop the chat."
        )
        return str(resp)

    # --- EXIT ---
    if incoming_msg in ["exit", "bye", "quit", "stop"]:
        msg.body("👋 Thank you for chatting! Stay healthy and take care 💚")
        return str(resp)

    # --- VALIDATION ---
    conditions = [c.strip() for c in incoming_msg.split(",")]
    if not all(c in valid_conditions for c in conditions):
        msg.body(
            "⚠️ I didn't recognize that condition.\n"
            "Try again using: diabetes, hypertension, or heart.\n\n"
            "Example: `diabetes, heart`"
        )
        return str(resp)

    # --- SEARCH KNOWLEDGE BASE ---
    safe_list = []
    limit_list = []
    avoid_list = []

    for food in kb["foods"]:
        if all(cond in food["safe_for"] for cond in conditions):
            safe_list.append(food["name"])
        elif any(cond in food["limit_for"] for cond in conditions):
            limit_list.append(food["name"])
        elif any(cond in food["avoid_for"] for cond in conditions):
            avoid_list.append(food["name"])

    # --- FORMAT RESPONSE ---
    reply = f"🍽️ *Diet Suggestions for {', '.join(conditions).title()}*\n\n"

    if safe_list:
        reply += "✅ *Safe Foods:*\n" + "\n".join([f"• {f}" for f in safe_list]) + "\n\n"
    if limit_list:
        reply += "⚠️ *Foods to Limit:*\n" + "\n".join([f"• {f}" for f in limit_list]) + "\n\n"
    if avoid_list:
        reply += "❌ *Foods to Avoid:*\n" + "\n".join([f"• {f}" for f in avoid_list]) + "\n\n"

    if not (safe_list or limit_list or avoid_list):
        reply = (
            f"⚠️ Sorry, I couldn’t find diet info for {', '.join(conditions)}.\n"
            "Please try with: diabetes, hypertension, or heart."
        )

    reply += "💬 Type another condition or `exit` to end the chat."

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
