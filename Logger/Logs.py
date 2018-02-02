
import json

def Registre(fileName="",data=None):

    try:
        with open(fileName, 'a') as f:
            f.write("\n")
            json.dump(data, f)
    except IOError:
        print("bir hata oluştu!")
    finally:
        f.close()
