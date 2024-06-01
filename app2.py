from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager
import autogen


config_list = [
    {
        "model" : "local-model",
        "api_type" : "open_ai",
        "base_url" : "http://localhost:1234/v1",
        "api_key" : "not-needed"
    }
]

llm_config={
      "timeout": 120,
      "seed": 42, 
      "config_list": config_list,
      "temperature": 0
}

#PM = autogen.AssistantAgent(
#      name = "Publisher",
#      llm_config = llm_config,
#      system_message = "You are the head of an important news outlet that publishes a journal on AI developments. You coordinate a journalist and a QA to deliver good journalistic work."
#)

coder = autogen.AssistantAgent(
      name="Journalist",
      llm_config=llm_config,
      system_message = "You are a journalist, and you write the world's best articles about AI science topics, but with some bias. You pass your work to the QA."
)

QualityAssurance = autogen.AssistantAgent(
      name = "Quality Assurance",
      llm_config = llm_config,
      system_message = "You are Quality Assurance Expert, and you review the work of the Journalist for bias issues."
)

user_proxy = autogen.UserProxyAgent(
      name = "user_proxy",  
      human_input_mode = "TERMINATE",
      max_consecutive_auto_reply = 3,
      is_termination_msg = lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
      code_execution_config = {"work_dir": "web", "use_docker" : False},
      llm_config = llm_config,
      system_message = """Reply TERMINATE if the task has been solved at full satisfaction and briefly explain what steps were taken.
      Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)


groupchat = GroupChat(
      agents = [user_proxy, coder, QualityAssurance], messages = []
      )

manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)


task = """
Write one paragraph on why AI is great for male humanity.
"""

user_proxy.initiate_chat(
      manager,
      message=task
)