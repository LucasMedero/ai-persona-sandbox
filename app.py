# app.py
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

# In-memory storage (disappears on server restart)
personas = []  # List of dicts: {"id": int, "name": str, "description": str}
conversations = {}  # {conv_id: {"personas": [persona_dicts], "messages": [{"name": str, "content": str}, ...]}}
next_conv_id = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/personas")
def get_personas():
    return jsonify(personas)

@app.route("/create_persona", methods=["POST"])
def create_persona():
    data = request.json
    persona = {
        "id": len(personas),
        "name": data["name"],
        "description": data["description"]
    }
    personas.append(persona)
    return jsonify(persona)

@app.route("/start_conversation", methods=["POST"])
def start_conversation():
    global next_conv_id
    data = request.json
    persona_ids = data["persona_ids"]
    selected_personas = [personas[i] for i in persona_ids]
    
    conv = {
        "personas": selected_personas,
        "messages": []
    }
    conv_id = next_conv_id
    conversations[conv_id] = conv
    next_conv_id += 1
    return jsonify({"conv_id": conv_id})

@app.route("/conversation/<int:conv_id>")
def conversation_page(conv_id):
    if conv_id not in conversations:
        return "Conversation not found", 404
    return render_template("conversation.html", conv_id=conv_id)

@app.route("/get_conversation/<int:conv_id>")
def get_conversation(conv_id):
    if conv_id not in conversations:
        return jsonify({"error": "Conversation not found"}), 404
    conv = conversations[conv_id]
    return jsonify({
        "personas": conv["personas"],
        "messages": conv["messages"]
    })

@app.route("/next_message", methods=["POST"])
def next_message():
    data = request.json
    conv_id = data["conv_id"]
    speaker_index = data.get("speaker_index", 0)
    
    conv = conversations[conv_id]
    selected_personas = conv["personas"]
    speaker = selected_personas[speaker_index % len(selected_personas)]
    
    # Build history: all previous messages formatted as "user" (with speaker name)
    history = []
    for msg in conv["messages"]:
        history.append({
            "role": "user",
            "parts": [{"text": f"{msg['name']}: {msg['content']}"}]
        })
    
    # Loose safety settings to avoid blocking during debates/simulations
    safety_settings = [
        {"category": HarmCategory.HARM_CATEGORY_HARASSMENT, "threshold": HarmBlockThreshold.BLOCK_ONLY_HIGH},
        {"category": HarmCategory.HARM_CATEGORY_HATE_SPEECH, "threshold": HarmBlockThreshold.BLOCK_ONLY_HIGH},
        {"category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, "threshold": HarmBlockThreshold.BLOCK_ONLY_HIGH},
        {"category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, "threshold": HarmBlockThreshold.BLOCK_ONLY_HIGH},
    ]
    
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash-lite",
        system_instruction=speaker["description"],
        generation_config={"temperature": 0.9},
        safety_settings=safety_settings
    )
    
    chat = model.start_chat(history=history)
    
    if len(conv["messages"]) == 0:
        user_prompt = "Start the conversation naturally."
    else:
        user_prompt = "Your turn. Respond in character."
    
    response = chat.send_message(user_prompt)
    
    new_msg = {
        "name": speaker["name"],
        "content": response.text
    }
    conv["messages"].append(new_msg)
    
    return jsonify(new_msg)

if __name__ == "__main__":
    app.run(debug=True)