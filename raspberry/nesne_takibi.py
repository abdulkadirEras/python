
import RPi.GPIO as GPIO
import numpy as np
import time
import cv2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo=GPIO.PWM(11,50)
def boyutlandirma(kare,yuzde=50):
    genislik=int(kare.shape[1]*yuzde/100)
    yukseklik=int(kare.shape[0]*yuzde/100)
    pikselboyut=(genislik,yukseklik)
    return cv2.resize(kare,pikselboyut,interpolation = cv2.INTER_AREA)


servo.start(0)
def main(): 
    kamera = cv2.VideoCapture(0)
    #kamera.set(3,640)
    #kamera.set(4,480)
    #kamera.set(15,-8.0)
    kamera.set(cv2.CAP_PROP_FPS,15)
    sayac=0 
    while True:

        _,video = kamera.read()
        videohsv=cv2.cvtColor(video,cv2.COLOR_BGR2HSV)
        video=boyutlandirma(video,50)
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
        cv2.imshow("video",video)

        # cv2.imshow("videoharman",videoharman)
        key=cv2.waitKey(1)&0xFF
        if key==ord("q"):
	    kamera.release()
	    cv2.destroyAllWindows()
            return

 
if __name__ == "__main__":
        main()
	servo.stop()
	GPIO.cleanup()
