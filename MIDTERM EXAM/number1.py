def is_palindrome(value):
    value_str = str(value)
    reversed_str = "".join(reversed(value_str))
    return value_str == reversed_str

with open("numbers.txt", "r") as file:
    content = file.readlines()

line_number = 1
for line in content:
    num_list = [int(num) for num in line.split(',') if num.strip().isdigit()]
    
    if num_list:
        total_sum = sum(num_list)
        status = "This sum is a palindrome." if is_palindrome(total_sum) else "This sum is not a palindrome."
        formatted_nums = ", ".join(map(str, num_list))
        
        print(f"Line {line_number}: {formatted_nums} (Sum: {total_sum}) - {status}")
    
    line_number += 1
