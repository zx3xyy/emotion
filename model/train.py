from feature_extraction import ResNet50_pooling,get_features_from_directory,VGG,prepare_image
from config import VGG_face_weights_path,dataset_path
import os,sys,numpy as np
from glob import glob
from subprocess import call
def extract_frames(directories):
	#directory is the absolute path of extracted frames from the avi file.
	for directory in directories:
		videos = os.listdir(dirctory)
		for video in videos:
			dir_path, _ = os.path.splitext(os.path.join(dirctory,video))
			os.mkdir(dir_path)
			call(["ffmpeg", "-i",os.path.join(dirctory,video),os.path.join(dir_path,u'%d.jpg')])

def extract_features(image_folders,model,id):
		for i,image_folder in enumerate(image_folders):
			features_path = os.path.join(image_folder,id+"_features.txt")
			print("Extracting %d of %d,saving to %s"%(i+1,len(image_folders),features_path))
			features = get_features_from_directory(image_folder,model)
			print(features.shape)
			np.savetxt(features_path,features)

def all_folders(dataset_path):
	folders = []
	directories = ["Angry","Disgust","Fear","Happy","Neutral","Sad","Surprise"]
	directories = [os.path.join(dataset_path,x) for x in directories]
	for directory in directories:
		image_folders = glob(os.path.join(directory,"*"))
		folders.extend(image_folders)
	return folders


if __name__ == "__main__":
	vgg = VGG()
	resnet = ResNet50_pooling()	
	frames_ready = 0
	features_ready = 0

	# directories = "~/dataset/Angry"
	# if 0:#not frames_ready:
	# 	extract_frames(directories)
	# 	frames_ready = 1

	if not features_ready:
		extract_features(all_folders(dataset_path),vgg,'VGG')
		# extract_features(all_folders(dataset_path),resnet,'ResNet')
		features_ready = 1

	# Starting training our LSTM