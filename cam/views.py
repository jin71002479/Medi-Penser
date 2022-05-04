from datetime import datetime
import PIL
from django.utils import timezone
import os
import threading
import cv2
from django.http.response import StreamingHttpResponse
from django.shortcuts import render,redirect
import numpy as np
from requests import request
import requests
from cam.models import Image,Photo
from PIL import Image


def camera_1(request):
	rows = Photo.objects.all()
	names=[]
	for i in rows:
		names.append(i.names)
	l=len(names)
	return render(request, 'cam/camera.html',{'names':names,'l':l})

def Register(request):
    if request.method == "POST": 
        print(request.POST)
        # number = request.POST.get("number")
        names = request.POST.get("names")

        Photo.objects.create( names=names)  
        return redirect("cam:cap")

    return render(request, "cam/input.html")

directory= os.getcwd()
filePath = directory + '/capture/'
paths=directory+'/dataset/'
trainpath=directory+'/trainer/trainer.yml'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def cap(request):
	rows = Photo.objects.all()
	nums=rows.count()
	cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
	cam.set(3, 640) # set video width
	cam.set(4, 480) # set video height
	face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	path=directory+"/dataset/User."
	# For each person, enter one numeric face id
	face_id = nums

	# Initialize individual sampling face count
	count = 0
	while(True):
		ret, img = cam.read()
		#img = cv2.flip(img, -1) # flip video image vertically
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_detector.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
			count += 1
			# Save the captured image into the datasets folder
			cv2.imwrite(path + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
			cv2.imshow('image', img)
		k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
		if k == 27:
			break
		elif count >= 30: # Take 30 face sample and stop video
			break
	cam.release()
	cv2.destroyAllWindows()

	return redirect('cam:show')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
        img_numpy = np.array(PIL_img,'uint8')
        id = int(os.path.split(imagePath)[-1].split(".")[1])-1
        faces = detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

def md(request):
	faces,ids = getImagesAndLabels(paths)
	recognizer.train(faces, np.array(ids))
	recognizer.write(trainpath)
	recognizer.read(trainpath)
	cascadePath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascadePath)
	font = cv2.FONT_HERSHEY_SIMPLEX

	id = 0
	rows = Photo.objects.all()
	names=[]
	for i in rows:
		names.append(i.names)

	while True:
		cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
		cam.set(3, 640) # set video widht
		cam.set(4, 480) # set video height

	# Define min window size to be recognized as a face
		minW = 0.1*cam.get(3)
		minH = 0.1*cam.get(4)
		ret, img =cam.read()
		img = cv2.flip(img, 1) # Flip vertically
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		
		faces = faceCascade.detectMultiScale( 
			gray,
			scaleFactor = 1.2,
			minNeighbors = 5,
			minSize = (int(minW), int(minH)),
		)

		for(x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
			id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

			if (confidence < 100):
				id = names[id]
				confidence = "  {0}%".format(round(100 - confidence))
			else:
				id = "unknown"
				confidence = "  {0}%".format(round(100 - confidence))
			
			cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
			cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
		cv2.imshow('camera',img) 
		k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
		if k == 27:
			cam.release()
			cv2.destroyAllWindows()
			break
	return redirect('cam:show')

# class VideoCamera(object):
# 	def __init__(self):
# 		self.video = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
# 		(self.grabbed, self.frame) = self.video.read()
# 		threading.Thread(target=self.update, args=()).start()

# 	def __del__(self):
# 		self.video.release()

# 	def get_frame(self):
# 		image = self.frame
# 		ret, jpeg = cv2.imencode('.jpg', image)
# 		return jpeg.tobytes()		

# 	def update(self):
# 		while True:
# 			(self.grabbed, self.frame) = self.video.read()

# 	def take_frame(self):
# 		now = datetime.now()
# 		fileName = filePath + now.strftime('%y%m%d_%H%M%S') + '.png'
# 		print (fileName)
# 		cv2.imwrite(fileName, self.frame)

# 		db = Image(image_name=now.strftime('%y%m%d_%H%M%S'), pub_date=timezone.now())
# 		db.save()




# def gen(camera):
# 	while True:
# 		frame = camera.get_frame()
# 		yield(b'--frame\r\n'
# 			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# def video(request):
#     try:
#         return StreamingHttpResponse(gen(md()), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass



'''
Jetson nano
'''

import Jetson.GPIO as GPIO     # 라즈베리파이 GPIO 관련 모듈을 불러옴
import time                 # 시간 관련 모듈을 불러옴


GPIO.setmode(GPIO.BCM)      # GPIO 핀들의 번호를 지정하는 규칙 설정

servo_pin = 14                   # 서보핀은 라즈베리파이 GPIO 14번핀으로 

GPIO.setup(servo_pin, GPIO.OUT)  # 서보핀을 출력으로 설정 
servo = GPIO.PWM(servo_pin, 50)  # 서보핀을 PWM 모드 50Hz로 사용
servo.start(0)  # 서보모터의 초기값을 0으로 설정

servo_min_duty = 3               # 최소 듀티비를 2으로
servo_max_duty = 12              # 최대 듀티비를 13로
current_deg = 90                 # 현재 각도를 90도로

def set_servo_degree(degree):    # 각도를 입력하면 듀티비를 알아서 설정해주고 서보모터를 움직이는 함수
    # #8.5편에 나온 방법대로 서보모터가 떨리지 않게 함
    # 각도는 최소0, 최대 180으로 설정
    GPIO.setup(servo_pin, GPIO.OUT)         # 모터를 움직여야 하니 서보핀을 출력으로 설정
    past_time = time.time()                 # 과거 시간을 기록
    if degree > 180:                        # 입력받은 각도를 0~180도 사이로 재조정
        degree = 180
    elif degree < 0:
        degree = 0
    duty = servo_min_duty+(degree*(servo_max_duty-servo_min_duty)/180.0)    # 각도를 듀티비로 환산
    # 환산한 듀티비를 서보모터에 전달
    servo.ChangeDutyCycle(duty)             # 해당 각도대로 서보모터를 움직임
    while True:                             # 이부분은 sleep(0.5)와 같음(움직이는 시간동안 대기)
        current_time = time.time()
        if current_time - past_time > 0.5:
            break
    GPIO.setup(servo_pin, GPIO.IN)          # 0.5초간 기다린 후 서보핀을 입력으로 설정(서보모터가 움직이지 않음)
    return degree                           # 입력받은 각도를 출력
    
    
set_servo_degree(current_deg)

def operation(request):                         # 여기서 index4#20.html을 화면에 보여주며, 서보모터 각도를 전달
    return render(request, 'control.html', {'deg' : current_deg, } )  

def servo_control(request):                # 서보모터를 제어하기 위한 뷰함수
    deg = request.args.get('deg')   # html파일에서 각도를 입력받음
    deg = int(deg)                  # 각도를 정수형으로 바꿔주고 적절한 범위로바꿔줌
    if deg < 0: deg = 0
    elif deg > 180: deg = 180
    deg = set_servo_degree(deg)     # 서보모터 각도를 바꿔줌
    # 'control.html'로 돌아가는데, 이때, deg 값을 넘겨줌(이 넘겨준 값은 html에서 사용할 수 있음)
    return render(request ,'control.html', {'deg' : deg, } )