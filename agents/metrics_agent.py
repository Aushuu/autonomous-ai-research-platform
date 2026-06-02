from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import json

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)


class MetricsAgent:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=0
        )

    def extract_metrics(self, report_text):

        prompt = f"""
You are a professional business analyst.

Analyze the report and assign scores between 0 and 100.

Definitions:

advantages:
Overall benefits and positive impact

challenges:
Severity of risks and obstacles

future_trends:
Future potential and innovation opportunities

market_growth:
Expected market growth and adoption

Return ONLY valid JSON.

Example:

{{
    "advantages": 85,
    "challenges": 45,
    "future_trends": 90,
    "market_growth": 80
}}

Report:

{report_text}
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        try:

            content = response.content.strip()

            # Remove markdown code fences if present
            if "```json" in content:
                content = (
                    content
                    .replace("```json", "")
                    .replace("```", "")
                    .strip()
                )

            metrics = json.loads(content)

            return {
                "advantages": int(
                    metrics.get("advantages", 70)
                ),
                "challenges": int(
                    metrics.get("challenges", 40)
                ),
                "future_trends": int(
                    metrics.get("future_trends", 80)
                ),
                "market_growth": int(
                    metrics.get("market_growth", 60)
                )
            }

        except Exception as e:

            print("Metrics Error:", e)

            return {
                "advantages": 70,
                "challenges": 40,
                "future_trends": 80,
                "market_growth": 60
            }