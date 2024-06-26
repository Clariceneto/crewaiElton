from crewai import Agent
from crewai_tools import SerperDevTool

def create_task_consultant(person_info):
    search_tool = SerperDevTool()
    
    return Agent(
        role='Task Consultant',
        goal=f'Analyze the provided task and suggest methods, tools, and strategies to complete it for {person_info['name']}, who is a {person_info["profession"]}.',
        verbose=True,
        memory=True,
        backstory = (
            f"You are a consultant specializing in problem-solving and providing practical solutions. "
            f"With access to various tools and resources, you are capable of offering valuable suggestions for any task. "
            f"Your current client is {person_info['name']}, a {person_info['profession']} with skills in {', '.join(person_info['skills'])}, "
            f"responsible for {person_info['responsibility']}, with a skill level of {person_info['skill_level']} and who speaks {person_info['language']}."
        ),
        tools=[search_tool]
    )
