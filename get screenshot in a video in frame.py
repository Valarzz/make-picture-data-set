import cv2,os

# Use opencv to capture video frames at regular intervals and save them as images

vc = cv2.VideoCapture('C:\\Users\\10300\\robomaster.flv')  # write your video address here
c = 0
print("------------")
if vc.isOpened():  # Determine if it is open properly
    print("yes")
    rval, frame = vc.read()
else:
    rval = False
    print("false")

timeF = 1000  # Video frame counting interval frequency

os.chdir("E:/baiduyun/looklok/" )  #write where you want to save here
i = 0

while rval:  
    rval,frame = vc.read()
    print(c,timeF,c%timeF)
    if (c % timeF == 0):# Store every timeF frame
        print("write...")
        cv2.imwrite( str(i) + '.jpg', frame)  # save as image
        print("success!")
    c = c + 1000
    i = i + 1
cv2.waitKey(1)
vc.release()
print("==================================")


