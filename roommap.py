
# !/usr/bin/env python3
'''Records measurments to a given file. Usage example:
$ ./record_measurments.py out.txt'''
#import sys

import time
import math

import pygame

from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'

lidar = RPLidar(PORT_NAME)
lidar.set_pwm(500)


# Simple pygame program


def FillCircleArray(_Array, nRadius, nStart, nEnd ):

    # for every collected reading, calculate and record all the positions on a circle from that position, return the array for processing
    # the radius is the current distance reading from vehicle to a point at 0,90,180 or 270

    for nIteration in range(len(nAngleFromOrigin)):

        #for nIteration in range(4):
        # find the adjusted x,y for the center of each circle
# 
#         x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
#         y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
# 
#         # postive x positive y
#         if (nAngleFromOrigin[nIteration] <= 90):
#             # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust - int(y * nScaleDown))), 5)
#             xStart = int(x * nScaleDown) + nXAdjust
#             yStart = nYAdjust - int(y * nScaleDown)
# 
#         elif (nAngleFromOrigin[nIteration] <= 180):
#             # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust + int(y * nScaleDown))), 5)
# 
#             xStart = int(x * nScaleDown) + nXAdjust
#             yStart = nYAdjust + int(y * nScaleDown)
# 
# 
#         elif (nAngleFromOrigin[nIteration] <= 270):
#             # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # pygame.draw.circle(screen, (0, 0, 255), ((nXAdjust - int(x * nScaleDown), nYAdjust + int(y * nScaleDown))), 5)
# 
#             xStart = nXAdjust - int(x * nScaleDown)
#             yStart = nYAdjust + int(y * nScaleDown)
# 
#         else:
#             # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
#             # pygame.draw.circle(screen, (0, 0, 255), (nXAdjust - int(x * nScaleDown), nYAdjust - int(y * nScaleDown)), 5)
#             xStart = nXAdjust - int(x * nScaleDown)
#             yStart = nYAdjust - int(y * nScaleDown)


        # using the adjusted starting postion, find adjusted circle location
        c = nStart

        xStart = nXPositions[nIteration]
        yStart = nYPositions[nIteration]
        
        #for c in range(nStart,nEnd):
        while( c <= nEnd ):
            #print(c)

            r = nRadius-1
            while(r <= nRadius+1) :
            
                y = abs(nRadius * math.cos((math.pi / 180) * c))
                x = abs(nRadius * math.sin((math.pi / 180) * c))

                if c <= 90:
                    if not ((int(x * nScaleDown) + xStart, yStart - int(y * nScaleDown)) in _Array ):
                        _Array.append((int(x * nScaleDown) + xStart, yStart - int(y * nScaleDown)))

                elif c <= 180:
                    if not ( (int(x * nScaleDown) + xStart, yStart + int(y * nScaleDown))  in _Array):
                        _Array.append( (int(x * nScaleDown) + xStart, yStart + int(y * nScaleDown)))


                elif c <= 270:
                    if not ((xStart - int(x * nScaleDown), yStart + int(y * nScaleDown)) in _Array) :
                        _Array.append(  (xStart - int(x * nScaleDown), yStart + int(y * nScaleDown)))

                else:
                    if not ((xStart - int(x * nScaleDown), yStart - int(y * nScaleDown)) in _Array) :
                        _Array.append(  (xStart - int(x * nScaleDown), yStart - int(y * nScaleDown)))

                r=r+1
                
            c=c+1


        #
        # #for c in range(nStart,nEnd):
        # while( c <= nEnd ):
        #     #print(c)
        #
        #     y = abs(nRadius * math.cos((math.pi / 180) * c))
        #     x = abs(nRadius * math.sin((math.pi / 180) * c))
        #
        #     if c <= 90:
        #         _Array.append( (nIteration, (int(x * nScaleDown) + xStart, yStart - int(y * nScaleDown))))
        #         #pygame.draw.circle(screen, (0, 0, 255), (int(x * nScaleDown) + xStart, yStart - int(y * nScaleDown)) , 5)
        #
        #     elif c <= 180:
        #         _Array.append( (nIteration, (int(x * nScaleDown) + xStart, yStart + int(y * nScaleDown))))
        #         #pygame.draw.circle(screen, (0, 0, 255), (int(x * nScaleDown) + xStart, yStart + int(y * nScaleDown)) , 5)
        #
        #     elif c <= 270:
        #         _Array.append(  (nIteration, (xStart - int(x * nScaleDown), yStart + int(y * nScaleDown))))
        #         #pygame.draw.circle(screen, (0, 0, 255), ( xStart - int(x * nScaleDown), yStart + int(y * nScaleDown)) , 5)
        #
        #     else:
        #         _Array.append( (nIteration, (xStart - int(x * nScaleDown), yStart - int(y * nScaleDown))))
        #         #pygame.draw.circle(screen, (0, 0, 255),  (xStart - int(x * nScaleDown), yStart - int(y * nScaleDown)) , 5)
        #
        #     c=c+1

    return _Array



