from tavily import TavilyClient
from config import TAVILY_API_KEY


class ResearchAgent:

    def __init__(self):
        self.client = TavilyClient(api_key=TAVILY_API_KEY)

    def research(self, topic: str):

        response = self.client.search(
            query=topic,
            search_depth="advanced",
            max_results=5
        )

        results = []

        for item in response["results"]:

            results.append(
                {
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "content": item.get("content", "")
                }
            )

        return results