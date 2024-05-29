from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

def load_model():
    # Load your model and tokenizer
    model_name = "distilbert-base-uncased-distilled-squad"  # Replace with your model name
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def get_answer_from_model(question, context, model, tokenizer):
    print("Question:", question)
    print("Context:", context)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    result = nlp(question=question, context=context)
    print("Result:", result)
    return result['answer']
