'''
Created on Dec 24, 2018

@author: siddardha.teegela
'''

class File():
    def __init__(self,fileName,mode):
        self.fileName = fileName
        self.mode = mode
        
    def __enter__(self):
        self.open_file = open(self.fileName,self.mode)
        return  self.open_file
    
    def __exit(self,*args):
        self.open_file.close()
        
    
if __name__ == "__main__":
    '''Creating objects'''
    file1 = File('demo.txt','r') 
    
    for x in range(10000):
        with File('demo.txt','r') as fileContextManger:
            print(fileContextManger.read())
    
'''
Other Context managers are
Lock objects in threading
zipfile.Zipfile, subporcess.Popen, tarfile.TarFile, telnetlib.Telnet, pathlib.Path are just a few
Essentially any object that needs to have close() after use must be a context manager
'''
