'''

    Author: Amal Majeed
    Version: 1.0
    Created: 05/21/22
    Updated: 05/22/22
    Purpose: Script that automatically cleans up downloads and desktop to categorized folders in the macOS environment.

'''

import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class deskBroom:
    def __init__(self):
        self.root = '/Users/'+os.getlogin()+'/Desktop'
        self.imagelist = [x for x in os.listdir(self.root) if ((x.endswith('.jpg')) or (
            x.endswith('.jpeg')) or (x.endswith('.png')) or (x.endswith('.HEIC')) or (x.endswith('.PNG')) or (x.endswith('.JPG')))]
        self.videolist = [x for x in os.listdir(self.root) if (
            (x.endswith('.mp4')) or (x.endswith('.wav')) or (x.endswith('.mov')) or (x.endswith('.MOV')))]
        self.pdfs = [x for x in os.listdir(self.root) if x.endswith('.pdf')]
        self.audiolist = [x for x in os.listdir(self.root) if (
            (x.endswith('.mp3')) or (x.endswith('.MP3')))]
        self.textlist = [x for x in os.listdir(self.root) if (
            (x.endswith('.txt')) or (x.endswith('.TXT')))]
        self.documentlist = [x for x in os.listdir(self.root) if (
            (x.endswith('.pptx')) or (x.endswith('.ppt')) or (x.endswith('.PPT')) or (x.endswith('.PPTX')) or (x.endswith('.doc')) or (x.endswith('.docx')) or (x.endswith('.DOC')) or (x.endswith('.DOCX')))]
        self.ziplist = [x for x in os.listdir(self.root) if (
            (x.endswith('.zip')) or (x.endswith('.gz')))]

    # This function initializes the cleanup bin directories within the root directory if already not created
    def init_destinations(self):
        self.imagepath = self.root+'/IMAGES'
        self.videopath = self.root+'/VIDEOS'
        self.pdfpath = self.root+'/PDFS'
        self.audiopath = self.root+'/AUDIO'
        self.textpath = self.root+'/TEXT'
        self.docpath = self.root+'/DOCUMENTS'
        self.zippath = self.root+'/ZIPFILES'
        if(os.path.exists(self.imagepath)):
            print("image path exists !")
        else:
            os.makedirs(self.imagepath)
        if(os.path.exists(self.videopath)):
            print("video path exists !")
        else:
            os.makedirs(self.videopath)
        if(os.path.exists(self.pdfpath)):
            print("pdf path exists !")
        else:
            os.makedirs(self.pdfpath)
        if(os.path.exists(self.audiopath)):
            print("audio path exists !")
        else:
            os.makedirs(self.audiopath)
        if(os.path.exists(self.textpath)):
            print("text path exists !")
        else:
            os.makedirs(self.textpath)
        if(os.path.exists(self.docpath)):
            print("documents path exists !")
        else:
            os.makedirs(self.docpath)
        if(os.path.exists(self.zippath)):
            print("zip path exists !")
        else:
            os.makedirs(self.zippath)

    # This function handles the migration of stray files to the right destination bins
    def MigrationHandler(self):
        self.init_destinations()
        for i in self.imagelist:
            try:
                shutil.move(self.root+'/'+i, self.imagepath)
            except Exception as e:
                print("Exception occured moving to", self.imagepath, " ", e)
        for i in self.videolist:
            try:
                shutil.move(self.root+'/'+i, self.videopath)
            except Exception as e:
                print("Exception occured moving to", self.videopath, " ", e)
        for i in self.pdfs:
            try:
                shutil.move(self.root+'/'+i, self.pdfpath)
            except Exception as e:
                print("Exception occured moving to", self.pdfpath, " ", e)
        for i in self.audiolist:
            try:
                shutil.move(self.root+'/'+i, self.audiopath)
            except Exception as e:
                print("Exception occured moving to", self.audiopath, " ", e)
        for i in self.textlist:
            try:
                shutil.move(self.root+'/'+i, self.textpath)
            except Exception as e:
                print("Exception occured moving to", self.textpath, " ", e)
        for i in self.documentlist:
            try:
                shutil.move(self.root+'/'+i, self.docpath)
            except Exception as e:
                print("Exception occured moving to", self.docpath, " ", e)
        for i in self.ziplist:
            try:
                shutil.move(self.root+'/'+i, self.zippath)
            except Exception as e:
                print("Exception occured moving to", self.zippath, " ", e)

    # def printer(self):
    #     print(self.imagelist, self.videolist, self.pdfs)


