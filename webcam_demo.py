#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import time
import copy

import cv2 as cv
import numpy as np
import tensorflow as tf


def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--fps", type=int, default=10)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=540)

    parser.add_argument("--model",
                        default='04_model/EfficientDetD0/saved_model')
    parser.add_argument("--score_th", type=float, default=0.75)

    args = parser.parse_args()

    return args


def run_inference_single_image(image, inference_func):
    tensor = tf.convert_to_tensor(image)
    output = inference_func(tensor)

    output['num_detections'] = int(output['num_detections'][0])
    output['detection_classes'] = output['detection_classes'][0].numpy()
    output['detection_boxes'] = output['detection_boxes'][0].numpy()
    output['detection_scores'] = output['detection_scores'][0].numpy()
    return output


def main():
    # 引数解析 #################################################################
    args = get_args()
    cap_device = args.device
    cap_width = args.width
    cap_height = args.height
    fps = args.fps

    model_path = args.model
    score_th = args.score_th

    # カメラ準備 ###############################################################
    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    # モデルロード #############################################################
    DEFAULT_FUNCTION_KEY = 'serving_default'
    loaded_model = tf.saved_model.load(model_path)
    inference_func = loaded_model.signatures[DEFAULT_FUNCTION_KEY]

    fps = 10

    while True:
        start_time = time.time()

        # カメラキャプチャ #####################################################
        ret, frame = cap.read()
        if not ret:
            continue
        frame_width, frame_height = frame.shape[1], frame.shape[0]
        debug_image = copy.deepcopy(frame)

        # 検出実施 #############################################################
        frame = frame[:, :, [2, 1, 0]]  # BGR2RGB
        image_np_expanded = np.expand_dims(frame, axis=0)

        output = run_inference_single_image(image_np_expanded, inference_func)

        num_detections = output['num_detections']
        for i in range(num_detections):
            score = output['detection_scores'][i]
            bbox = output['detection_boxes'][i]
            # class_id = output['detection_classes'][i].astype(np.int)

            if score < score_th:
                continue

            # 検出結果可視化 ###################################################
            x1, y1 = int(bbox[1] * frame_width), int(bbox[0] * frame_height)
            x2, y2 = int(bbox[3] * frame_width), int(bbox[2] * frame_height)

            cv.putText(debug_image, '{:.3f}'.format(score), (x1, y1 - 15),
                       cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2,
                       cv.LINE_AA)
            cv.rectangle(debug_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # キー処理(ESC：終了) #################################################
        key = cv.waitKey(1)
        if key == 27:  # ESC
            break

        # FPS調整 #############################################################
        elapsed_time = time.time() - start_time
        sleep_time = max(0, ((1.0 / fps) - elapsed_time))
        time.sleep(sleep_time)

        # 画面反映 #############################################################
        cv.putText(
            debug_image,
            "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
            (10, 50), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow(' ', debug_image)
        cv.moveWindow(' ', 100, 100)

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
