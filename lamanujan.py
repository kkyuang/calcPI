#기본 연산 모듈 임포트
from basicCalc import *
#시간측정
import time
#엑셀 입출력 모듈
from openpyxl import Workbook

#라마누잔 급수 계산
#매개변수: (소숫점 아래 size자리 까지, 더해진 항 반환 여부(True이면 더해진 항(ex. 123) 반환, False이면 구해진 PI 값(ex. 3.14) 반환))
def lamanujanSeries(size, isTerm):
    #라마누잔 급수에서의 n
    n = 0
    #4n
    n4 = 0
    #n!
    nf = 1
    #(4n)!
    n4f = 1

    #2sqrt(2) = sqrt(8)
    sqrt8 = intSqrt(8, size)

    #급수의 부분합 결과값 S_n (=1/ㅠ)
    Sum = longDecimal(size)
    #이전 결과값 S_n-1 (비교해 수렴 여부 판단 위함)
    exSum = Sum
    #수렴할 때까지 무한 반복
    while True:
        #부분합 결과값에 라마누잔 급수의 시그마 내부 값 더하기
        Sum = add(Sum, intDiv(intMul(sqrt8, n4f * ((n * 26390) + 1103)), 9801 * (nf**4) * (396**n4)))

        #S_n과 S_n-1의 값 비교
        if Sum.data == exSum.data:
            #더해진 항 반환
            if isTerm == True:
                print(n)
                return n
            #파이값 반환
            else:
                print(Sum.toString())
                return Sum

        #변수 값 갱신
        n += 1
        nf *= n
        n4 += 4
        n4f *= n4 * (n4 - 1) * (n4 - 2) * (n4 - 3)

        #S_n-1 갱신
        exSum = Sum

#파이 구하기 함수
#매개변수: (소숫점 아래 size자리 까지)
def pi(size):
    #ㅠ = 라마누잔 급수의 역수
    return div(longDecimal('1'), lamanujanSeries(size, False))

#size자리 까지 수렴할 때 더해진 항 구하기 함수
#매개변수: (소숫점 아래 size자리 까지)
def piTerm(size):
    return lamanujanSeries(size, True)

#size자리까지의 파이 계산에 소요되는 시간, 더해진 항 측정
#매개변수: (소숫점 아래 size자리 까지 계산)
#반환값: [소요시간, 더해진 항]
def piTime(size):
    #시작 시간 체크
    start = time.time()
    #size자리까지 구하는 데 더해진 항
    _term = pi(size, True)
    return [time.time() - start, _term]


# 엑셀파일 쓰기
write_wb = Workbook()
# 시트 생성
write_ws = write_wb.create_sheet('라마누잔 공식의 수렴속도')
#행 생성
write_ws['A1'] = '원주율 자릿수'
write_ws['B1'] = '계산 시간'
write_ws['C1'] = '더해진 항'

#파이 자릿수별로 실행속도, 더해진 항 측정
#10자리부터 1000자리까지 10자리 간격으로 측정
for i in range(1, 100 + 1):
    #계산속도, 더해진 항 측정
    t = piTime(i * 10)
    #엑셀에 행 단위로 추가
    write_ws.append([i * 10, t[0], t[1]])
    #결과 터미널에 출력
    print(str(i * 10) + "자리에서 소요시간: " + str(t[0] + ", 더해진 항: " + str(t[1])))

#엑셀 파일로 결과 저장
write_wb.save("lamanujan.xlsx")