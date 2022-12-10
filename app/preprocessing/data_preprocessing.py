#Import libraries
import re       # RegEx
import string
import nltk     # Natural Lenguage ToolKit
from nltk.corpus import stopwords       # Stopwords
from nltk.stem.porter import PorterStemmer  # Stemming

## Stemming and stopwords
nltk.download('stopwords')

ps = PorterStemmer()

all_stopwords = stopwords.words('english')
all_stopwords.remove('not')


# Data Preprocessing 

def label_cat(label):
    # No funciona de otra manera si no convierto de bool a int64
    label[label==False] = 0
    label[label==True] = 1
    label = label.astype(dtype=int)
    return label

def data_tokens(text):
    # Cleaning Data and Tokens : corpus
    corpus=[]

    #Quitamos espacios en todos los comentarios
    #Borra espacios xa0
    text = text.replace(u'\xa0', u' ')
    #Borra espacios en blanco
    text = text.strip()

    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    # Comprobar los caracteres para ver si están en la puntuación
    review = [char for char in review if char not in string.punctuation]
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    #review = [ps.stem(word) for word in review if not word in set(lemmas)]
    #review = ' '.join(review)
    #corpus.append(review)
    return review

    return(corpus)




