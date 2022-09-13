from fastapi import FastAPI
# import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from  . import models
from  .database import engine
from  .routers import user, post, auth, vote
from .config import settings



# models.Base.metadata.create_all(bind=engine) no longer need this command cause we use alembic instead

app = FastAPI()


origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



# if __name__ == '__main__':
#     uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)