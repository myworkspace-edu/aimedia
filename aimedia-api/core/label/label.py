import os
import logging
from core.predict.yolo import Predictor
from util.yolo import YoloUtil

logger = logging.getLogger()
class YoloLabel():
    def __init__(self, input_folder, output_folder=None):
        '''
        :param current_path: folder of yolo dataset. This folder contains:
        obj_Train_data
        obj.data
        obj.names
        Train.txt
        '''
        self.input_folder = input_folder

        if not output_folder:
            self.output_folder = 'output'
        else:
            self.output_folder = output_folder

        self.obj_train_data_dir = os.path.join(self.output_folder, 'obj_Train_data')
        self.obj_names_file = os.path.join(self.output_folder, 'obj.names')
        self.obj_data_file = os.path.join(self.output_folder, 'obj.data')
        self.train_txt_file = os.path.join(self.output_folder, 'Train.txt')

        os.makedirs(self.output_folder, exist_ok=True)
        os.makedirs(self.obj_train_data_dir, exist_ok=True)

        self.predictor = Predictor()
        self.train_file = open(self.train_txt_file, 'a')

    def __del__(self):
        if self.train_file:
            self.train_file.close()

    # def test_convert_bbox(self):
    #     result = YoloUtil.convert_bbox(100, 100, 200, 200,1000, 1000)  # WxH of the image
    #     self.assertIsNotNone(result)
    def label_folder(self):
        '''
        :param path_input: .../<Object name>
        :param path_output: folder
        :param prefix_output:
        :return:
        '''

        print(f'Predicting images in folder {self.input_folder}...')

        image_files = [f for f in os.listdir(self.input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        for image_file in image_files:
            result, image = self.predictor.predict(image_file)
            image_name, _ = os.path.splitext(image_file)
            image_txt = os.path.join(self.obj_train_data_dir, f'{image_name}.txt')
            self.write_result_to_txt(result, image_txt)
            self.train_file.write(os.path.join(self.obj_train_data_dir, f'{image_file}') + '\n')

        print(f'Done. Check result at: {self.output_folder}')

    def write_result_to_txt(self, result, image_txt):
        with(open(image_txt, 'w')) as f:
            f.write(result)


