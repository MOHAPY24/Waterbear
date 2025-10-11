import json
import datetime
from pathlib import Path
import errors
import os

class Waterbear:
    def __init__(self, dbpassword:int=None, dbfilename:str="waterbear_db1.json", autosnapshot:bool=True):
        self.dbfilename = dbfilename
        self.__dbpassword = dbpassword
        self.autosnapshot = autosnapshot
        self.snapshot_file = "db_snapshot.json"
        self.w = open(dbfilename, 'w')
        self.r = open(dbfilename , 'r')
        try:
            self.data = json.loads(self.r.read())
        except json.decoder.JSONDecodeError:
            self.data = {}
            pass
    
    def Get_Value(self, key:str):
        return self.data[key]
    
    def Update_Key(self, key:str, value, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            if self.autosnapshot:
                self.Snapshot()
            self.data[key] = value
        else:
            raise errors.PasswordInvalid()
    
    def Delete_Key(self, key:str, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            if self.autosnapshot:
                self.Snapshot()
            del self.data[key]
        else:
            raise errors.PasswordInvalid()
    
    def Reset_Db_Password(self, old_password:int, new_password:int):
        if old_password == self.__dbpassword:
            self.__dbpassword = new_password
        else:
            raise errors.PasswordInvalid()
    
    def Snapshot(self):

        with open(self.snapshot_file, "w") as f:
            f.write(json.dumps(self.data, indent=4))
    
    def Get_All(self):
        return self.data
    
    def Close(self, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            self.Push(dbpass)
        else:
            raise errors.PasswordInvalid()
    
    def Push(self, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            if self.data != {}:
                self.w.write(json.dumps(self.data, indent=4))
            else:
                self.w.write(self.data)
        else:
            raise errors.PasswordInvalid()
    
    def PushSnapshot(self, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            self.data = json.loads(open(self.snapshot_file, 'r').read())
        else:
            raise errors.PasswordInvalid()
    
    def Delete(self, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            if str(input("Are you sure you wanna delete the database, this cannot be overidden and can only be recovered by the snapshot (Y/N): ")).lower() == "y":
                self.data = {} 
                self.Push(dbpass)
            else:
                pass
        else:
            raise errors.PasswordInvalid()
    
    def DeleteNoPreserve(self, dbpass):
        if self.__dbpassword != None and dbpass == self.__dbpassword:
            if str(input("Are you sure you wanna delete the database, this cannot be overidden and the snapshot will be deleted (Y/N): ")).lower() == "y":
                self.data = {}
                open(self.snapshot_file, 'r+').truncate(0)
                self.Push(dbpass)
            else:
                pass
        else:
            raise errors.PasswordInvalid()


    


    
        




        