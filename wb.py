import db

if __name__ == "__main__":
    dB = db.Waterbear(1234,"water_bear.json", True) 
    dB.Update_Key("hi", "no", 1234)
    print(dB.Get_All())
    
    dB.Close(1234)
    
    