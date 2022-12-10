from fastapi import FastAPI
from routes.api_router import api_router
#from config.openapi import tags_metadata

app = FastAPI(
    title="Hate Speech API",
    description="a REST API using python to classify whether a comment or several comments are hateful or not",
    version="0.0.1",
    #openapi_tags=tags_metadata,
)

#Enrutamos
app.include_router(api_router)
