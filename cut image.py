import cv2
import os

def on_mouse(event, x, y, flags, param):
    global point1, point2,img       #Prevent p1 and p2 from being released at any time
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #Left click
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):     #Drag the mouse to select the section    
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #Loosen the left key
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5) 
        cv2.imshow('image', img2)
        min_x = min(point1[0],point2[0])     
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]       #Cut images
        cv2.imwrite(dest ,cut_img)                              #save image
        
def CropImage4File(filepath,destpath):
    global img,i
    pathDir =  os.listdir(filepath)    # Lists all the paths or files in the file path
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        global dest
        dest = os.path.join(destpath,allDir)
        if os.path.isfile(child):
            img = cv2.imread(child)
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', on_mouse)
            cv2.imshow('image', img)
           
            k = cv2.waitKey(0)&0xFF
            if k == 27:         # wait for ESC key to exit
                cv2.destroyAllWindows()
 
                


filepath ='E:\\baiduyun\\looklok'             #The source image's address
destpath='E:\\baiduyun\\goodgod'              #Resized images saved here
CropImage4File(filepath,destpath)    

