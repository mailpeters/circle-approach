import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
 
from tankmotionclass import TankMotion

from rplidar import RPLidar

# 6 meter range on A1 model.
nMaxRange = 6000   
nLidarSpeed = 660

nForwardTolerance = 3           # degrees of forward tolerance, widens if time is too long
nMaxWaitForward = 2             # wait no more than 2 seconds for forward measurement
nGeneralTolerance = .03

cCurrentDirection=""
LOWSPINTIME = .2
HIGHSPINTIME = .5

nCurrentSpinTime = HIGHSPINTIME
nSpinningTolerance = 600 #a percent of the total?  #when spinning to new direction, how much error is allowed?

# 40 cm
nMinimumDrivingDistance = 500
nMinimumQuality = 10

# a set of forward looking distances for the IR
#Positions = [315, 330, 345, 0, 15, 30, 45]

# the tank class for movement
TheTank = TankMotion(24, 23, 25, 5, 6, 13)
TheTank.Initialize()


def largestIndex(arr):
    # Initialize maximum element
    MaxValue = 0
    MaxPosition = 0

    # Traverse array elements from second
    # and compare every element with
    # current max
    for x in range(0, len(arr)):
        current = int(arr[x])
        if arr[x] > MaxValue :
            MaxValue = arr[x]
            MaxPosition=x

    return MaxPosition

# 
# 
# def FillAllDistances(nTolerance) :
#     
#     
#     TheLidar = RPLidar('/dev/ttyUSB0')
# 
#     
#     try:
# 
# 
#         #  GO THRU ALL THE POSITIONS AT ONCE
#         
#    
#         TheLidar.set_pwm(nSpeed)
# 
#        
#         x = 0
#        
#         
# 
#         # curious what is the max in the entire 360 degrees
#         
#         nObservedMax = 0
#         nMaxHeading = -1
# 
#         
#         for measurment in TheLidar.iter_measurments():
#         
#             # are all the distances set already?
#             if ( Distances.count(0) == 0)   :
#                 break
#             else:
# 
#                 for x in range(0, len(Positions)):
#                     
#                     # fill in only the empty ones
#                     if Distances[x] == 0 :
# 
#                         #look at good measurements only
#                         #if (( measurment[1] > 10) and (measurment[3] < nMaxRange)):
#                         if ( measurment[1] > 10):
#                                 
#                             if ((measurment[2] > Positions[x] - nTolerance)  and (measurment[2] < Positions[x] + nTolerance)):
#                                 Distances[x] =  measurment[3]
#                                 Headings[x] = measurment[2]
#                                 #print("range "+str(Distances[x]))
#                                 #break
# 
#     except:
#         print("exception FillAllDistances")
#         raise
#         
#     finally:
#         
#         TheLidar.stop()  
#         TheLidar.disconnect()
#         
        


def GetForwardDistance(nMaxWaitForward) :

    nDistance = -1
    
    global nForwardTolerance
    
    TheLidar = RPLidar('/dev/ttyUSB0')

    try :
            
        TheLidar.set_pwm(nLidarSpeed)
        tStart = time.perf_counter()

        # search or zero bearing (straight ahead)
        for measurment in TheLidar.iter_measurments():

            # apply quality checks
            # if (( measurment[1] > 10) and (measurment[3] < nMaxRange)):
            if ( measurment[1] >= nMinimumQuality) :      
                #print(measurment[2])
                if (measurment[2] > (360-nForwardTolerance)):
                    nDistance =   measurment[3]
                    break
                else:
                    if (measurment[2] < (0+nForwardTolerance)):
                        nDistance =   measurment[3]
                        break
                    
#                 if ((measurment[2] > (360 - nForwardTolerance)) or ((measurment[2] < 0 + nForwardTolerance))):            
#                     nDistance =   measurment[3]
# #                     
#                     if (time.perf_counter()-tStart) < .05  and nForwardTolerance > .5 :
#                         # take opportunity to narrow the range
#                         nForwardTolerance = nForwardTolerance -.01
#                         print("lowering tolerance to:"+str(nForwardTolerance) + " time "+str(time.perf_counter()-tStart))
#                         tStart = time.perf_counter()
#     
        
            #print(time.perf_counter()-tStart)
             
            # widen range  if taking too long
            if (time.perf_counter()-tStart) > nMaxWaitForward :
                nForwardTolerance = nForwardTolerance +1    # add a degree, wider field of view beyond zero
                print("raising tolerance to:"+ str(nForwardTolerance)+ " time "+str(time.perf_counter()-tStart))
                tStart = time.perf_counter()
                
#     
    except:
        print("exception GetForwardDistance ")
        raise
    
    finally :
        TheLidar.stop()
        TheLidar.disconnect()

    return nDistance


