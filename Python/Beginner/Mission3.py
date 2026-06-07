# 1. 연락처 딕셔너리 만들기 (이름: Key, 전화번호: Value)
contacts = {
    "김철수": "010-1234-5678",
    "이영희": "010-9876-5432"
}
print("초기 연락처 목록:", contacts)

# 2. 새로운 연락처 추가하기
contacts["박지성"] = "010-1111-2222"
print("박지성 연락처 추가 후:", contacts)

# 3. 특정 사람의 전화번호 검색하기
search_name = "김철수"
if search_name in contacts:
    print(f"{search_name}의 전화번호: {contacts[search_name]}")
else:
    print(f"{search_name}의 연락처를 찾을 수 없습니다.")

# 4. 기존 연락처 수정하기
contacts["이영희"] = "010-0000-0000"
print("✏이영희 연락처 수정 후:", contacts)