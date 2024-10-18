# PiAyN

# Definition of agents
- primary agent = Content creator
- sample assistant agent = Reviewer agent

# Definition of agent flow
- primary agent (content creation)
- => sample assistant agent (hallucination identified? + recommendation)
- => primary agent (final output)

# How the Test Results are captured
- Each agent pair's results are logged in an xlxs file in the github folder. The filename contains which agent pair it related to
- All ever workflow results run, are stored in the workflow_log.txt - this let's you review each interaction in highest detail

# How the Test Results are measured
- Each case was also manually reviewed. Specifically the cases where the final output still had a hallucination.
- The "Hallucination Analysis" tab captures the agent pair results at a high level: 
  - "Reviewer Accuracy (%)"	
  - "Reviewer Error Rate (%)"
  - "Primary Correction Rate (%)"

# How the Test Results are visualised
- First matrix "# of test runs" shows the primary agent in the left vertical column, and the assistant agent in the top vertical row
- The second matrix from the top "Reviewing LLM Identified Hallucination" means I measured how many times the assistant agent identified a hallucination in the output of the primary agent. For your information, the primary agent in all cases hallucinated the existence of a Danish artist flipfloppidy.
- The third matrix from the top "Initial LLM Accepted Critique of all Identified Hallucinations " identifies how well the primary agent corrected itself to revise the output and acknowledge that there was a hallucination and the Danish artist flipfloppidy is not real.
- The last matrix shows how fast these interactions were.

# Observations
The observation tab captures observations


# Running the code
1) Add your groq and openAI api keys to .env

2) workflow_Example_of_Hallucination_(Danish_artist_flipflopidy).json is where the workflow is handled. Here you can replace the agents (you can use the agent names mentioned in the [sheet]. The respective base urls are 
- GPT4 models: https://api.openai.com/v1
- Groq models (Mixtral, Gemma, LLama3): https://api.groq.com/openai/v1
- Local model (not used in our case): use LMStudio for that 

3) run_workflow.py is required to cycle through the agent cylces (an agent cycle is what is defined under the section above "Definition of agent flow"). At the end of the run_workflow.py file you can define how many cycley you want to run, and what the time out is between each cycle. Once this file runs, it stores each cycle in an xlxs file (for that specific agent pair) and creates a workflow_log.txt file.

=> If you want to try another task that is not the Danish artist, just change the "task_query" in the run_workflow.py file

4) install the libraries mentioned in the run_workflow.py file
- conda create -n autogen python=3.11
- conda activate autogen
- pip install autogenstudio# PiAyN
