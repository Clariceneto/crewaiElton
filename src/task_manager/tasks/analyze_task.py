from crewai import Task

def create_analyze_task(agent, task_description, language):
    if language == 'português' or language == 'portugues':
        description = (
            f"Analise a seguinte tarefa: {task_description}. "
            "Forneça um plano detalhado com métodos, ferramentas e estratégias para completá-la. "
            "Inclua também uma lista de ferramentas necessárias para a execução da tarefa. "
            "Além disso, liste os documentos relacionados que podem ser úteis para completar a tarefa. "
            "Considere todos os aspectos necessários, como planejamento, execução e recursos. "
            "Por fim, verifique se a pessoa-alvo compreendeu a tarefa, pedindo para ela repetir os principais pontos."
        )
        expected_output = 'Um plano detalhado com sugestões de ferramentas e métodos para completar a tarefa, uma lista de documentos relacionados e uma verificação de compreensão da tarefa.'
    elif language == 'espanhol':
        description = (
            f"Analiza la siguiente tarea: {task_description}. "
            "Proporcione un plan detallado con métodos, herramientas y estrategias para completarla. "
            "Incluya también una lista de herramientas necesarias para la ejecución de la tarea. "
            "Además, enumere los documentos relacionados que pueden ser útiles para completar la tarea. "
            "Considere todos los aspectos necesarios, como planificación, ejecución y recursos. "
            "Finalmente, verifique si la persona objetivo comprendió la tarea, pidiéndole que repita los puntos principales."
        )
        expected_output = 'Un plan detallado con sugerencias de herramientas y métodos para completar la tarea, una lista de documentos relacionados y una verificación de comprensión de la tarea.'
    elif language == 'chinês' or language == 'chines':
        description = (
            f"分析以下任务: {task_description}. "
            "提供详细的计划，包括完成任务的方法、工具和策略。 "
            "还要包括执行任务所需的工具清单。 "
            "此外，列出可能有助于完成任务的相关文件。 "
            "考虑所有必要的方面，如计划、执行和资源。 "
            "最后，请确认目标人物是否理解任务，要求他们重复主要要点。"
        )
        expected_output = '提供详细的计划，包括完成任务的方法、工具和策略，相关文件列表，并确认任务的理解。'
    else:  # Default to English
        description = (
            f"Analyze the following task: {task_description}. "
            "Provide a detailed plan with methods, tools, and strategies to complete it. "
            "Also include a list of necessary tools for task execution. "
            "Additionally, list related documents that may be useful for completing the task. "
            "Consider all necessary aspects such as planning, execution, and resources. "
            "Finally, verify if the target person understood the task by asking them to repeat the main points."
        )
        expected_output = 'A detailed plan with suggestions of tools and methods to complete the task, a list of related documents, and a comprehension verification of the task.'
    
    return Task(
        description=description,
        expected_output=expected_output,
        tools=agent.tools,
        agent=agent,
    )
