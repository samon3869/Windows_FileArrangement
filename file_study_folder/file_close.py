# file = open("my_favorite_song.txt", encoding="utf-8")

# for line in file:
#     print(line)

# file.close()

with open("my_favorite_song.txt", encoding="utf-8") as file:
    for line in file:
        print(line)
        
# 파일 닫기 (닫지 않으면 다른 프로그램들이 해당 파일에 접근할 수 없음)