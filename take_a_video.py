
## Usage
# python C:\Users\c804324\Documents\GitHub\people_counter\take_a_video.py

from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2


print("[INFO] conectando cámara...")
vs = cv2.VideoCapture(0)

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(vs.get(3))
frame_height = int(vs.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('./videos/video_Teusaquillo.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
print("[INFO] grabando en C:/Users/c804324/Documents/GitHub/people_counter/videos/video_Teusaquillo.avi...")

fps = FPS().start()
while True:
	(grabbed, frame) = vs.read()

	# if the frame was not grabbed, then we have reached the
	# end of the stream
	if not grabbed:
		break
	
	# Write the frame into the file './videos/video_Teusaquillo.avi'
	out.write(frame)

	# put text into video with date time
	text = "{}".format(time.strftime("%Y-%m-%d %H:%M:%S"))
	cv2.putText(frame, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) #color (0, 0, 255)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] tiempo transcurrido: {:.2f}".format(fps.elapsed()))
print("[INFO] FPS aprox.: {:.2f}".format(fps.fps()))

vs.release()
out.release()

# do a bit of cleanup
cv2.destroyAllWindows()