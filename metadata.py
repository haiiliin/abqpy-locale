import json
from pathlib import Path

import polib

medatada = {path.as_posix(): polib.pofile(path.as_posix()).metadata for path in Path(".").rglob("*.po")}
medatada |= {path.as_posix(): polib.pofile(path.as_posix()).metadata for path in Path(".").rglob("*.pot")}
with open("metadata.json", "w") as f:
    json.dump(medatada, f, indent=4)
