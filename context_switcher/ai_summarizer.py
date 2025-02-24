import os
from openai import OpenAI

def get_enhanced_summary(commit_hash, commit_message, diff):
    """Generate an enhanced summary of the commit using GPT-4."""
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            return "Error: OPENAI_API_KEY not set. Please add 'export OPENAI_API_KEY=your_api_key_here' to your ~/.zshrc or ~/.bashrc"
            
        client = OpenAI(api_key=api_key)
        
        prompt = f"""Analyze this git commit and provide a clear, detailed summary that helps developers understand the changes without needing to see the raw diff.

        Commit: {commit_hash}
        Message: {commit_message}

        Changes:
        {diff}

        Provide a summary that includes:
        1. What changed (be specific about files and functionality)
        2. Why these changes were made (based on commit message and changes)
        3. Technical impact and any potential considerations
        
        Format the response in clear markdown bullet points."""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a senior developer analyzing git commits. Be thorough but concise, focusing on what other developers need to know."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1  # Keep it focused and consistent
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating summary: {str(e)}" 