def PrintCircle(nradius, nIteration) :

    try:

        x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
        y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))

        # postive x positive y
        if (nAngleFromOrigin[nIteration] < 90):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            #pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust - int(y * nScaleDown))), 5)
            xStart = int(x * nScaleDown) + nXAdjust
            yStart = nYAdjust - int(y * nScaleDown)

        elif (nAngleFromOrigin[nIteration] < 180):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            #pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust + int(y * nScaleDown))), 5)

            xStart = int(x * nScaleDown) + nXAdjust
            yStart = nYAdjust + int(y * nScaleDown)


        elif (nAngleFromOrigin[nIteration] < 270):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            #pygame.draw.circle(screen, (0, 0, 255), ((nXAdjust - int(x * nScaleDown), nYAdjust + int(y * nScaleDown))), 5)

            xStart = nXAdjust - int(x * nScaleDown)
            yStart =  nYAdjust + int(y * nScaleDown)

        else:
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            #pygame.draw.circle(screen, (0, 0, 255), (nXAdjust - int(x * nScaleDown), nYAdjust - int(y * nScaleDown)), 5)
            xStart = nXAdjust - int(x * nScaleDown)
            yStart = nYAdjust - int(y * nScaleDown)


        c=0
        for c in range(360) :
            y = abs(nradius * math.cos((math.pi / 180)*c))
            x = abs(nradius * math.sin((math.pi / 180)*c))

            if c < 90:
                pygame.draw.circle(screen, (100, 150, 50), (( int( x * nScaleDown) + xStart, yStart - int(y * nScaleDown))), 1)
            elif c < 180:
                pygame.draw.circle(screen, (100, 150, 50), (( int( x * nScaleDown) + xStart, yStart + int(y * nScaleDown))), 1)
            elif c < 270:
                pygame.draw.circle(screen, (100, 150, 50), (( xStart - int( x * nScaleDown), yStart + int(y * nScaleDown))), 1)
            else:
                pygame.draw.circle(screen, (100, 150, 50), (( xStart - int( x * nScaleDown) , yStart - int(y * nScaleDown))), 1)

            #pygame.display.flip()
            #print(c, x,y)

        # circle center
        pygame.draw.circle(screen, (200, 50, 150), (xStart, yStart ), 10)

        print("circle print xstart, ystart", xStart,yStart )

    finally:
        print("radius, iteration ",nradius, nIteration)
        pygame.display.flip()

def PaintMeasures() :

        pygame.draw.circle(screen, (110, 110, 255), (nXAdjust, nYAdjust), 10)
        text_surface = font.render( str(0), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust ))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust+ int(1000 * nScaleDown) ), 5)
        text_surface = font.render(str(-1000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust+int(1000*nScaleDown) ))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(2000 * nScaleDown)), 5)
        text_surface = font.render(str(-2000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(2000 * nScaleDown)))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(3000 * nScaleDown)), 5)
        text_surface = font.render( str(-3000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(3000 * nScaleDown)))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(4000 * nScaleDown)), 5)
        text_surface = font.render(str(-4000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(4000 * nScaleDown)))


        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(-1000 * nScaleDown)), 5)
        text_surface = font.render(str(1000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(-1000 * nScaleDown)))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(-2000 * nScaleDown)), 5)
        text_surface = font.render(str(2000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(-2000 * nScaleDown)))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(-3000 * nScaleDown)), 5)
        text_surface = font.render(str(3000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(-3000 * nScaleDown)))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust, nYAdjust + int(-4000 * nScaleDown)), 5)
        text_surface = font.render(str(4000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust, nYAdjust + int(-4000 * nScaleDown)))



        pygame.draw.circle(screen, (0, 0, 255), ( nXAdjust + int(nScaleDown*1000), nYAdjust), 5)
        text_surface = font.render(str(1000), True, (0, 0, 0))
        screen.blit(text_surface, ( nXAdjust + int(nScaleDown*1000) , nYAdjust) )

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * 2000), nYAdjust), 5)
        text_surface = font.render(str(2000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * 2000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * 3000), nYAdjust), 5)
        text_surface = font.render(str(3000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * 3000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * 4000), nYAdjust), 5)
        text_surface = font.render(str(4000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * 4000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * 5000), nYAdjust), 5)
        text_surface = font.render(str(5000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * 5000), nYAdjust))


        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * -1000), nYAdjust), 5)
        text_surface = font.render(str(-1000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * -1000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * -2000), nYAdjust), 5)
        text_surface = font.render(str(-2000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * -2000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * -3000), nYAdjust), 5)
        text_surface = font.render(str(-3000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * -3000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * -4000), nYAdjust), 5)
        text_surface = font.render(str(-4000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * -4000), nYAdjust))

        pygame.draw.circle(screen, (0, 0, 255), (nXAdjust + int(nScaleDown * -5000), nYAdjust), 5)
        text_surface = font.render(str(-5000), True, (0, 0, 0))
        screen.blit(text_surface, (nXAdjust + int(nScaleDown * -5000), nYAdjust))

        pygame.display.flip()


