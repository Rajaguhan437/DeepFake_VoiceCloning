# %%
import numpy as np
import cv2
import dlib

#%%

### initialize dlib's face detector module
frontal_face_detector = dlib.get_frontal_face_detector()
### face predictor
frontal_face_preictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')  ### downlload from http://dlib.net/files/


# %%
src_img = cv2.imread("johnny_depp.jpeg")
