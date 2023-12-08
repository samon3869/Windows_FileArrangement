### 1. 확장자분리하기

```python
# 바닐라 split 사용
filename = "하품하는 고양이.jpeg"

name, extension = filename.split(".")

print("파일 이름: {}".format(name))
print("확장자: {}".format(extension))

# OS 모듈 사용
import os

file = 'codeit.report.pdf'
filename, extension = os.path.splitext(file)
```

### 2. 파이썬 문자열 기능 정리

문자열 합치기 - join()
```python
# syntax: string.join(반복 가능한 객체)

phone_number_segments = ["010", "0000", "1111"]
print("-".join(phone_number_segments)) # 010-0000-1111
```

문자열 바꾸기 - replace()
```python
message = "Codeit은 여러분을 응원합니다. Codeit은 여러분과 함께합니다. 새로운 코딩 교육의 시작, Codeit!"

print(message.replace("Codeit", "코드잇")) 
# "코드잇은 여러분을 응원합니다. 코드잇은 여러분과 함께합니다. 새로운 코딩 교육의 시작, 코드잇!"
```

공백 제거하기 - strip()
```python
# strip은 문자 사이 공백을 제외하고 공백을 제거한다

message = " 새로운 코딩 교육의 시작, 코드잇 "

print(message)
print(message.strip()) # "새로운 코딩 교육의 시작, 코드잇"

# 문자열 중간의 공백을 제거하고 싶다면 replace 사용하기

message = "새로운 코딩 교육의 시작, 코드잇"
remove_whitespace = message.replace(" ", "")

print(remove_whitespace) # 새로운코딩교육의시작,코드잇
```

대문자 소문자 바꾸기 - lower(), upper(), capitalize()

```python
word = "codeIt"

print(word.lower()) # "codeit"
print(word.upper()) # "CODEIT"
print(word.capitalize()) # "Codeit"
```

특정 문자열 위치 찾기 - find()

```python
message = "코드잇 코딩 테스트 합격자: 최지웅, 오종훈, 성소원, 김대위"

print(message.find("오종훈")) # 21
print(message.find("최지웅")) # 16
print(message.find("유재석")) # -1
```

특정 문자열 나오는 횟수 세기 - count()
```python
log = "카드 결제 기록: 코드잇 멤버십 구독, 쇼핑몰, 편의점, 쇼핑몰, 식당, 스트리밍 서비스 구독, 쇼핑몰, 핸드폰 요금"

print(log.count("쇼핑몰")) # 3
print(log.count("콘서트")) # 0
```

특정 문자열 존재하는 지 확인하기 - in 연산자

```python
print("A" in "ABCD") # True
print("ABC" in "ABCD") # True
print("E" in "ABCD") # False

numbers = [2, 3, 5, 7, 11]

print(3 in numbers)
print(10 in numbers)

```

### 3. 문자열로 파일 찾기

```python
# 확장자로 파일 찾기
# endswith(), startswith() 해당 단어로 끝나거나 시작하는 지 확인하여 boolean값 return

filename1 = "file.txt"
filename2 = "photo.png"
str1 = "codeit_report"

print(filename1.endswith(".txt")) # True
print(filename1.endswith(".png")) # False
print(str1.endswith("repot")) # True

print(filename2.startswith("photo")) # True
print(filename2.startswith("file")) # False
print(str1.startswith("codeit")) # True

# 모두 문자로 이루어진 파일 찾기 (영어 한국어 무관)
# isalpha()

text1 = "Codeit"
text2 = "코드잇"
text3 = "코드잇!"
text4 = "내가 좋아서 하는 코딩 공부 코드잇"
text5 = "코드잇123"

print(text1.isalpha())  # True
print(text2.isalpha())  # True
print(text3.isalpha())  # False
print(text4.isalpha())  # False
print(text5.isalpha())  # False

## 모두 숫자로 이루어진 파일찾기
# isdigit()

text1 = "0812"
text2 = "birthday0812"
text3 = "birthday"
text4 = "08 12"

print(text1.isdigit())  # True
print(text2.isdigit())  # False
print(text3.isdigit())  # False
print(text4.isdigit())  # False

# 모두 문자 및 숫자로 이루어진 파일 찾기
# isalnum()

text1 = "100ABC"
text2 = "혼자코딩공부하기좋은서비스1위코드잇"
text3 = "혼자 코딩 공부하기 좋은 서비스 1위 코드잇"
text4 = "5분이면 레슨 완료!"

print(text1.isalnum())  # True
print(text2.isalnum())  # True
print(text3.isalnum())  # False
print(text4.isalnum())  # False

```

### 3. python datetime 모듈 정리
```python
# 1. 기본 객체 생성

import datetime

birthday = datetime.datetime(2020, 3, 14) # datetime 객체 생성
print(birthday) # 2020-03-14 00:00:00

birthday_include_time = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(birthday_include_time) # 2020-03-14 13:06:15

# 2. 현재 시각 객체 생성
now = datetime.datetime.now()

print(now.date()) # 날짜만 추출 2021-06-23
print(now.time()) # 시간만 추출 19:16:07.623483

# 3. 포맷팅 하여 출력

now = datetime.datetime.now()
now_format = now.strftime('%Y/%m/%d %H시 %M분 %S초')

print(now_format)  # 2021/06/23 19시 42분 49초
```