#spin to match a set distance
#def TurnToDistance(nDistance, nHeading) :
def TurnToDistance() :
#     cDirection = "L"
#     # go right
#     if nHeading < 180:
#         cDirection = "R"
    global cCurrentDirection
    global nCurrentSpinTime
    global Headings
    global Distances
    

    while(True):
        
        # spin for 1 second at medium speed
        TheTank.TinySpin(cCurrentDirection, nCurrentSpinTime)
        time.sleep(1)
         # new measuremnt?
         
        nReading=0
        while(nReading==0):
            nReading = GetForwardDistance(nMaxWaitForward)
        
        print("spinning "+cCurrentDirection +" current distance "+str(nReading) +" target distance "+ str(Distances[0]) +" heading "+str(Headings[0]) )
        
        if nReading > Distances[0] :
            if nReading - nSpinningTolerance < Distances[0] :
                print(Distances[0], nReading, nSpinningTolerance)
                break
        else:
            if nReading + nSpinningTolerance > Distances[0] :
                print(Distances[0], nReading, nSpinningTolerance)
                break
    
        # if not outof loop
        #check 360 again
        # if there is a new direction, set it and reset the spin time
        Find360Distance(4)
        
        if (Headings[0] > 180 and cCurrentDirection =="R"):
            
            if (nCurrentSpinTime>LOWSPINTIME):
               nCurrentSpinTime=LOWSPINTIME
            else:
               nCurrentSpinTime=nCurrentSpinTime-.05
            cCurrentDirection = "L"
            print("changed to L, slow spin rate:", nCurrentSpinTime)
            
        else:
            if (Headings[0] < 180 and cCurrentDirection =="L"):
                if (nCurrentSpinTime>LOWSPINTIME):
                   nCurrentSpinTime=LOWSPINTIME
                else:
                   nCurrentSpinTime=nCurrentSpinTime-.05

                cCurrentDirection = "R"
                print("changed to R, slow spin rate:", nCurrentSpinTime)
    
        #dont go below zero
        if nCurrentSpinTime < .01:
            print("max slowness, resetting")
            nCurrentSpinTime = LOWSPINTIME
       

def Find360Distance(nTimeToSearch) :

    nDistance = -1
    
    global nForwardTolerance
    
    TheLidar = RPLidar('/dev/ttyUSB0')

    try :
            
        TheLidar.set_pwm(nLidarSpeed)
        tStart = time.perf_counter()
        
        nLongest = 0
        nAngleForLongest = 0
 
        global Distances 
        global Headings
    
    
        for measurment in TheLidar.iter_measurments():
             
            # apply quality checks
            if (( measurment[1] >= nMinimumQuality) ):
                
                if measurment[3] >nLongest:
                    nLongest= measurment[3]
                    nAngleForLongest= measurment[2]
                    #print(nLongest,nAngleForLongest)
                    
                if (time.perf_counter()-tStart) > nTimeToSearch:
                    Distances = [nLongest]
                    Headings =  [nAngleForLongest]
                    print("New longest 360 distance ",nLongest)
                    break
                
    except:
        print("exception GetForwardDistance ")
        raise
    
    finally :
        TheLidar.stop()
        TheLidar.disconnect()




############################################################################################
##   main application
############################################################################################
        
try :
    
    print("start")
    #GetForwardDistance(nMaxWaitForward)
            
    while (1):
                
        print("collecting all new distances, find a new heading")

        # empty distances and headings yet to be set
        Distances = [0,0,0,0,0,0,0]
        Headings =  [-1,-1,-1,-1,-1,-1,-1]
        
        # populates distances and headings
        #FillAllDistances(nGeneralTolerance)
        
        Find360Distance(4)
        
        # the longest heading is new direction    
        nLargestPosition = largestIndex(Distances)
          
        print(Distances)
        print(Headings)

        #turn vehicle to heading for the longest distance
        # turn slowly to the new heading  Headings[nLargestPosition)
        
        #set initial direction and speed for this round
        if Headings[nLargestPosition] < 180:
            cCurrentDirection = "R"
        else:
            cCurrentDirection = "L"
        
        nCurrentSpinTime = HIGHSPINTIME
        
        #TurnToDistance( Distances[nLargestPosition], Headings[nLargestPosition] )
        TurnToDistance()
        
    
        #when close enough distance is found by spinning, start driving forward
        
        print("Driving Distance of " +str(Distances[nLargestPosition]) + " heading " + str(Headings[nLargestPosition]))


        #move forward
        TheTank.Speed("L")
        TheTank.Forward()
 
        #check distances constantly
        # tune to get a reading each second

        while True:
            
            #time.sleep((0.5))
            # tunes inside to get a reading each second
            x = GetForwardDistance(nMaxWaitForward)
            print("Distance to object "+ str(x))
            
          
            if x < nMinimumDrivingDistance :
                print("too close, stop tank")
                TheTank.Stop()
                break


        #too close, then stop and do another loop

        
except KeyboardInterrupt:
   print('interrupted.')
        

except :
 
    print("exeption main loop")
    raise

    
finally :
    TheTank.Stop()
    
    