import pybboxes as pbx
class YoloUtil:
    @staticmethod
    def convert_bbox(x1, y1, x2, y2, w, h):
        '''

        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :param w:
        :param h: WxH of the image
        :return:
        '''
        voc_bbox = (x1, y1, x2, y2)
        label_info = pbx.convert_bbox(voc_bbox, from_type="voc", to_type="yolo", image_size=(w, h))

        return label_info

    @staticmethod
    def convert_bbox_to_yolo(x1, y1, x2, y2, image_width, image_height):
        x_center = (x1 + x2) / 2
        y_center = (y1 + y2) / 2
        width = x2 - x1
        height = y2 - y1

        # Normalize coordinates
        x_normalized = x_center / image_width
        y_normalized = y_center / image_height
        width_normalized = width / image_width
        height_normalized = height / image_height

        return x_normalized, y_normalized, width_normalized, height_normalized