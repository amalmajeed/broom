'''

    Author: Amal Majeed
    Version: 1.0
    Created: 06/25/22
    Updated: 06/25/22
    Purpose: Script that automatically clusters up folders and files that are older than 6 months, 3 months and 1 months 
            for macOS environment.

'''

from calendar import month
import os
import time
import shutil

oneMonth = float(2630000)


class MonthCluster:
    def __init__(self, month=6, user=os.getlogin()):
        self.month = month
        self.threshold = self.month * oneMonth
        self.user = user

    def folderiser(self, endpoint="Downloads"):
        self.root = "/Users"+"/"+self.user+"/"+endpoint
        self.destination = self.root+"/"+"Older_"+str(self.month)+"Month"
        if(os.path.exists(self.destination)):
            print(f"Target path exists for {self.month} month folder!")
        else:
            os.makedirs(self.destination)
        self.listFiles = os.listdir(self.root)
        for file in self.listFiles:
            tMod = os.path.getmtime(self.root+"/"+file)
            gap = int((time.time()-tMod)//oneMonth)
            if(gap >= self.month):
                try:
                    shutil.move(self.root+'/'+file, self.destination)
                except Exception as e:
                    print(
                        f"Exception occured while moving to {self.destination} as : {e}\n")


mCluster_6 = MonthCluster(month=6)
mCluster_3 = MonthCluster(month=3)
mCluster_1 = MonthCluster(month=1)
mCluster_6.folderiser(endpoint="Desktop")
mCluster_3.folderiser(endpoint="Desktop")
mCluster_1.folderiser(endpoint="Desktop")
