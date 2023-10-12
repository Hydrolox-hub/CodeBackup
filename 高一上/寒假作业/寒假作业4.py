score=int(input("请输入百分制成绩(0-100)："))
if score >=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=70:
    grade='C'
elif score>=60:
    grade='D'
else:
    grade='E'
print("五分制成绩：",grade)
