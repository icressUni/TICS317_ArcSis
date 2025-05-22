import json
from datetime import datetime
def create_repo_json(document_route: str, author: str) -> None:
    """
    Creates a JSON file with an empty list of tasks.

    Args:
        document_route (str): The path where the JSON file will be created.
    """
    try:
        # Create an empty list to represent tasks
        repo = {"author": author, "tasks": {}}

        # Write the empty list to the specified JSON file
        with open(document_route, 'x') as file:
            json.dump(repo, file, indent=4)

    except Exception as e:
        raise RuntimeError(f"An error occurred while creating the JSON file: {e}")
    
def generate_task_json(task_id: int, task_name: str, task_description: str, start_date: datetime, end_date: datetime, task_dependencies: set, task_owners: set) -> str:
    """
    Generates a JSON-formatted string representing a task.

    Args:
        task_id (int): The unique identifier for the task.
        task_name (str): The name of the task.
        task_description (str): A description of the task.
        start_date (datetime): The start date of the task.
        task_dependencies (set): A set of task IDs that this task depends on.
        task_owners (set): A set of owners responsible for the task.

    Returns:
        str: A JSON-formatted string representing the task.
    """
    task_data = {
        "task_id": task_id,
        "task_name": task_name,
        "task_description": task_description,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "task_dependencies": list(task_dependencies),
        "task_owners": list(task_owners)
    }
    
    return json.dumps(task_data, indent=4)

def update_task_json(task_id: int, updated_attributes: dict, document_route: str) -> str:
    """
    Updates the attributes of a task in a JSON file and returns the updated JSON as a formatted string.

    Args:
        task_id (int): The unique identifier of the task to update.
        updated_attributes (dict): A dictionary containing the attributes to update.
        document_route (str): The path to the JSON file containing the tasks.

    Returns:
        str: A JSON-formatted string representing the updated tasks.
    """
    try:
        # Load the existing tasks from the JSON file
        with open(document_route, 'r') as file:
            tasks = json.load(file)

        # Find the task with the matching task_id and update its attributes
        task_found = False
        for task in tasks:
            if task.get("task_id") == task_id:
                task.update(updated_attributes)
                task_found = True
                break

        if not task_found:
            raise ValueError(f"Task with task_id {task_id} not found.")

        # Save the updated tasks back to the JSON file
        with open(document_route, 'w') as file:
            json.dump(tasks, file, indent=4)

        # Return the updated tasks as a JSON-formatted string
        return json.dumps(tasks, indent=4)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {document_route} was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file at {document_route} is not a valid JSON file.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

def delete_task_json(task_id: int):
    """
    Deletes a task from the JSON file.

    Args:
        task_id (int): The unique identifier of the task to delete.
    """
    try:
        # Load the existing tasks from the JSON file
        with open("TEST_tasks.json", 'r') as file:
            tasks = json.load(file)

        # Find and remove the task with the matching task_id
        tasks = [task for task in tasks if task.get("task_id") != task_id]

        # Save the updated tasks back to the JSON file
        with open("TEST_tasks.json", 'w') as file:
            json.dump(tasks, file, indent=4)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at TEST_tasks.json was not found.")
    except json.JSONDecodeError:
        raise ValueError(f"The file at TEST_tasks.json is not a valid JSON file.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

date1 = datetime(2023, 10, 1, 14, 30, 0)  # October 1, 2023, 14:30:00
date2 = datetime(2023, 10, 15, 9, 15, 0) # October 15, 2023, 09:15:00
task0 = generate_task_json(1, "test0", "this is a task description for Test0", date1, date2, (), ())
create_repo_json("TEST_tasks.json", "test_author")

#print(task0)
#update_task_json()
#print("holaaa")