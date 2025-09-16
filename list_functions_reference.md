# Python 리스트 함수 참조표

| 함수명      | 사용 방법             | 설명                                       |
| :---------- | :-------------------- | :----------------------------------------- |
| del()       | del(List[pos])        | List에서 pos 위치의 항목 삭제              |
| len()       | len(List)             | List 항목의 전체 개수를 센다               |
| sorted()    | newList = sorted(List) | List 항목을 정렬해 newList 만듬            |
| append()    | List.append(val)      | List 맨 뒤에 val 항목 추가                 |
| clear()     | List.clear()          | List의 내용을 지움                         |
| copy()      | newList = List.copy() | List의 내용을 newList에 복사               |
| count()     | List.count(val)       | List에서 val 값의 갯수를 센다              |
| extend()    | List.extend(newList)  | List 뒤에 newList를 추가                   |
| index()     | List.index(val)       | val을 찾아 해당 첨자 반환                  |
| insert()    | List.insert(pos, val) | List의 pos 위치에 val 삽입                 |
| pop()       | List.pop()            | List 맨 뒤에서 항목 삭제                   |
| remove()    | List.remove(val)      | List에서 val 값 항목 삭제(여러 개면 첫번째만) |
| reverse()   | List.reverse()        | List 항목을 뒤집어 역순으로 만듬           |
| sort()      | List.sort()           | List 항목을 정렬                           |

## 사용 예시

### 기본 리스트 생성
```python
my_list = [1, 2, 3, 4, 5]
```

### 함수 사용 예시
```python
# append() - 항목 추가
my_list.append(6)  # [1, 2, 3, 4, 5, 6]

# insert() - 특정 위치에 삽입
my_list.insert(0, 0)  # [0, 1, 2, 3, 4, 5, 6]

# remove() - 값으로 삭제
my_list.remove(3)  # [0, 1, 2, 4, 5, 6]

# pop() - 마지막 항목 삭제
last_item = my_list.pop()  # last_item = 6, my_list = [0, 1, 2, 4, 5]

# sort() - 정렬
my_list.sort()  # [0, 1, 2, 4, 5]

# reverse() - 역순
my_list.reverse()  # [5, 4, 2, 1, 0]

# len() - 길이 확인
length = len(my_list)  # length = 5

# count() - 특정 값 개수
count = my_list.count(1)  # count = 1

# index() - 값의 위치 찾기
position = my_list.index(4)  # position = 1
```
