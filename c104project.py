import cv2 
img= cv2.imread("C:/Users/santh/Downloads/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg")
cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Mercury",
            (105,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Venus",
            (200,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Earth",
            (300,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Mars",
            (375,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Jupiter",
            (500,250),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,0)
            
            
            
            
            
            )
cv2.putText(img,
            "Saturn",
            (750,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Uranus",
            (950,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.putText(img,
            "Neptune",
            (1125,250),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            
            
            
            
            
            )
cv2.imshow("output",img)
cv2.waitKey(0)

