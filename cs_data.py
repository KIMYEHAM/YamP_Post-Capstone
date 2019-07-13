import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

# save file from python(MCU) to COM
class saveData:
    def __init__(self, dev, val):
        self.val = val
        self.dev = dev
        self.saveAd = 'D:/YamP/Python/PyCharm Project/Post Capstone/Report/'

    # Get Time =======================================================
    def getTime(self):
        Now = datetime.datetime.now()
        Now_str = Now.strftime('%Y:%m:%d:%H:%M:%S')
        lst = Now_str.split(':')
        return lst

    def save_file(self):
        time_lst = self.getTime()
        dataAd  = self.saveAd + str(time_lst[0]) + str(time_lst[1]) + str(time_lst[2]) + '/'
        fileName = self.dev + str(time_lst[0]) + str(time_lst[1]) + str(time_lst[2]) + '.txt'  # title of file

        f = open(dataAd + fileName, 'a')
        f.write('{}{}{}{}{}{}-{}\n'.format(time_lst[0], time_lst[1], time_lst[2], time_lst[3], time_lst[4], time_lst[5],
                                           self.val))
        f.close()

# load data from file to python
class loadData:
    def __init__(self, dev, date):
        self.dev = dev
        self.baseAd = 'D:/YamP/Python/PyCharm Project/Post Capstone/Report/'
        self.dataAd = self.baseAd + date + '/'
        self.loadAd = self.dev + date + '.txt'

    def readFile(self):
        f = open(self.dataAd + self.loadAd, 'r')
        #print(self.dataAd + self.loadAd)
        dataSet = f.readlines()
        dataLst = [[0]*2 for i in range(len(dataSet))]
        for i in range(len(dataLst)):
            dataTmp = dataSet[i].split('-')
            dataTmp[1] = dataTmp[1][0:-1]
            dataLst[i] = dataTmp

        f.close()

        return dataLst

def fb_start():
    cred = credentials.Certificate("mykey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://post-capstone.firebaseio.com/'
    })


class fb_loadData:
    def __init__(self, dev, dataLst, loc):
        self.dev = dev
        self.dataLst = dataLst
        self.loc = loc


    def upload(self):
        for i in range(len(self.dataLst)):
            dataLoc = db.reference(self.loc + str(i))

            dataLoc.update({'dateTime' : self.dataLst[i][0]})
            dataLoc.update({'value'    : self.dataLst[i][1]})

class fb_getData:
    def __init__(self, dev, loc, dataLen):
        self.dev = dev
        self.loc = loc
        self.dataLen = dataLen


    def download(self):
        dataLst      = [0] * self.dataLen
        dataLst_date = [0] * self.dataLen
        dataLst_val  = [0] * self.dataLen

        for i in range(self.dataLen):
            dataLoc = db.reference(self.loc + str(i))
            dataLst[i] = dataLoc.get()
            dataLst_date[i] = dataLst[i]['dateTime']
            dataLst_val[i]  = dataLst[i]['value']


        return [dataLst_date, dataLst_val]