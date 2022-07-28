#기본 랜덤 모듈 임포트
import random
#엑셀 이불력 모듈 임포트
from openpyxl import Workbook

#몬테카를로법 함수
def mont(repeat):

    #원 내부인 점 개수
    inCircle = 0

    #원 내부 : 전체 비율
    circleRatio = 0

    #파이 값
    pi = 0

    #repeat번 반복
    for i in range(1, repeat + 1):
        #중심이 원점이고 한 변의 길이가 2인 정사각형 내부에 임의의 점 찍기
        px = random.uniform(-1, 1)
        py = random.uniform(-1, 1)

        #원 내부인지 판단
        if px**2 + py**2 < 1:
            #원 내부 점 개수 카운트
            inCircle += 1

        #원 안의 점 개수 : 전체 점 개수 계산
        circleRatio = inCircle / i

        #PI = Ratio * 4
        pi = circleRatio * 4

    #계산된 파이값 반환
    return pi



# 엑셀파일 쓰기
write_wb = Workbook()
# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('몬테카를로 방법으로 구한 원주율과 실제의 오차')
write_ws['A1'] = '반복 횟수(점의 개수)'
write_ws['B1'] = '원주율과의 오차'

#3.1415926535(원주율 소수점 아래 10자리까지와의 오차 비교)
for i in range(1, 1000 + 1):
    #오차 = 원주율 소수점 아래 10자리과 몬테카를로로 구한 원주율의 차의 절댓값
    error = abs(3.1415926535 - mont(i * 100))
    #해당 점 개수에서의 오차 출력
    print(str(i * 100) + " : " + str(error))
    #엑셀 행 추가
    write_ws.append([i * 100, error])

#엑셀 파일 저장
write_wb.save("montecarloError.xlsx")