clc;clear all;close all;
load 1.mat

%suppose we have already got the face
faceDetector = vision.CascadeObjectDetector;
x(1,:,:,:) = video.frames(i).cdata;
bbox = step(faceDetector, squeeze(x(i,:,:,:)));
cropped_face = squeeze(x(i,bbox(2):bbox(2)+1.4*bbox(4),bbox(1):bbox(1)+bbox(3),:));
 x =imresize(x,[50 50]);
imshow(cropped_face)
for i = 2:95
x(i,:,:,:) = video.frames(i).cdata;
bbox = step(faceDetector, squeeze(x(i,:,:,:)));
cropped_face = squeeze(x(i,bbox(2):bbox(2)+1.4*bbox(4),bbox(1):bbox(1)+bbox(3),:));
imshow(cropped_face)
end