import random


# Compare the answer and input function - 5
def compare_number(answer, input_num):
    if answer == input_num:
        print("정답!")
        return True
    elif answer < input_num:
        print("다운")
        return False
    else:
        print("업")
        return False


def main():
    random_num = random.randint(1, 20)
    print("Debug", random_num)

    # Process up down game - 2, 3, 4, 6
    for i in range(3):
        # Receive user input - 1
        pred_num = int(input("숫자를 맞춰보세요"))
        if compare_number(random_num, pred_num):
            break
    else:
        print("실패!")


if __name__ == "__main__":
    main()
