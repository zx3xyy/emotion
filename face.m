clear;clc;
modelFile = 'C:\Users\Fan\Desktop\shape_predictor_68_face_landmarks.dat';
frames = find_face_landmarks(modelFile, '000450454.avi');
show_face_landmarks('000450454.avi', frames);