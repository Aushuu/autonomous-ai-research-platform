from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from config import (
    GROQ_API_KEY,
    MODEL_NAME
)


class AnalyzerAgent:

    def __init__(self):

        self.llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME,
            temperature=0.3
        )

    def analyze(self, topic, research_results, rag_context):

        combined_text = ""

        references_text = ""

        for index, item in enumerate(
            research_results[:3],
            start=1
        ):

            combined_text += f"""
Title:
{item['title']}

Content:
{item['content'][:500]}  # Limiting content to first 500 characters
"""

            references_text += f"""
[{index}]
Title: {item['title']}
URL: {item['url']}
"""

        prompt = f"""
You are a professional research analyst.

Topic:
{topic}

RAG Context:
{rag_context}

Research Data:
{combined_text}

Available Sources:
{references_text}

Write a professional report with:

1. Introduction
2. Market Overview
3. Key Technologies
4. Advantages
5. Challenges
6. Future Trends
7. Conclusion

Use source citations throughout the report.

Examples:

Artificial Intelligence improves healthcare [1].

Machine learning enables better diagnosis [2].

Electric vehicles reduce emissions [3].

For every important statement, add a citation using
the source numbers provided.

At the end include:

References

[1] Source Title

[2] Source Title

[3] Source Title
"""

        response = self.llm.invoke(
            [HumanMessage(content=prompt)]
        )

        return response.content