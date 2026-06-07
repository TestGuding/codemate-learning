import random

# 1. 사용자 입력 받기
user_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")

# 2. 컴퓨터의 선택 (랜덤)
choices = ["가위", "바위", "보"]
computer_choice = random.choice(choices)

print(f"나의 선택: {user_choice}")
print(f"컴퓨터의 선택: {computer_choice}")

# 3. 조건문을 활용한 승패 판별 로직
if user_choice == computer_choice:
    print("결과: 무승부입니다!")
elif (user_choice == "가위" and computer_choice == "보") or \
     (user_choice == "바위" and computer_choice == "가위") or \
     (user_choice == "보" and computer_choice == "바위"):
    print("결과: 승리했습니다!")
elif user_choice not in choices:
    print("결과: 잘못된 입력입니다. '가위', '바위', '보'만 입력해주세요.")
else:
    print("결과: 패배했습니다.")