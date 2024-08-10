import unittest
from core.label.auto_label import YoloLabel


class MyTestCase(unittest.TestCase):


if __name__ == '__main__':
    annotator = YoloLabel('../core/label/yolov8n.pt')
    annotator.label_folder(input_folder='./my_input', output_folder='./my_output')

