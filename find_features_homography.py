import cv2
import click
import logging
import numpy as np
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

def _find_features_homography(image_gray_file_path, align_image_gray_file_path, feature_retention=0.3, min_match_count=10):
    matches_output_file_name = os.path.basename(image_gray_file_path)
    
    # Load the images
    image_gray = cv2.imread(image_gray_file_path)
    align_image_gray = cv2.imread(align_image_gray_file_path)

    # Detect SIFT features and compute descriptors.
    detector = cv2.SIFT_create(edgeThreshold=10, contrastThreshold=0.1)
    kp_image, desc_image = detector.detectAndCompute(image_gray, None)
    kp_align_image, desc_align_image = detector.detectAndCompute(align_image_gray, None)

    # Match
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    try:
        matches = flann.knnMatch(desc_image, desc_align_image, k=2)
    except Exception as e:
        return None

    # Filter good matches following Lowe's ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < feature_retention * n.distance:
            good_matches.append(m)

    matches = good_matches

    if len(matches) < min_match_count:
        return None

    # Debug
    imMatches = cv2.drawMatches(image_gray, kp_image, align_image_gray, kp_align_image, matches, None)
    cv2.imwrite(matches_output_file_name, imMatches)

    # Extract location of good matches
    points_image = np.zeros((len(matches), 2), dtype=np.float32)
    points_align_image = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points_image[i, :] = kp_image[match.queryIdx].pt
        points_align_image[i, :] = kp_align_image[match.trainIdx].pt

    # Find homography
    h, _ = cv2.findHomography(points_image, points_align_image, cv2.RANSAC)
    return h

@click.command()
@click.argument('image_gray_file_path')
@click.argument('align_image_gray_file_path')
def find_features_homography(image_gray_file_path, align_image_gray_file_path):
    # Log the homography matrix
    logging.info('find_features_homography: %s', _find_features_homography(image_gray_file_path, align_image_gray_file_path))

if __name__ == '__main__':
    find_features_homography()