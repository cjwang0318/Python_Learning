import json
from tqdm import tqdm
def write_file(path, write_data):
    with open(path, 'w', encoding='utf-8') as writer:
        writer.writelines(write_data)


def det_format(f):
    data = json.load(f)
    output_list = []
    for fineName in tqdm(data):
        # print(data[fineName]["ann"])
        for dict in data[fineName]["ann"]:
            if dict["cls"] == "exp":
                result_dict = {}
                point_list = []
                result_dict["transcription"] = dict["transcription"]
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
                output_list.append(f"{fineName}\t[{jsondict}]\n")
    return output_list




if __name__ == '__main__':
    path="D:/temp/Products-Real/evaluation/"
    # Opening JSON file
    f = open(path+'annotations.json')
    output_list=det_format(f)
    write_file(path+"paddle_det.txt",output_list)
    # Closing file
    f.close()