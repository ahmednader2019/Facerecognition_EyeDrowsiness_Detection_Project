#Importing OpenCV Library for basic image processing functions
import cv2
# Numpy for array related functions
import numpy as np
# Dlib for deep learning based Modules and face landmark detection
import dlib
#face_utils for basic operations of conversion
from imutils import face_utils


from simple_facerec import SimpleFacerec

import smartWatch 


# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Initializing the camera and taking the instance
cap = cv2.VideoCapture(0)

#Initializing the face detector and landmark detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#status marking for current state
sleep = 0
drowsy = 0
active = 0
status=""
color=(0,0,0)
RequiredFrames = 20
LastName = "Unknown"
FaceDetectPerFrame = 10

FrameCounter = 0

def compute(ptA,ptB):
	dist = np.linalg.norm(ptA - ptB)
	return dist

def blinked(a,b,c,d,e,f):
	up = compute(b,d) + compute(c,e)
	down = compute(a,f)
	ratio = up/(2.0*down)

	#Checking if it is blinked
	if(ratio>0.25):
		return 2
	elif(ratio>0.21 and ratio<=0.25):
		return 1
	else:
		return 0


while True:

    FrameCounter += 1

    ret, frame = cap.read()

    # Detect Faces

    if FrameCounter % FaceDetectPerFrame == 0:

        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            LastName = name
            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    #detected face in faces array
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        face_frame = frame.copy()
        cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        #The numbers are actually the landmarks which will show eye
        left_blink = blinked(landmarks[36],landmarks[37], 
        	landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42],landmarks[43], 
        	landmarks[44], landmarks[47], landmarks[46], landmarks[45])
        
        #Now judge what to do for the eye blinks
        if(left_blink==0 or right_blink==0):
        	sleep+=1
        	drowsy=0
        	active=0

        	if(sleep>RequiredFrames):
        		status="SLEEPING"
        		color = (255,0,0)

            # if(sleep <= 50):
        	# 	status= string(sleep)
        	# 	color = (0,255,0)


        # elif(left_blink==1 or right_blink==1):
        # 	sleep=0
        # 	active=0
        # 	drowsy+=1
        # 	if(drowsy>6):
        # 		status="Drowsy !"
        # 		color = (0,0,255)

        else:
        	drowsy=0
        	sleep=0
        	active+=1
        	if(active>6):
        		status="Awake"
        		color = (0,255,0)
        	
        cv2.putText(frame, LastName, (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)
        
        cv2.putText(frame, status, (20,100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)
        # cv2.putText(frame,, (20,200), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)

        if (sleep != 0 and sleep <= RequiredFrames):
           cv2.putText(frame, "Counter: " + str(sleep), (20,150), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color,3)


        for n in range(0, 68):
        	(x,y) = landmarks[n]
        	cv2.circle(face_frame, (x, y), 1, (255, 255, 255), -1)
        
        smartWatch.smartWatch(status,"120/80", 90)
            
    cv2.imshow("Frame", frame)
    
    # cv2.imshow("Result of detector", face_frame)
    key = cv2.waitKey(1)
    if key == 27:
    	break
