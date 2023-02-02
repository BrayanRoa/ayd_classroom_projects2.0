from dotenv import load_dotenv

load_dotenv(".env")
import cloudinary
import os

CLOUD_NAME = os.environ["CLOUD_NAME"]
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ALLOWED_PHOTO_EXTENSIONS = {"png", "jpg", "jpeg"}

cloudinary.config(cloud_name=CLOUD_NAME, api_key=API_KEY, api_secret=API_SECRET)


def allowed_photo_file(filename):
    return ("." in filename and filename.split(".")[-1] in ALLOWED_PHOTO_EXTENSIONS)
