import os

if __name__ == '__main__':
     # 專案路徑
    project_dir = 'Y:/BT/JAV_output/'
    # project_dir = './JAV_output/'
    source = os.walk(project_dir)
    for folder, subfolders, filenames in source:
        print(f'目前資料夾路徑為：{folder}')
        for filename in filenames:
            currentPath = os.path.join(folder, filename)
            currentPath = currentPath.replace('\\', '/')
            print(f"currentPath={currentPath}")
            # print(os.path.join(folder, filename))
            # rename thumb.jpg to folder_name.jpg
            if filename == "thumb.jpg":
                subfolder = currentPath.rsplit('/')[-2]
                sourceName = os.path.join(folder, "thumb.jpg")
                sourceName = sourceName.replace('\\', '/')
                targetName = os.path.join(folder, f"{subfolder}.jpg")
                targetName = targetName.replace('\\', '/')
                # print(sourceName)
                # print(targetName)
                print(f"修改檔名 thumb.jpg -> {subfolder}.jpg")
                os.rename(sourceName, targetName)
            if filename == "poster.jpg":
                targetName = currentPath
                print(f"刪除 poster.jpg -> {targetName}")
                os.remove(targetName)
            if ".nfo" in filename:
                targetName = currentPath
                print(f"刪除 .nfo -> {targetName}")
                os.remove(targetName)
