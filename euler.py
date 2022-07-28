#기본 연산 모듈 임포트
from basicCalc import *
#시간측정
import time
#엑셀 입출력 모듈 임포트
from openpyxl import Workbook

#엑셀파일 쓰기
write_wb = Workbook()
#시트 생성
write_ws = write_wb.create_sheet('오일러 방법의 더해진 항에 따른 원주율과의 오차')
write_ws['A1'] = '더해진 항'
write_ws['B1'] = '원주율과의 오차'

#14자리의 원주율 근삿값(오차 계산에 사용)
_pi = 3.14159265358979

#x의 배수 번째 오차 출력
def eulerSeries(size, x):
    #분모
    nowDeno = 1
    #분모에 더해질 홀수(n^2 = n_Σ_k=1(2k - 1))
    i = 3
    #급수 ㅠ^2 = 6 * ∞_Σ_n(1/n^2) 의 부분합(결과값)
    Sum = 0
    #size회 반복(size개의 항을 더함)
    for n in range(1, size + 1):
        #결과값에 항을 더함
        Sum += 6/nowDeno

        #분모에 2n-1을 더함
        nowDeno += i
        #2n-1에 2를 더함(등차수열의 다음 항)
        i += 2

        #x == false 일 때는 오차를 구하지 않음
        if x != False:
            #x의 배수 번째 항일 때
            if n % x == 0:
                #원주율 = 급수의 제곱근
                p = math.sqrt(Sum)
                #오차 = 14자리 원주율 근삿값 - 계산값
                error = abs(_pi - p)
                #엑셀에 행 추가
                write_ws.append([n, error])
                #결과 출력
                print(str(n) + "번째 항까지의 부분합에서 오차: " + str(error))
                print(str(n) + "번째 항까지의 부분합에서 원주율: " + str(p))

    #size번째 항까지 더한 후 원주율(급수의 제곱근) 반환
    return math.sqrt(Sum)

#원주율 계산 함수
def pi(size):
    #소수점 아래 size자리 까지 계산(10^(size+1)번째 항까지의 부분합)
    return eulerSeries(10**(size + 1), False)

#시간 측정 함수
#isDec == True 이면 size는 소수점 아래 자리수
#isDec == False 이면 size는 부분합의 항 수
def piTime(size, isDec):
    start = time.time()
    if isDec == True:
        pi(size)
    else:
        eulerSeries(size, False)
    return time.time() - start

#소수점 아래 1자리부터 10자리까지 계산 시간 구함
for i in range(1, 10 + 1):
    print(str(i) + "자리: " + str(piTime(i, True)))

#항 수에 따른 오차 데이터를 엑셀로 저장
write_wb.save("eulerError.xlsx")