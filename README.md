# Context Switcher Assistant

A developer tool that helps engineers track their work by providing detailed summaries of their commits.

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

Context Switcher Assistant creates detailed, readable summaries of your commits:

1. **Automatic Commit Summaries**:
   - Generates a markdown summary after each commit
   - Includes commit message, timestamp, and complete diff
   - Shows changes across all modified files

2. **Easy to Read Format**:
   - Clean markdown formatting
   - Syntax-highlighted diffs
   - Clear structure showing commit info and changes

## Technical Stack

### Core Technologies
- Python 3.11+
- Git integration via subprocess
- Markdown for readable output

### Project Structure
- `generate_summary.py` - Main entry point
- `git_utils.py` - Git operations
- `commit_formatter.py` - Markdown formatting

## Usage Instructions

To automatically generate summaries of your commits, follow these steps:

1. **Set Up the Python Script**:
   - Clone this repository or copy the scripts to your project directory

2. **Configure the Git Hook**:
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

3. **Test the Setup**:
   - Make a commit in your repository
   - Check `last_working_session.md` to see your commit summary

Each time you make a commit, a new summary will be generated containing:
- Commit timestamp
- Commit hash
- Commit message
- Complete diff of all changed files
