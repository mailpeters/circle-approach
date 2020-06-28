import RPi.GPIO as GPIO
from compassclass import RTCompass
import time

class TankMotion:

    #constructor sets the pin values
    def __init__(self, nLeftin1, nLeftin2, nLeftEN, nRightin1, nRightin2, nRightEN):

        # two motors

        self.Onein1 = nLeftin1
        self.Onein2 = nLeftin2
        self.Oneen = nLeftEN

        self.Twoin1 = nRightin1
        self.Twoin2 = nRightin2
        self.Twoen = nRightEN

        self.nFrequency = 1000    #setting a default

        # 1 is forward, variable keeps track of last direction for the GO method, value set in forward and backward methods
        self.nDirection = 1


    def SetFrequency(self, nFreq):

        self.nFrequency = nFreq

    def Initialize(self):


        #initialize the GPIO with the constructor values

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.Onein1, GPIO.OUT)
        GPIO.setup(self.Onein2, GPIO.OUT)

        GPIO.setup(self.Oneen, GPIO.OUT)
        GPIO.output(self.Onein1, GPIO.LOW)
        GPIO.output(self.Onein2, GPIO.LOW)

        GPIO.setup(self.Twoin1, GPIO.OUT)
        GPIO.setup(self.Twoin2, GPIO.OUT)

        GPIO.setup(self.Twoen, GPIO.OUT)
        GPIO.output(self.Twoin1, GPIO.LOW)
        GPIO.output(self.Twoin2, GPIO.LOW)

        self.nMotor1Speed = GPIO.PWM(self.Oneen, 1000)
        self.nMotor2Speed = GPIO.PWM(self.Twoen, 1000)

        self.nMotor1Speed.start(25)
        self.nMotor2Speed.start(25)
        
        self.Speed("L")

    def Cleanup(self):

        GPIO.cleanup()


    def Go(self):

        if (self.nDirection == 1):
            GPIO.output(self.Onein1, GPIO.HIGH)
            GPIO.output(self.Onein2, GPIO.LOW)

            GPIO.output(self.Twoin1, GPIO.HIGH)
            GPIO.output(self.Twoin2, GPIO.LOW)

        else:
            GPIO.output(self.Onein1, GPIO.LOW)
            GPIO.output(self.Onein2, GPIO.HIGH)

            GPIO.output(self.Twoin1, GPIO.LOW)
            GPIO.output(self.Twoin2, GPIO.HIGH)

    def Stop(self):

        GPIO.output(self.Onein1, GPIO.LOW)
        GPIO.output(self.Onein2, GPIO.LOW)

        GPIO.output(self.Twoin1, GPIO.LOW)
        GPIO.output(self.Twoin2, GPIO.LOW)

    def Forward(self):

        GPIO.output(self.Onein1, GPIO.HIGH)
        GPIO.output(self.Onein2, GPIO.LOW)

        GPIO.output(self.Twoin1, GPIO.HIGH)
        GPIO.output(self.Twoin2, GPIO.LOW)

        self.nDirection = 1

    def Backward(self):

        GPIO.output(self.Onein1, GPIO.LOW)
        GPIO.output(self.Onein2, GPIO.HIGH)

        GPIO.output(self.Twoin1, GPIO.LOW)
        GPIO.output(self.Twoin2, GPIO.HIGH)

        self.nDirection = 0

    def Speed(self, cSpeed):
        #cSpeed = L, M, H
        nSpeedValue = 0
        cSpeed=cSpeed.upper()

        if cSpeed  == 'L':
            nSpeedValue = 25
        elif cSpeed== 'M':
            nSpeedValue = 50
        elif cSpeed == 'H':
            nSpeedValue = 75

        if nSpeedValue > 0:
            self.nMotor1Speed.ChangeDutyCycle(nSpeedValue)
            self.nMotor2Speed.ChangeDutyCycle(nSpeedValue)

    def Spin(self,cDirection):

        cDirection = cDirection.upper()

        if cDirection == 'R':
            GPIO.output(self.Onein1, GPIO.HIGH)
            GPIO.output(self.Onein2, GPIO.LOW)

            GPIO.output(self.Twoin1, GPIO.LOW)
            GPIO.output(self.Twoin2, GPIO.HIGH)

        elif cDirection == 'L':
            GPIO.output(self.Onein1, GPIO.LOW)
            GPIO.output(self.Onein2, GPIO.HIGH)

            GPIO.output(self.Twoin1, GPIO.HIGH)
            GPIO.output(self.Twoin2, GPIO.LOW)
            
            
        
    def SpinToHeading(self,nHeading, Compass):

        cDirection = cDirection.upper()

        if cDirection == 'R':
            GPIO.output(self.Onein1, GPIO.HIGH)
            GPIO.output(self.Onein2, GPIO.LOW)

            GPIO.output(self.Twoin1, GPIO.LOW)
            GPIO.output(self.Twoin2, GPIO.HIGH)

        elif cDirection == 'L':
            GPIO.output(self.Onein1, GPIO.LOW)
            GPIO.output(self.Onein2, GPIO.HIGH)

            GPIO.output(self.Twoin1, GPIO.HIGH)
            GPIO.output(self.Twoin2, GPIO.LOW)
            
            
            
         
    def TinySpin(self,cDirection, nSleep):

        cDirection = cDirection.upper()
        self.Speed("H")

        if cDirection == 'R':
            GPIO.output(self.Onein1, GPIO.HIGH)
            GPIO.output(self.Onein2, GPIO.LOW)

            GPIO.output(self.Twoin1, GPIO.LOW)
            GPIO.output(self.Twoin2, GPIO.HIGH)

        elif cDirection == 'L':
            GPIO.output(self.Onein1, GPIO.LOW)
            GPIO.output(self.Onein2, GPIO.HIGH)

            GPIO.output(self.Twoin1, GPIO.HIGH)
            GPIO.output(self.Twoin2, GPIO.LOW)
            
        time.sleep(nSleep)
        self.Stop()
        
        
            
            
    
    