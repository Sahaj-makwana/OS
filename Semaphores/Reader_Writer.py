import threading
import time

class ReaderWriter():
    def __init__(self):
        self.rd = threading.Semaphore() 
                                       
        self.wrt = threading.Semaphore()  

        self.readCount = 0  

    def reader(self):
        while True:
            self.rd.acquire()  

            self.readCount+=1    

            if self.readCount == 1: 
                self.wrt.acquire() 
            self.rd.release()    

            print(f"Reader {self.readCount} is reading")

            self.rd.acquire() 

            self.readCount-=1   

            if self.readCount == 0: 
                self.wrt.release()  

            self.rd.release()      

            time.sleep(3)          

    def writer(self):
        while True:
            self.wrt.acquire()     

            print("Wrting data.....")
            print("-"*20)

            self.wrt.release()      

            time.sleep(3)    

    def main(self):
    
        t1 = threading.Thread(target = self.reader) 
        t1.start()
        t2 = threading.Thread(target = self.writer) 
        t2.start()
        t3 = threading.Thread(target = self.reader) 
        t3.start()
        t4 = threading.Thread(target = self.reader) 
        t4.start()
        t6 = threading.Thread(target = self.writer) 
        t6.start()
        t5 = threading.Thread(target = self.reader) 
        t5.start()

if __name__=="__main__":
    c = ReaderWriter()
    c.main()
