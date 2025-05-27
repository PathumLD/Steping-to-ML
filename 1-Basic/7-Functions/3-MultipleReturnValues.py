def analyze_numbers(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

minimum, maximum, average = analyze_numbers([4, 2, 9, 5])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average}")