import unittest
from ultralytics import YOLO


class MyTestCase(unittest.TestCase):
    def test_detect_by_YOLO(self):
        model_path = 'yolov8n.pt'
        model = YOLO(model_path)

        image = 'image.png'
        results = model(image)

        self.assertIsNotNone(results)

        list_results = list(results)
        self.assertIsNotNone((list_results[0]))

        first_result = list_results[0]

        list_boxes = list(first_result.boxes)
        box = list_boxes[0]

        index_object = int(box.cls[0])

        #self.assertEqual(index_object, 8)

        detected_classname = first_result.names[index_object]
        self.assertEqual(detected_classname, 'person')

        self.assertGreater(box.conf[0], 0.5)


if __name__ == '__main__':
    unittest.main()
