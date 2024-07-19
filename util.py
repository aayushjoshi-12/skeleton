import cv2 as cv
import numpy as np


def draw_skeleton(image, keypoints):
    for i in range(len(keypoints.xy)):
        for j in range(len(keypoints.xy[i])):
            if np.array(keypoints.xy[i][j]).all() != 0:
                cv.circle(image, np.array(keypoints.xy[i][j], dtype=int), 5, (0, 0, 255), -1)
        if np.array(keypoints.xy[i][0]).all() != 0 and np.array(keypoints.xy[i][1]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][0], dtype=int), np.array(keypoints.xy[i][1], dtype=int), (0, 0, 255), 2) # nose to left eye
        if np.array(keypoints.xy[i][0]).all() != 0 and np.array(keypoints.xy[i][2]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][0], dtype=int), np.array(keypoints.xy[i][2], dtype=int), (0, 0, 255), 2) # nose to right eye
        if np.array(keypoints.xy[i][1]).all() != 0 and np.array(keypoints.xy[i][2]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][1], dtype=int), np.array(keypoints.xy[i][3], dtype=int), (0, 0, 255), 2) # left eye to left ear
        if np.array(keypoints.xy[i][2]).all() != 0 and np.array(keypoints.xy[i][4]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][2], dtype=int), np.array(keypoints.xy[i][4], dtype=int), (0, 0, 255), 2) # right eye to right ear
        if np.array(keypoints.xy[i][1]).all() != 0 and np.array(keypoints.xy[i][5]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][1], dtype=int), np.array(keypoints.xy[i][5], dtype=int), (0, 0, 255), 2) # left eye to left shoulder
        if np.array(keypoints.xy[i][2]).all() != 0 and np.array(keypoints.xy[i][6]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][2], dtype=int), np.array(keypoints.xy[i][6], dtype=int), (0, 0, 255), 2) # right eye to right shoulder
        if np.array(keypoints.xy[i][5]).all() != 0 and np.array(keypoints.xy[i][6]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][5], dtype=int), np.array(keypoints.xy[i][6], dtype=int), (0, 0, 255), 2) # left shoulder to left elbow
        if np.array(keypoints.xy[i][6]).all() != 0 and np.array(keypoints.xy[i][8]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][6], dtype=int), np.array(keypoints.xy[i][8], dtype=int), (0, 0, 255), 2) # right shoulder to right elbow
        if np.array(keypoints.xy[i][7]).all() != 0 and np.array(keypoints.xy[i][9]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][7], dtype=int), np.array(keypoints.xy[i][9], dtype=int), (0, 0, 255), 2) # left elbow to left wrist
        if np.array(keypoints.xy[i][8]).all() != 0 and np.array(keypoints.xy[i][10]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][8], dtype=int), np.array(keypoints.xy[i][10], dtype=int), (0, 0, 255), 2) # right elbow to right wrist
        if np.array(keypoints.xy[i][5]).all() != 0 and np.array(keypoints.xy[i][11]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][11], dtype=int), np.array(keypoints.xy[i][5], dtype=int), (0, 0, 255), 2) # left hip to left shoulder
        if np.array(keypoints.xy[i][6]).all() != 0 and np.array(keypoints.xy[i][12]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][12], dtype=int), np.array(keypoints.xy[i][6], dtype=int), (0, 0, 255), 2) # right hip to right shoulder
        if np.array(keypoints.xy[i][11]).all() != 0 and np.array(keypoints.xy[i][12]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][11], dtype=int), np.array(keypoints.xy[i][12], dtype=int), (0, 0, 255), 2) # left hip to right hip
        if np.array(keypoints.xy[i][11]).all() != 0 and np.array(keypoints.xy[i][13]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][11], dtype=int), np.array(keypoints.xy[i][13], dtype=int), (0, 0, 255), 2) # left hip to left knee
        if np.array(keypoints.xy[i][12]).all() != 0 and np.array(keypoints.xy[i][14]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][12], dtype=int), np.array(keypoints.xy[i][14], dtype=int), (0, 0, 255), 2) # right hip to right knee
        if np.array(keypoints.xy[i][13]).all() != 0 and np.array(keypoints.xy[i][15]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][13], dtype=int), np.array(keypoints.xy[i][15], dtype=int), (0, 0, 255), 2) # left knee to left ankle
        if np.array(keypoints.xy[i][14]).all() != 0 and np.array(keypoints.xy[i][16]).all() != 0:
            cv.line(image, np.array(keypoints.xy[i][14], dtype=int), np.array(keypoints.xy[i][16], dtype=int), (0, 0, 255), 2) # right knee to right ankle
    return image