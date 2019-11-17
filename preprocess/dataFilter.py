# 추출된 데이터에서 필요한 칼럼들만 따로 추출

import dataCollect
import dataForm
import csv
import datetime
import random

input_file1 = "../data/data1.csv"
input_file2 = "../data/data2.csv"
output_file1 = "../data/data1_filter.csv"
output_file2 = "../data/data2_filter.csv"

selected_column1 = [0,3,4,5,6,7,8,9,16,17,18,23,24,25,26,27,29,30]
selected_column2 = [4,5,6,7,10,11,12,13,14,15,16,17]

# label = "취업"
# "BG" 대기업
# "MS" 중소기업
# "PC"  공기업
# "PU"  공무원
# label = "자격증"
# "IT"  IT분야
# "CK"  요리분야
# "SO"  사회분야
# label = "전공"
# "AZ"  공학계열
# "CO"  인문학계열
# "ID"  자연과학계열
# "MT"  사회계열
# "NE"  상경계열
# "NM"  예체능계열
# label = "어학"
# "EN"  영어
# "JP"  일본어
# "CH"  중국어
# "DE"  독일어
# "ET"  기타언어
# label = "기타"
# "CO"  회화
# "EX"  운동


# "JB" 취업
# "CT" 자격증
# "MJ" 전공
# "LA" 어학
# "AC" 기타

with open(input_file1, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file1, 'w', newline='', encoding="utf-8") as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwriter = csv.writer(csv_out_file)
        next(freader)
        for row_list in freader:
            row_list_output = []
            for index_value in selected_column1:
                if index_value == 4: #생일
                    now = datetime.datetime.now()
                    age = now.year - int((row_list[index_value])[:4])
                    row_list_output.append(age)
                elif index_value == 5: #주소
                    address = (row_list[index_value]).split(" ")
                    row_list_output.append(address[0])
                    row_list_output.append(address[1])
                else:
                    row_list_output.append(row_list[index_value].replace("{","").replace("}",""))
            fwriter.writerow(row_list_output)

with open(input_file2, 'r', newline='', encoding="utf-8") as csv_in_file1:
    with open(output_file2, 'w', newline='', encoding="utf-8") as csv_out_file1:
        freader1 = csv.reader(csv_in_file1)
        fwriter1 = csv.writer(csv_out_file1)
        next(freader1)
        for row_list in freader1:
            row_list_output = []
            for index_value in selected_column2:
                if index_value == 10: #생일
                    now = datetime.datetime.now()
                    age = now.year - int((row_list[index_value])[:4])
                    row_list_output.append(age)
                elif index_value >=13 and index_value <=16:
                    score = dataForm.nlpCal(row_list[index_value])
                    row_list_output.append(score)
                else:
                    row_list_output.append(row_list[index_value].replace("{","").replace("}",""))
            row_list_output.append(round(random.random(), 2))
            fwriter1.writerow(row_list_output)

