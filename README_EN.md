[[Japanese](https://github.com/Kazuhito00/FingerFrameDetection-TF2)/English]
# FingerFrameDetection-TF2
This is a model for FingerFrame detection created by Tensorflow2 Object Detection API.<br>
Currently, the model of EfficientDet-D0 is open to the public.<br>
Be careful when git clone, as this repository contains datasets and trained-models and is approximately 2.9 GB in size.

![2fzd3-s9k3u](https://user-images.githubusercontent.com/37477845/93489320-56583300-f942-11ea-9084-f0c441c0f9cd.gif)

# Requirement 
* Tensorflow 2.3.0 or later
* OpenCV 3.4.2 or later

# Demo
Here's how to run an inference demo using a webcam.
```bash
python webcam_demo.py
```
If you just want to perform inference, you can do it only with the following files.
* webcam_demo.py
* 04_model directory

The following options can be specified when running the demo.
* --device<br>camera device number (Default：0)
* --width<br>Width at the time of camera capture (Default：960)
* --height<br>Vertical width at the time of camera capture (Default：540)
* --model<br>Model loading path (Default：'04_model/EfficientDetD0/saved_model')
* --score_th<br>Detection threshold (Default：0.75)
* --fps<br>Processing FPS (Default：10) ※Valid only if the inference time is less than FPS

# Directory
<pre>
│ [Colaboratory]train.ipynb
│ webcam_demo.py
│  
├─01_dataset
│  ├─annotation─┬─FingerFrameDetection-export.csv
│  │            └─FingerFrameDetection-export.json 
│  │      
│  └─image──────┬─000000.jpg
│               │     :
│               └─003471.jpg
│          
├─02_tfrecord───┬─000000.tfrecord
│               │        :
│               ├─003471.tfrecord
│               └─tf_label_map.pbtxt
│      
├─03_config───efficientdet_d0_pipeline.config
│      
└─04_model───EfficientDetD0─┬─pipeline.config
                            ├─checkpoint──┬─checkpoint
                            │             ├─ckpt-0.data-00000-of-00001
                            │             └─ckpt-0.index
                            └─saved_model─┬─saved_model.pb
                                          └─variables─┬─variables.data-00000-of-00001
                                                      └─variables.index
</pre>
### [Colaboratory]train.ipynb
This is a script for model training.<br>
Training and model export are done only on Google Colaboratory.<br>
Checkpoints and export models during training are stored on Google Drive.

### webcam_demo.py
This is a sample program for inference.

### 01_dataset
Contains image datasets and annotation files.<br>
The annotation file is created by VoTT.
* image directory
* annotation directory<br>
    * FingerFrameDetection-export.csv
    * FingerFrameDetection-export.json

### 02_tfrecord
The annotated dataset is converted to TFRecord and stored.
TFRecord and tf_label_map.pbtxt are created by VoTT.

### 03_config
Contains the pipeline config for fine tuning.
* efficientdet_d0_pipeline.config
      
### 04_model
Contains fine-tuned models.
* EfficientDetD0

# Training
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Kazuhito00/FingerFrameDetection-TF2/blob/master/[Colaboratory]train.ipynb)<br>
This is a script for model training on Colaboratory.<br>
Please carry out in order from the top.<br>
Export the model to Google Drive.<br>
Training on the Colaboratory takes about 30 minutes in 1000 steps.<br>
It takes about 10,000 steps to converge, but detection itself is possible even with 1000 steps.


# ToDo
- [ ] SSD MobileNet v2 320x320 training

# Author
Kazuhito Takahashi(https://twitter.com/KzhtTkhs)
 
# License 
FingerFrameDetection-TF2 is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
