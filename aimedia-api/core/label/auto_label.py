import os
import logging
from core.predict.yolo import Predictor
from util.yolo import YoloUtil
import cv2

logger = logging.getLogger()
class YoloLabel():
    def __init__(self, model_path):
        '''
        :param current_path: folder of yolo dataset. This folder contains:
        obj_Train_data
        obj.data
        obj.names
        Train.txt
        '''
        self.predictor = Predictor(model_path)

    # def test_convert_bbox(self):
    #     result = YoloUtil.convert_bbox(100, 100, 200, 200,1000, 1000)  # WxH of the image
    #     self.assertIsNotNone(result)
    def label_folder(self, input_folder, output_folder=None):
        '''
        :param path_input: .../<Object name>
        :param path_output: folder
        :param prefix_output:
        :return:
        '''

        if not output_folder:
            output_folder = 'output'

        obj_train_data_dir = os.path.join(output_folder, 'obj_train_data')
        os.makedirs(obj_train_data_dir, exist_ok=True)

        obj_names_file = os.path.join(output_folder, 'obj.names')
        obj_data_file = os.path.join(output_folder, 'obj.data')
        train_txt_file = os.path.join(output_folder, 'train.txt')

        with open(obj_names_file, 'w') as f:
            for name in self.predictor.model.names.values():
                f.write(f"{name}\n")

        with open(obj_data_file, 'w') as f:
            f.write(f"classes = {len(self.predictor.model.names)}\n")
            f.write(f"names = {os.path.basename(obj_names_file)}\n")
            f.write(f"train = {os.path.basename(train_txt_file)}\n")
            f.write(f"valid = \n")
            f.write(f"backup = backup/\n")

        print(f'Predicting images in folder {input_folder}...')

        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        for image_file in image_files:
            image_path = os.path.join(input_folder, image_file)
            detected_objects, annotated_image = self.predictor.predict(image_path)

            if detected_objects is not None:
                image_name, _ = os.path.splitext(image_file)
                image_txt = os.path.join(obj_train_data_dir, f'{image_name}.txt')
                self.write_result_to_txt(detected_objects, image_txt)

                output_image_path = os.path.join(obj_train_data_dir, image_file)
                cv2.imwrite(output_image_path, annotated_image)

                with open(train_txt_file, 'a') as train_file:
                    train_file.write(f"{os.path.join('obj_train_data', image_file)}\n")

        print(f'Done. Check result at: {output_folder}')

    def write_result_to_txt(self, results, image_txt):
        with open(image_txt, 'w') as f:
            for result in results:
                class_id, x_center, y_center, w, h = result
                f.write(f'{class_id} {x_center} {y_center} {w} {h}\n')


model_path = './yolov8n.pt'
yolo_label = YoloLabel(model_path)
yolo_label.label_folder('my_input', 'my_output')

