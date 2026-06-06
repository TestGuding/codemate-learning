# 1. 변수 선언
menu_name = "아이스 아메리카노"
price = 4500
tax = 450  # 10% 세금 가정

# 2. 합계 계산
total = price + tax

# 3. 영수증 형태로 깔끔하게 출력
print("--- 영수증 ---")
print(f"메뉴: {menu_name}")
print(f"가격: {price:,}원")
print(f"세금: {tax:,}원")
print("--------------")
print(f"합계: {total:,}원")