from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the SerperDevTool
tool = SerperDevTool(api_key=os.getenv("SERPER_API_KEY"))