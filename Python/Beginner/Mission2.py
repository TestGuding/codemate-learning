# 1. 할 일(To-do) 목록 리스트 만들기 (초기화)
todo_list = ["파이썬 문법 복습하기", "이메일 확인하기"]
print("초기 할 일 목록:", todo_list)

# 2. 새로운 항목 추가하기 (append)
todo_list.append("알고리즘 문제 풀기")
print("항목 추가 후:", todo_list)

# 3. 완료된 항목 삭제하기 (remove)
# '이메일 확인하기'를 완료했다고 가정하고 삭제합니다.
completed_task = "이메일 확인하기"

# 삭제하려는 항목이 리스트에 있는지 확인 후 안전하게 삭제
if completed_task in todo_list:
    todo_list.remove(completed_task)

print("완료된 항목 삭제 후:", todo_list)