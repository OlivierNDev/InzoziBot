from flask import Flask, request, jsonify
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

# File to store dreams
DREAMS_FILE = "dreams.json"

def load_dreams():
    """Load dreams from file."""
    try:
        with open(DREAMS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_dreams(dreams):
    """Save dreams to file."""
    with open(DREAMS_FILE, "w") as file:
        json.dump(dreams, file, indent=4)

@app.route("/api/dreams", methods=["GET"])
def get_dreams():
    """Get all dreams."""
    dreams = load_dreams()
    return jsonify(dreams)

@app.route("/api/dreams", methods=["POST"])
def add_dream():
    """Add a new dream."""
    data = request.json
    if "dream" not in data or not data["dream"]:
        return jsonify({"error": "Dream content is required"}), 400

    new_dream = {
        "id": len(load_dreams()) + 1,
        "dream": data["dream"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    dreams = load_dreams()
    dreams.append(new_dream)
    save_dreams(dreams)

    return jsonify(new_dream), 201


@app.route("/api/analyze", methods=["POST"])
def analyze_dream():
    """Analyze a dream with an expanded list of keywords and interpretations."""
    data = request.json
    if "dream" not in data or not data["dream"]:
        return jsonify({"error": "Dream content is required"}), 400

    dream = data['dream'].lower()

    # Expanded dream analysis based on keywords
    if "fly" in dream or "flying" in dream:
        analysis = "Flying in a dream often represents freedom, ambition, or the desire to escape."
    elif "lost" in dream or "wallet" in dream:
        analysis = "Losing something in a dream may symbolize feelings of insecurity or fear of loss."
    elif "water" in dream or "ocean" in dream:
        analysis = "Water symbolizes emotions. A calm ocean suggests emotional peace, while a stormy sea indicates turmoil."
    elif "school" in dream:
        analysis = "Dreams about school might reflect self-esteem issues, challenges, or feelings of being unprepared."
    elif "dark" in dream or "night" in dream:
        analysis = "A dark dream often represents fear, uncertainty, or a sense of being lost in your waking life."
    elif "treasure" in dream:
        analysis = "Finding treasure in a dream often symbolizes self-discovery, potential, or newfound wealth in your life."
    elif "death" in dream:
        analysis = "Dreams about death may reflect the end of a phase or transformation in your life. It can also indicate fear of change or the unknown."
    elif "snake" in dream:
        analysis = "Snakes in dreams often represent hidden fears, threats, or transformations. They can also symbolize healing or renewal."
    elif "baby" in dream:
        analysis = "Dreaming of a baby might represent new beginnings, innocence, or the potential for growth and development."
    elif "chase" in dream or "running" in dream:
        analysis = "Chasing or being chased in a dream may signify avoidance of certain situations or feelings of anxiety or fear."
    elif "fall" in dream or "falling" in dream:
        analysis = "Falling in a dream often represents a loss of control or insecurity in your waking life."
    elif "fire" in dream:
        analysis = "Fire in a dream can represent passion, destruction, or purification. It might also symbolize anger or intense emotions."
    elif "house" in dream:
        analysis = "A house in a dream often reflects the self or the mind. Different rooms might symbolize different aspects of your life."
    elif "cat" in dream:
        analysis = "Cats in dreams can symbolize independence, intuition, and curiosity. They may also represent feminine energy or mystery."
    elif "car" in dream:
        analysis = "Dreaming of a car might reflect your current life direction or the speed at which you are progressing in life."
    elif "teeth" in dream:
        analysis = "Teeth in a dream may signify self-image, communication issues, or feelings of powerlessness. Losing teeth often symbolizes fear of aging or loss of control."
    elif "money" in dream:
        analysis = "Dreaming about money can symbolize your self-worth, material desires, or concerns about financial security."
    elif "love" in dream:
        analysis = "Dreams about love can reflect your desires for connection, affection, or fear of rejection."
    elif "birds" in dream:
        analysis = "Birds in a dream may represent freedom, spirituality, or a desire to rise above challenges."
    elif "mountain" in dream:
        analysis = "Mountains in dreams often symbolize obstacles, challenges, or the pursuit of a goal. Climbing a mountain represents personal growth and perseverance."
    elif "storm" in dream:
        analysis = "A storm in a dream can represent emotional turmoil, conflict, or a significant challenge you're currently facing."
    elif "zombie" in dream:
        analysis = "Dreaming about zombies often indicates feelings of stagnation, being stuck, or lacking direction in life."
    else:
        analysis = f"The dream '{data['dream']}' shows creativity and potential for new ideas. Keep dreaming :)"

    response = {
        "analysis": analysis
    }
    return jsonify(response)







    response = {
        "analysis": analysis
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
