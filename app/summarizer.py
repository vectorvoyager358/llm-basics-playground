from app.llm import generate_response

def summarize_text(text):
    prompt = f"""
    Summarize the following text in 3 concise bullet points:

    {text}
    """
    return generate_response(prompt)