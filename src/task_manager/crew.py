
from crewai import Crew, Process
from task_manager.agents.task_consultant import create_task_consultant
from task_manager.tasks.analyze_task import create_analyze_task
from task_manager.utils.setup import setup_environment,translate_text

def create_crew(task_description, person_info):
    setup_environment()
    consultor_de_tarefas = create_task_consultant(person_info)
    analisar_tarefa = create_analyze_task(consultor_de_tarefas, task_description, person_info['language'].lower())
    
    crew = Crew(
        agents=[consultor_de_tarefas],
        tasks=[analisar_tarefa],
        process=Process.sequential
    )
    
    result = crew.kickoff(inputs={'task_description': task_description, 'person_info': person_info})
    
    return result