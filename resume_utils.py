import os
import anthropic

def analyze_resume_with_claude(resume_text, target_role):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = (
        "\n\nHuman: "
        f"You're a helpful career coach. Analyze the resume below and give detailed feedback "
        f"tailored to the target role '{target_role}'. "
        f"Point out what’s strong, what can be improved, and whether it matches the job.\n\n"
        f"Resume:\n{resume_text}\n\n"
        "\n\nAssistant:"
    )

    response = client.completions.create(
        model="claude-2.1",
        prompt=prompt,
        max_tokens=1000,
        temperature=0.7,
        stop_sequences=["\n\nHuman:"]
    )

    return response.completion
