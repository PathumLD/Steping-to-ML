# Pattern matching example (Python 3.10+)
def analyze_data(data):
    match data:
        case []:
            return "Empty list"
        case [x]:
            return f"Single item: {x}"
        case [x, y]:
            return f"Two items: {x} and {y}"
        case [x, y, *rest]:
            return f"Multiple items starting with: {x}, {y} and {len(rest)} more"
        case {"name": name, "age": age}:
            return f"Person: {name}, {age} years old"
        case _:
            return "Unknown data structure"

print(analyze_data([]))  # Outputs: Empty list
print(analyze_data([1]))  # Outputs: Single item: 1
print(analyze_data([1, 2]))  # Outputs: Two items: 1 and 2
print(analyze_data([1, 2, 3, 4]))  # Outputs: Multiple items starting with: 1, 2 and 2 more
print(analyze_data({"name": "Alice", "age": 25}))  # Outputs: Person: Alice, 25 years old