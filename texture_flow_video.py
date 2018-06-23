#!/usr/bin/env python

'''
Texture flow direction estimation.

Sample shows how cv.cornerEigenValsAndVecs function can be used
to estimate image texture flow direction.

Usage:
    texture_flow_video.py
'''

import numpy as np
import cv2 as cv

if __name__ == '__main__':

    vc = cv.VideoCapture(0)
    vc.set(cv.CAP_PROP_FRAME_WIDTH, 2560)
    vc.set(cv.CAP_PROP_FRAME_HEIGHT, 1440)

    while (1):
        _, vis = vc.read()
        gray = cv.cvtColor(vis, cv.COLOR_BGR2GRAY)
        h, w = vis.shape[:2]

        eigen = cv.cornerEigenValsAndVecs(gray, 15, 3)
        eigen = eigen.reshape(h, w, 3, 2)  # [[e1, e2], v1, v2]
        flow = eigen[:,:,2]

        vis[:] = 255 #Set the back ground to White - gets inverted to Black later

        d = 12 #Sample Size  - this controls how long the directional line will be
        points =  np.dstack( np.mgrid[d/2:w:d, d/2:h:d] ).reshape(-1, 2)
        for x, y in np.int32(points):
            vx, vy = np.int32(flow[y, x]*d)
            cv.line(vis, (x-vx, y-vy), (x+vx, y+vy), (0, 0, 0), 1, cv.LINE_AA)

        #cv.imshow('input', img)
        vis = cv.bitwise_not(vis)
        cv.imshow('flow', vis)

        key = cv.waitKey(5) & 0xFF
        if key == 27:
            break

    vc.release()
    cv.destroyAllWindows()
