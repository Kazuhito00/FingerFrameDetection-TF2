# FingerFrameDetection-TF2
Tensorflow2 Object Detection APIで作成したFinger Frame検出用のモデルです。

# Requirement 
* Tensorflow 2.3.0 or later
* OpenCV 3.4.2 or later

# Usage
推論サンプル(Webカメラ)の実行方法は以下です。
```bash
python webcam_demo.py
```
推論を実行するだけであれば、以下のみで実行可能です。
* webcam_demo.py
* 04_modelディレクトリ

# Directory
<pre>
2.87 GiB 
│  [Colaboratory]train.ipynb
│  webcam_demo.py
│  
├─01_dataset
│  ├─annotation─┬─FingerFrameDetection-export.csv
│  │            └─FingerFrameDetection-export.json 
│  │      
│  └─image─┬─000000.jpg
│          │     :
│          └─003471.jpg
│          
├─02_tfrecord─┬─000000.tfrecord
│             │        :
│             ├─003471.tfrecord
│             └─tf_label_map.pbtxt
│      
├─03_config───efficientdet_d0_pipeline.config
│      
└─04_model───EfficientDetD0─┬─pipeline.config
                            ├─checkpoint─┬─checkpoint
                            │            ├─ckpt-0.data-00000-of-00001
                            │            └─ckpt-0.index
                            └─saved_model─┬─saved_model.pb
                                          └─variables─┬─variables.data-00000-of-00001
                                                      └─variables.index
</pre>

# Note
-

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
FingerFrameDetection-TF2 is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
