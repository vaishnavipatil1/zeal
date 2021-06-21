import matplotlib.pyplot as plt
%matplotlib inline 
from sklearn.datasets import load_digits
digits = load_digits()
import pylab as pl
pl.gray()
pl.matshow(digits.images[0])
pl.show()
digits.images[0]
images_and_labels = list(zip(digits.images,digits.target))
plt.figure(figsize=(5,5))
for index, (images,label) in enumerate(images_and_labels[:15]):
    plt.subplot(3,5,index + 1)
    plt.axis('off')
    plt.imshow(images,cmap=plt.cm.gray_r,interpolation ='nearest')
    plt.title('%i'%label)
import random
import pylab as pl 
import matplotlib.pyplot as plt
digits = load_digits()
from sklearn.datasets import load_digits
digits.images[0]
i = 0 

pl.gray()
pl.matshow(digits.images[i])
pl.show()
classifer.predict(x(i))
i=234

pl.gray()
pl.matshow(digits.images[i])
pl.show()
classifier.predict(x[i])
