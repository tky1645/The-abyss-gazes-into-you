import time as t
import datetime as dt




class CalcTime:
    
    def __init__(self):
       self.initialTime = t.time()
       self.startTime = dt.datetime.now()
       self.finishTime = dt.datetime.now()
       print("you started to  watch from : "+ str(dt.datetime.now()))

    def TryTest(self):
        print(t.time())

    def __GetDatetimeNow(self):
        datetime = dt.datetime.now()
        print(str(dt.datetime.now()))

    def StartTimer(self):
        self.startTime = dt.datetime.now()
        print("time start")


    def StopTimer(self):
        self.finishTime = dt.datetime.now()
        print("time stop")


    def Display(self):
        print("start  : " + str(self.startTime))
        print("finish : " + str(self.finishTime))
        print("Total  : " + str(self.finishTime - self.startTime))