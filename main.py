import os
from enum import Enum
from pathlib import Path

import openai
from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI
from instructor import patch
from pydantic import BaseModel, Field

load_dotenv()

patch()

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

DATASTORE_PATH = Path("assets")
DATASTORE_PATH.mkdir(parents=True, exist_ok=True)
CSV_FILE_PATH = DATASTORE_PATH / "data.csv"


class Email(BaseModel):
    body: str


class CategoryEnum(str, Enum):
    ride = "Transportation"
    hotel = "Accommodation"
    learn = "Education"
    misc = "Others"


class Content(BaseModel):
    """Correctly classify and extract context from a text"""

    category: CategoryEnum
    amount: str = Field(description="amount with currency e.g $12")
    summary: str = Field(description="short description of the text")
    date: str = Field(description="date from text")


def extract_fn(data, model=Content):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        response_model=model,
        messages=[
            {"role": "user", "content": f"Extract from {data}"},
        ],
    )


def process_email(data):
    content: Content = extract_fn(data=data)

    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, "w") as f:
            f.write("category,amount,summary,date\n")

    with open(CSV_FILE_PATH, "a") as f:
        f.write(
            f"{content.category.value},{content.amount},{content.summary},{content.date}\n"
        )


@app.post("/")
async def log_email(data: Email, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_email, data.body)
    return "Successfully received data"

@app.get("/")
async def get_response():
    return "This page is currently being worked on."