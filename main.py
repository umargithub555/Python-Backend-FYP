from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import clinicalNotes,diseasePrediction,prescription,textExtraction


app = FastAPI()


origins=[
    "http://localhost",  
    "http://localhost:3000",  
    "http://localhost:5173",
    "http://localhost:8080",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(clinicalNotes.router)
app.include_router(diseasePrediction.router)
app.include_router(prescription.router)
app.include_router(textExtraction.router)