def RefreshMap():

    # grid values
    PaintMeasures()

    for nIteration in range(len(nAngleFromOrigin)):

        x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
        y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))

        # y = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
        # x = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))

        # postive x positive y
        if (nAngleFromOrigin[nIteration]  >= 0 and nAngleFromOrigin[nIteration]< 90):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust - int(y * nScaleDown))), 5)

        elif (nAngleFromOrigin[nIteration]>= 90 and nAngleFromOrigin[nIteration]< 180):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust + int(y * nScaleDown))), 5)

        elif (nAngleFromOrigin[nIteration]>= 180 and nAngleFromOrigin[nIteration]< 270):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            pygame.draw.circle(screen, (0, 0, 255), ((nXAdjust - int(x * nScaleDown), nYAdjust + int(y * nScaleDown))), 5)

        elif (nAngleFromOrigin[nIteration]>= 270 and nAngleFromOrigin[nIteration]< 360):
            # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
            # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
            pygame.draw.circle(screen, (0, 0, 255), (nXAdjust - int(x * nScaleDown), nYAdjust - int(y * nScaleDown)), 5)

    pygame.display.flip()

'''Main function'''


# Import and initialize the pygame library

# for scanning values
nMinRange = 200
nMaxRange = 6000

#for the painted grid
nXAdjust = 250
nYAdjust = 250
nScaleDown = .08

# percentage
nMapCoverage = .7


    
    
def LidarLoadArrays()  :
    
    print('Recording measurments... Press Crl+C to stop.')


    nFound =0
    nTries =0
   
    for measurment in lidar.iter_measurments():

        #convert angle and distance to x and y

        if measurment[1] == 15 and  measurment[3] < nMaxRange and measurment[3] > nMinRange :
            #finding the 2 missing legs given a hypotenuse(distance) and angle in degrees from the lidar

            #  569.371   664.411    875.000    8.562
            # correct???   130, 865, 875 at 8.562

            #see if you have covered enough of the map
            if round(measurment[2],3) in nAngleFromOrigin :
                nFound = nFound +1
                nIndexFound = nAngleFromOrigin.index(round(measurment[2],3))
                #print("angle/distance/original dist/% found, array size: ", measurment[2], measurment[3], nDistancefromOrigin[nIndexFound],(nFound/nTries)*100, len(nAngleFromOrigin))

            else:
                nAngleFromOrigin.append(round(measurment[2],3))
                nDistancefromOrigin.append(int(measurment[3]))

                # storing negatives

                x = round(measurment[3] * math.sin((math.pi/180)*measurment[2]),0)
                y = round(measurment[3] * math.cos((math.pi/180)*measurment[2]),0)

                #                 nXPositions.append(x)
                #                 nYPositions.append(y)
                
                #save    
                #x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
                #y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))

                # postive x positive y
                if (measurment[2]<= 90):
                    # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust - int(y * nScaleDown))), 5)
                    xStart = int(x * nScaleDown) + nXAdjust
                    yStart = nYAdjust - int(y * nScaleDown)

                elif (measurment[2] <= 180):
                    # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # pygame.draw.circle(screen, (0, 0, 255), ((int(x * nScaleDown) + nXAdjust, nYAdjust + int(y * nScaleDown))), 5)

                    xStart = int(x * nScaleDown) + nXAdjust
                    yStart = nYAdjust + int(y * nScaleDown)


                elif (measurment[2]<= 270):
                    # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # pygame.draw.circle(screen, (0, 0, 255), ((nXAdjust - int(x * nScaleDown), nYAdjust + int(y * nScaleDown))), 5)

                    xStart = nXAdjust - int(x * nScaleDown)
                    yStart = nYAdjust + int(y * nScaleDown)

                else:
                    # x = abs(nDistancefromOrigin[nIteration] * math.sin((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # y = abs(nDistancefromOrigin[nIteration] * math.cos((math.pi / 180) * nAngleFromOrigin[nIteration]))
                    # pygame.draw.circle(screen, (0, 0, 255), (nXAdjust - int(x * nScaleDown), nYAdjust - int(y * nScaleDown)), 5)
                    xStart = nXAdjust - int(x * nScaleDown)
                    yStart = nYAdjust - int(y * nScaleDown)

                nXPositions.append(xStart)
                nYPositions.append(yStart)
                
                #print(measurment[2], x, y)

            nTries = nTries + 1

             # if over the last 1000 iterrations, the hit percentages is high, then exit
            if nFound/nTries > nMapCoverage :
                print("exiting")
                break
            elif nTries%1000 ==0:
                nTries =1
                nFound =0


