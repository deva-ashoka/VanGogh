import cv2, sys

img1 = cv2.imread('colored/frame0.jpg')

number_of_frames = int(sys.argv[1])

height, width, layers =  img1.shape

video = cv2.VideoWriter('colored_videos/video.mp4',-1,1,(width,height))

for i in range(number_of_frames):
	print ('frame' + str(i) + '.jpg')
	img = cv2.imread('colored/frame' + str(i) + '.jpg')
	video.write(img)

cv2.destroyAllWindows()
video.release()

print('Done!')
