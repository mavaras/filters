import cv2


CASCADE_FOLDER = 'res/cascade'

def get_face_classifier() -> cv2.CascadeClassifier:
    return cv2.CascadeClassifier(
        f'{CASCADE_FOLDER}/haarcascade_frontalface_default.xml'
    )


def get_eyes_classifier() -> cv2.CascadeClassifier:
    return cv2.CascadeClassifier(f'{CASCADE_FOLDER}/haarcascade_eye.xml')
