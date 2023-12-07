import os
import datetime

def timestamp_to_time(timestamp):
    return datetime.datetime.fromtimestamp(timestamp)

creattime = os.path.getctime("cat.jpeg")
modifytime = os.path.getmtime("cat.jpeg")
accesstime = os.path.getatime("cat.jpeg")

print(
    "만든날짜 Time Stamp(1980년 1월 1일부터 지난 시각을 초로 환산한 것): {}"
    .format(creattime))

print(
    "만든날짜 표준단위로 변환한 시간: {}".format(timestamp_to_time(creattime))
    + "\n"
    + "수정날짜 표준단위로 변환한 시간: {}".format(timestamp_to_time(modifytime))
    + "\n"
    + "액세스한 날짜 표준단위로 변환한 시간: {}".format(timestamp_to_time(accesstime)))
