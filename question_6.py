'''
Question 6 (Dictionaries):
Given a dictionary that maps the string of a job title in a coorperation to a list of employee's
names with that job title, complete people_to_title function so that it returns a new dictionary
maping people's names to a SET of their job title(s).

Any employee could have multiple job titles.

Function must be O(n^2) time complexity at most

Example:
    employee_to_title({'IT': ['Generic Name', 'Ditto']}) -> {'Generic Name': {'IT'}, 'Ditto': {'IT'}}
    employee_to_title({'IT': ['Generic Name', 'Ditto'], 'HR': [Ditto]}) -> {'Generic Name': {'IT'}, 'Ditto': {'IT', 'HR'}}
'''
def employee_to_title(title_to_employee: dict[str, list[str]]) -> dict[str, set[str]]:
    result_dict = dict()
    for job_title in title_to_employee:
        for employee in title_to_employee[job_title]:
            if employee not in result_dict:
                result_dict[employee] = set()
            result_dict[employee].add(job_title)
    return result_dict
