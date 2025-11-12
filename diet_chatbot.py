import json

# Load the knowledge base
with open("diet_kb.json", "r") as f:
    knowledge_base = json.load(f)

foods = knowledge_base["foods"]

print("⚕️ Welcome to the Diet Chatbot!")
print("Type your health conditions (currently we have only diabetes, hypertension, heart related suggestions on board.)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("👉 You: ").strip().lower()

    if user_input in ["exit", "quit", "bye", "stop"]:
        print("Goodbye! Stay healthy 💙")
        break

    conditions = [c.strip() for c in user_input.replace(",", " ").split()]

    safe_list = []
    limit_list = []
    avoid_list = []

    for food in foods:
        # Safe foods
        if all(cond in food["safe_for"] for cond in conditions):
            safe_list.append(food)
        # Limit foods
        elif any(cond in food["limit_for"] for cond in conditions):
            limit_list.append(food)
        # Avoid foods
        elif any(cond in food["avoid_for"] for cond in conditions):
            avoid_list.append(food)

    if safe_list:
        print(f"\n✅ Foods safe for {', '.join(conditions)}:")
        for f in safe_list:
            print(f"- {f['name']} (Source: {f['source']})")

    if limit_list:
        print(f"\n⚠️ Foods to limit for {', '.join(conditions)}:")
        for f in limit_list:
            print(f"- {f['name']} (Source: {f['source']})")

    if avoid_list:
        print(f"\n❌ Foods to avoid for {', '.join(conditions)}:")
        for f in avoid_list:
            print(f"- {f['name']} (Source: {f['source']})")

    if not (safe_list or limit_list or avoid_list):
        print("\n⚠️ Sorry, I don’t have data for that condition yet.\n")

    print()
