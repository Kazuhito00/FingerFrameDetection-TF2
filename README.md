# FingerFrameDetection-TF2
Tensorflow2 Object Detection APIで作成したFinger Frame検出用のモデルです。<br>
現在はEfficientDet D0のモデルを公開しています。<br>
このリポジトリはデータセット・訓練済みモデルを含み、サイズが約2.9 GBあるため、クローンする際には注意ください。

![2fzd3-s9k3u](https://user-images.githubusercontent.com/37477845/93489320-56583300-f942-11ea-9084-f0c441c0f9cd.gif)

# Requirement 
* Tensorflow 2.3.0 or later
* OpenCV 3.4.2 or later

# Demo
Webカメラを使った推論デモの実行方法は以下です。
```bash
python webcam_demo.py
```
推論を実行するだけであれば、以下のみで実行可能です。
* webcam_demo.py
* 04_model ディレクトリ

また、デモ実行時には、以下のオプションが指定可能です。
* --device<br>カメラデバイス番号の指定 (デフォルト：0)
* --width<br>カメラキャプチャ時の横幅 (デフォルト：960)
* --height<br>カメラキャプチャ時の縦幅 (デフォルト：540)
* --model<br>モデル読み込みパス (デフォルト：'04_model/EfficientDetD0/saved_model')
* --score_th<br>検出閾値 (デフォルト：0.75)
* --fps<br>処理FPS (デフォルト：10) ※推論時間がFPSを下回る場合のみ有効

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
モデル訓練用スクリプトです。<br>
Google Colaboratory上のみで訓練とモデルのエクスポートまで行います。<br>
訓練中のチェックポイントとエクスポートモデルはGoogleドライブ上に保存します。

### webcam_demo.py
推論用のサンプルプログラムです。

### 01_dataset
画像データセットとアノテーションファイルを格納しています。<br>
アノテーションファイルはVoTTで作成しています。
* imageディレクトリ
* annotationディレクトリ<br>
    * FingerFrameDetection-export.csv
    * FingerFrameDetection-export.json

### 02_tfrecord
アノテーション済みデータセットをTFRecordに変換し格納しています。
TFRecordとtf_label_map.pbtxtはVoTTで作成しています。

### 03_config
ファインチューニング用のパイプラインコンフィグを格納しています。
* efficientdet_d0_pipeline.config
      
### 04_model
ファインチューニング済モデルを格納しています。
* EfficientDetD0

# Training
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Kazuhito00/FingerFrameDetection-TF2/blob/master/[Colaboratory]train.ipynb)

# Note
-

# ToDo
- [ ] SSD MobileNet v2 320x320 訓練

# Author
高橋かずひと(https://twitter.com/KzhtTkhs)
 
# License 
FingerFrameDetection-TF2 is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
