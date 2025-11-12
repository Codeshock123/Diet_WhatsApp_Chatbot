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

    valid_conditions = ["diabetes", "hypertension", "heart", "sugar", "bp","heart issues", "heart issue"]

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
            "• Type a condition for which you would love to know which food is best.\n"
            "• Example: `diabetes`or `heart`, or `sugar, bp`\n\n"
            "👉 Available conditions: diabetes (sugar), hypertension (bp), heart (heart issues)\n"
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
        # Safe foods
        if all(any(cond in s for s in food["safe_for"]) for cond in conditions):
            safe_list.append(food["name"])

        # Foods to limit
        if any(any(cond in s for s in food["limit_for"]) for cond in conditions):
            limit_list.append(food["name"])

        # Foods to avoid
        if any(any(cond in s for s in food["avoid_for"]) for cond in conditions):
            avoid_list.append(food["name"])

        # --- FORMAT RESPONSE ---
    reply = f"🍽️ *Diet Suggestions for {', '.join(conditions).title()}*\n\n"

    # Create lists of foods and track their sources
    safe_sources = []
    limit_sources = []
    avoid_sources = []

    if safe_list:
        reply += "✅ *Safe Foods:*\n"
        for f in safe_list:
            reply += f"• {f}\n"
            # Find and collect source from KB
            for food in kb["foods"]:
                if food["name"] == f:
                    safe_sources.append(food["source"])
                    break
        reply += "\n"

    if limit_list:
        reply += "⚠️ *Foods to Limit:*\n"
        for f in limit_list:
            reply += f"• {f}\n"
            for food in kb["foods"]:
                if food["name"] == f:
                    limit_sources.append(food["source"])
                    break
        reply += "\n"

    if avoid_list:
        reply += "❌ *Foods to Avoid:*\n"
        for f in avoid_list:
            reply += f"• {f}\n"
            for food in kb["foods"]:
                if food["name"] == f:
                    avoid_sources.append(food["source"])
                    break
        reply += "\n"

    # If nothing matched
    if not (safe_list or limit_list or avoid_list):
        reply = (
            f"⚠️ Sorry, I couldn’t find diet info for {', '.join(conditions)}.\n"
            "Please try with: diabetes, hypertension, or heart."
        )
    else:
        # Add unique list of sources at the end
        all_sources = set(safe_sources + limit_sources + avoid_sources)
        if all_sources:
            reply += "📚 *Information Sources:*\n" + "\n".join([f"• {src}" for src in all_sources]) + "\n\n"

    reply += "💬 Type another condition or `exit` to end the chat."

    msg.body(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)
