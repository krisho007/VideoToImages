import cv2
import os
import util


if __name__ == '__main__':

    # Read the video
    sVideoPath = input("Enter the video URL: ")
    iFPSToCapture = int(input("How many frames per second to be captured? : "))
    oVideo = cv2.VideoCapture(sVideoPath)
    sTargetDirectory = '{}/data'.format(os.path.dirname(sVideoPath))
    iFPS = util.get_fps(sVideoPath)
    # Capture all frames
    if iFPSToCapture == 0:
        iFPSToCapture = iFPS
    iSkipFrames = iFPS//iFPSToCapture
    try:
        if not os.path.exists(sTargetDirectory):
            os.makedirs(sTargetDirectory)
    except OSError:
        print('Error creating directory {}'.format(sTargetDirectory))

    currentFrame = 0

    while(True):
        # read next frame
        ret, frame = oVideo.read()
        if (ret):
            name = '{}/frame_{}.jpg'.format(sTargetDirectory, str(currentFrame))
            if ((currentFrame % iFPSToCapture) == 0):
                cv2.imwrite(name, frame)
            currentFrame += 1
        else:
            break

    oVideo.release()
    cv2.destroyAllWindows()
