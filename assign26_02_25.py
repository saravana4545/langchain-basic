# Integrate AI Chatbot with MongoDB

# from fastapi import FastAPI
# from pydantic import BaseModel
# from pymongo import MongoClient
# from langchain.llms import Ollama

# app = FastAPI()

# client     = MongoClient("mongodb+srv://saravana45454:kumar123@saravana.kg1trkw.mongodb.net/")
# db         = client["chatbot_db"]
# collection = db["chat_history"]

# llm = Ollama(model="llama2")

# class ChatRequest(BaseModel):
#     message : str

# @app.post("/chat")
# async def chat(request: ChatRequest):
#     user_input = request.message

#     bot_reply = llm.invoke(user_input)

#     store_data = {"user_message": user_input, "bot_response": bot_reply}
#     collection.insert_one(store_data)

#     return {"reply": bot_reply}

# @app.get("/history")
# async def get_chat_history():
#     chats = list(collection.find({}, {"_id": 0}))
#     return {"history": chats}


# Using Flask Frame work

from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from langchain.llms import Ollama

app = Flask(__name__)

client = MongoClient("mongodb+srv://saravana45454:kumar123@saravana.kg1trkw.mongodb.net/")
db = client["chatbot_db"]
collection = db["chat_history"]

llm = Ollama(model="llama2")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["GET","POST"])
def chat():
    user_input = request.form.get("message")

    if not user_input:
        return "Message is required", 400

    bot_reply = llm.invoke(user_input)

    store_data = {"user_message": user_input, "bot_response": bot_reply}
    collection.insert_one(store_data)

    return render_template("index.html", user_message=user_input, bot_response=bot_reply)


# @app.route("/history", methods=["GET"])
# def get_chat_history():
#     chats = list(collection.find({}, {"_id": 0}))
#     return render_template('index.html',chats=chats)

if __name__ == "__main__":
    app.run(debug=True)