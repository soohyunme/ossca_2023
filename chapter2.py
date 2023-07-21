import random


# Compare the answer and input function - 5
def compare_number(answer, input):
    if answer == input:
        print("정답!")
        return True
    elif answer < input:
        print("다운")
        return False
    else:
        print("업")
        return False


random_num = random.randint(1, 20)

# Print welcome message - 1
print("숫자를 맞춰보세요")

# Process up down game - 2, 3, 4, 6
for i in range(3):
    # Receive user input - 1
    pred_num = int(input())
    if compare_number(random_num, pred_num):
        break
else:
    print("실패!")
