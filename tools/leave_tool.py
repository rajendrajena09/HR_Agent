import json
from langchain.tools import tool


@tool
def get_leave_balance(employee_name: str):
    """
    Returns the leave balance of an employee.
    """

    with open("data/leave_data.json", "r") as file:
        leave_data = json.load(file)

    for employee in leave_data:
        if employee["name"].lower() == employee_name.lower():
            return {
                "employee": employee["name"],
                "casual_leave": employee["casual_leave"],
                "sick_leave": employee["sick_leave"]
            }

    return {
        "error": f"No leave record found for {employee_name}"
    }