def GetDistances()  :
    
    
    lidar = RPLidar(PORT_NAME)
    lidar.set_pwm(500)

    print("move unit now!")
    time.sleep(10)
    print("measuring new location!")

    for measurment in lidar.iter_measurments():

        # convert angle and distance to x and y

        if measurment[1] == 15 and measurment[3] < nMaxRange and measurment[3] > nMinRange:
            # finding the 2 missing legs given a hypotenuse(distance) and angle in degrees from the lidar

            if round(measurment[2], 0) in [359, 0, 1]:
                # print("north ", measurment[2], measurment[3] )
                nCurNorth = measurment[3]

            if round(measurment[2], 0) in [89, 90, 91]:
                # print("East ", measurment[2], measurment[3])
                nCurEast = measurment[3]

            if round(measurment[2], 0) in [179, 180, 181]:
                # print("south ", measurment[2], measurment[3])
                nCurSouth = measurment[3]

            if round(measurment[2], 0) in [269, 270, 271]:
                # print("West ", measurment[2], measurment[3])
                nCurWest = measurment[3]

            if nCurNorth != 0 and nCurEast != 0 and nCurSouth != 0 and nCurWest != 0:
                break

    print("4 directions NESW ", nCurNorth, nCurEast, nCurSouth, nCurWest)


try:

    pygame.init()
    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])
    font = pygame.font.Font(pygame.font.get_default_font(), 24)
    # Fill the background with white
    screen.fill((255, 255, 255))

    nXPositions = []
    nYPositions = []

    nDistancefromOrigin = []
    nAngleFromOrigin = []



    n1stCircle = []
    n2ndCircle = []
    n3rdCircle = []
    n4thCircle = []

    


    LidarLoadArrays()
 
    RefreshMap()


    nCurNorth = 0
    nCurEast = 0
    nCurWest = 0
    nCurSouth = 0

    #tStart = time.perf_counter()
    # if here too long, widen the view?

    nTimesHere=0
    while (True) :
        

        print("wider", nTimesHere)
        GetDistances()
        
        
        # do this every time?   maybe add records instead?
        n1stCircle = []
        n2ndCircle = []
        n3rdCircle = []
        n4thCircle = []

        print("start remote circle")

        # calculate a few points (for error) in each direction from every initial reading
        # uses the radius based on 4 directions measured above
        FillCircleArray(n1stCircle, nCurNorth, 180-nTimesHere, 180+nTimesHere)    #3
        print("north")
        FillCircleArray(n2ndCircle, nCurEast, 270-nTimesHere, 270+nTimesHere)      #3
        print("east")
        FillCircleArray(n3rdCircle, nCurSouth, 360-nTimesHere, 360-nTimesHere)     #2
        FillCircleArray(n3rdCircle, nCurSouth, 0+nTimesHere, 0+nTimesHere)     #2
        print("south")
#         FillCircleArray(n4thCircle, nCurWest, 89,91)     #2
#         print("west")


        print("arrays filled ", len(n1stCircle))

        found = False

        nReadingsFound =[]

        for search in range(len(n1stCircle)) :

            if n1stCircle[search] in n2ndCircle :
                print("match 1,2 ", n1stCircle[search])
             
                if n1stCircle[search] in n3rdCircle :
                    print("match 1,2,3", n1stCircle[search])
                    aa, bb = n1stCircle[search]
                    pygame.draw.circle(screen, (150, 100, 150), (aa, bb), 20)
                    text_surface = font.render(str(aa) + "," + str(bb), True, (0, 0, 0))
                    screen.blit(text_surface, (aa, bb))
                    pygame.display.flip()                
                    found = True
                    break

        if found:
            # print("readings ",nReadingsFound)
            # PrintCircle(nCurNorth,nReadingsFound[0])
            # PrintCircle(nCurEast ,nReadingsFound[1])
            # PrintCircle(nCurSouth,nReadingsFound[2])
            # PrintCircle(nCurWest ,nFoundReadings[3])
            print("found breaking out")
            break
        else:
            nTimesHere=nTimesHere +1

        RefreshMap()


    # show location  on screen

    print("done looking ", found)


    print("sleeping")
    time.sleep(1000)

except KeyboardInterrupt:
    print('Stoping.')

finally:

    lidar.stop()
    lidar.disconnect()

    # Done! Time to quit.
    pygame.quit()

