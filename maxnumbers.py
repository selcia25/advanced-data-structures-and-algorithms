import multiprocessing

def max_numbers(numbers):
    return max(numbers)

'''numbers = [23, 45, 12, 67, 89, 34, 56, 78, 91, 21, 43, 65, 87, 98, 32, 54, 76, 99, 11, 33,
           55, 77, 89, 10, 20, 30, 40, 50, 60, 70, 80, 90, 16, 27, 38, 49, 59, 69, 79, 89,
           81, 82, 83, 84, 85, 86, 92, 94, 96, 97, 13]'''
numbers = eval(input("Enter a list of numbers: "))
pool = multiprocessing.Pool()

chunk_size = len(numbers) // multiprocessing.cpu_count()
print(chunk_size)
chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
print(chunks)
result = pool.map(max_numbers, chunks)
print(result)
maximum = max(result)

print(f"The maximum value is {maximum}")
