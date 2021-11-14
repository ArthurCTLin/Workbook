### Targets
  * Solve image classification with convolutional neural networks.
  * **Data Augmentation :** Take advantage of `torchvision.transforms` to process existing images and create more usable data.
  * **Semi-supervised Learning :** Understand how to utilize unlabeled data and how it benefits.
### Task & Data
* Task: Food Classification
* Data:
    * The images are collected from the food-11 dataset classified into 11 classes.
    * The dataset here is slightly modified:
        * Training set: 280 * 11 labeled images + 6786 unlabeled images
        * Validation set: 60 * 11 labeled images
        * Testing set: 3347 images
* Other detailed information can be check in the HW03.pdf
      
***Noting :*** In order to let us practice the semi-supervised learning, utilizing the original dataset or labels is limited.

### Implementation
* Based on TA' source code and make some improvements
* Data augmentation : randomly tuned the **brightness**, **flip** and **rotation** of the original labeled training dataset.
* Semi-supervised learning : used models trained with training dataset to classified and labeled the unlabeled images. There are extra two hyper-parameters should be tuned. 
    * The probability of image classification on the unlabeled data  is set to be larger than a threshold.
    * Only when the model accuracy on the validation set is larger than a threshold, will the semi-supervised learning be used.
* Tuned the architecture of the model provided by TA.
* Tuned hyperparameters (learning rate and batch size)
* Tried with well-known models such as Residual Network (resnet(18/50/101/152) and efficientnet-(b0/b6) )
* Tried with pretrained models. (Although TA had warned that using pretrained model is prohibited, I still want to experience standing on the shoulders of giants)

### Result
* The strong baseline of (public/private) score 0.82138/0.81410
* The best (public/private) score of *self-designed model* + *data augmentation* + *slight tuning hyper-parameters* + *semi-supervised learning* are 0.57945/0.56126 which achieve the medium baseline.
* The well-known models (Resnet-18/50/101 and EfficientNet-b0/b6) without pre-trained gives slight better results (acc: 0.6~6.5) but took much time to be stable.
* Resnet18 (pretrained) model + *data augmentation* + semi-supervised learning gives the (public/private) score: 0.81481/0.82665.
  The accuracy of training and validation sets
<img src="https://i.imgur.com/2geeRrr.png" width=50%>
 

* Possible improvement methods: ***self-supervised learning*** or ***essemble method***. 

### Reference
* Source code provided by Course TA : https://colab.research.google.com/github/ga642381/ML2021-Spring/blob/main/HW03/HW03.ipynb
* Data Augmentation: 
    * https://pytorch.org/vision/stable/transforms.html
    * https://blog.csdn.net/flyfish1986/article/details/108831332
    * https://chih-sheng-huang821.medium.com/03-pytorch-dataaug-a712a7a7f55e
    * https://arxiv.org/abs/2002.05709
* Semi-supervised:
    * https://speech.ee.ntu.edu.tw/~tlkagk/courses/ML_2016/Lecture/semi%20(v3).pdf
    * https://github.com/yassouali/awesome-semi-supervised-learning
* Models
    * https://pytorch.org/vision/stable/models.html
