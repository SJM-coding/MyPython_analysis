time = 12345

hour = time//3600
rest_second = time%3600
minute = rest_second //60
second = time %60

print(f'{time}초는 {hour}시간 {minute}분 {second}초입니다.')