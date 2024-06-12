import logging
from autogenstudio import AutoGenWorkFlowManager as WorkflowManager
import warnings
import json
import os
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import time

# Configure logging to file
log_filename = "workflow_log.txt"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler(log_filename), logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Print warning if needed packages are missing.
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", message="IProgress not found. Please update jupyter and ipywidgets.")

# Load environment variables from .env file
load_dotenv()

# Ensure the script's directory is the current working directory
script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

# Debug: Print current directory and check if .env file exists
print("Current Directory:", script_dir)
print(".env file exists:", os.path.exists(os.path.join(script_dir, ".env")))

# Load workflow from specific json file
workflow_file = "workflow_Example_of_Hallucination_(Danish_artist_flipflopidy).json"
with open(workflow_file, "r") as f:
    config = json.load(f)

# Set the API keys from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Debug: Print the API keys to verify they are loaded
print("GROQ_API_KEY:", groq_api_key)
print("OPENAI_API_KEY:", openai_api_key)

if not groq_api_key or not openai_api_key:
    logger.error("API keys for Groq and/or OpenAI are not set in the environment variables.")
    raise EnvironmentError("API keys for Groq and/or OpenAI are not set in the environment variables.")

# Update the API keys in the workflow configuration
for agent in config['receiver']['config']['llm_config']['config_list']:
    if "groq.com" in agent['base_url']:
        agent['api_key'] = groq_api_key
    elif "openai.com" in agent['base_url']:
        agent['api_key'] = openai_api_key

for agent in config['receiver']['groupchat_config']['agents']:
    for agent_config in agent['config']['llm_config']['config_list']:
        if "groq.com" in agent_config['base_url']:
            agent_config['api_key'] = groq_api_key
        elif "openai.com" in agent_config['base_url']:
            agent_config['api_key'] = openai_api_key

# Assuming AgentWorkFlowConfig is the appropriate data structure
from autogenstudio.datamodel import AgentWorkFlowConfig
workflow_config = AgentWorkFlowConfig(**config)

# Define the task query
task_query = "Write a very short blog about the Danish artist flipflopidy."

# Function to run the workflow and write to Excel
def run_workflow_and_log():
    # Initialize the workflow manager
    workflow_manager = WorkflowManager(config=workflow_config)
    
    # Record the start time
    start_time = time.time()
    
    # Run the workflow on the task
    workflow_manager.run(message=task_query)
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the duration in seconds, formatted to two decimal places
    duration_seconds = round(end_time - start_time, 2)
    
    # Fetch the last message in the conversation
    last_message = workflow_manager.agent_history[-1]
    
    # Extract details for the Excel file
    timestamp = last_message['timestamp']
    date, time_of_day = timestamp.split('T')
    
    # Extract the model names of the agents involved
    models = []
    for agent in config['receiver']['groupchat_config']['agents']:
        model_name = agent['config']['llm_config']['config_list'][0]['model']
        models.append(model_name)
    
    content = last_message['message']['content']
    
    # Function to generate an abbreviation from the task query
    def abbreviate_task(task):
        words = task.split()
        abbreviation = ''.join(word[0].upper() for word in words if word.isalpha())
        return abbreviation
    
    # Generate abbreviation for the task
    task_abbreviation = abbreviate_task(task_query)
    
    # Generate abbreviation for the models
    models_abbreviation = '_'.join(models)
    
    # Extract workflow name and create an abbreviation
    workflow_name = config['name']
    workflow_abbreviation = ''.join(word[0].upper() for word in workflow_name.split() if word.isalpha())
    
    # Define the Excel file path
    excel_file_name = f"{workflow_abbreviation}_{task_abbreviation}_{models_abbreviation}.xlsx"
    excel_file_path = os.path.join(script_dir, excel_file_name)
    
    # Create a DataFrame for the new data
    data = {
        'date': [date],
        'time': [time_of_day],
        'Primary Agent': [models[0]],
        'Assistant Agent': [models[1]],
        'task': [task_query],
        '': [''],  # Blank column
        'content': [content],
        'duration_seconds': [f"{duration_seconds:.2f}"]
    }
    
    df_new = pd.DataFrame(data)
    
    # Write to Excel file
    if os.path.exists(excel_file_path):
        # If file exists, append new data
        with pd.ExcelWriter(excel_file_path, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            df_existing = pd.read_excel(writer, sheet_name='Sheet1')
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_excel(writer, sheet_name='Sheet1', index=False)
    else:
        # If file does not exist, create it with the new data
        with pd.ExcelWriter(excel_file_path, mode='w', engine='openpyxl') as writer:
            df_new.to_excel(writer, sheet_name='Sheet1', index=False)
    
    # Print the agent history
    logger.info("Agent History:")
    for event in workflow_manager.agent_history:
        logger.info(event)
    
    # Confirm the last message was written to Excel
    logger.info(f"Last message written to Excel: {excel_file_path}")

# Run the workflow X times with a Y-second pause between each run
for _ in range(84):
    run_workflow_and_log()
    time.sleep(45)
