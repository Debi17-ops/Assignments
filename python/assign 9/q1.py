def calculate_stats(*args):
    if not args:
        return None, None, None
    
    minimum = min(args)
    maximum = max(args)
    average = sum(args) / len(args)
    
    return minimum, maximum, average


numbers = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = calculate_stats(*numbers)
print(f"Minimum: {min_val}, Maximum: {max_val}, Average: {avg_val}")
