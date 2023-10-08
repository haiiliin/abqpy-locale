from pathlib import Path
import json


edit_urls = {}
crowdin_edit_url_template = "https://crowdin.com/translate/abqpy-locale/{file_id}/en-{lang}"
github_edit_url_template = "https://github.com/haiiliin/abqpy-locale/edit/main/{file}"

# Read metadata
with open("metadata.json", "r") as f:
    metadata = json.load(f)

# Generate edit URLs
for version in range(2023, 2015, -1):
    edit_urls[f"{version}"] = edit_urls_version = {}
    for language in ("zh_CN",):
        edit_urls[f"{version}"][language] = {}
        lang = language.replace("_", "").lower()
        for pofile in Path(f"{version}/{language}/LC_MESSAGES").rglob("*.po"):
            key = pofile.relative_to(f"{version}/{language}/LC_MESSAGES").with_suffix("").as_posix()
            if f"{version}/{language}/LC_MESSAGES/{pofile.name}" not in metadata:
                edit_urls[f"{version}"][language][key] = github_edit_url_template.format(file=pofile.as_posix())
                continue
            meta_key = pofile.relative_to(f"{version}/{language}/LC_MESSAGES").as_posix()
            meta = metadata[f"{version}/{language}/LC_MESSAGES/{meta_key}"]
            if "X-Crowdin-File-ID" in meta:
                edit_urls[f"{version}"][language][key] = crowdin_edit_url_template.format(
                    file_id=meta["X-Crowdin-File-ID"],
                    lang=lang
                )
            else:
                edit_urls[f"{version}"][language][key] = github_edit_url_template.format(file=pofile.as_posix())


with open("edit-urls.json", "w") as f:
    json.dump(edit_urls, f, indent=4)
