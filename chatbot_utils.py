import os

from fastapi import HTTPException, Request

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables.utils import ConfigurableField


# environment variables ======================================================
os.environ["TOKENIZERS_PARALLELISM"] = "false"
op_api_key = "enter your openai api key"

model = ChatOpenAI(api_key=op_api_key, model='gpt-4o')

def buffer(input):
    print(input)
    return input

buffer = RunnableLambda(buffer)

chat_stream = buffer | model | StrOutputParser()

