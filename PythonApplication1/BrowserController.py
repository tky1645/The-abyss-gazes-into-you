from selenium import webdriver as wd
import time
import calcTime as calc

class BrowserController:
    
    def __init__(self):
        self.driver = wd.Chrome()
        self.CT = calc.CalcTime()

        self.flag = False;

    def GetURL(self):
       print(str(self.driver.current_url))

    def test(self):
       self.driver.get("https://www.google.com/?hl=ja")

       while True:
           #現在のページタイトルを取得     
           #print(self.driver.title)
           
           #禁止サイトと比較
           if self.flag == False:
               if  self.IsBannedTitle(self.driver.title):
                    #タイマースタート    
                    self.CT.StartTimer()
                    self.flag = True

           if self.flag  and not self.IsBannedTitle(self.driver.title):
                #タイマーストップ＆視聴時間計算
                self.CT.StopTimer()
                self.CT.Display()
                self.flag =False


           time.sleep(1)

           
    def IsBannedTitle(self, title):
        if 'YouTube' in title :
            print("YOU WATCH 「YOUTUBE」!")
            return True
        if 'ニコニコ' in title :
            print("YOU WATCH 「ニコニコ」!")
            return True
        else:
            return False

