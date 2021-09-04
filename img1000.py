import os

def search_del(path):
    file_list=os.listdir(path)
    for file in file_list:
        fpath=os.path.join(path,file)
        files=os.listdir(fpath)
        if(len(files)>1000):
            print("true")
            print("현재폴더")
            count=len(files)
            for img in files:
                fp=os.path.join(fpath,img)
                print("delete:",fp)
                os.remove(fp)
                count-=1
                if(count<1001):
                    print("남은 파일 1000개 삭제 멈춤")
                    break



path="F:\py" #경로지정

search_del(path)
    


