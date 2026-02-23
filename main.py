import os.path
import cv2
from operations import apply_top_hat_filter, apply_gaussian_smoothing, \
    apply_median_filter, apply_erosion, apply_dilation, increase_contrast

# Modify this path to reflect the proper location in your file system
image_name = "original_image.tiff"
image_path = f"/Users/nicholasdalsass/PycharmProjects/CSC429IntroProject/{image_name}"

# Read in the image, assert that there no issues with file path
squares_image = cv2.imread(image_path)
assert squares_image is not None, "This file could not be read, uncomment the next line to check if it exists in your system"
# print(os.path.exists(image_path))

# To see the plotted result of each function in main() simply uncomment and run the program
def main():
    #CHAPTER 2 OPERATION FUNCTIONS
    increase_contrast(squares_image)
    # apply_erosion(squares_image)
    # apply_dilation(squares_image)

    #CHAPTER 3 OPERATION FUNCTIONS
    # apply_gaussian_smoothing(squares_image)
    # apply_median_filter(squares_image)
    # apply_top_hat_filter(squares_image)

    # Uncomment these for some data about the image from OpenCV fields
    # print(squares_image.shape)
    # print(squares_image.size)
    # print(squares_image.dtype)

if __name__ == "__main__":
    main()
