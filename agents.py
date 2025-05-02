from dotenv import load_dotenv
import os
from litellm import completion
from crewai import Agent
from tools import tool

# Load environment variables
load_dotenv()
os.environ['GEMINI_API_KEY'] = os.getenv("GOOGLE_API_KEY")


# ✅ Minimal custom LLM wrapper using litellm.completion
class LiteLLMGemini:
    def __init__(self, model="gemini/gemini-1.5-flash", temperature=0.4):
        self.model = model
        self.temperature = temperature
        self.api_key = os.environ['GEMINI_API_KEY']

    def run(self, prompt: str):
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
            api_key=self.api_key
        )
        return response['choices'][0]['message']['content']


# ✅ Instantiate shared LiteLLM Gemini object
llm = LiteLLMGemini()

# ✅ Define the Senior Researcher Agent
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory="Driven by curiosity, you are at the forefront of innovation.",
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)

# ✅ Define the News Writer Agent
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory="A storyteller who crafts captivating narratives.",
    tools=[tool],
    llm=llm,
    allow_delegation=False,
)
