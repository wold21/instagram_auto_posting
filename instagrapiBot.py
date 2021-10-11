from instagrapi import Client


def posting():
    manager = Client()  
    photos = ["./assets/nightmare1.jpg", "./assets/nightmare2.jpg", "./assets/nightmare3.jpg"]
    print("----------- Login -----------")
    manager.login("seohae_kim", "@Gur178432")
    print("----------- Uploading Photo -----------")
    manager.album_upload(photos, caption="test upload")  