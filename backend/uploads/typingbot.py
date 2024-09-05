import time
import random
import pyautogui

def type_text(text, wpm=100):
    # Calculate the average delay between characters
    chars_per_minute = wpm * 5  # Assuming average word length of 5 characters
    avg_delay = 60 / chars_per_minute

    for char in text:
        pyautogui.write(char)
        
        # Add a random variation to the delay for more natural typing
        variation = random.uniform(-0.1, 0.1)
        time.sleep(avg_delay + variation)

def main():
    print("Welcome to the 30 WPM Typing Simulator!")
    print("This script will type the text you enter at approximately 30 WPM.")
    print("Make sure to focus on the application where you want the text to appear.")
    print("Enter the text you want to simulate typing (or 'q' to quit):")
    
    while True:
        user_input = '''
def binary_search_first(arr, n, k):
    left, right = 0, n - 1
    first_occurrence = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == k:
            first_occurrence = mid
            right = mid - 1  # Continue to search in the left half
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return first_occurrence

def binary_search_last(arr, n, k):
    left, right = 0, n - 1
    last_occurrence = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == k:
            last_occurrence = mid
            left = mid + 1  # Continue to search in the right half
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    
    return last_occurrence

def count_occurrences(arr, n, k):
    first_occurrence = binary_search_first(arr, n, k)
    if first_occurrence == -1:
        return 0  # If the first occurrence is not found, K is not in the array
    
    last_occurrence = binary_search_last(arr, n, k)
    return last_occurrence - first_occurrence + 1

def main():
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N, K = map(int, input().strip().split())
        arr = list(map(int, input().strip().split()))
        result = count_occurrences(arr, N, K)
        results.append(result)
    
    for result in results:
        print(result)

'''
        if user_input.lower() == 'q':
            print("Thank you for using the Typing Simulator. Goodbye!")
            break
        
        print("\nPreparing to type. Please focus on your target application.")
        print("Typing will begin in 5 seconds...")
        time.sleep(5)
        
        type_text(user_input)
        print("\nTyping complete.")

if __name__ == "__main__":
    main()