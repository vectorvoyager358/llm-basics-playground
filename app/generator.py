from app.llm import generate_response

def generate_content(topic):
    prompt = f"""
    Write a LinkedIn post about {topic}.
    Make it engaging and professional.
    """
    return generate_response(prompt)

from app.llm import generate_response