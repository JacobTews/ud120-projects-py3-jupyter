import nltk
from nltk.corpus import stopwords
# nltk.download("stopwords")
# print(stopwords.words("english"))
print(f"Number of English stopwords: {len(stopwords.words('english'))}")
print(f"Number of German stopwords: {len(stopwords.words('german'))}")
# print(stopwords.words("german"))
