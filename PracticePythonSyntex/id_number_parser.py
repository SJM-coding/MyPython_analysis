Id = '901212-1234567'

birthY = int(Id[:2])
birthm = int(Id[2:4])
birthd = int(Id[4:6])
birthY += 1900


print(f'{birthY}년 {birthm}월 {birthd}일')