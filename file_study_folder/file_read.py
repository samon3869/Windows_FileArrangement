file = open("my_favorite_song.txt", encoding="utf-8")

# 1번째 줄 읽기
print(file.readline())
# 2번째 줄 읽기
print(file.readline())
# 3번째 줄부터 끝까지 읽기
print(file.read())

# 커서 처음으로 가져와서 1째줄부터 끝까지 읽기
file.seek(0)
print("\n커서 처음으로 가져와서 1째줄부터 끝까지 읽기\n")
print(file.read())

# 파일 내용 한줄 씩 리스트에 담기
print("\n파일 내용 한줄씩 리스트에 담아서 출력\n")
file.seek(0)
print(file.readlines())

# 파일 내용 한줄 씩 끊어서 출력하기
print("\n파일 내용 한줄 씩 끊어서 출력하기\n")
file.seek(0)
for line in file:
    print(line)
