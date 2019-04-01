
## Usage
# python C:\Users\c804324\Documents\GitHub\people_counter\take_a_video.py

from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import time
import cv2


print("[INFO] conectando cámara...")
vs_0 = cv2.VideoCapture(0)
vs_1 = cv2.VideoCapture(2)

# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
# camera 0
frame_width_0 = int(vs_0.get(3))
frame_height_0 = int(vs_0.get(4))

# camera 2
frame_width_1 = int(vs_1.get(3))
frame_height_1 = int(vs_1.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out_0 = cv2.VideoWriter('C:/Users/c804324/Documents/GitHub/people_counter/videos/video_Teusaquillo_cam_0_p.avi', 
	cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width_0,frame_height_0))
out_1 = cv2.VideoWriter('C:/Users/c804324/Documents/GitHub/people_counter/videos/video_Teusaquillo_cam_1_p.avi', 
	cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width_1,frame_height_1))

print("[INFO] grabando en C:/Users/c804324/Documents/GitHub/people_counter/videos/video_Teusaquillo.avi...")

fps = FPS().start()
while True:
	(grabbed_0, frame_0) = vs_0.read()

	# if the frame was not grabbed, then we have reached the
	# end of the stream
	if grabbed_0:
		# Write the frame into the file './videos/video_Teusaquillo.avi'
		out_0.write(frame_0)

		# put text into video with date time
		text = "cam 0 {}".format(time.strftime("%Y-%m-%d %H:%M:%S"))
		cv2.putText(frame_0, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) #color (0, 0, 255)

		# show the output frame
		cv2.imshow("camera 0", frame_0)
	else: 
		break
	
	#*********************
	## camera 2
	#*********************
	(grabbed_1, frame_1) = vs_1.read()

	# if the frame was not grabbed, then we have reached the
	# end of the stream
	if grabbed_1:
		# Write the frame into the file './videos/video_Teusaquillo.avi'
		out_1.write(frame_1)

		# put text into video with date time
		text = "cam 1 {}".format(time.strftime("%Y-%m-%d %H:%M:%S"))
		cv2.putText(frame_1, text, (5, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) #color (0, 0, 255)

		# show the output frame
		cv2.imshow("camera 1", frame_1)
	else: 
		break


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

vs_0.release()
vs_1.release()
out_0.release()
out_1.release()

# do a bit of cleanup
cv2.destroyAllWindows()