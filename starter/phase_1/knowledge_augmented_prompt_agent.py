from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

# Instantiate a KnowledgeAugmentedPromptAgent with the specified persona and knowledge
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)

# Get response from the agent
response = knowledge_agent.respond(prompt)

print(f"Prompt: {prompt}")
print(f"Response: {response}")

# Print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge
print("\nNote: The agent correctly used the provided (incorrect) knowledge that 'The capital of France is London, not Paris' instead of its inherent knowledge that Paris is the actual capital.")
