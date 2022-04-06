from pathlib import Path


def write_file(text, path):
    f = Path(''.join(map(str, path)))
    if f.exists():
        raise OSError("File exists")
    with f.open("w", encoding="utf-8") as f:
        if type(text) == list:
            for item in text:
                f.write("%s\n" % item)
            return
        f.write(text)
