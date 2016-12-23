import cv2, sys

def createFrames(vidName):
	vidcap = cv2.VideoCapture(vidName)
	success, image = vidcap.read()
	count = 0
	success = True
	
	while success:

	    success, image = vidcap.read()
	    print 'Read a new frame: ', success
	    cv2.imwrite("frames/frame%d.jpg" % count, image)  # save frame as JPEG file
	    count += 1

video = sys.argv[1]

createFrames(video)
