#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math
import cv2

def Representational(r, g, b):
    return (0.299 * r + 0.287 * g + 0.114 * b)

def calculate(img):
    b, g, r = cv2.split(img)
    pixelAt = Representational(r, g, b)
    return pixelAt

def main():
        
        #Loading images (orignal image and compressed image)
        original_image = cv2.imread('original_image.png', 1)
        compressed_image = cv2.imread('compressed_image.png', 1)

        #Getting image height and width
        height, width = original_image.shape[:2]

        originalPixelAt = calcualte(original_image)

        originalPixelAt = calculate(compressed_image)

        diff = originalPixelAt = compressedPixelAt
        error = np.sum(np.abs(diff) ** 2)

        error = error / (height * width)
        #MSR = error_sum / (height * width)
        PSNR = -(10 * math.log10(error / (255 * 255)))

        print("PSNR value is {}".format(PSNR))

if __name__ == '__main__':
        main()

