from agents.researcher import ResearchAgent
from agents.analyzer import AnalyzerAgent

topic = "Artificial Intelligence in Healthcare"

research_agent = ResearchAgent()
analyzer_agent = AnalyzerAgent()

research_data = research_agent.research(topic)

report = analyzer_agent.analyze(
    topic,
    research_data
)

print(report)