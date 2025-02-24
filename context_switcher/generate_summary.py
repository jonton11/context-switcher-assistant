#!/usr/bin/env python3

from .git_utils import get_latest_commit_info
from .commit_formatter import write_commit_summary
from colorama import init, Fore
init()  # Initialize colorama

def main():
    """Generate a summary for the latest commit."""
    print("Fetching commit info...")
    commit_hash, commit_message, diff = get_latest_commit_info()
    
    if not commit_hash:
        print(f"{Fore.RED}ERROR: Could not fetch commit info{Fore.RESET}")
        return

    print("Parsing commit info...")
    result = write_commit_summary(commit_hash, commit_message, diff)
    
    if result is False:
        print(f"{Fore.RED}ERROR: Failed to generate summary{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}SUCCESS: Summary generated{Fore.RESET}")

if __name__ == "__main__":
    main() 