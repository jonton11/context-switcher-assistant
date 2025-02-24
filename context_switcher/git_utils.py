import subprocess

def get_latest_commit_info():
    """Retrieve the commit message and diff for the latest commit."""
    try:
        # Get the latest commit hash
        commit_hash = subprocess.check_output(
            ['git', 'rev-parse', 'HEAD'],
            universal_newlines=True
        ).strip()

        # Get the commit message
        commit_message = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=%B'],
            universal_newlines=True
        ).strip()

        # Get the diff
        diff = subprocess.check_output(
            ['git', 'diff', 'HEAD~1', 'HEAD'],
            universal_newlines=True
        )

        return commit_hash, commit_message, diff
    except subprocess.CalledProcessError:
        return None, None, None 