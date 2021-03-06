#기본 랜덤 모듈 임포트
import random
#그래픽 관련 모듈 임포트
import tkinter
#기본 수학 모듈 임포트
import math

#그래픽 관련 상수들

#캔버스 높이, 너비 설정
cvs_width = 640
cvs_height = 480

#좌표평면 범위 설정
x_range = 2.5
y_range = 1.875 

#좌표평면에서 1스케일의 픽셀
x_scale = cvs_width / (x_range * 2)
y_scale = cvs_height / (y_range * 2)

#윈도우 생성
window = tkinter.Tk()
window.title("MONTECARLO")
window.geometry('800x600')
window.configure()


#캔버스 만들기
cvs = tkinter.Canvas(window, bd=0, bg="black", width=cvs_width, height=cvs_height)
cvs.create_line(0, cvs_height / 2, cvs_width, cvs_height / 2, fill="green", width=1)
cvs.create_line(cvs_width / 2, 0, cvs_width / 2, cvs_height, fill="green", width=1)

#사각형, 원 그리기

#원점 좌표 설정
origin_x = cvs_width / 2
origin_y = cvs_height / 2

#1px당 x좌표는 얼마?
pxPerX = cvs_width / (x_range * 2) 
#1y좌표당 픽셀은 얼마?
pxPerY = cvs_height / (y_range * 2)

#정사각형 그리기
cvs.create_rectangle(origin_x - pxPerX * -1, origin_y - pxPerY * -1, origin_x - pxPerX * 1, origin_y - pxPerY * 1, outline="green", width=1)

#원 그리기
cvs.create_oval(origin_x - pxPerX * -1, origin_y - pxPerY * -1, origin_x - pxPerX * 1, origin_y - pxPerY * 1, outline="green", width=1)

#라벨 만들기
labelEvery = tkinter.Label(window, text="전체 점:", fg="black")
labelCirle = tkinter.Label(window, text="원 내부:", fg="black")
labelRatio = tkinter.Label(window, text="내부/전체:", fg="black")
labelPI = tkinter.Label(window, text="PI:", fg="black")

#x축 눈금(정수 좌표) 
for i in range(int(math.floor(x_range))):
    origin_x = cvs_width / 2
    nowX = ((cvs_width / 2) / x_range) * (i + 1)
    cvs.create_line(origin_x + nowX, cvs_height / 2 + 5, origin_x + nowX, cvs_height / 2 - 5, fill="green", width=1)
    cvs.create_line(origin_x - nowX, cvs_height / 2 + 5, origin_x - nowX, cvs_height / 2 - 5, fill="green", width=1)

#y축 눈금(정수 좌표)
for i in range(int(math.floor(y_range))):
    origin_y = cvs_height / 2
    nowY = ((cvs_height / 2) / y_range) * (i + 1)
    cvs.create_line(cvs_width / 2 + 5, origin_y + nowY, cvs_width / 2 - 5, origin_y + nowY, fill="green", width=1)
    cvs.create_line(cvs_width / 2 + 5, origin_y - nowY, cvs_width / 2 - 5, origin_y - nowY, fill="green", width=1)

#캔버스, 라벨 적용
cvs.pack()
labelEvery.pack()
labelCirle.pack()
labelRatio.pack()
labelPI.pack()


#반복 횟수 입력
repeat = int(input())

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

    #원 외부의 점 색 = 파란색
    color = 'blue'

    #원 내부인지 판단
    if px**2 + py**2 < 1:
        #원 내부 점 수 카운트
        inCircle += 1
        #원 내부의 점 색 = 빨간색
        color = 'red'

    #점의 색깔은 원 안이 빨강, 밖이 파랑
    cvs.create_oval(origin_x - pxPerX * px, origin_y - pxPerY * py, origin_x - pxPerX * px, origin_y - pxPerY * py, outline=color, width=1)
    #캔버스 적용
    cvs.pack()

    #원 안의 점 개수 : 전체 점 개수 계산
    circleRatio = inCircle / i

    #PI = Ratio * 4
    pi = circleRatio * 4


    #라벨 갱신
    labelEvery.configure(text="전체 점: " + str(i))
    labelCirle.configure(text="원 내부: " + str(inCircle))
    labelRatio.configure(text="내부/전체: " + str(circleRatio))
    labelPI.configure(text="PI: " + str(pi))
    labelEvery.pack()
    labelCirle.pack()
    labelRatio.pack()
    labelPI.pack()


#계산된 파이값 출력
print(pi)
#창 자동 닫김 방지
input()