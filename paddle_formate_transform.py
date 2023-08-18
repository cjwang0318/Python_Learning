import json
from tqdm import tqdm
import cv2
def write_file(path, write_data):
    with open(path, 'w', encoding='utf-8') as writer:
        writer.writelines(write_data)


def det_format(f, path):
    data = json.load(f)
    output_det_list = []
    output_rec_list = []
    for fineName in tqdm(data):
        # print(data[fineName]["ann"])
        for dict in data[fineName]["ann"]:
            if dict["cls"] == "exp":
                result_dict = {}
                transcription=dict["transcription"]
                result_dict["transcription"] = transcription
                bbox_list = dict["bbox"]
                x1 = int(bbox_list[0])
                y1 = int(bbox_list[1])
                x3 = int(bbox_list[2])
                y3 = int(bbox_list[3])
                x2 = x3
                y2 = y1
                x4 = x1
                y4 = y3
                point1 = [x1, y1]
                point2 = [x2, y2]
                point3 = [x3, y3]
                point4 = [x4, y4]
                result_dict["points"] = [point1, point2, point3, point4]
                jsondict = json.dumps(result_dict)
                #print(f"{fineName}\t{jsondict}")
                output_det_list.append(f"{fineName}\t[{jsondict}]\n")
                #crap image for recogination
                img = cv2.imread(f"{path}/images/{fineName}")
                crop_img = img[y1:y3, x1:x3]
                #cv2.imshow("cropped", crop_img)
                #cv2.waitKey(0)
                cv2.imwrite(f"{path}/images_paddle/{fineName}", crop_img)
                output_rec_list.append(f"{fineName}\t{transcription}\n")
    return output_det_list, output_rec_list




if __name__ == '__main__':
    path="D:/temp/Products-Real/evaluation/"
    # Opening JSON file
    f = open(path+'annotations.json')
    output_dec_list, output_rec_list=det_format(f, path)
    write_file(path+"paddle_det.txt",output_dec_list)
    write_file(path + "paddle_rec.txt", output_rec_list)
    # Closing file
    f.close()