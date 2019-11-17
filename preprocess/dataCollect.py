# 로그 파일로 부터 필요한 데이터 추출

log = open("../data/logsshow.log", 'r', encoding="utf-8")
f = open("../data/data1.csv", "w",encoding="utf-8")
f2 = open("../data/data2.csv", "w",encoding="utf-8")
col = "조회신청,유저아이디,이메일,성별,생년월일,주소,관심사,목표,주최횟수,참여횟수,스터디아이디,제목,소개,모집대상,커리큘럼,코맨트,비용,현재인원,총인원,유형,등록일,데드라인,참여일,장소,도시,세부지역,대분류,중분류,소분류,모임날짜,모임요일,모임시간"
col2 = "유저아이디,스터디아이디,학교,학과,졸업유무,경력횟수,어학개수,자격개수,유저아이디,스터디아이디,생일,평점,프리미엄,목적,목표,자기소개,요청사항,작성소요시간"
f.write(col+"\n")
f2.write(col2+"\n")
while True:
    line = log.readline()
    if "[회원 스터디 클릭]" in line:
        rec = ""
        while "[회원 스터디 클릭 끝]" not in rec:
            data = log.readline()
            if "]" in data:
                rec += data[data.find("]")+2:]
            else:
                rec += data
        f.write(rec.replace("\n", " ").replace("[회원 스터디 클릭 끝]", "").strip())
        f.write("\n")

    if "[스터디 신청 완료]" in line:
        rec = ""
        while "[스터디 신청 완료 끝]" not in rec:
            data = log.readline()
            if "]" in data:
                rec += data[data.find("]")+2:]
            else:
                rec += data
        f.write(rec.replace("\n", " ").replace("[스터디 신청 완료 끝]", "").strip())
        f.write("\n")

    if "[신청서 정보]" in line:
        rec = ""
        while "[신청서 정보 끝]" not in rec:
            data = log.readline()
            if "]" in data:
                if "careernum" in data:
                    rec += data[data.find("]")+2:].split(",")[1].strip()+","
                elif "langnum" in data:
                    rec += data[data.find("]") + 2:].split(",")[1].strip()+","
                elif "certnum" in data:
                    rec += data[data.find("]") + 2:].split(",")[1].strip()+","
                else:
                    rec += data[data.find("]")+2:].strip()+","
            else:
                rec += data
        f2.write(rec.replace("\n", " ").replace("[신청서 정보 끝]", "").strip()[:-2])
        f2.write("\n")
    if not line: break
f.close()
f2.close()
log.close()


