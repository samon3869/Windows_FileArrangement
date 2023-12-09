## 1. 폴더 생성하기

### Difference between os.makedirs() and os.mkdir()

`os.makedirs()` and `os.mkdir()` are both functions in the `os` module in Python that are used to create directories. However, there is a key difference between them:

- `os.makedirs()` can create multiple directories at once, including any intermediate directories that do not exist. It recursively creates all the directories specified in the given path.

- `os.mkdir()` can only create a single directory at a time. If any intermediate directories in the given path do not exist, it will raise an error.

그러면 그냥 makedirs만 사용하면 안되냐구요? 만약 우리가 생성하려는 경로가 잘못된 경로라면 어떻게 될까요? os.makedirs(경로)는 해당 경로가 잘못된 경로라고 하더라도 경로에 해당하는 모든 디렉토리를 생성합니다. 반면에 os.mkdir(경로)는 해당 경로가 존재하지 않는다면 에러를 내고 디렉토리를 생성하지 않겠죠. 그러니까 둘 중에 하나만 사용하면 된다기 보다 구현하려는 로직에 맞게 함수를 사용하는 것이 좋습니다.

## 2. 폴더 삭제하기

### 빈디렉토리 삭제

```python
import os

os.rmdir("test_directory") # test_directory가 비어있지 않다면 삭제가 되지않습니다.
```

### 내용이 있는 디렉토리 삭제 - shutil 모듈사용

```python
import shutil

shutil.rmtree("test_directory")
```
## 3. 폴더 이름변경/이동

```python
# 이름변경
import os

os.rename("test_directory", "data")

# 이동
import os

os.rename("meeting-log/day1", "test_directory")

```

## 4. 폴더 복사

```python
import shutil
shutil.copytree("data", "copy_of_data")
```

## 5. 폴더 압축

```python
import shutil

# 압축
shutil.make_archive("archive", "zip", "data") # shutil.make_archive("생성되는 압축 파일 이름", "zip", "압축 대상 폴더")

# 해제
shutil.unpack_archive("archive.zip", "unpack")

```