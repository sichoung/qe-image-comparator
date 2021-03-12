#-*- encoding: utf-8 -*-
import os
from diffimg import diff
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from diffimg import diff as diff_util


# "file_name , diff_value, diff_img_path, img1_path, img2_path"
result_dict = {}

# https://github.com/nicolashahn/diffimg
# pip install diffimg
def image_compare(file_name, img1_path, img2_path, output_path): 
    """diff(im1_file, im2_file, delete_diff_file=False, diff_img_file=DIFF_IMG_FILE , ignore_alpha=False)
    im1_file, im2_file: filenames of images to diff.
    delete_diff_file: a file showing the differing areas of the two images is generated in order to measure the diff ratio with the same dimensions as the first image. Setting this to True removes it after calculating the ratio.
    diff_img_file: filename for the diff image file. Defaults to diff_img.png (regardless of inputed file's types).
    ignore_alpha: ignore the alpha channel for the ratio and if applicable, sets the alpha of the diff image to fully opaque.
    """
    output_path = output_path+"/"+file_name+".png"
    diff_ratio = diff(img1_path, img2_path, False, output_path, False)
    result_dict.update({file_name : {diff_ratio, output_path, img1_path, img2_path }})
    return diff_ratio

# def get_current_path():
#     """ 현재 파일의 상위 폴더를 절대경로로 반환한 후 응답값 json 정보가 있는 'responses' 폴더명을 붙여 반환합니다 
#     """
#     dir_path = os.path.dirname(os.path.abspath(__file__))
#     return dir_p
def get_current_path():
    """ 현재 파일의 상위 폴더를 절대경로로 반환한 후 응답값 json 정보가 있는 'responses' 폴더명을 붙여 반환합니다 
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return dir_path


# if __name__ == "main":
    # img1_path = get_current_path() + "/test_resource/test_image1.jpg"
    # img2_path = get_current_path() + "/test_resource/test_image2.jpg"
    # output_path = get_current_path() + "/test_result"
    # print(img1_path)
    # print(img2_path)
    # print(output_path)
    # diff_ratio = img_comparator.diff("test01", img1_path, img2_path, output_path)
    # print(diff_ratio)
