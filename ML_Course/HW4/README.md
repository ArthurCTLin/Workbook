## Homework 4 from [***Machine Learning***](https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html)
* **Professor :** Hung-Yi, Lee
* **Objectives :**
  * Learn how to use Transformer
  * Solve multiclass classification problem with Transformer (Predict speaker class from given speech)
  * Optimize the performance with Conformer.
* **Description of HW :** https://speech.ee.ntu.edu.tw/~hylee/ml/ml2021-course-data/hw/HW04/HW04.pdf
* **Kaggle Link :** https://www.kaggle.com/c/ml2021spring-hw4

### Task & Data
* Task: Speaker Classification
* Data
    * Overview of dataset:
        * Original dataset is [Voxceleb1](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/)
        * The [license](https://creativecommons.org/licenses/by/4.0/) and [complete version](https://www.robots.ox.ac.uk/~vgg/data/voxceleb/files/license.txt) of Voxceleb1.
    * Preprocess of HW4 dataset:
        * Randomly select 600 speakers from Voxceleb1.
        * Preprocess the raw waveforms into mel-spectrograms.
    * Dataset:
        * Training: 69438 processed audio features with labels.
        * Testing: 6000 processed audio features without labels.
        * Label: 600 classes in total, each class represents a speaker.
    * Directory and Information 
        * Args:
            * data_dir: The path to the data directory.
            * metadata_path: The path to the metadata.
            * segment_len: The length of audio segment for training. 
        * The architecture of data directory 
            * data directory 
                * metadata.json 
                * testdata.json 
                * mapping.json 
                * uttr-{random string}.pt 
        * The information in metadata
            * "n_mels": The dimention of mel-spectrogram.
            * "speakers": A dictionary. 
                * Key: speaker ids.
                * value: "feature_path" and "mel_len"
* Other detailed information can be check in the HW04.pdf

### Implementation
* Based on TA' source code and make some improvements
  * Tuned the d_model (the number of expected features of the input)
  * Tuned the dim_feedforward (the dimension of the feedforward network model) and had tried dim_feedforward = 256, 512, 1024
  * Transformer Layer (had tried layer=1, 3, 5)
  * The layers of prediction layer which is used to accept the encoder representation with statistical pooling
* Further
  * Change **Transformer** into **Conformer**
  * Change **Mean Pooling** into **Attention Pooling**


### Result
* The baseline: 
  * Simple(Public/Private): (0.82523/0.83000)
  * Medium(Public/Private): (0.90547/0.90166)
  * Strong(Public/Private): (0.95404/0.95333)
* BreakTrough:
  * Medium Baseline
    * Increased n_model and dim_feedforward to 200 and 1024. (Made the model more complex) (Public, Private): (0.92904,	0.92166)
    * Increased n_model(200) + Conformer (Public, Private): (0.95142,	0.95111) -> close to strong baseline.
    * Increased n_model(256) + dim_feedforward(1024) + Attention Pooling (Public, Private): (0.94547,	0.94833) -> close to strong baseline and faster than applying Conformer.
   * Strong Baseline 
    * Increased n_model(256) + Conformer (Public, Private): (0.95476	0.95666)

***Note :*** The combination of conformer + Attention Pooling gives score(Public, Private): (0.95285	0.95500) which doesn't pass strong baseline.

* Possible improvement method: ***Additive margin softmax*** or ***Essemble method***. 

### Reference
* Source code provided by Course TA : https://colab.research.google.com/github/ga642381/ML2021-Spring/blob/main/HW04/HW04.ipynb
* Conformer
  * https://arxiv.org/abs/2005.08100
  * https://github.com/lucidrains/conformer
* Self-Attentive Speaker Embeddings
    * Paper: [Self-Attention Encoding and Pooling for Speaker Recognition](https://arxiv.org/pdf/2008.01077v1.pd)
