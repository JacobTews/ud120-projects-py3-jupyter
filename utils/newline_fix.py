
def newline_fixer(original):
    """
    convert dos linefeeds (crlf) to unix (lf)
    usage: dos2unix.py
    """

    content = ""
    outsize = 0
    destination = original[:-4] + "_unix.pkl"
    with open(original, "rb") as fin:
        content = fin.read()
    with open(destination, "wb") as fout:
        for line in content.splitlines():
            outsize += len(line) + 1
            fout.write(line + str.encode("\n"))

    print(f"Done. Saved {outsize} bytes.")

if __name__ == "__main__":
    original = r"C:\Users\00986562\Dropbox\Personal\pivot\Udacity - Intro to Machine Learning\ud120-projects-py3-jupyter\utils\python2_lesson13_keys.pkl"
    newline_fixer(original)