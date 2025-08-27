from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

augmented_agent = AugmentedPromptAgent(openai_api_key, persona)
augmented_agent_response = augmented_agent.respond(prompt)

print(f"Prompt: {prompt}")
print(f"Response: {augmented_agent_response}")

# The agent uses general knowledge from the LLM's training data.
# The persona affects the response style - makes it start with "Dear students,"
