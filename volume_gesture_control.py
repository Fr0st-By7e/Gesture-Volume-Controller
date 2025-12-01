import cv2
import mediapipe as mp
import hand_tracker_module as htm
import numpy as np
import time
from pycaw.pycaw import AudioUtilities

# Parameters
wCam, hCam = 1280, 720

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pT = 0

detecter = htm.HandTracker(detectionCon=0.75) # 0.75 to avoid flickering

device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
print(f"Audio output: {device.FriendlyName}")
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0] # -63.5
max_vol = vol_range[1] # 0.0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detecter.findHands(img)
    lmList = detecter.findPosition(img, draw=False)
    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]   # Thumb tip
        x2, y2 = lmList[8][1], lmList[8][2]   # Index tip
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        length = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        vol = volume.GetMasterVolumeLevelScalar() * 100  # Current volume in percentage

        vol_db = np.interp(length, [50, 300], [min_vol, max_vol]) # Map length to dB
        volume.SetMasterVolumeLevel(vol_db, None)
        
        cv2.putText(img, f'Vol: {int(vol)} %', (40, 450), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3) # Display volume level
        
        if length < 50:
            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)  # Green when volume is 0

    cT = time.time()
    fps = 1/(cT-pT)
    pT = cT
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        volume.SetMasterVolumeLevel(-15, None)
        break