# Last Working Session Summaries


### Commit Summary

**Commit**: 5d4e19dc4305bbeddc88e937aaf644f320dfe54c
**Message**: feat: Add manual mode; add steps for usage in README

**Changes**:
```
diff --git a/README.md b/README.md
index ea9001a..f22091a 100644
--- a/README.md
+++ b/README.md
@@ -75,3 +75,30 @@ Context Switcher Assistant leverages the Model Context Protocol (MCP) to create
 - Ruff for linting and formatting
 - Pytest for testing
 - GitHub Actions for CI/CD
+
+## Usage Instructions
+
+To automatically generate summaries of your commits and store them in `last_working_session.md`, follow these steps:
+
+1. **Set Up the Python Script**:
+   - Ensure the `generate_summary.py` script is in your project directory.
+
+2. **Configure the Git Hook**:
+   - Navigate to your `.git/hooks` directory.
+   - Create a `post-commit` file and make it executable:
+     ```bash
+     touch .git/hooks/post-commit
+     chmod +x .git/hooks/post-commit
+     ```
+   - Add the following line to the `post-commit` file:
+     ```bash
+     #!/bin/sh
+     python3.11 /path/to/your/generate_summary.py
+     ```
+   - Replace `/path/to/your/generate_summary.py` with the actual path to your script.
+
+3. **Test the Setup**:
+   - Make a commit in your repository.
+   - Check the `last_working_session.md` file to see if the summary is appended correctly.
+
+This setup will ensure that every time you make a commit, a summary of the changes is automatically generated and stored, helping you keep track of your work sessions efficiently.
diff --git a/generate_summary.py b/generate_summary.py
index 6e85c4b..90d44b0 100644
--- a/generate_summary.py
+++ b/generate_summary.py
@@ -1,6 +1,7 @@
 import subprocess
 import os
 import logging
+import argparse
 
 # Configure logging
 logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
@@ -36,11 +37,16 @@ def append_to_last_session(summary, filename='last_working_session.md'):
     with open(filename, 'a') as session_file:
         session_file.write("\n" + summary)
 
-def main():
+def main(manual=False):
     """Main function to execute the summary generation and storage."""
+    if manual:
+        logging.info("Running in manual mode.")
     commit_hash, commit_message, diff = get_commit_info()
     summary = generate_summary(commit_hash, commit_message, diff)
     append_to_last_session(summary)
 
 if __name__ == "__main__":
-    main() 
\ No newline at end of file
+    parser = argparse.ArgumentParser(description="Generate commit summaries.")
+    parser.add_argument('--manual', action='store_true', help="Run the script manually.")
+    args = parser.parse_args()
+    main(manual=args.manual) 
\ No newline at end of file

```
