# Context Switcher Assistant

A developer tool that helps engineers track their work by providing AI-enhanced summaries of their commits.

## Problem Statement

I'm looking to alleviate the frustrations with context switching at work:

1. **Context Loss**: When returning to a project after working on something else, it takes time to rebuild mental context about:
   - What changes were made in the last commit
   - Why certain decisions were made
   - What the next planned steps were

2. **Time Inefficiency**: Significant time is spent:
   - Re-reading old commits and changes
   - Reconstructing the reasoning behind decisions
   - Getting back into the flow of complex work

## Solution

Context Switcher Assistant creates intelligent, readable summaries of your commits:

1. **AI-Powered Commit Analysis**:
   - Uses GPT-4o-mini to analyze commit changes
   - Provides clear, detailed summaries of what changed
   - Explains why changes were made and their technical impact

2. **Easy to Read Format**:
   - Clean markdown formatting
   - Bullet-point summaries
   - Focused on what developers need to know

## Technical Stack

### Core Technologies
- Python 3.11+
- OpenAI GPT-4o-mini for commit analysis
- Git integration via subprocess
- Markdown for readable output

### Project Structure
- `generate_summary.py` - Main entry point
- `git_utils.py` - Git operations
- `commit_formatter.py` - Markdown formatting
- `ai_summarizer.py` - GPT-4o-mini integration

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure OpenAI API**:
   ```bash
   # Copy example env file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Set Up Git Hook**:
   ```bash
   # Navigate to your .git/hooks directory
   cd .git/hooks
   
   # Create and make the post-commit hook executable
   touch post-commit
   chmod +x post-commit
   
   # Add the following to post-commit:
   #!/bin/sh
   python3.11 /path/to/your/generate_summary.py
   ```
   Replace `/path/to/your/generate_summary.py` with the actual path to the script.

## Usage

After setup, the tool automatically runs after each commit:
1. Analyzes the commit changes using GPT-4o-mini
2. Generates a detailed summary including:
   - What changed (specific files and functionality)
   - Why changes were made
   - Technical impact and considerations
3. Saves the summary to `last_working_session.md`

You can also run it manually:
```bash
python3.11 generate_summary.py
```
