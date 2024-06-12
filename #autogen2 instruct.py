#autogen2 instruct

#conda create -n autogen2 python=3.11
#conda create -n autogen5 python=3.11 (for resilience testing)
#conda info --envs
#_______
# conda activate autogen4
#set GROQ_API_KEY "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"
#set OPENAI_API_KEY "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"
# (WORKFLOW RUN): powershell, navigate to #cd AppData => Local => Anaconda3 => Scripts and conda activate autogen4
#then navigate to cd "C:\Users\alan.aqrawi\OneDrive - Accenture\Documents\Python Scripts\autogen" and python run_workflow.py
#cd "C:\Users\alan.aqrawi\OneDrive - Accenture\Documents\Python Scripts\resilience" and python run_workflow_Fortune.py
#for each specific workflow change the workflow file name in the run_workflow.py file (here: with open("workflow_Example_of_Reasoning_(TEST).json", "r") as f:

#------------------
#conda init bash
#conda activate autogen2

#pip install autogenstudio

#API token: innersource
#PJkOhhMysAKGXKCIkqqywI0ppjL7p424DLs3kB 

# (WORKFLOW RUN): powershell, navigate to #cd AppData => Local => Anaconda3 => Scripts and "conda activate autogen2"
#autogenstudio ui --port 8085

#export OPENAI_API_KEY='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' for GPT4
#export OPENAI_API_KEY='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' for Groq
#GOOGLE API SEARCH KEY= AIzaSyAhKCz3IL60Tw07ux9bBs5pkQnnxeOt4kc
#Custom Search Engine ID (CSE_ID)=80facf90e45194085

#https://www.youtube.com/watch?v=mUEFwUU0IfE
#https://gptpluginz.com/autogen-studio-ui/

#Peter has 3 candles that are all the same. He lights them all at the same time. He blows them out at different points in time. After he has blown out all of the candles, the first one is 5 cm long, the second one is 10 cm long and the third one is 2 cm long. Which one of the three candles did he blow out first? Think step by step.

#LITELLM & AUTOGEN (autogen5)
##pip install litellm
##pip install litellm[proxy]
##pip install aioboto3
#cd "C:\Users\alan.aqrawi\OneDrive - Accenture\Documents\Python Scripts\resilience"
#litellm --config litellm_config.yaml --host 127.0.0.1
# 
# git status
#   17  git add template.env run_workflow_Fortune.py workflow_Example_of_Hallucination_\(Fortune\).json
#  18  git statuts
#   19  git status
#   20  git commit -m "New files to run workflow"
#   21  git push