class downloadBroom:
    def __init__(self):
        self.root = '/Users/'+os.getlogin()+'/Downloads'
        self.imagelist = [x for x in os.listdir(self.root) if ((x.endswith('.jpg')) or (
            x.endswith('.jpeg')) or (x.endswith('.png')) or (x.endswith('.HEIC')) or (x.endswith('.PNG')) or (x.endswith('.JPG')))]
        self.videolist = [x for x in os.listdir(self.root) if (
            (x.endswith('.mp4')) or (x.endswith('.wav')) or (x.endswith('.mov')) or (x.endswith('.MOV')))]
        self.pdfs = [x for x in os.listdir(self.root) if x.endswith('.pdf')]
        self.audiolist = [x for x in os.listdir(self.root) if (
            (x.endswith('.mp3')) or (x.endswith('.MP3')))]
        self.textlist = [x for x in os.listdir(self.root) if (
            (x.endswith('.txt')) or (x.endswith('.TXT')))]
        self.documentlist = [x for x in os.listdir(self.root) if (
            (x.endswith('.pptx')) or (x.endswith('.ppt')) or (x.endswith('.PPT')) or (x.endswith('.PPTX')) or (x.endswith('.doc')) or (x.endswith('.docx')) or (x.endswith('.DOC')) or (x.endswith('.DOCX')))]
        self.ziplist = [x for x in os.listdir(self.root) if (
            (x.endswith('.zip')) or (x.endswith('.gz')))]

    # This function initializes the cleanup bin directories within the root directory if already not created
    def init_destinations(self):
        self.imagepath = self.root+'/IMAGES'
        self.videopath = self.root+'/VIDEOS'
        self.pdfpath = self.root+'/PDFS'
        self.audiopath = self.root+'/AUDIO'
        self.textpath = self.root+'/TEXT'
        self.docpath = self.root+'/DOCUMENTS'
        self.zippath = self.root+'/ZIPFILES'
        if(os.path.exists(self.imagepath)):
            print("image path exists !")
        else:
            os.makedirs(self.imagepath)
        if(os.path.exists(self.videopath)):
            print("video path exists !")
        else:
            os.makedirs(self.videopath)
        if(os.path.exists(self.pdfpath)):
            print("pdf path exists !")
        else:
            os.makedirs(self.pdfpath)
        if(os.path.exists(self.audiopath)):
            print("audio path exists !")
        else:
            os.makedirs(self.audiopath)
        if(os.path.exists(self.textpath)):
            print("text path exists !")
        else:
            os.makedirs(self.textpath)
        if(os.path.exists(self.docpath)):
            print("documents path exists !")
        else:
            os.makedirs(self.docpath)
        if(os.path.exists(self.zippath)):
            print("zip path exists !")
        else:
            os.makedirs(self.zippath)

    # This function handles the migration of stray files to the right destination bins
    def MigrationHandler(self):
        self.init_destinations()
        for i in self.imagelist:
            try:
                shutil.move(self.root+'/'+i, self.imagepath)
            except Exception as e:
                print("Exception occured moving to", self.imagepath, " ", e)
        for i in self.videolist:
            try:
                shutil.move(self.root+'/'+i, self.videopath)
            except Exception as e:
                print("Exception occured moving to", self.videopath, " ", e)
        for i in self.pdfs:
            try:
                shutil.move(self.root+'/'+i, self.pdfpath)
            except Exception as e:
                print("Exception occured moving to", self.pdfpath, " ", e)
        for i in self.audiolist:
            try:
                shutil.move(self.root+'/'+i, self.audiopath)
            except Exception as e:
                print("Exception occured moving to", self.audiopath, " ", e)
        for i in self.textlist:
            try:
                shutil.move(self.root+'/'+i, self.textpath)
            except Exception as e:
                print("Exception occured moving to", self.textpath, " ", e)
        for i in self.documentlist:
            try:
                shutil.move(self.root+'/'+i, self.docpath)
            except Exception as e:
                print("Exception occured moving to", self.docpath, " ", e)
        for i in self.ziplist:
            try:
                shutil.move(self.root+'/'+i, self.zippath)
            except Exception as e:
                print("Exception occured moving to", self.zippath, " ", e)

    # def printer(self):
    #     print(self.imagelist, self.videolist, self.pdfs)


class Watcher:

    def __init__(self, directory='.', handler=FileSystemEventHandler()):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        self.observer.schedule(
            self.handler, self.directory, recursive=True)
        self.observer.start()
        print("\nWatcher Running in {}/\n".format(self.directory))
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
        self.observer.join()
        print("\nWatcher Terminated\n")


class MyHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        print(event)
        db = deskBroom()
        db.MigrationHandler()
        dd = downloadBroom()
        dd.MigrationHandler()


if __name__ == "__main__":
    w = Watcher('/Users/'+os.getlogin()+'/Downloads', MyHandler())
    w.run()
