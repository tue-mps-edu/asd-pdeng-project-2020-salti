import cv2
class Visualizer():
    def __init__(self,img):
        self.img=img  # Common image for drawing boxes and printing

    def draw_bboxs( classNames, detection ,self):
        for i in range(len(detection.boxes)):
            box, conf, name = detection.boxes[i], detection.confidences[i], detection.classes[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(self.img, (x, y), (x + w, y + h), (255, 0, 255),
                          2)  # rectangle(starting point which is top left, ending point which is bottom right, color , thickness)
            cv2.putText(self.img, f'{classNames[detection.classes[i]].upper()} {int(detection.confidences[i] * 100)}%', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)

    def print_output(img_type,self):
        cv2.imshow(img_type,self.img)