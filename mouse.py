import cv2
import mediapipe as mp
import pyautogui as pyg
cap=cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height=pyg.size()
index_Y=0
while True:
    _,frame= cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width, _=frame.shape
    rgb_frame= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmarks=hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                print(x,y)
                if id==8:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    index_X=screen_width/frame_width*x
                    index_Y=screen_height/frame_height*y
                    pyg.moveTo(index_X,index_y)
                if id==4:
                    cv2.circle(img=frame,center=(x,y),radius=10,color=(0,255,255))
                    thumb_X=screen_width/frame_width*x
                    thumb_Y=screen_height/frame_height*y
                    if abs(index_Y-thumb_Y)<20:
                        pyg.click()
                        pyg.sleep(1)   
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
