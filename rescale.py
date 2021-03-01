import cv2 as cv

# resizing and rescaling images

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)


def rescale_frame(frame, scale=0.75):
    # work for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width, height):
    # only work for live videos like from cameras/web cam
    capture.set(3, width)
    capture.set(4  , height)


# image
resized_image = rescale_frame(img)
cv.imshow('Resized image', resized_image)


# rescaling / resizing videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    is_true, frame = capture.read()

    frame_resized = rescale_frame(frame, scale=.2)

    # show each frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


# release and close all windows
capture.release()
cv.destroyAllWindows()

