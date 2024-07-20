from handDetector import HandDetector
import cv2





handDetector = HandDetector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)
Takeoff = False
pause_recognition = False
pause_start_time = 0

while True:
   status, image = webcamFeed.read()
   handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
   instruction = ""
 
   

   if len(handLandmarks) != 0:
      if handLandmarks[4][1] > handLandmarks[3][1] and handLandmarks[8][2] < handLandmarks[6][2] and handLandmarks[20][2] < handLandmarks[18][2] and handLandmarks[12][2] < handLandmarks[10][2] and handLandmarks[16][2] < handLandmarks[14][2] :
         instruction = "HI"
         
      elif handLandmarks[4][1] > handLandmarks[3][1] and handLandmarks[8][2] < handLandmarks[6][2] and handLandmarks[20][2] < handLandmarks[18][2] : 
         instruction = "ONE"
         

      elif handLandmarks[8][2] < handLandmarks[6][2] and handLandmarks[12][2] < handLandmarks[10][2] and handLandmarks[16][2] > handLandmarks[14][2] :
         instruction = "PEACE"
         
         
      elif handLandmarks[8][2] < handLandmarks[6][2] and handLandmarks[12][2] < handLandmarks[10][2] and handLandmarks[16][2] < handLandmarks[14][2] :
         instruction = "Stop"
         
      elif handLandmarks[8][2] < handLandmarks[6][2] and handLandmarks[20][2] < handLandmarks[18][2] :   
         instruction = "LEFT"
        

   
      elif handLandmarks[4][1] > handLandmarks[3][1] and handLandmarks[8][2] < handLandmarks[6][2] :     
         instruction = "Right"
         

      elif handLandmarks[8][2] < handLandmarks[6][2] :
         instruction = "NO"
          
   

   cv2.putText(image, instruction, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)
   cv2.imshow("Volume", image)
   cv2.waitKey(1)
   