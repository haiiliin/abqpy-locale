import re

from git import Diff, Repo

pattern = r'"PO-Revision-Date: \d+-\d+-\d+ \d+:\d+\\n"'
repo = Repo(".")
for diff in repo.index.diff(repo.branches["main"].commit).iter_change_type("M"):  # type: Diff
    # Get deleted lines
    filepath = diff.a_blob.path
    original_text = diff.b_blob.data_stream.read().decode("utf-8")
    original_lines = original_text.splitlines()
    modified_text = diff.a_blob.data_stream.read().decode("utf-8")
    modified_lines = modified_text.splitlines()
    deleted_lines = [line for line in original_lines if line not in modified_lines]
    added_lines = [line for line in modified_lines if line not in original_lines]
    if all([re.match(pattern, line) for line in deleted_lines + added_lines]):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(original_text)
            print(f"# Reverted {filepath}")
