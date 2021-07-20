"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py
"""
original = "word_data.pkl"
destination = "word_data_unix.pkl"

content = ""
outsize = 0
with open(original, "rb") as fin:
    content = fin.read()
with open(destination, "wb") as fout:
    for line in content.splitlines():
        outsize += len(line) + 1
        fout.write(line + str.encode("\n"))

print(f"Done. Saved {outsize} bytes.")