kg = int(input("체중(kg): "))
cm = int(input("키(cm): "))
cm = cm/100
BMI = round(kg/(cm*cm),1)

print(f'BMI:{BMI}')