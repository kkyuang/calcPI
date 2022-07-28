#파이썬 기본 수학 모듈 임포트
import math

#Long Decimal Number Class
#긴 소수 클래스 정의
class longDecimal:
    #클래스 선언 함수
    def __init__(self, input):
        #input의 자료형이 int(정수일 때)
        #inpu 선언(0.0000...)
        #input은 소숫점 n자리까지를 의미(ex input=2 에서 0.00)
        if type(input) == int:
            #자릿수 지정
            #수 배열 설정
            #data[0] = 정수부분
            #data[1] ~ data[n] = 소수부분 (data[k] = 소수점 아래 k번째 자리)
            self.size = input + 1
            self.data = [0 for i in range(0, self.size)]

        #문자열로 선언(ex 2.1213...)
        elif type(input) == str:
            #소숫점이 없을 때
            if input.find('.') == -1:
                #정수부에 입력
                self.data = [int(input)]
                self.size = 1
                return

            #소숫점을 기준으로 정수부분과 소수부분을 나눈다
            intPart = input.split('.')[0] #정수부
            decimalPart = input.split('.')[1] #소수부
            self.size = len(decimalPart) + 1 #size는 정수부 1개, 소수부 숫자 개수만큼

            try:
                #data 변수 초기화
                self.data = [0 for i in range(0, self.size)]
                #data[0]은 정수부분
                self.data[0] = int(intPart)
                #data[1] ~ data[n]은 소수부분
                for i in range(1, self.size):
                    self.data[i] = int(decimalPart[i - 1])
            except:
                print('NaN')

    #문자열로 변환(ex "3.14159")
    def toString(self):
        #정수부와 소숫점 입력
        self.outStr = str(self.data[0]) + '.'
        #소수부 입력
        for i in range(1, self.size):
            self.outStr += str(self.data[i])
        #outStr 반환
        return self.outStr
    #값이 0인지 체크
    def isZero(self):
        #self.data[0]부터 체크하며 0이 아닌 자리가 발견되면 False, 발견되지 않으면 True를 반환한다.
        for i in range(0, len(self.data)):
            if self.data[i] != 0:
                return False
        return True


#수의 크기 비교. a가 더 크거나 같으면 true, b가 더 크면 false를 반환한다.
def comparisonNum(a: longDecimal, b: longDecimal):
    #길이가 더 긴 수의 길이만큼 반복
    for i in range(0, a.size if a.size > b.size else b.size):
        #해당 자릿수에서 a가 더 크다면 True 반환
        if (a.data[i] if i < a.size else 0) > (b.data[i] if i < b.size else 0): #배열 길이를 초과할 때에는 0으로 채움
            return True
        #더 작다면 False 반환
        if (a.data[i] if i < a.size else 0) < (b.data[i] if i < b.size else 0):
            return False
    #a와 b의 길이가 같다면 a==b로 true 반환
    if a.size == b.size:
        return True
    else: #다르다면 a!=b 이므로 false 반환
        return False

#수의 동치 비교. a와 b가 같으면 true, 다르면 false를 반환한다. 길이가 다르면 false를 반환한다.
def isEqualNum(a: longDecimal, b: longDecimal):
    #a와 b의 길이가 다르다면 false 반환
    if a.size != b.size:
        return False
    
    #a의 길이만큼 반복
    for i in range(0, a.size):
        #해당 자릿수가 다르다면 false 반환
        if a.data[i] != b.data[i]: 
            return False

    #이 모든 과정을 통과했다면 합격이다
    return True

#사이즈 같게 맞추기
def sizeEqualize(a: longDecimal, b: longDecimal):
    #더 큰 사이즈에 맞춘다
    #a가 b보다 사이즈가 클 때 b의 배열 길이를 a에 맞추고 b에 새로 추가된 자리를 0으로 채운다.
    if a.size > b.size:
        for i in range(a.size - b.size):
            b.data.append(0)
            b.size = a.size
    #b가 a보다 사이즈가 클 때 a의 배열 길이를 b에 맞추고 a에 새로 추가된 자리를 0으로 채운다.
    elif b.size > a.size:
        for i in range(b.size - a.size):
            a.data.append(0)
            a.size = b.size

