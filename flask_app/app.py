# import moduls
from flask import Flask, request, jsonify, render_template
from run_qa import load_model, get_answer_from_model
import json

app = Flask(__name__)

# Load the context data from the JSON file
with open('data/wordpress_content.json', 'r') as f:
    context_data = json.load(f)

# Combine all post content into a single context string
context = " ".join(post['content'] for post in context_data)

# Load the model and tokenizer globally
model, tokenizer = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_answer', methods=['POST'])
def get_answer():
    if request.method == 'POST':
        print(request.headers)  # Print headers to debug content type
        data = request.get_json()
        if data is None:
            return jsonify({'error': 'Invalid JSON'}), 400
        
        question = data.get('question')
        if not question:
            return jsonify({'error': 'No question provided'}), 400
        
        # Get the genuine answer from the model
        answer = get_answer_from_model(question, context, model, tokenizer)
        return jsonify({'answer': answer})
    else:
        return jsonify({'error': 'Invalid method'}), 405

if __name__ == '__main__':
    app.run(debug=True)
