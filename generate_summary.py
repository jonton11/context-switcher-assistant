import subprocess
import os
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_commit_info():
    """Retrieve the latest commit hash, message, and diff."""
    try:
        commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        commit_message = subprocess.check_output(['git', 'log', '-1', '--pretty=%B']).strip().decode('utf-8')
        diff = subprocess.check_output(['git', 'diff', 'HEAD~1', 'HEAD']).decode('utf-8')
        return commit_hash, commit_message, diff
    except subprocess.CalledProcessError as e:
        logging.error("Error retrieving commit information: %s", e)
        return None, None, None

def generate_summary(commit_hash, commit_message, diff):
    """Generate a summary based on commit information."""
    if not commit_hash or not commit_message or not diff:
        return "Error generating summary due to missing commit information."
    summary = (
        f"### Commit Summary\n\n"
        f"**Commit**: {commit_hash}\n"
        f"**Message**: {commit_message}\n\n"
        f"**Changes**:\n```\n{diff}\n```\n"
    )
    return summary

def append_to_last_session(summary, filename='last_working_session.md'):
    """Append the summary to the specified file, creating it if necessary."""
    if not os.path.exists(filename):
        with open(filename, 'w') as session_file:
            session_file.write("# Last Working Session Summaries\n\n")
    with open(filename, 'a') as session_file:
        session_file.write("\n" + summary)

def main(manual=False):
    """Main function to execute the summary generation and storage."""
    if manual:
        logging.info("Running in manual mode.")
    commit_hash, commit_message, diff = get_commit_info()
    summary = generate_summary(commit_hash, commit_message, diff)
    append_to_last_session(summary)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate commit summaries.")
    parser.add_argument('--manual', action='store_true', help="Run the script manually.")
    args = parser.parse_args()
    main(manual=args.manual) 