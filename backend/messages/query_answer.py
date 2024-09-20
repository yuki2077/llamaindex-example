from pydantic import BaseModel, Field
from typing import Optional


class QeryAnswer(BaseModel):
    """LLMの回答スキーマ定義"""

    answer: str = Field(description="質問に対する回答")
    source_file_name: str = Field(
        description="回答のソースに使った ファイル名", default=""
    )
    source_file_path: str = Field(
        description="回答のソースに使った ファイルパス", default=""
    )
    related_topics: list[str] = Field(description="関連するトピック", default=[])
