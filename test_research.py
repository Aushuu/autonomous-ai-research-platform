from agents.researcher import ResearchAgent

agent = ResearchAgent()

data = agent.research("Electric Vehicles")

print("\nRESULTS FOUND:", len(data))

for article in data[:3]:
    print("\nTITLE:")
    print(article["title"])

    print("\nURL:")
    print(article["url"])

    print("\nCONTENT:")
    print(article["content"][:300])

    print("-" * 80)