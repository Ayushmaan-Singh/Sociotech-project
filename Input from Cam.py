import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    #showing original frame
    cv2.imshow('Original', frame)

    #sharpening the image using kernel
    kernel = np.array([[-1,-1,-1],
                       [-1,9,-1],
                       [-1,-1,-1]])
    sharpened_image = cv2.filter2D(frame, -1, kernel)
    cv2.imshow('Sharpened', sharpened_image)
    
    #resizing the sharpened image
    resized_image = cv2.resize(sharpened_image, (256, 256))
    cv2.imshow('Resized', resized_image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

