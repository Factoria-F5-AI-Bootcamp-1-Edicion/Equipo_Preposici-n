from typing import List
# import fastapi libraries
from fastapi import APIRouter, Depends, HTTPException, status   #Exceptions HTTP y status
# import nlp libraries
from preprocessing.data_preprocessing import data_tokens
from sklearn.feature_extraction.text import CountVectorizer
import pickle   # Loading BoW dictionary
import joblib   # Load Classifier/Model to later use in prediction
import lightgbm     #Import classifier LGBM


router = APIRouter()
    
####----------------CRUD functions in youtube comments--------------------------#####

@router.post("/",
    response_model=int,
    description="Return if comments is a hate speech",
    status_code=200
)
async def is_hateSpeech(text: str):
    corpus = []
    corpus = data_tokens(text)
    print("Hola")
    print(corpus)
    # Loading BoW dictionary
    cvFile='c1_BoW_HateSpeech_Model.pkl'
    # cv = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open('./drive/MyDrive/Colab Notebooks/2 Sentiment Analysis (Basic)/3.1 BoW_Sentiment Model.pkl', "rb")))
    cv = pickle.load(open(cvFile, "rb"))

    X_fresh = cv.transform(corpus).toarray()
    print(X_fresh.shape)
 
 
    print(X_fresh)
    # Predictions (via hate Speech classifier)
    classifier = joblib.load('c2_Classifier_HateSpeech_Model')

    y_predict = classifier.predict(X_fresh)
    print("Hate Speech: ", (y_predict * 100), "%")

    
    return y_predict
