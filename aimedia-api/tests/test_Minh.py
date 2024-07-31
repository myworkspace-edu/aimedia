import unittest
from ultralytics import YOLO

class MyTestCase(unittest.TestCase):
    def test_YOLO8s(self):
        model_path = 'tests/yolo8s.pt'
        model = YOLO(model_path)

        img = 'tests/resource/person.jpg'
        result = model(img)

        self.assertIsNotNone(result)
        list_results = list(result)

        first_result = list_results[0]

        list_boxes = list(first_result.boxes)
        box = list_boxes[0]

        index_object = int(box.cls[0])
        self.assertEqual(index_object, 0)

        detect_classname = first_result.names[index_object]
        self.assertEqual(detect_classname, 'person')

        self.assertGreater(box.conf, 0.5)

        first_result.save(filename='result.jpg')


if __name__ == '__main__':
    unittest.main()
