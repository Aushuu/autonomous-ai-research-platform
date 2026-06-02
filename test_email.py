from agents.email_agent import EmailAgent

agent = EmailAgent()

agent.send_report(
    "vu.241fa04a89@gmail.com",
    "reports/report.pdf"
)

print("Email Sent Successfully")