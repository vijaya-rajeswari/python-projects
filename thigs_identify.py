import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


video = cv2.VideoCapture()  # Modified this line, use 0 for default camera or change to the appropriate camera index if needed
labels = []

while True:
    ret, frame = video.read()
    if not ret:
        break

    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("Object Detection", output_image)

    for item in label:
        if item in labels:
            continue
        else:
            labels.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

new_sentence = []
for i, label in enumerate(labels):
    if i == 0:
        new_sentence.append(f"I found a {label} and")
    else:
        new_sentence.append(f"a {label}")

sentence = " ".join(new_sentence)
speech(sentence)
