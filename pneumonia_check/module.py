import numpy as np
from tensorflow.keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.models import model_from_json
import importlib_resources
import json

class Pneumonia:
    loaded_model = 0

    def __init__(self):
        try:
            import importlib.resources as pkg_resources
        except ImportError:
            import importlib_resources as pkg_resources

        with pkg_resources.path("oleh_module_lib", "model.json") as json_file_path:
            json_file = open(json_file_path, 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            self.loaded_model = model_from_json(loaded_model_json)
            with pkg_resources.path("oleh_module_lib", "model.h5") as h5_file_path:
                self.loaded_model.load_weights(h5_file_path)
                print(self.loaded_model.summary())
                print("Model successfully loaded from disk and ready for use.")


    def predict(self, img_name):
        img_width = 196
        img_height = 196
        img = image.load_img(img_name, target_size=(img_width,img_height))
        img = image.img_to_array(img)
        img = preprocess_input(img)
        prediction = self.loaded_model.predict(img.reshape(1,img_width,img_height,3))
        output = np.argmax(prediction)
        return output
