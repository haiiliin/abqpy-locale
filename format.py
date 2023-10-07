from pathlib import Path
import re


pattern = re.compile(r'msgid ""\nmsgstr ""\n([\w\W]+?)\n\n')
for pofile in Path(".").glob("**/*.po"):
    with pofile.open("r", encoding="utf=8") as f:
        content = f.read()

    # Find all patterns
    for match in pattern.finditer(content):
        msgstr = match.group(1).replace('"', "").replace("\n", "")
        msgstr_formatted = "\n".join([f'"{split}\\n"' for split in msgstr.split("\\n") if split])
        content = content.replace(msgstr, msgstr_formatted)

    with pofile.open("w", encoding="utf=8") as f:
        f.write(content)
