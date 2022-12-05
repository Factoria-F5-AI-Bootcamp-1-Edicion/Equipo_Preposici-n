#Import libraries
import re       # RegEx
import nltk     # Natural Lenguage ToolKit
from nltk.corpus import stopwords       # Stopwords
from nltk.stem.porter import PorterStemmer  # Stemming

# Data Preprocessing 


def data_tokens(texts):
    ## Stemming and stopwords
    nltk.download('stopwords')

    ps = PorterStemmer()

    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    # Cleaning Data and Tokens : corpus
    corpus=[]

    if texts is list:
        for i in range(0, len(texts)):
            review = re.sub('[^a-zA-Z]', ' ', texts[i])
            review = review.lower()
            review = review.split()
            review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
            review = ' '.join(review)
            corpus.append(review)
    else:
        review = re.sub('[^a-zA-Z]', ' ', texts)
        review = review.lower()
        review = review.split()
        review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)

    return(corpus)




