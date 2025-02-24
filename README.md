# Context Switcher Assistant

A developer tool that helps engineers track their work by providing AI-enhanced summaries of their commits.

## Quick Start

### Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/jonton11/context-switcher-assistant.git
```

### Setup

1. **Configure OpenAI API**:
   ```bash
   # Add to your ~/.zshrc or ~/.bashrc
   export OPENAI_API_KEY=your_api_key_here

   # Then reload your shell configuration
   source ~/.zshrc  # or source ~/.bashrc
   ```

### Usage

The tool can be run manually to analyze your latest commit:
```bash
context-switcher
```

This will:
1. Analyze the latest commit using GPT-4o-mini
2. Generate a detailed summary including:
   - What changed (specific files and functionality)
   - Why changes were made
   - Technical impact and considerations
3. Save the summary to `last_working_session.md`

### Automatic Usage (Optional)

You can set up a git hook to run automatically after each commit:
```bash
# Navigate to your project's .git/hooks directory
cd .git/hooks

# Create and make the post-commit hook executable
echo '#!/bin/sh
context-switcher' > post-commit
chmod +x post-commit
```

## Project Overview

### Problem Statement

I'm looking to alleviate the frustrations with context switching at work:

1. **Context Loss**: When returning to a project after working on something else, it takes time to rebuild mental context about:
   - What changes were made in the last commit
   - Why certain decisions were made
   - What the next planned steps were

2. **Time Inefficiency**: Significant time is spent:
   - Re-reading old commits and changes
   - Reconstructing the reasoning behind decisions
   - Getting back into the flow of complex work

### Solution

Context Switcher Assistant creates intelligent, readable summaries of your commits:

1. **AI-Powered Commit Analysis**:
   - Uses GPT-4o-mini to analyze commit changes
   - Provides clear, detailed summaries of what changed
   - Explains why changes were made and their technical impact

2. **Easy to Read Format**:
   - Clean markdown formatting
   - Bullet-point summaries
   - Focused on what developers need to know

## Technical Details

### Core Technologies
- Python 3.11+
- OpenAI GPT-4o-mini for commit analysis
- Git integration via subprocess
- Markdown for readable output

### Project Structure
- `generate_summary.py` - Main entry point and CLI interface
- `git_utils.py` - Git operations and commit handling
- `commit_formatter.py` - Markdown formatting and file writing
- `ai_summarizer.py` - GPT-4o-mini integration and prompt handling
