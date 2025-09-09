# 1. 다음 요구사항에 맞는 변수 선언하기
#    1) 정수 5를 저장하는 변수, 
int num = 5

#    2) 실수 2.14를 저장하는 변수, 
float decimal = 2.14

#    3) “Hello”를 저장하는 변수, 숫자의 목록 1,2,3,4를 저장하는 변수, 
char hi = "hello"       # 파이썬에는 char 키워드가 없음. 정답 : hi = "hello"
int num[4] = {1,2,3,4}  # 마찬가지로 배열 타입 선언 필요 없음. 정답 : num = [1,2,3,4]

#    4) 문자열 목록 “Apple”, “Banana”, “Cherry”, “Durian”을 저장하는 변수, 
char fruit[4] = {"Apple", "Banana", "Cherry", "Durian"}
# 파이썬에서는 char나 {} 쓰지않고 []로 적음

#    5) 원주율 3.141592 상수를 저장하는 매크로 변수 혹은 상수형 변수 선언, 
define  pi = 3.141592
# define는 c 스타일 문법 -> 파이썬에서는 동작 안 함. 정답 : PI = 3.141592

#    6) 자신의 이름, 나이, 전화번호로 초기화된 구조체 변수 선언
# 구조체는 c언어에 존재. 파이썬에는 존재하지 않음
#struct information {
#	char name = "이호현";
#	int age = 22
#	char Phone_Number = "01085165474"}
# 따라서 딕셔너리, 클래스를 사용
person = {
    "name": "이호현",
    "age": 22,
    "Phone_Number": "01085165474"
}

class Person:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

me = Person("이호현", 22, "01085165474")
