try:
    with open("data.txt") as f:
        content = f.read()
        numbers = [int(n) for n in content.split()]
        print(numbers[10])
except (FileNotFoundError, IndexError) as e:
    print(f"Error occurred: {type(e).__name__} - {e}")