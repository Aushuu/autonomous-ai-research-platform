import json

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)


class DataExtractorAgent:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=0
        )

    def extract_data(self, report_text):

        prompt = f"""
Extract the most important numerical statistics
from this report.

Return ONLY JSON.

Example:

{{
    "Statistic 1": 100,
    "Statistic 2": 50,
    "Statistic 3": 20,
    "Statistic 4": 10
}}

Report:

{report_text}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        try:
            content = response.content.strip()

            if "```json" in content:
                content = (
                    content
                    .replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            return json.loads(content)

        except:

            return {}