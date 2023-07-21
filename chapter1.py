# Print welcome message - 1
print("환영합니다!")

question_item_list = ["취존", "솔까말", "케바케"]
answer_list = ["취향존중", "솔직히까놓고말해서", "케이스바이케이스"]

answer_cnt = 0
for question_item, answer in zip(question_item_list, answer_list):
    # Print question and receive user input - 2
    print(f"{question_item}이(가) 어떤 문장의 줄임말인가요?")
    put = input().strip().replace(" ", "")

    # Compare the answer and input - 3
    if put == answer:
        print("정답입니다!")
        answer_cnt += 1
    else:
        print("틀렸습니다!")

# Print the result - 4
print(f"{len(question_item_list)}개 퀴즈 중 {answer_cnt}개 정답!")
