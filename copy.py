import shutil

def copy_files():
    try:
        # 指定原始文件路径
        source_file = r'C:\Users\wjc00\Downloads\網頁\33333.html'
        
        # 指定目标文件夹路径
        destination_folder = r'C:\Users\wjc00\Downloads\網頁'

        # 循环复制文件
        for i in range(4, 24):
            destination_file = f"{destination_folder}\\{i}.html"
            shutil.copy2(source_file, destination_file)
            print(f"已成功复制文件 '{source_file}' 到 '{destination_file}'")
    
    except FileNotFoundError:
        print(f"找不到文件 '{source_file}'")
    except Exception as e:
        print(f"复制文件时发生错误: {str(e)}")

if __name__ == "__main__":
    copy_files()
