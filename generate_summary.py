#!/usr/bin/env python3

from git_utils import get_latest_commit_info
from commit_formatter import write_commit_summary

def main():
    """Generate a summary for the latest commit."""
    commit_hash, commit_message, diff = get_latest_commit_info()
    if commit_hash:
        write_commit_summary(commit_hash, commit_message, diff)

if __name__ == "__main__":
    main() 