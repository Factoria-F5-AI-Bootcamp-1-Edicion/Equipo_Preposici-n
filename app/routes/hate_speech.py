import pandas as pd
from typing import List
# import fastapi libraries
from fastapi import APIRouter, Depends, HTTPException, status   #Exceptions HTTP y status
# import nlp libraries
from schemas.classifier import ModelClassifier
from schemas.comment import Comment, CommentCount
from preprocessing.data_preprocessing import data_tokens
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import joblib   # Load Classifier/Model to later use in prediction


router = APIRouter()

#Variable global para recuento de predicciones
router.num_pred = 0
    
####----------------Funciones CRUD sobre comentarios en YouTube------------------#####
####-------------------------Detection on HateSpeech-----------------------------#####

@router.get(
    "/comments",
    #response_model=List[Comment],
    description="Get a Dict of all comments",
)
async def get_list_predicted_comments(model_classifier: ModelClassifier):
    result = []
    try:
    
        ## Leer df
        path = 'data/test_comments_1k.csv'
        df = pd.read_csv(path)

        X_valid = df['comment_text']
        # Carga el modelo
        pipeline = joblib.load(model_classifier)
        #print(pipeline)
        # Predictions (via hate Speech classifier)
        y_predict = pipeline.predict(X_valid)
        unique_list = list(set(y_predict))
        #print(unique_list)
        df['label'] = y_predict
        series = df['label'].value_counts()
        #print(series)
        router.num_pred = series[1].astype(dtype=int)
        #print(router.num_pred)
        df.to_csv('predictions/prediction_' + model_classifier + '', index=False)
        result = df.to_dict()
    except:
        #En caso de que no se pueda ejecutar la transacción hago rollback de la transacción y lanzo HttpException
        raise HTTPException(status_code=404, detail="Data Frame not found")
    return result

@router.get(
        "/comments/count",
        description="Get a number of predictions on comments", 
        response_model=CommentCount,
)
async def get_predictions_count():
    print(router.num_pred)
    try:
        router.num_pred
        print(f'Number predictions: {router.num_pred}')
        
    except:
        #En caso de que no se pueda ejecutar la transacción lanzo HttpException
        raise HTTPException(status_code=404, detail="Seleccion una lista de comentarios a predecir")
    return {"total": router.num_pred}

@router.post("/",
    response_model=int,
    description="Return if comment is a hate speech",
    status_code=200
)
async def is_hateSpeech(model_classifier: ModelClassifier, new_text: str):

    '''    
    corpus = []
    corpus = data_tokens(new_text)

    print(corpus)
    # Loading BoW dictionary
    cvFile='BoW_HateSpeech_Model.pkl'
    # cv = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open('./drive/MyDrive/Colab Notebooks/2 Sentiment Analysis (Basic)/3.1 BoW_Sentiment Model.pkl', "rb")))
    tfidf = pickle.load(open(cvFile, "rb"))

    print("Hola")
    print(tfidf.get_feature_names_out())
    X_fresh = tfidf.transform(corpus).toarray()
    print(X_fresh)
    '''

    columns = ['Text']
    df = pd.DataFrame([new_text], columns = columns)
    #print(df['Text'])
 
    # Predictions (via hate Speech classifier)
    pipeline = joblib.load(model_classifier)
    # Transformamos con los nuevos datos
    #print(pipeline)
    y_predict = pipeline.predict(df['Text'])
    print("Hate Speech: ", (y_predict * 100), "%")
   
    return y_predict
