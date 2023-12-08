os.path.isdir()
os.path.isfile()
### 1. 경로 접근법

구분기호는 '\\'를 사용한다.

```python
# codeit 디렉토리 안에 있는 codeit_report.txt 파일

path = 'codeit/codeit_report.txt' # macOS/Linux/Unix
path = 'codeit\\codeit_report.txt' # windows
```

 ``사실 windows의 경로 구분 기호는 \ 입니다. 하지만 \ 다음 특정 문자가 오게 되면 그것을 \n 같은 이스케이프 문자로 처리할 수 있기 때문에 \\ 로 적어주는 것이 안전한 코딩 방법입니다. 실제로 경로를 \ 적은 것과 \\ 로 적은 것을 print 해보면 모두 \ 로 경로가 구분 되어 있는 것을 볼 수 있습니다.``

절대경로 알아내기

```python
import os

print(os.path.abspath("filename.txt")
```

운영체제와 관계없이 경로에 접근 - os.path.sep

```python
import os

# 기본 접근법
print(os.path.sep) # window라면 '\'가 출력되고, macOS라면 '/'가 출력됩니다.

# 추가팁1. 파일, 디렉토리 여부 확인 os.path.isdir() os.path.isfile()


# 추가팁2. 경로 검증 os.path.exists()
    # 없는 경로일경우 에러나는것을 피하기 위함

import os
import shutil

path = "데이터 사이언스.png"

if os.path.exists(path): # 데이터 사이언스.png 파일이 없기 때문에
    shutil.copy(path, "데이터 사이언스 심화.png") # 이 코드가 실행되지 않습니다.
```

### 2. 경로 작성법

운영체제와 관계없이 경로 작성 - os.path.join

```python
import os

file_path = os.path.join('Users', 'Codeit', 'cat.jpg')

print(file_path)

# windows
    # Users\Codeit\cat.jpg 
# macOS
    # Users/Codeit/cat.jpg 
```

### 3. 파일 이동하기

```python
# 방법1. 이름이 곧 파일경로임을 알면 rename으로 파일 이동이 가능함도 알게 되지

import os

os.rename("codeit_news.txt", "news/2021_codeit.txt")

# 방법2. shutil.move 이용

import shutil
shutil.move("codeit_news.txt", "news/2021_codeit.txt")

# 주의점 같은 이름의 파일이 있는 경우 덮어쓰기 되므로 안정장치 마련하기
import os
if not os.path.exists("Hello_kor.txt"):
    os.rename("Hello_eng.txt", "Hello_kor.txt")
```

``
자, 그러면 os.rename과 shutil.move는 어떤 차이점이 있을까요? 가장 큰 차이점은 os.rename이 실패할 수 있는 작업을 shutil.move는 성공적으로 할 수 있다는 것입니다. 예를 들어 우리가 이동하려는 위치가 현재 내가 있는 C 드라이브가 아닌 D 드라이브, 즉 다른 드라이브에 있을 수도 있고, 아니면 파일 시스템이 다를 수도 있습니다. 여기서 파일 시스템이란 운영 체제가 파일을 다루는 기본 형식을 말하는데, 윈도우라면 NTFS, FAT32등의 형식입니다. 한 번쯤 보신 적이 있으시죠? 만약 파일 시스템에 대해 더 자세히 알고 싶다면 다음 링크를 참조해보세요. 파일 시스템(위키백과)
``
https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%BC_%EC%8B%9C%EC%8A%A4%ED%85%9C

``
자, 이렇게 이동하려는 곳이 특수한 상황일때 os.rename은 파일 이동을 실패할 수 도 있지만 shutil.move는 실패하지 않습니다. 왜냐하면 shutil.move는 복사하려는 대상이 같은 파일 시스템인지 여부를 확인하고 만약 동일한 파일시스템이라면 파일 이동을, 다른 시스템이라면 먼저 대상 위치로 파일을 복사하고 그다음에 원본 파일을 지우는 방식이 적용되어 있기 때문입니다.
``

### 4. 폴더 살펴보기

현재 폴더 살펴 보기

```python
import os

# data 디렉토리 안의 내용을 문자열로 이루어된 리스트로 모두 가져옵니다.
contents = os.listdir("data")  

print(contents) # <class: list> [ 모든 파일 또는 디렉토리 ]
```

깊숙히 들어가며 모든 폴더 살펴보기

```python
import os

for path, dirs, files in os.walk("/"):
    print("Path: {}".format(path))
    print("Folders: {}".format(dirs))
    print("Files: {}".format(files))
    print("-----")
```