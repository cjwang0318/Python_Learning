import os
if __name__ == '__main__':
    #dirPath = r"Y:/BT/JAV_output"
    # 專案路徑
    project_dir = 'Y:/BT/JAV_output/'
    #project_dir = './JAV_output/'
    source = os.walk(project_dir)
    for folder, subfolders, filenames in source:
        #print(f'目前資料夾路徑為：{folder}')
        for subfolder in subfolders:
            print(f'{folder}的子資料夾為：{subfolder}')
        for filename in filenames:
            print(f'{folder}/{subfolder}內含檔案為：{filename}')
            current_path=f'{folder}/'
            current_path=current_path.replace("\\","/")
            #print("current_path:"+current_path)
            #rename thumb.jpg to folder_name.jpg
            if filename =="thumb.jpg":
                sourceName=f"{current_path}/thumb.jpg"
                targetName=f"{current_path}/{subfolder}.jpg"
                #print(sourceName)
                #print(targetName)
                os.rename(sourceName, targetName)
            if filename == "poster.jpg":
                targetName = f"{current_path}poster.jpg"
                os.remove(targetName)
            if ".nfo" in filename:
                targetName = f"{current_path}{filename}"
                #print(targetName)
                os.remove(targetName)