import sys

# inline the word list into src.html and wrap it as a full page
words = open(sys.argv[1] if len(sys.argv) > 1 else "words.txt").read().strip()
src = open("src.html").read().replace("__WORDS__", words)
head, body = src.split('<div class="wrap">', 1)
desc = "every page that could ever be written, and a miner that digs for real english in it"
open("index.html", "w").write(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    f'<meta name="description" content="{desc}">\n'
    + head + '</head>\n<body>\n<div class="wrap">' + body + "</body>\n</html>\n"
)
