
def newline_fixer(original, destination):
    """
    convert dos linefeeds (crlf) to unix (lf)
    usage: dos2unix.py
    """

    content = ""
    outsize = 0
    with open(original, "rb") as fin:
        content = fin.read()
    with open(destination, "wb") as fout:
        for line in content.splitlines():
            outsize += len(line) + 1
            fout.write(line + str.encode("\n"))

    print(f"Done. Saved {outsize} bytes.")

if __name__ == "__main__":
    newline_fixer(r"C:\Users\00986562\Dropbox\Personal\pivot\Udacity - Intro to Machine Learning\ud120-projects-py3-jupyter\17-final-project\final_project_dataset.pkl", "final_project_dataset_unix.pkl")