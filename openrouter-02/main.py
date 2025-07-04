from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig


load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY") 


# Check if the API key is present; if not, raise an error
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")


#Reference: https://openrouter.ai/docs/quickstart
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-r1-0528:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


agent = Agent(
    name = "Global Translator",
    instructions = "Translate any input into the user’s english language using simple and urdu language. Support formal and informal tones.",

)

response = Runner.run_sync( 
    agent,
    input = "what is capital of pakistan?",
    run_config = config
)

print(response)