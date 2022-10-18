import cloudinary
from cloudinary import  uploader as c_uploader, api as c_api

cloudinary.config( 
  cloud_name = "student147", 
  api_key = "867159752559147", 
  api_secret = "Te-PyNNmGLcb_Ic7uU-lVDphyRs" 
)

print(c_uploader.upload("imgbb.py"))
#print(c_api.delete_all_resources())

"""
[LOG] Running From:  /storage/emulated/0/C_coding/Python/Web Leach/Web-leach/Web-leach_CLI/v7/upload_test/cloudinary_upload.py
[LOG] Program started:  2022-09-08 03;48;10.424694
 ==============================

{'asset_id': '9581aff394453ba02a162f630710fbe6', 'public_id': 'lfwqgb5w7oeiocfty0uj', 'version': 1662587294, 'version_id': 'a74fc8521846ca7a02255b8cb470ae66', 'signature': '2ab5367b435e16b55e39515eb88093f4a91781d9', 'width': 1280, 'height': 1814, 'format': 'jpg', 'resource_type': 'image', 'created_at': '2022-09-07T21:48:14Z', 'tags': [], 'bytes': 546921, 'type': 'upload', 'etag': '418048d356e6e31a1ef703bf1e8d4125', 'placeholder': False, 'url': 'http://res.cloudinary.com/student147/image/upload/v1662587294/lfwqgb5w7oeiocfty0uj.jpg', 'secure_url': 'https://res.cloudinary.com/student147/image/upload/v1662587294/lfwqgb5w7oeiocfty0uj.jpg', 'folder': '', 'original_filename': '8', 'api_key': '867159752559147'}


[LOG] [Runtime:  4.6191253662109375 s]

[Program finished]


[LOG] Running From:  /storage/emulated/0/C_coding/Python/Others/Insta save/bot-1.py
[LOG] Program started:  2022-09-08 04;00;06.503301
 ==============================

/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.9/site-packages/telegram/ext/_applicationbuilder.py:270: PTBUserWarning: `Application` instances should be built via the `ApplicationBuilder`.
  ] = DefaultValue.get_value(  # pylint: disable=not-callable
2022-09-08 04:00:11,265 - apscheduler.scheduler - INFO - Scheduler started
2022-09-08 04:00:11,265 - telegram.ext._application - INFO - Application started
working
{'file_id': 'CgACAgUAAxkBAAIBemMZFJWHUp_K6-_av2R-Qrtoh3a0AAJMBgACULbIVKPGIzeNS-5bKQQ', 'file_size': 28014, 'file_unique_id': 'AgADTAYAAlC2yFQ', 'file_path': 'https://api.telegram.org/file/bot5552810521:AAHkdE9KwGnKIghb6ZdwT-SyhejDV551QGA/animations/file_7.mp4'}

"""