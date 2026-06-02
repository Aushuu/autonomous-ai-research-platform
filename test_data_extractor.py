from agents.data_extractor import DataExtractorAgent

agent = DataExtractorAgent()

report = """
Tourism generated 140 billion dollars.

Domestic visits reached 2948 million.

Foreign visits reached 20.94 million.

Growth rate was 17.51%.
"""

print(
    agent.extract_data(report)
)