import cv2
from tensorflow.python.platform import gfile
import tensorflow as tf

filename = 'test.png'

# When we use FastGFile to read an image, it is ordered RGB after decoding
image_data = gfile.FastGFile(filename, 'rb').read()
coded_data = tf.placeholder(tf.string, name='something')
decoded_image = tf.image.decode_image(coded_data, channels=3)
#with tf.Session() as sess:
output = tf.Session().run(decoded_image, {coded_data: image_data})
print('Image read with FastGFile:')
print(output)



# When we use OpenCV to read an image, it is ordered BGR
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print('Image read with OpenCV:')
print(img)





# Here, we try passing the image read using OpenCV into the decoder op

coded_data = tf.placeholder(tf.string, name='something')
decoded_image = tf.image.decode_jpeg(coded_data, channels=3)
#with tf.Session() as sess:
output = tf.Session().run(decoded_image, {coded_data: img})
print('Image read with FastGFile:')
print(output)

