import json
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union


class SourceReference(BaseModel):
    pdf_sha1: str = Field(..., description="SHA1 hash of the PDF file")
    page_index: int = Field(..., description="Physical page number in the PDF file")


class Answer(BaseModel):
    question_text: str = Field(..., description="Text of the question")
    kind: Literal["number", "name", "boolean", "names"] = Field(..., description="Kind of the question")
    value: Union[float, str, bool, List[str], Literal["N/A"]] = Field(..., description="Answer to the question, according to the question schema")
    references: List[SourceReference] = Field([], description="References to the source material in the PDF file")


class AnswerSubmission(BaseModel):
    team_email: str = Field(..., description="Email that your team used to register for the challenge")
    submission_name: str = Field(..., description="Unique name of the submission (e.g. experiment name)")
    answers: List[Answer] = Field(..., description="List of answers to the questions")


def get_companies_dict(path: str) -> dict:
    # TODO adapt path
    with open(path, "r") as file:
        dataset = json.load(file)

    company_ls = {}
    for idx, data in dataset.items():
        if "sha1" not in data:
            continue
        if "meta" not in data:
            continue
        company_name = data["meta"]["company_name"]
        sha = data["sha1"]
        company_ls[company_name] = {"id": idx[:-4], "sha1": sha}

    return company_ls


def get_company_name(query):
    pass