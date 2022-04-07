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


def get_wordlist(path):
    WORDLIST = []
    words = open(path, 'r').read().split('\n')
    for word in words:
        WORDLIST.append(word.upper())
    return WORDLIST


def analyse_text(text, wordlist_path):
    wordlist = get_wordlist(wordlist_path)
    text = text.upper()
    matches = 0
    for word in text.split(' '):
        if word in wordlist:
            matches += 1
    return matches


def get_text(args, prop):
    if args.sourceFile:
        return open(' '.join(args.sourceFile), 'r').read()
    else:
        return ''.join(vars(args)[prop])
