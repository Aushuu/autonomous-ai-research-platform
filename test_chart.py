from agents.chart_agent import ChartAgent

agent = ChartAgent()

path = agent.generate_chart()

print("Chart Saved:", path)