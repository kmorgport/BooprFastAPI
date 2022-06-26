from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import database
from routers import user, pup, auth


database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
# )

app.include_router(user.router)
app.include_router(pup.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message" : "Hello World" }