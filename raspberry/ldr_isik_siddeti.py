import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
devreye_giden_pim=7


def rc_zaman(devreye_giden_pim):
	sayac=0
	GPIO.setup(devreye_giden_pim,GPIO.OUT)
	GPIO.output(devreye_giden_pim,GPIO.LOW)
	time.sleep(0.1)
	
	GPIO.setup(devreye_giden_pim,GPIO.IN)
	while (GPIO.input(devreye_giden_pim)==GPIO.LOW):
		sayac+=1
	return sayac
try:
	while True:
		print(rc_zaman(devreye_giden_pim))
		isik_siddeti=rc_zaman(devreye_giden_pim)
		if isik_siddeti>300 and isik_siddeti<400:
			os.system("raspistill -o {}_hedef.jpg".format(isik_siddeti))
		elif isik_siddeti>150 or isik_siddeti<200:
			os.system("raspistill -o {}_hedef.jpg".format(isik_siddeti))
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()

