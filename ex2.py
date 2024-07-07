from collections import deque

def is_palindrome(input_string):
    # Очищення рядка від пробілів та приведення до нижнього регістру
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Додавання символів до двосторонньої черги
    char_deque = deque(cleaned_string)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    
    return True

# Тестування функції
test_strings = [
    "A man a plan a canal Panama",
    "No lemon, no melon",
    "Hello, World!",
    "Was it a car or a cat I saw",
    "Not a palindrome"
]

for test_string in test_strings:
    result = is_palindrome(test_string)
    print(f"'{test_string}' is a palindrome: {result}")
