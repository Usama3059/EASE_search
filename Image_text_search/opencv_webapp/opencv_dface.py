
from django.conf import settings
import numpy as np
import cv2
from django.contrib import messages
import Algorithmia
from django.conf import settings
import requests
import io
import json
import os
from PIL import Image
def opencv_dface (path,adr):









   
        im=Image.open(path)
        path1=adr+"new.jpg"
        
        
        #if os.path.getsize(path) > 100000:



        im.save(path1,quality = 10)
        
              
        img=cv2.imread(path1,1)
    
    
    
    
    
    
    
    
    
    #while True:

            #if os.path.getsize(path) > 900
            #else:
                    #break



   
        print(path)
    #cv2.imwrite(path, img)
    #print("Usama")
    #path1="http://usama024.pythonanywhere.com/"
        imageURL = settings.MEDIA_URL + adr






    #img1 = cv2.imread(path, 1)
    #print("usama")
    #print(path)

        if(type(img) is np.ndarray):


        #import cv2

        #import numpy as np
        
#img = cv2.imread("capture1.jpg")
        #cv2.imshow("img",img)
#cv2.waitKey(0)
                height, width, _ = img.shape


# Cutting image
                roi = img[0: height, 400: width]
                roi = img
# Ocr
                url_api = "https://api.ocr.space/parse/image"
                _, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
                file_bytes = io.BytesIO(compressedimage)

                result = requests.post(url_api,
                files = {"screenshot.jpg": file_bytes},
                data = {"apikey": "fbb292377588957",
                      "language": "eng",
                      "detectOrientation":"True"
                      })

                result = result.content.decode()
                result = json.loads(result)
#print(result)
                parsed_results = result.get("ParsedResults")[0]
                text_detected = parsed_results.get("ParsedText")
                print(text_detected)

#cv2.imshow("roi", roi)
#cv2.imshow("Img", img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                import webbrowser
                new =2
#new=2
                tabUrl="http://www.google.com/?#q="
                webbrowser.open(tabUrl+text_detected,new=new)
        #print(img.shape)
        #baseUrl = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        #print(baseUrl)
        #face_cascade = cv2.CascadeClassifier(
            #baseUrl+'haarcascade_frontalface_default.xml')
        #eye_cascade = cv2.CascadeClassifier(baseUrl+'haarcascade_eye.xml')
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        # x=40
        # y=100
        # w=40
        # h=40
        # th=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)

        #for(x, y, w, h) in faces:

            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            #roi_gray = gray[y:y+h, x:x+w]
            #roi_color = img[y:y+h, x:x+w]
            #eyes = eye_cascade.detectMultiScale(roi_gray)
            #for(ex, ey, ew, eh) in eyes:
                #cv2.rectangle(roi_color, (ex, ey),
                              #(ex+ew, ey+eh), (0, 255, 0), 2)

                #cv2.imwrite(path1, img)
        #messages.success(request,"Yo did")
        #messages.add_message(request, messages.INFO, 'Post added.')
        #usama=3
        return text_detected  

#else:

        #print('something error')
        #print(path)