#덧셈
def add(a: longDecimal, b: longDecimal):
    #길이 같게 맞추기
    sizeEqualize(a, b)
    #결과 변수 선언
    output = longDecimal(a.size - 1)
    #끝자리 부터 더해간다.
    c = 0 #자리올림수
    for i in range(1, output.size):
        j = output.size - i
        #1의 자리수(10으로 나눈 나머지)
        output.data[j] = int((a.data[j] + b.data[j] + c) % 10) 
        #자리올림수 = 10의 자리수(10으로 나눈 수)
        c = int((a.data[j] + b.data[j] + c) / 10)
    #정수부분
    output.data[0] = a.data[0] + b.data[0] + c
    #결과 반환
    return output

#뺄셈(a - b)
def sub(a: longDecimal, b: longDecimal):
    #b가 더 크면 오류발생
    if comparisonNum(a, b) == False:
        raise Exception('더 큰 수를 뺄 수 없습니다.')

    #길이 같게 맞추기
    sizeEqualize(a, b)
    #결과 변수 선언
    output = longDecimal(a.size - 1)
    #끝자리 부터 빼간다.
    c = 0 #자리내림수
    for i in range(1, output.size):
        j = output.size - i
        #1의 자리수
        if a.data[j] - b.data[j] + c >= 0: #0보다 크거나 같을때
            output.data[j] = int((a.data[j] - b.data[j] + c))
            #자리내림 = 0
            c = 0
        else: #0보다 작을때
            output.data[j] = int((10 + a.data[j] - b.data[j] + c))
            #자리내림 = -1
            c = -1
    #정수부분
    output.data[0] = a.data[0] - b.data[0] + c
    #결과 반환
    return output

#곱셈
def mul(a: longDecimal, b: longDecimal):
    #길이 같게 맞추기
    sizeEqualize(a, b)

    #어느 한쪽이 0일때 0으로 반환
    if a.isZero() == True or b.isZero() == True:
        return longDecimal(a.size - 1)
    
    #곱하는 수 정수 배열로 변환(앞뒤 0 제거 위함)
    b2 = longDecimalTobigInt(b)

    #앞뒤 0 제거 위한 변수
    startP = 0 #앞에서부터 0이 아닌 최초의 자리
    endP = 0 #뒤에서부터 0이 아닌 최초의 자리
    trimCount = 0 #소숫점이 이동한 양, 뒤에서 0 잘린만큼(b2의 길이에서 endP를 뺀 값)

    #앞에서부터 반복해 0이 아닌 수가 발견된 최초의 자리를 startP에 저장
    for i in range(0, len(b2)):
        if b2[i] != 0:
            startP = i
            break
    #뒤에서부터 반복해 0이 아닌 수가 발견된 최초의 자리를 endP에 저장
    for i in range(1, len(b2) + 1):
        if b2[len(b2) - i] != 0:
            endP = len(b2) - i 
            trimCount = i - 1
            break
    
    #b2 변수에 startP와 endP 사이의 숫자 배열을 저장한다.
    b2 = b2[startP:endP+1:1]
    #소숫점 이동한 양
    DPshift = len(b.data) - 1 - trimCount

    #결과
    output = intDiv(intMul(a, bigIntToInt(b2)), 10**DPshift)
    
    #결과값 반환
    return output

