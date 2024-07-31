import cv2

class Predictor:
    def predict(self, img_in=None):
        '''
        Detect and annotate multi found object into the image.
        :param img_in: path of image or image object
        :param label_visible
        :return:
        Format of info: {"classname": ..., "confidence": ...," classno":..., "x1": x1, "y1": y1, "x2": x2, "y2": y2, "w": w, "h":h}
        image: highlights with rectangle(s) and detected names if label_visible is True.
        '''

        # Sample code
        image = img_in
        if type(img_in) == str:  # load nếu là file path
            image = cv2.imread(img_in, cv2.IMREAD_UNCHANGED)

        if image is not None:
            results = self.model(image)

        return results

