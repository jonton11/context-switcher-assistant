# Context Switcher Assistant

A developer tool that helps engineers manage context switching between different types of work by providing intelligent summaries of past working sessions.

## Problem Statement

I'm looking to alleviate the frustrations with context switching at work:

1. **Context Loss**: When returning to a project after working on something else, it takes time to rebuild mental context about:
   - What changes were made in the last session
   - Why certain decisions were made
   - What the next planned steps were

2. **Mental Overhead**: Having to maintain multiple contexts for:
   - Individual contributor work (coding, reviews)
   - Strategic planning and technical design
   - Cross-team coordination and negotiations
   - Project management and mentoring

3. **Time Inefficiency**: Significant time is spent:
   - Re-reading old commits and changes
   - Reconstructing the reasoning behind decisions
   - Getting back into the flow of complex work

## Solution

Context Switcher Assistant leverages the Model Context Protocol (MCP) to create an intelligent system that:

1. **Tracks Working Sessions**:
   - Automatically detects coding sessions based on git activity
   - Groups related commits into logical sessions
   - Identifies different types of work (IC, strategy, collaboration)

2. **Generates Smart Summaries**:
   - Creates semantic summaries of code changes
   - Captures key decisions and their context
   - Maintains relationships between related changes

3. **Provides Quick Context Recovery**:
   - Offers concise session summaries when returning to work
   - Shows progression of changes in a meaningful way
   - Highlights important decisions and their rationale

## Technical Stack

### Core Technologies
- **Language**: Python 3.11+
  - Strong ecosystem for git integration
  - Excellent AI/NLP capabilities
  - Great for CLI applications
  - Type hints for better maintainability

### Key Components
1. **Git Integration**:
   - GitPython for repository interaction
   - Custom commit analysis and grouping

2. **Summary Storage**:
   - Inline comments in code for context-specific summaries
   - Separate text files for session or commit summaries
   - Optional use of Git notes for attaching summaries to commits

3. **Intelligence Layer**:
   - Model Context Protocol (MCP) for system interactions
   - OpenAI API for semantic analysis
   - LangChain for AI orchestration

4. **CLI Interface**:
   - Typer for command-line interface
   - Rich for beautiful terminal output
   - Click for command composition

### Development Tools
- Rye for dependency management
- Ruff for linting and formatting
- Pytest for testing
- GitHub Actions for CI/CD
