from fastapi import FastAPI
from chatbot_utils import chat_stream
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# initialise app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# custom LLM chain
add_routes(
    app,
    chat_stream,
    path = '/chat'
)

# start app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)