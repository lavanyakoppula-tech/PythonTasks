f = open("article.txt");
text = f.read();
f.close()
print(len(text.split()), "words,", len(text.splitlines()), "lines,", len(text), "chars")
