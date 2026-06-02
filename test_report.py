from agents.report_agent import ReportAgent

agent = ReportAgent()

sample_report = """
Electric vehicles are transforming transportation.

Advantages:
- Zero emissions
- Lower maintenance

Challenges:
- Charging infrastructure
- Battery cost
"""

pdf = agent.generate_pdf(
    topic="Electric Vehicles",
    report_text=sample_report,
    chart_path="charts/ev_chart.png"
)

print("PDF Created:", pdf)