from datetime import datetime
from django.utils import timezone
import os
import threading
import cv2
from django.http.response import StreamingHttpResponse
from django.shortcuts import render
from cam.models import Image

directory= os.getcwd()

filePath = directory + '/capture/'

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		(self.grabbed, self.frame) = self.video.read()
		threading.Thread(target=self.update, args=()).start()

	def __del__(self):
		self.video.release()

	def get_frame(self):
		image = self.frame
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()		

	def update(self):
		while True:
			(self.grabbed, self.frame) = self.video.read()

	def take_frame(self):
		now = datetime.now()
		fileName = filePath + now.strftime('%y%m%d_%H%M%S') + '.png'
		print (fileName)
		cv2.imwrite(fileName, self.frame)

		db = Image(image_name=now.strftime('%y%m%d_%H%M%S'), pub_date=timezone.now())
		db.save()



cam = VideoCamera()

def gen(camera):
	while True:
		frame = cam.get_frame()
		yield(b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video(request):
    try:
        return StreamingHttpResponse(gen(()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass

def camera_1(request):
	if request.method == 'POST':
		cam.take_frame()

	return render(request, 'cam/camera.html')