import re
import openpyxl

# python VS java 라는 원본 문자열을 ' VS ' 를 기준으로 분리해보기
pattern = re.compile(" [A-Z]{2} ")
splited = pattern.split("python VS java")
print(splited)
print("\n")

# 801210-1011323 주민번호에서 - 기호를 * 로 바꿔서 출력하기
print(re.sub("-", "*", "801210-1011323"))
print("\n")

# data_kr.xlsx 의 첫번째 시트를 읽어서
# 주민번호 뒷자리를 * 로 바꿔서 출력하기
wb = openpyxl.load_workbook("./regex/data_kr.xlsx")
sheet1 = wb.active
pattern = re.compile("[0-9]{7}")

for row in sheet1.rows:
    # print(row[1].value)
    print(re.sub(pattern, "*******", row[1].value))

# train.xlsx를 읽어서 성별대로 4개의 시트를 만들어 정보 삽입하기
# train_gender.xlsx로 저장
# Mr(sheet 명은 남성), Miss(미혼여성), Mrs(기혼여성), Others(기타)
