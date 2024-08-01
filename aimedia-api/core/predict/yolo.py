import cv2
from ultralytics import YOLO

class Predictor:
    def __init__(self, model_path):
        # Load the YOLOv8 model
        self.model = YOLO(model_path)
    def predict(self, img_in=None, label_visible= True):
        '''
        Detect and annotate multi found object into the image.
        :param img_in: path of image or image object
        :param label_visible
        :return:
        Format of info: {"classname": ..., "confidence": ...," classno":..., "x1": x1, "y1": y1, "x2": x2, "y2": y2, "w": w, "h":h}
        image: highlights with rectangle(s) and detected names if label_visible is True.

        Developer: Đòan Thái
        '''

        image = img_in
        if isinstance(img_in, str):
            image = cv2.imread(img_in, cv2.IMREAD_UNCHANGED)

        # Perform detection using YOLOv8
        if image is None:
            return None

        results = self.model(image)

        # Get image dimensions
        height, width, _ = image.shape
        # Prepare the list of detected objects with their information
        detected_objects = []
        for result in results[0].boxes:
            x1, y1, x2, y2 = map(int, result.xyxy[0])#thuộc tính chứa tọa độ của bounding box dưới dạng [x1, y1, x2, y2]
            confidence = result.conf.item()#result.conf: accuracy , .item(): chuyển từ Tensor -> dang Python

            class_id = int(result.cls.item())# id_class 
            w = x2 - x1
            h = y2 - y1
            x_center = x1 + w / 2
            y_center = y1 + h / 2
            
            #tọa độ and kthuoc
            x_center /= width
            y_center /= height
            w /= width
            h /= height

            detected_objects.append([
                class_id,
                x_center,
                y_center,
                w,
                h
            ])

            # Annotate the image with rectangles and labels if label_visible is True
            if label_visible:
                cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{self.model.names[class_id]}:{confidence:.2f}"
                cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return detected_objects, image


predictor = Predictor('aimedia_api_model\yolov8n.pt')
detected_objects, annotated_image = predictor.predict(r'core\predict\test_image.jpg', label_visible=True)
if annotated_image is not None:
    cv2.imshow('Annotated Image', annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for obj in detected_objects:
    print(obj)