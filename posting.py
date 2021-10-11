from instabot import Bot as Manager
import os


photos = ["./assets/nightmare1.jpg", "./assets/nightmare2.jpg", "./assets/nightmare3.jpg"]
def deleteCookie():
    print("----------- Delete Cookie -----------")
    os.rmtree("./config")

def auto_posting():
    manager = Manager()
    print("----------- Login -----------")
    manager.login(username = "seohae_kim", password = "@Gur178432")
    print("----------- Upload Photo -----------")
    manager.upload_photo(photos, caption = "test_file🎉")
    deleteCookie()
    