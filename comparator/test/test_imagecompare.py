
#-*- encoding: utf-8 -*-
import os, sys
import pytest
from test import diffimg_image_compare as img_comparator
# import diffimg_image_compare as img_comparator

def test_diffimg_imagecompare():
    img1_path = get_current_path() + "/test_resource/test_image1.jpg"
    img2_path = get_current_path() + "/test_resource/test_image2.jpg"
    output_path = get_current_path() + "/test_result"
    
    diff_ratio = img_comparator.image_compare("test01", img1_path, img2_path, output_path)
    print(str(diff_ratio))


def test_foldercompare():
    img1_path = get_current_path() + "/test_resource/img1"
    img2_path = get_current_path() + "/test_resource/img2"
    output_path = get_current_path() + "/test_result/20210316"
    
    img_comparator.get_filelist(img1_path, img2_path, output_path)
    
def get_current_path():
    """ 현재 파일의 상위 폴더를 절대경로로 반환한 후 응답값 json 정보가 있는 'responses' 폴더명을 붙여 반환합니다 
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return dir_path
