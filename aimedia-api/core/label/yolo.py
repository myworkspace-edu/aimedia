import os
import logging
from core.predict.yolo import Predictor
from util.yolo import  YoloUtil

logger = logging.getLogger()
class YoloLabel():
    def __init__(self):
        '''

        :param current_path: folder of yolo dataset. This folder contains:
        obj_Train_data
        obj.data
        obj.names
        Train.txt
        '''

        self.predictor = Predictor()
        self.yolo_train_txtfile = open('Train.txt', "a")

    def __del__(self):
        self.yolo_train_txtfile.close()

    # def test_convert_bbox(self):
    #     result = YoloUtil.convert_bbox(100, 100, 200, 200,1000, 1000)  # WxH of the image
    #     self.assertIsNotNone(result)
    def labeling_1folder(self, path_image, path_output, prefix_output):
        '''
        :param path_image: .../<Object name>
        :param path_output: folder
        :param prefix_output:
        :return:
        '''

        print(f'Predicting images in folder {path_image}...')
        infos_df, images = self.predictor.predict_1folder(path_image)

        output_fpath = f'{path_output}/{prefix_output}_{self.predict.config.model.name}.xlsx'
        print(f'Writing Excel file: {output_fpath}...')
        infos_df.to_excel(output_fpath, index=False)

        # Get class no
        folder_name = pathlib.PurePath(path_image).name
        # Get index of folder name
        class_no = self.get_class_index(folder_name)
        self.write_yolo_file(infos_df, class_no, path_output)


        print(f'Done. Check result at: {output_fpath}')
    def write_predict_result_to_yolo_file(self, item, class_no, path_output):
        # Write to label file

            class_name = item['folder']
            image_file = item['image_file']
            x1 = item['x1']
            y1 = item['y1']
            x2 = item['x2']
            y2 = item['y2']
            w = item['w']
            h = item['h']
            # label_info = YoloUtil.convert_bbox_to_yolo(x1, y1, x2, y2, w, h)
            label_info = YoloUtil.convert_bbox(x1, y1, x2, y2, w, h)

            file_name = os.path.splitext(os.path.basename(image_file))[0]

            fpath_label = os.path.join(path_output, f'{file_name}.txt')
            self.create_file(fpath_label, label_info, class_no)
