import random

import time
import tkinter
import math

from openpyxl import Workbook

def mont(repeat):

    #원 내부인 점 개수
    inCircle = 0

    #원 내부 : 전체 비율
    circleRatio = 0

    #파이 값
    pi = 0

    #repeat번 반복
    for i in range(1, repeat + 1):
        #점 찍기
        px = random.uniform(-1, 1)
        py = random.uniform(-1, 1)


        #원 내부인지 판단
        if px**2 + py**2 < 1:
            inCircle += 1

        #원 안의 점 개수 : 전체 점 개수 계산
        circleRatio = inCircle / i

        #PI = Ratio * 4
        pi = circleRatio * 4

    return pi



# 엑셀파일 쓰기
write_wb = Workbook()
# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('몬테카를로 방법으로 구한 원주율과 실제의 오차')
write_ws['A1'] = '반복 횟수'
write_ws['B1'] = '원주율과의 오차'

#3.1415926535(원주율 소수점 아래 10자리까지와의 오차 비교)
for i in range(1, 1000 + 1):
    error = abs(3.1415926535 - mont(i * 100))
    print(str(i * 100) + " : " + str(error))
    write_ws.append([i * 100, error])


write_wb.save("montecarloError.xlsx")