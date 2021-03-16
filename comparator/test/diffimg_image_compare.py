#-*- encoding: utf-8 -*-
import os
import sys
import csv
import argparse
from datetime import datetime
from diffimg import diff
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from diffimg import diff as diff_util


# "file_name , diff_value, diff_img_path, img1_path, img2_path"
result_dict = {}

def image_dir_compare(origin_dir, target_dir, result_dir):
    file_name = None
    compare_result = None
    file_list = os.listdir(origin_dir)
    # CHECKME 하위 디렉토리도 들어가서 리컬시브하게 해야 하는지? 
    if len(file_list) <= 0:
        raise Exception("There is no file in dir1 - " +origin_dir)
    
    success_count = 0
    for this_file in file_list:
        if this_file.endswith(".jpg"):
            
            target_file = target_dir + "/"+this_file
            if os.path.exists(target_file):
                file_name = os.path.splitext(this_file)[0]
                output_path = result_dir+"/"+file_name+"_diff.png"
                compare_result = image_file_compare(origin_dir+"/"+this_file, target_file, output_path)
                success_count += success_count
                result_dict.update({file_name : [compare_result, output_path, origin_dir+"/"+this_file, target_dir+"/"+this_file]})
            else:
                compare_result = "file not found"
                result_dict.update({this_file : [compare_result, "", origin_dir+"/"+this_file, ""]})
        else:
            print("this is not jpg file." + this_file)
    write_result(result_dict, result_dir+"/compare_result.csv")
    return result_dir+"/compare_result.csv"

def write_result(dict_info, file_path):
    f = open(file_path,'w', newline='')
    wr = csv.writer(f)
    wr.writerow(["FILE_NAME","COMPARE_RESULT","DIFF_IMG", "ORIGIN","TARGET"])
    for this_row in dict_info:
        lines = [this_row]
        # lines.append(dict_info.get(this_row))
        wr.writerow(lines+dict_info.get(this_row))
    f.close()

def get_now_datetime():
    return get_now_format_datetime('%Y%m%d_%H%M%S')

def get_now_format_datetime(format_str):
    today = datetime.now()
    # today.strftime('%Y-%m-%d')
    format_str = today.strftime(format_str)
    return str(format_str)

# https://github.com/nicolashahn/diffimg
# pip install diffimg
def image_file_compare(img1_path, img2_path, diff_file_path): 
    """diff(im1_file, im2_file, delete_diff_file=False, diff_img_file=DIFF_IMG_FILE , ignore_alpha=False)
    im1_file, im2_file: filenames of images to diff.
    delete_diff_file: a file showing the differing areas of the two images is generated in order to measure the diff ratio with the same dimensions as the first image. 
    Setting this to True removes it after calculating the ratio.
    diff_img_file: filename for the diff image file. Defaults to diff_img.png (regardless of inputed file's types).
    ignore_alpha: ignore the alpha channel for the ratio and if applicable, sets the alpha of the diff image to fully opaque.
    """
    if os.path.exists(img1_path) == False:
        raise Exception("img1 not exist - "+img1_path)
    if os.path.exists(img2_path) == False:
        raise Exception("img2 not exist - "+img2_path)
    # output_path = output_path+"/"+file_name+"_diff.png"
    diff_ratio = diff(img1_path, img2_path, False, diff_file_path, False)
    
    return diff_ratio

def get_current_path():
    """ 현재 파일의 상위 폴더를 절대경로로 반환한 후 응답값 json 정보가 있는 'responses' 폴더명을 붙여 반환합니다 
    """
    dir_path = os.path.dirname(os.path.abspath(__file__))
    return dir_path


if __name__ == '__main__':
    # 옵션1 : -f, -d : 2개의 파일 비교인지, 2개의 디렉토리 비교인지 
    # 옵션2,3 : origin / target
    # output path
    parser = argparse.ArgumentParser(description='comparing two files or directories (mode option f or d)')
    parser.add_argument('--mode', "-m",'--foo', choices=['f','d'], help='-f or -d, execute mode - comparing two files or direcotries')
    parser.add_argument('origin_path', help='origin file or directory')
    parser.add_argument('target_path', help='target file or directory')
    parser.add_argument('output_path', help='output path(diff files and csv report will be generated)')
    args = parser.parse_args()
    _mode = args.mode
    
    _origin_path = args.origin_path
    _target_path = args.target_path
    _output_path = args.output_path

    if _mode == "f":
        diff_ratio = image_file_compare(_origin_path, _target_path, _output_path)
        print(f"_compare_result = {diff_ratio}")
    elif _mode =="d":
        _output_path = _output_path+"/"+get_now_datetime()
        os.makedirs(_output_path)
        result_file = image_dir_compare(_origin_path, _target_path, _output_path)
        print(f"Finish - result file is generated in {result_file}")
    else:
        print("Not supporting mode(should -f or -d) - " +_mode)
        sys.exit(0)

    # python .\diffimg_image_compare.py -m d .\test_resource/img1 ./test_resource/img2 ./test_result
