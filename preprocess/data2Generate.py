import csv
import random

input_file = "../data/data2_filter.csv"
output_file = "../data/data2_generate.csv"

with open(input_file, 'r', newline='', encoding="utf-8") as csv_in_file:
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_out_file:
        freader = csv.reader(csv_in_file)
        fwriter = csv.writer(csv_out_file)
        #next(freader)
        #졸업,1,1,1,29,0.0,1,0.5,1.0,0.5,0.5,4000,0.38
        for row_list in freader:
            for i in range(1000):
                row_list_output = []
                for i in range(len(row_list)):
                    if i == 0: # 학적
                        l = ["0", "1", "0", "1", "2"]
                        row_list_output.append(l[random.randint(0,4)])
                    elif i >= 1 and i <=3: # 스팩 갯수
                        mrand = random.randint(-1,1)
                        if int(row_list[i]) +mrand <=0:
                            row_list_output.append(int(row_list[i]))
                        else:
                            row_list_output.append(int(row_list[i]) +mrand)
                    elif i ==4:
                        rand = random.randint(-2,2)
                        row_list_output.append(int(row_list[i]) + rand)
                    elif i ==5:
                        rand = round(random.uniform(0, 5),1)
                        row_list_output.append(rand)
                    elif i ==6:
                        rand = random.randint(0,1)
                        row_list_output.append(rand)
                    elif i >=7 and i<=10:
                        rand = random.randint(-3,3)
                        rand = rand + 0.5
                        if float(row_list[i]) + rand <= 0:
                            row_list_output.append(float(row_list[i]))
                        else:
                            row_list_output.append(float(row_list[i]) + rand)
                    elif i == 11:
                        rand = random.randrange(-3000,3000, 1000)
                        if float(row_list[i]) + rand <= 0:
                            row_list_output.append(int(row_list[i]))
                        else:
                            row_list_output.append(int(row_list[i]) + rand)
                    elif i ==12:
                        rand = round(random.uniform(-0.1,0.2),2)
                        if float(row_list[i]) + rand <= 0:
                            row_list_output.append(float(row_list[i]))
                        elif float(row_list[i]) + rand > 1:
                            row_list_output.append(float(row_list[i]))
                        else:
                            row_list_output.append(round(float(row_list[i]) + rand,2))
                fwriter.writerow(row_list_output)