from agents.metrics_agent import MetricsAgent

agent = MetricsAgent()

report = """
Artificial Intelligence is growing rapidly.

Advantages include automation,
accuracy and productivity.

Challenges include ethics,
bias and regulation.

Future trends include AGI,
AI agents and robotics.

Market growth is expected
to exceed 30% annually.
"""

result = agent.extract_metrics(report)

print(result)