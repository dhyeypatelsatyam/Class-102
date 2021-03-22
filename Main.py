import cv2
import dropbox
import random   
import time




def take_pic():
    number=random.randint(0,100)
    #start cv2      
    videoCaptureObject=cv2.VideoCapture(0)
    result=True

    while(result):
        #take pic while cam is on
        ret.frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2..imwrite(img_name,frame)
        start_time=time.time()    
        result=False
    
    return img_name
    print("Pic Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()