# Python program to convert JSON to Python
import json

# JSON string
employee = '[{"id":"09", "name": "Nitin", "department":"Finance"},' \
    '{"id":"10", "name": "Ravi", "department":"Health"},' \
    '{"id":"11", "name": "Prajwal", "department":"MHA"}]'

# Convert string to Python dict
employee_dict = json.loads(employee)
print(json.dumps(employee_dict, indent=2))

# print(employee_dict['name'])
