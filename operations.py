import cv2
import numpy as np
from matplotlib import pyplot as plt

#----------------------------------------CHAPTER 2 OPERATIONS-------------------------------------------#

# Operation 1: Change the Contrast of an Image
def increase_contrast(input_image):
    # Increasing alpha gives control over contrast
    contrast_image = cv2.convertScaleAbs(input_image, alpha=2.5, beta=0)

    # Plot side-by-side output for comparison
    plt.subplot(121), plt.imshow(input_image), plt.title('Original Image')
    plt.subplot(122), plt.imshow(contrast_image), plt.title('Increased Contrast')
    plt.show()

    # Navigate to the /Altered_Images/ directory to see the saved results of this operation
    cv2.imwrite('Altered_Images/increased_contrast_image.jpg', input_image)

# Operation 2: Erode/Shrink a Binary Region
def apply_erosion(input_image):
    # Define the size and type of the 5x5 kernel array which will iterate through all the pixel neighborhoods
    kernel = np.ones((5, 5), np.uint8)

    # Apply pre-built OpenCV erode() function with 1 iteration
    eroded_image = cv2.erode(input_image, kernel, iterations=1)

    # Plot side-by-side output for comparison
    plt.subplot(121), plt.imshow(input_image), plt.title('Original Image')
    plt.subplot(122), plt.imshow(eroded_image), plt.title('After Erosion')
    plt.show()

    # Navigate to the /Altered_Images/ directory to see the saved results of this operation
    cv2.imwrite('Altered_Images/eroded_image.jpg', eroded_image)


# Operation 3: Dilate/Enlarge a Binary Region
def apply_dilation(input_image):
    # This time, I exaggerated the kernel's size, which will dilate the squares in the image much more noticeably
    # Feel free to mess with the kernel size to see the different results
    kernel = np.ones((15, 15), np.uint8)

    # Apply pre-built OpenCV dilate() function (I tried changing the amount of iterations, an interesting test...)
    dilated_image = cv2.dilate(input_image, kernel, iterations=1)

    # Plot side-by-side output for comparison
    plt.subplot(121), plt.imshow(input_image), plt.title('Original Image')
    plt.subplot(122), plt.imshow(dilated_image), plt.title('After Dilation')
    plt.show()

    # Navigate to the /Altered_Images/ directory to see the saved results of this operation
    cv2.imwrite('Altered_Images/dilated_image.jpg', dilated_image)


#----------------------------------------CHAPTER 3 OPERATIONS-------------------------------------------#

# Operation 1: Gaussian Smoothing
def apply_gaussian_smoothing(input_image):
    # SigmaY, if not specified, is the same as SigmaX, so I just put them into on var
    sigma = 2.0
    gaussian_blurred_image = cv2.GaussianBlur(input_image, (7, 7), sigma)

    # Plot side-by-side output for comparison
    plt.subplot(121), plt.imshow(input_image), plt.title('Original Image')
    plt.subplot(122), plt.imshow(gaussian_blurred_image), plt.title('After Gaussian Blur')
    plt.show()

    # Navigate to the /Altered_Images/ directory to see the saved results of this operation
    cv2.imwrite('Altered_Images/gaussian_blurred.jpg', gaussian_blurred_image)


# Operation 2: Median Filter
def apply_median_filter(input_image):
    # Apply pre-built OpenCV medianBlur() function
    median_filtered_image = cv2.medianBlur(input_image, 9)

    # Plot side-by-side output for comparison
    plt.subplot(121), plt.imshow(input_image), plt.title('Original Image')
    plt.subplot(122), plt.imshow(median_filtered_image), plt.title('After Median Filter')
    plt.show()

    # Navigate to the /Altered_Images/ directory to see the saved results of this operation
    cv2.imwrite('Altered_Images/median_filtered_image.jpg', median_filtered_image)


# Operation 3: Top Hat Filter
def apply_top_hat_filter(input_image):
    filter_size = (2, 2)

    # Apply the rectangular shape and filter size of the structuring element structuring
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filter_size)

    # Applying the Top-Hat operation using the developed kernel
    tophat_filtered_image= cv2.morphologyEx(input_image, cv2.MORPH_TOPHAT, kernel)

    # Plot side-by-side output for comparison
    plt.subplot(121), plt.imshow(input_image), plt.title('Original Image')
    plt.subplot(122), plt.imshow(tophat_filtered_image), plt.title('After Top Hat Filter')
    plt.show()

    # Navigate to the /Altered_Images/ directory to see the saved results of this operation
    cv2.imwrite('Altered_Images/tophat_filtered_image.jpg', tophat_filtered_image)

#-------------------------------------------------------------------------------------------------------#

