API = "55ffff3f376e89c8da919ac036752edb"

# import asyncio
import imgbbpy

def main():
    client = imgbbpy.SyncClient(API)
    image = client.upload(file='8.jpg')
    print(image.url)

main()
