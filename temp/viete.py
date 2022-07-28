#기본 연산 모듈 임포트
from basicCalc import *
#시간측정
import time


def vieteSeries(size):
    #값
    p = add(longDecimal("1"), longDecimal(size))
    #전 항
    a = intDiv(intSqrt(2, size), 2)
    exp = p

    i = 1
    while True:
        #곱하기
        p = mul(p, a)
        
        #점화식 이용해 계산
        a = sqrt(intDiv(add(a, add(longDecimal("1.0"), longDecimal(size))), 2))
        print(str(i) + "번째 항에서 파이값: " + div(add(longDecimal("2"), longDecimal(size)),p).toString())

        #전 항과 현재 항이 같으면 반환
        if comparisonNum(sub(exp, p)):
            return p

        #전 항 갱신
        exp = p
        i+=1



def pi(size):
    return div(add(longDecimal("2"), longDecimal(size)), vieteSeries(size))


def piTime(size):
    start = time.time()
    i = pi(size)
    return time.time() - start

print(pi(10).toString())


#파이 자릿수별로 실행속도 측정
#for i in range(0, 100):
#    print(str(i * 10) + " : " + str(piTime(i * 10)))
