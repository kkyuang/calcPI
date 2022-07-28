#기본 연산 모듈 임포트
from basicCalc import *
#시간측정
import time
#엑셀 입출력 모듈
from openpyxl import Workbook

#단항 atan 함수
#매개변수: (계수, 변수의 역수, 소수의 길이)
#m atan 1/x
def atan(m, x, size):
    #atan 테일러 급수의 부분합 -> 결과값
    output = longDecimal(size)
    #m값을 longDecimal 형태로 변환
    m2 = longDecimal(str(m))
    #소수 길이 맞추기
    sizeEqualize(output, m2)

    #i번째 항(0부터 시작)
    i = 0
    
    #이전 결과값 S_n-1 (비교해 수렴 여부 판단 위함)
    exOutput = output

    #수렴할 때까지 무한 반복
    while True:
        #i가 짝수일 때
        if i % 2 == 0:
            #짝수번째 항은 음수
            output = add(output, intDiv(m2, (i * 2 + 1) * (x**(i * 2 + 1))))
        else:
            #홀수번째 항은 짝수
            output = sub(output, intDiv(m2, (i * 2 + 1) * (x**(i * 2 + 1))))

        #갱신
        i += 1

        #S_n과 S_n-1의 값 비교해 같으면 수렴
        if output.data == exOutput.data:
            #결과값 반환
            return output

        #S_n 갱신
        exOutput = output


#다항 atan 함수
#sign_1*m_1*atan(1/x_1) + sign_2*m_2*atan(1/x_2) + ...
#매개변수: (list = [[sign_1(부호이고 1 또는 -1), m_1(계수이고 양수), x_1(atan 변수의 역수이고 양수)], [sign_2, m_2, x_2], ...], size = 소숫점 아래 size자리 까지, isTerm = 더해진 항 반환 여부(false이면 구해진 PI값 반환))
def atan(list, size, isTerm):
    #atan 테일러 급수들의 부분합 -> 결과값
    output = longDecimal(size)
    #소숫점 아래 size자리인 0.000... longDecimal
    blc = longDecimal(size)

    #n번째 항(0부터 시작)
    n = 0
    #이전 결과값 S_n-1 (비교해 수렴 여부 판단 위함)
    exOutput = output

    #수렴할 때까지 무한 반복
    while True:
        #list의 항 개수만큼 반복
        for i in range(0, len(list)):
            #짝수번째 항이고 계수가 양수이거나, 홀수번째 항이고 계수가 음수일 때
            if (n % 2 == 0 and list[i][0] == 1) or (n % 2 != 0 and list[i][0] == -1):
                output = add(output, intDiv(add(longDecimal(str(list[i][1])), blc), (n * 2 + 1) * (list[i][2]**(n * 2 + 1))))
            #짝수번째 항이고 계수가 음수이거나, 홀수번째 항이고 계수가 양수일 때
            else:
                output = sub(output, intDiv(add(longDecimal(str(list[i][1])), blc), (n * 2 + 1) * (list[i][2]**(n * 2 + 1))))

        #갱신
        n += 1

        #S_n과 S_n-1의 값 비교해 같으면 수렴
        if output.data == exOutput.data:
            if isTerm == True:
                #소요된 항 반환
                return n
            else:
                #계산 결과(PI값) 반환
                return output

        #S_n-1 값 갱신
        exOutput = output

### #n => n번째 마친 공식 ###

#파이 구하기 함수
#매개변수: (소숫점 아래 size자리 까지)
def pi(size):
    #Term = atan([[1, 4, 2],[1, 4, 3]], size) #1
    #Term = atan([[1, 8, 3],[1, 4, 7]], size) #2
    #Term = atan([[1, 16, 5],[-1, 4, 239]], size) #3
    #Term = atan([[1, 32, 10],[-1, 4, 239],[-1, 16, 515]], size) #4
    Term = atan([[1, 332, 107],[1, 68, 1710],[-1, 88, 103697],[-1, 96, 2513489],[-1, 176, 18280007883],[1, 48, 7939642926390344818],[1, 88, 3054211727257704725384731479018]], size) #5

#size자리까지의 파이 계산에 소요되는 시간, 더해진 항 측정
#매개변수: (소숫점 아래 size자리 까지 계산)
#반환값: [소요시간, 더해진 항]
def piTerm(size):
    start = time.time()
    #Term = atan([[1, 4, 2],[1, 4, 3]], size) #1
    #Term = atan([[1, 8, 3],[1, 4, 7]], size) #2
    #Term = atan([[1, 16, 5],[-1, 4, 239]], size) #3
    #Term = atan([[1, 32, 10],[-1, 4, 239],[-1, 16, 515]], size) #4
    Term = atan([[1, 332, 107],[1, 68, 1710],[-1, 88, 103697],[-1, 96, 2513489],[-1, 176, 18280007883],[1, 48, 7939642926390344818],[1, 88, 3054211727257704725384731479018]], size) #5
    return [Term, time.time() - start]


#size자리 까지 수렴할 때 소요된 시간 구하기 함수
#매개변수: (소숫점 아래 size자리 까지)
def piTime(size):
    start = time.time()
    i = pi(size)
    return time.time() - start

# 엑셀파일 쓰기
write_wb = Workbook()
# 이름이 있는 시트를 생성
write_ws = write_wb.create_sheet('마친 공식의 수렴속도')
#행 생성
write_ws['A1'] = '원주율 자릿수'
write_ws['B1'] = '더해진 항'
write_ws['C1'] = '소요 시간'

#파이 자릿수별로 실행속도 측정 
for i in range(1, 100 + 1):
    #계산속도 측정
    x = piTerm(i * 10)
    #더해진 항
    term = x[0]
    #소요된 시간
    tm = x[1]
    #행 단위로 추가
    write_ws.append([i * 10, term, tm])
    #결과값 터미널에 출력
    print(str(i * 10) + "자리: " + " : " + str(term) + "항, " + str(tm) + "초 소요")

#엑셀 파일로 저장
write_wb.save("machin5.xlsx")