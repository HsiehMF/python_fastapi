import uvicorn
from fastapi import FastAPI
from koodata_exam.router import pokemon

try:
    app = FastAPI()
    app.include_router(pokemon.router, prefix="/exam", tags=["exam"])
    uvicorn.run(app, host='0.0.0.0')
except Exception as err:
    print(err)