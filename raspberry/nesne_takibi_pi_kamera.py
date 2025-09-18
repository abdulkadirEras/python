from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import numpy as np
import time
import cv2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
servo=GPIO.PWM(11,50)
servosag=GPIO.PWM(13,50)
servosol=GPIO.PWM(15,50)

servo.start(0)
servosag.start(0)
servosol.start(0)
def main(): 
    kamera = PiCamera()
    kamera.resolution=(640,480)
    kamera.framerate=32
    rawCapture=PiRGBArray(kamera,size=(640,480))
    #kamera.set(3,640)
    #kamera.set(4,480)
    #kamera.set(15,-8.0)
    ##kamera.set(cv2.CAP_PROP_FPS,15)
    sayac=0
    time.sleep(0.1) 
    for cerceve in kamera.capture_continuous(rawCapture,format="bgr",use_video_port=True):

        video=cerceve.array
        videohsv=cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
        videoharmandusuk=cv2.inRange(videohsv,np.array([0,135,135]),np.array([18,255,255]))
        videoharmanyuksek=cv2.inRange(videohsv,np.array([165,135,135]),np.array([179,255,255]))
 
        videoharman=cv2.add(videoharmandusuk,videoharmanyuksek)
 
        videoharman=cv2.GaussianBlur(videoharman,(3,3),2)
 
        videoharman = cv2.dilate(videoharman,np.ones((5,5),np.uint8))
        videoharman = cv2.erode(videoharman,np.ones((5,5),np.uint8))
 
        satirlar,sutunlar = videoharman.shape
 
        daireler = cv2.HoughCircles(videoharman,cv2.HOUGH_GRADIENT,5,satirlar/4,minRadius=50,maxRadius=60) 
        cv2.line(video,(320,230),(320,250),(255,0,0),2)
        cv2.line(video,(310,240),(330,240),(255,0,0),2)
        if daireler is not None:
            for daire in daireler[0]:
                x,y,yaricap=daire
                cv2.circle(video,(x,y),3,(0,255,0),-1)
                cv2.circle(video,(x,y),yaricap,(0,0,255),3)
        	cv2.line(video,(320,240),(x,y),(0,255,0),1)
        
            if (x<325 and x>315) and (y<245 and y>235) :
           	 sayac+=1
            if sayac==1:
                print("hedef pozisyonu: x= "+str(x)+" ,y= "+str(y)+"yaricap= "+str(yaricap))
                
            elif sayac==2 or sayac==3:
                servo.ChangeDutyCycle(2+(180/18))
                cv2.putText(video,"bomba atildi",(300,300),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),2)
                time.sleep(0.5)
                servo.ChangeDutyCycle(0)
                time.sleep(1)
                servo.ChangeDutyCycle(2)
                time.sleep(0.5)
                servo.ChangeDutyCycle(0)
            else:
                sayac=0
       	    if x>380:
           	 servosol.ChangeDutyCycle(2+(45/18))
		 time.sleep(0.1)
            	 servosol.ChangeDutyCycle(0)
	    elif x>325:
		 servosol.ChangeDutyCycle(2+(20/18))
		 time.sleep(0.1)
		 servosol.ChangeDutyCycle(0)
            else:
            	servosol.ChangeDutyCycle(2)
            	time.sleep(0.1)
            	servosol.ChangeDutyCycle(0)
            if x<260:
            	servosag.ChangeDutyCycle(2+(45/18))
            	time.sleep(0.1)
            	servosag.ChangeDutyCycle(0)
            elif x<315:
		servosag.ChangeDutyCycle(2+(20/18))
		time.sleep(0.1)
		servosag.ChangeDutyCycle(0)
	    else:
            	servosag.ChangeDutyCycle(2)
            	time.sleep(0.1)
            	servosag.ChangeDutyCycle(0)
        cv2.imshow("video",video)
   	rawCapture.truncate(0)
        # cv2.imshow("videoharman",videoharman)
        key=cv2.waitKey(1)&0xFF
        if key==ord("q"):
            return

 
if __name__ == "__main__":
    main()
    servo.stop()
    GPIO.cleanup()

