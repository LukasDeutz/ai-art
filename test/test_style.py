import numpy as np
np.random.seed(222)
import tensorflow as tf
tf.random.set_seed(222)
from matplotlib import pyplot as plt
import skimage.io as io
import skimage.transform as T

from transfer_style import Stylizer
from optimizers import GradientDescent, Adam, L_BFGS
from callback import Callback

img_dir = '../img/'

class Synthesizer():
    '''
    Synthesises given content and style to a new image.
    '''
    
    
    def __init__(self, content_filename, style_filename):
        '''
        
        :param content_filename:
        :param style_filename:
        :param iterations:
        :param content_layer_name:
        :param content_weight:
        :param style_layer_names:
        :param style_layer_weights:
        :param style_weight:
        :param total_variation_weight:
        '''
                        
        self.content_filename = content_filename                        
        self.style_filename = style_filename
                
        self.read_images()
            
    def read_images(self):

        self.content = io.imread(img_dir + 'content/' + self.content_filename)                
        self.style = T.resize(io.imread(img_dir + 'styles/' + self.style_filename), 
                              self.content.shape[:-1], 
                              preserve_range=True).astype('uint8')

        return

    def stylize(self,
            iterations = 30,
            content_layer_name = 'block4_conv2',
            content_weight = 1,
            style_layer_names = ['block1_conv1','block2_conv1','block3_conv1','block4_conv1','block5_conv1'],
            style_layer_weights = None,
            style_weight = 1e4,
            total_variation_weight = 0.0):
        '''
        Syntehsise image from content and style image
        '''
            
        styler = Stylizer(content_layer_name = content_layer_name,
                          content_weight = content_weight, 
                          style_weight = style_weight,
                          style_layer_weights = style_layer_weights,
                          total_variation_weight = total_variation_weight)

        styler(content=self.content,
               style=self.style,
               optimize=L_BFGS(max_evaluations=20),
               iterations=iterations,
               callback=Callback(f'build/style-transfer/{self.style_filename}')
        )
        io.imsave(img_dir + f'style-transfer/{self.style_filename}.jpg', output)
        
        return
    
    def stylize_batch(self, parameter_arr):
        
        for parameter in parameter_arr:            
            self.stylize(**parameter)
        
        return
        
if __name__ == '__main__':
        
    synthi = Synthesizer('liam.jpg', 'two-sisters.jpg')
    synthi.stylize()
        