#정수배
def intMul(a: longDecimal, b: int):
    #결과 변수 선언
    output = longDecimal(a.size - 1)
    #끝자리 부터 곱해간다.
    c = 0 #자리올림수
    for i in range(1, a.size):
         j = a.size - i
         #1의 자리수(10으로 나눈 나머지)
         output.data[j] = int((a.data[j] * b + c) % 10) 
         #자리올림수 = 10의 자리수(10으로 나눈 수)
         c = int(int(a.data[j] * b + c) // 10)
    #정수부분
    output.data[0] = a.data[0] * b + c
    #결과 반환
    return output

#정수로 나눗셈
def intDiv(a: longDecimal, b:int):
    #결과
    output = longDecimal(a.size - 1)
    
    #0으로 나누기 방지
    if b == 0:
        raise Exception('0으로 나눌 수 없습니다.')
    
    tmp = a.data[0]

    for i in range(0, a.size):
        output.data[i] = int(tmp // b)
        if i < a.size - 1: tmp = (tmp % b) * 10 + a.data[i + 1]
    
    return output

#정수 a의 n번째 자릿수(1의자리 = 0번째)
def NthNumber(a: int, n: int):
    return int((int(a) // int(10**n)) % 10)
    
#longDecimal을 bigInt로 변환
def longDecimalTobigInt(a: longDecimal):
    #정수부의 길이
    if a.data[0] != 0:
        intPartLength = math.floor(math.log(a.data[0], 10)) + 1
        #정수부 bigint 배열
        intPart = [0 for i in range(0, intPartLength)]
        for i in range(0, intPartLength):
            intPart[i] = NthNumber(a.data[0], intPartLength - i - 1)
    else:
        intPart = [0]
    #결과 반환
    return intPart + a.data[1:len(a.data):1]

#int배열을 int로 변환
def bigIntToInt(a):
    output = 0
    for i in range(0, len(a)):
        output += a[i] * 10**(len(a) - i - 1)
    return output
        

#나눗셈
def div(a: longDecimal, b:longDecimal):
    #0으로 나누기 금지
    if b.isZero() == True:
        raise Exception('0으로 나눌 수 없습니다.')

    #길이 같게 맞추기
    sizeEqualize(a, b)
    
    #곱하는 수 정수 배열로 변환(앞뒤 0 제거 위함)
    b2 = longDecimalTobigInt(b)

    #앞뒤 0 제거 위한 변수
    startP = 0 #앞에서부터 0이 아닌 최초의 자리
    endP = 0 #뒤에서부터 0이 아닌 최초의 자리
    trimCount = 0 #소숫점이 이동한 양, 뒤에서 0 잘린만큼(b2의 길이에서 endP를 뺀 값)

    #앞에서부터 반복해 0이 아닌 수가 발견된 최초의 자리를 startP에 저장
    for i in range(0, len(b2)):
        if b2[i] != 0:
            startP = i
            break
    #뒤에서부터 반복해 0이 아닌 수가 발견된 최초의 자리를 endP에 저장
    for i in range(1, len(b2) + 1):
        if b2[len(b2) - i] != 0:
            endP = len(b2) - i 
            trimCount = i - 1
            break
    
    #b2 변수에 startP와 endP 사이의 숫자 배열을 저장한다.
    b2 = b2[startP:endP+1:1]
    #소숫점 이동한 양
    DPshift = len(b.data) - 1 - trimCount

    #결과 계산
    output = intDiv(intMul(a, 10**DPshift), bigIntToInt(b2))
    
    #결과 반환
    return output

#정수 제곱근
def intSqrt(a: int, size:int):
    #소숫점 아래 size자리인 빈 bigDecimal 생성(자리수 맞추기 위함)
    blc = longDecimal(size)
    #첫 값은 루트a
    An = add(blc, longDecimal(str(math.sqrt(a))))

    #이전 결과값
    exAn = An
    #수렴 할 때까지 무한 반복
    while True:
        #바빌로니아 방법 제곱근 계산 사용
        An = intDiv(add(An, (div(add(blc, longDecimal(str(a))), An))), 2)
        #이전 결과값과 비교해서 같으면 반환
        if An.data == exAn.data:
            break
        exAn = An

    return An

#제곱근
def sqrt(a: longDecimal):
    #길이가 a와 같은 빈 bigDecimal 생성(자리수 맞추기 위함)
    blc = longDecimal(a.size - 1)
    #첫 값은 float로 변환 후 루트a(빠르게 수렴하기 위함)
    An = add(blc, longDecimal(str(math.sqrt(bigIntToInt(longDecimalTobigInt(a)) / (a.size - 1)))))
    while True:
        #전후 차이 비교
        d = div(a, An)
        if comparisonNum(An, d):
            s = sub(An, d)
        else:
            s = sub(d, An)
        
        #dif = 연산 전후의 차이
        dif = intDiv(s, 2)

        #바빌로니아법 이용한 연산
        An = intDiv(add(An, (div(a, An))), 2)

        #이전 결과값과 비교해서 같으면 반환(연산 전후 차이가 0이면 반환)
        if dif.isZero() == True:
            return An
