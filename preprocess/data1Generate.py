import csv
import random
from itertools import combinations as cb

input_file = "../data/data1_filter.csv"
output_file = "../data/data1_generate.csv"
#
# def comb(lst):
#     l = []
#     for i in range(1,4):
#         t = list(cb(lst, i))
#         l.append(t)
#     print(l)
#

interest = ["BG","MS","PC","PU","IT","CK","SO","AZ","CO","ID","MT","NE", "NM", "EN", "JP", "CH","DE", "ET","EX"]
goal = ["JB", "CT", "MJ", "LA"," AC"]
cat = ["대기업 자소서", "대기업 인적성", "대기업 면접"
,"공기업 자소서"
,"공기업 NCS"
,"공기업 면접"
,"중소기업 자소서"
,"중소기업 면접"
,"공무원 7급"
,"공무원 9급"
,"공무원 5급"
,"컴퓨터 정보처리기사"
,"컴퓨터 정보보안기사"
,"컴퓨터 컴퓨터활용능력"
,"컴퓨터 리눅스마스터"
,"사회 사회조사분석사"
,"요리 한식조리기사"
,"요리 일식조리기사"
,"요리 양식조리기사"
,"사회 유통관리사"
,"사회 한국사능력검정시험"
,"영어 TOEIC"
,"영어 OPIC"
,"영어 SAT"
,"영어 TOEFL"
,"일본어 JPLT"
,"일본어 JPT"
,"중국어 HSK"
,"독일어 ZD"
,"공학 기계공학"
,"공학 컴퓨터공학"
,"공학 화학공학"
,"공학 환경공학"
,"공학 로봇공학"
,"공학 생명공학"
,"인문 국어국문학"
,"인문 철학"
,"인문 사학"
,"인문 유학"
,"인문 중어중문학"
,"사회 심리학"
,"사회 통계학"
,"사회 사회학"
,"사회 커뮤니케이션학"
,"자연과학 물리학"
,"자연과학 수학"
,"자연과학 생물학"
,"자연과학 지구과학"
,"회화 영어회화"
,"운동 웨이트"
,"운동 조깅"]

loc = ["강남"
,"홍대"
,"신촌"
,"종로"
,"신사"
,"목동"
,"잠실"
,"양재"
,"사당"
,"노원"
,"은평"
,"혜화"
,"성수"
,"인사동"
,"고양"
,"서면"
,"송도"
,"건대"
,"신림"
,"마포"
,"성북"
,"영등포"
,"용산"
,"왕십리"
,"구로"
,"동작"
,"수유"
,"회기"
,"충무로"
,"미아"
,"청량리"
,"강서"
,"수원"
,"고양"
,"분당"
,"의정부"
,"송도"
,"구월동"
,"부평"
,"대전역"
,"중앙"
,"서면"
,"부경대"
,"해운대"
,"남포"
,"구미"
,"울산대"]

# intercomb = comb(interest)
# goalcomb = comb(goal)

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwriter = csv.writer(csv_out_file)
        #next(freader)
        #0.5,여,29,경기,고양시,BG@IT@AZ,JB,2,2,남포,한국사능력검정시험,6@
        #[0.5,1.0],[남,여],[20~29],조합,[0~3],[0~3],상세지역랜덤,소분류랜덤,요일랜덤(조합)
        for row_list in freader:
            for i in range(1000):
                row_list_output = []
                for i in range(len(row_list)):
                    if i == 0: # 신청, 조회
                        l = [0.5, 0.5, 1.0]
                        row_list_output.append(l[random.randint(0,2)])
                    elif i == 1: # 남여
                        mrand = random.randint(0,1)
                        row_list_output.append(mrand)
                    elif i == 2: # 나이
                        mrand = random.randint(20, 29)
                        row_list_output.append(mrand)
                    elif i == 3:
                        r = random.randint(0, len(interest) - 1)
                        row_list_output.append(r)
                    elif i ==4:
                        r = random.randint(0,len(goal)-1)
                        row_list_output.append(r)
                    elif i ==5 or i == 6:
                        l = [0,0,0,1,1,2,3]
                        r = random.randint(0,6)
                        row_list_output.append(l[r])
                    elif i ==7:
                        r = random.randint(0,len(cat)-1)
                        row_list_output.append(r)
                    elif i ==8:
                        r = random.randint(0,len(loc)-1)
                        row_list_output.append(r)
                    elif i ==9: #평일, 주말, 둘다
                        r = random.randint(0,2)
                        row_list_output.append(r)
                fwriter.writerow(row_list_output)