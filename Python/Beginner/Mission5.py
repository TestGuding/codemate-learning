# 1. 사용자로부터 영문 문장 입력 받기
sentence = input("영문 문장을 입력하세요: ")

# 2. 모음 개수를 저장할 카운터 변수와 모음 모음집 준비
vowel_count = 0
vowels = "aeiouAEIOU"  # 대문자 입력까지 고려한 센스 있는 처리!

# 3. 반복문을 돌며 문장을 한 글자씩 검사
for char in sentence:
    if char in vowels:
        vowel_count += 1  # 모음을 발견할 때마다 1씩 증가

# 4. 최종 결과 출력
print(f"입력하신 문장에 포함된 모음의 총 개수는 {vowel_count}개입니다.")