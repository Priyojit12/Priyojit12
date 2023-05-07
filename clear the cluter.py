import os
class co:
    def create(self):
        if(not os.path.exists("oa")):
            os.mkdir("oa")
        for i in range(0,10):
            os.mkdir(f"oa/f{i+1}")

    def rename(self):
        for i  in range(0,5):
            os.rename(f"oa/f{i+1}",f"oa/1.png{i+1}")
# a = co()
# a.create()
# a.rename()