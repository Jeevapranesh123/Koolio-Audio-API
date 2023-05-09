import pymongo
import os
import hashlib
from hurry.filesize import size
from mutagen.mp3 import MP3
import wave


class FileUpload:
    
    def __init__(self) -> None:
        self.client = pymongo.MongoClient(
            os.getenv("DB_HOST"),
            username=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
        )
        self.db = self.client["file_upload"]
        self.collection = self.db["files"]
        self.file_dir = "uploads"
        
        if not os.path.exists(self.file_dir):
            os.mkdir(self.file_dir)
        
    def upload(self, file):
        file_name = file.filename
        title = file_name.split(".")[0]
        extension = file_name.split(".")[1]
        file_id = self.generate_id(file_name.encode())
    
        fpath = os.path.join(self.file_dir,file_id)
        
        file.save(fpath)
        
        fsize=size(self.get_file_size(fpath))
        time=self.get_file_length(fpath,extension)
        length="{}:{}".format(int(time[0]),int(time[1]))
        
        meta_data = self.gen_metadata(file_id,title,extension,fsize,length,fpath)
        meta_data = self.process_data(meta_data)
        self.store_metadata(meta_data)
        
        return meta_data
            
    def generate_id(self,fname):
        return hashlib.md5(fname).hexdigest()
    
    def gen_metadata(self,id,title,type,size,length,path):
        data = {
            "id":id,
            "title":title,
            "type":type,
            "size":size,
            "length":length,
            "path":path,
            "genre":""   
        }
        return data
        
    def store_metadata(self,meta):
        self.collection.insert_one(meta)
        
    
    def get_file_size(self,file):
        return os.path.getsize(file)
    
    def get_file_length(self,file,type):
        if type=="wav":
            return self.get_wav_length(file)

        audio = MP3(file)

        audio_info = audio.info    

        length_in_secs = int(audio_info.length)

        mins, seconds = self.convert(length_in_secs)
        return mins, seconds
    
    
    def convert(self,seconds):
        hours = seconds // 3600
        seconds %= 3600

        mins = seconds // 60
        seconds %= 60

        return mins, seconds
    
    def process_data(self,meta_data):
        for i in meta_data.values():
            if i == None or i == "":
                i = "NA"
        return meta_data
    
    def get_wav_length(self,file):

        with wave.open(file) as mywav:
            duration_seconds = mywav.getnframes() / mywav.getframerate()
        
        mins, seconds = self.convert(duration_seconds)
        return mins, seconds        
        
                    