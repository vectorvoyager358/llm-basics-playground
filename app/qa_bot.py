from app.llm import generate_response

def ask_question(question):
    prompt = f"""
    Answer the following question clearly and concisely:

    Question: {question}
    """
    return generate_response(prompt)