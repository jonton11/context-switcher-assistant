import os
from datetime import datetime
from .ai_summarizer import get_enhanced_summary

SUMMARY_FILE = 'last_working_session.md'  # Keep filename for backwards compatibility

def write_commit_summary(commit_hash, commit_message, diff):
    """Generate and write a summary of the latest commit using AI analysis."""
    if not commit_hash or not commit_message or not diff:
        print("Error: Missing commit information")
        return False

    print("Generating AI summary...")
    ai_summary = get_enhanced_summary(commit_hash, commit_message, diff)
    if ai_summary.startswith("Error"):
        print(ai_summary)
        return False

    print("Writing summary to file...")
    with open(SUMMARY_FILE, 'w') as summary_file:
        summary_file.write("# Commit Summary\n\n")
        summary_file.write(f"**Time**: {datetime.now().isoformat()}\n")
        summary_file.write(f"**Commit**: {commit_hash}\n")
        summary_file.write(f"**Message**: {commit_message}\n\n")
        summary_file.write("## Analysis\n\n")
        summary_file.write(f"{ai_summary}\n")
    
    return True 