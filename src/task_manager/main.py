import json
from task_manager.crew import create_crew

def main():
    # Solicitar a descrição da tarefa ao usuário
    task_description = input("Task description:: ")

    # Solicitar informações da pessoa-alvo
    person_info = {
    "name": input("Name: "),
    "skills": input("Person's skills (separated by commas): ").split(','),
    "profession": input("Person's profession: "),
    "responsibility": input("Person's responsibility: "),
    "skill_level": input("Skill level: "),
    "language": input("Language: ")
}


    result = create_crew(task_description, person_info)
    
    # Exibir as informações da pessoa-alvo e o resultado
    print("\nPerson's Information:")
    for key, value in person_info.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\nTask Description:")
    print(task_description)
    
    print("\nResult of Task Analysis :")
    print(result)

    # Verificação de compreensão da tarefa
    comprehension_check = input("Did you understand the task?Please describe the main points: ")
    print(f"\n Task Understanding Check: {comprehension_check}")

    # Salvar os dados em um arquivo JSON
    output_data = {
        "person_info": person_info,
        "task_description": task_description,
        "task_analysis": result,
        "comprehension_check": comprehension_check
    }

    with open('task_analysis_output.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()