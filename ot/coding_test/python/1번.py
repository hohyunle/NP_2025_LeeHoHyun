# 1. “나는 OOO입니다” 형태로 나를 소개하는 함수를 작성하고 호출하여 실행되는 프로그램을 작성하기
print("나는 이호현입니다")

def print_name():
    print("나는 ", name, "입니다")

name = input("이름을 입력하세요: ")
print_name()

# 개선된 코드
def print_name(name):           # 전역 변수 의존 제거
    print(f"나는 {name}입니다") # f-string 사용으로 깔끔한 출력 → "나는 홍길동입니다" 형태 유지.

name = input("이름을 입력하세요: ")
print_name(name)
