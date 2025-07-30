import os
import anthropic

def analyze_resume_with_claude(resume_text, target_role):
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""
You are an expert tech recruiter. A candidate has submitted their resume and specified the role they are targeting: '{target_role}'.

Please do the following:
1. Provide 3 specific strengths from the resume that match this role.
2. Suggest 3 improvements they can make to be a stronger candidate.
3. Rate how well this resume fits the role on a scale from 1 to 10 and justify your score.

Resume:
{resume_text}
"""

    response = client.messages.create(
        model="claude-2.1"
,
        max_tokens=1024,
        temperature=0.7,
        system="You are an expert resume reviewer for tech roles.",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # ✅ Extract the full message content safely
    return response.content[0].text if response.content else "No response from Claude"
