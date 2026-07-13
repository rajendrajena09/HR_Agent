import json
from langchain.tools import tool


@tool
def get_employee_details(employee_name: str):
    """
    Returns employee information such as manager,
    department and email.
    """

    with open("data/employee_data.json", "r") as file:
        employee_data = json.load(file)

    for employee in employee_data:
        if employee["name"].lower() == employee_name.lower():
            return employee

    return {
        "error": f"No employee found with name '{employee_name}'."
    }