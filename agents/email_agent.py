import smtplib
from email.message import EmailMessage

from config import (
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)


class EmailAgent:

    def send_report(
        self,
        receiver_email,
        pdf_path
    ):

        msg = EmailMessage()

        msg["Subject"] = "AI Generated Research Report"

        msg["From"] = EMAIL_ADDRESS

        msg["To"] = receiver_email

        msg.set_content(
            "Your AI-generated report is attached."
        )

        with open(pdf_path, "rb") as f:

            file_data = f.read()

            file_name = pdf_path.split("/")[-1]

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename=file_name
        )

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                EMAIL_ADDRESS,
                EMAIL_PASSWORD
            )

            smtp.send_message(msg)

        return True