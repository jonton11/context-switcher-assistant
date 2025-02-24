import os
from datetime import datetime

SUMMARY_FILE = 'last_working_session.md'  # Keep filename for backwards compatibility

def write_commit_summary(commit_hash, commit_message, diff):
    """Generate and write a summary of the latest commit.
    
    The diff will include all files changed in this commit. The output is formatted
    as a markdown file with the commit hash, message, timestamp, and a diff section
    showing all file changes.
    """
    if not commit_hash or not commit_message or not diff:
        print("Error: Missing commit information")
        return
    
    with open(SUMMARY_FILE, 'w') as summary_file:
        summary_file.write("# Latest Commit Summary\n\n")
        summary_file.write(f"**Time**: {datetime.now().isoformat()}\n\n")
        summary_file.write(f"**Commit**: {commit_hash}\n\n")
        summary_file.write(f"**Message**: {commit_message}\n\n")
        summary_file.write(f"**Changes**:\n```diff\n{diff}\n```\n") 