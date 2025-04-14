   
string1 = input(" ")
check_cond1 = False
check_cond2 = False

# 조건1: @ 기호 포함 여부
for i in string1:
    if i == '@':
        check_cond1 = True

# 조건2: 도메인이 .com (거꾸로 보면 'moc.')
if string1[-4:] == '.com':
    check_cond2 = True

# 결과 출력
if check_cond1 and check_cond2:
    print(f'이메일주소: {string1}\n유효함')
else:
    print(f'이메일주소: {string1}\n유효하지 않음')
