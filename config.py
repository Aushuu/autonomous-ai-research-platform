from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

REPORTS_DIR = "reports"
CHARTS_DIR = "charts"
VECTORSTORE_DIR = "vectorstore"
DATA_DIR = "data"

MODEL_NAME = "llama-3.1-8b-instant"