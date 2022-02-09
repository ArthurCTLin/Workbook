## Homework 7 from [***Machine Learning***](https://speech.ee.ntu.edu.tw/~hylee/ml/2021-spring.html)
* **Professor :** Hung-Yi, Lee
* **Objectives :**
  * Learn how to fine tune a pretrained model on downstream task using BERT
  * Solve Question Answering problem
  * Improve performance with some techniques
      * Tune hyperparameters (e.g. doc_stride)
      * Apply linear learning rate decay
      * Try other pretrained models
      * Improve preprocessing
      * Improve postprocessing
* **Description of HW :** https://speech.ee.ntu.edu.tw/~hylee/ml/ml2021-course-data/hw/HW07/HW07.pdf
* **Kaggle Link :** https://www.kaggle.com/c/ml2021-spring-hw7

### Task & Data
* **Task:** Chinese Extractive Question Answering
  - Input: Paragraph + Question
  - Output: Answer
* **Data**
    * **Types of datasets:**
        - Training set: 26935 QA pairs
        - Dev set: 3523  QA pairs
        - Test set: 3492  QA pairs
    * **Information of dataset:**
        - ***{train/dev/test}_questions*** (list of dicts with the following keys):
           - id (int)
           - paragraph_id (int)
           - question_text (string)
           - answer_text (string)
           - answer_start (int)
           - answer_end (int)
        - ***{train/dev/test}_paragraphs:***
          - List of strings
          - paragraph_ids in questions correspond to indexs in paragraphs
          - A paragraph may be used by several questions 
* Other detailed information can be check in the HW07.pdf

### Implementation
* Based on TA's source code and make some improvements
* Follow the tips provided by TAs:
    * **Linear learning rate decay (warmup)**
    * **doc_stride :** distance between the start position of two consecutive windows. (**overlapping w/ndow**)
    * **Preprocessing :** avoid model learning incorrect features caused by the preprocess of data.
    * **Postprocessing :** check if the results are normal (open the output file to see what's strange).
    * **Change the pretrained model :** Try different QA models.

### Result
* ***Had achieved strong baseline (Public/Private): (0.7929/0.80802)***
* My best (public/private) score: 0.81464/0.81833
* The process of tuning hyperparameters and applying above tips:
    * Baseline: 0.504/0.51346
    * Step 1: 0.58352/0.57421
        * Applied linear learning rate decay
    * Step 2: 0.70938/0.71747 (**Medium baseline**)
        * doc_stride = (150->50) 
        * Linear learning rate decay 
    * Step 3: 0.70823/0.71805
        * doc_stride = (150->50) 
        * Linear learning rate decay 
        * postprocess: avoid the situation that predicted end_index < predicted start_index
    * Step 4: 0.74084/0.77306
        * doc_stride = (150->50) 
        * Linear learning rate decay 
        * Postprocess: avoid the situation that predicted end_index < predicted start_index
        * Preprocess: add the randomness of the answer positions in the window while training.
    * Step 5: 0.78661/0.79369
        * doc_stride = (150->30) 
        * Linear learning rate decay 
        * Postprocess: avoid the situation that predicted end_index < predicted start_index
        * Preprocess: add the randomness of the answer positions in the window while training.
        * Change pretrained model
        from `bert-base-chinese` to `luhua/chinese_pretrain_mrc_roberta_wwm_ext_large`
    * Step 6: 0.81464/0.81833 (**Strong baseline**)
        * doc_stride = (150->30) 
        * Linear learning rate decay 
        * Postprocess: avoid the situation that predicted end_index < predicted start_index
        * Preprocess: add the randomness of the answer positions in the window while training.
        * Change pretrained model
        from `bert-base-chinese` to `luhua/chinese_pretrain_mrc_roberta_wwm_ext_large`
        * Tuned learning rate: 1.00E-04 -> 1.00E-05
* ***Noting: To obtain above results, many trials had been tested and I had just selected and shown the most meaningful results.***
* Possible improvement methods: ***essemble method***. 


### Reference
* Source code provided by Course TA : https://colab.research.google.com/github/ga642381/ML2021-Spring/blob/main/HW07/HW07.ipynb
* Huggingface : https://huggingface.co/models
* Paper: [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
