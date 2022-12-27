import boto3
import json
import urllib.parse
from PIL import Image

# boto3.setup_default_session(profile_name='iamadmin-production')
s3 = boto3.client(service_name='s3')


def lambda_handler(event, context):
    try:

        # Get the bucket name and the object key from the incoming S3 event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        print(key)
        # file_obj = event["Records"][0]
        # filename = str(file_obj["s3"]["object"]["key"])

        print(f"Object created in {bucket} with key {key}")
        tmp_imgraw = '/tmp/' + str(key)  # create temporary file to save image to

        s3.download_file(bucket, key, tmp_imgraw)
        # Do further processing as required

        temp = Image.open(tmp_imgraw)

        # downsize the image with an ANTIALIAS filter (gives the highest quality)
        temp = temp.resize((300, 300), Image.ANTIALIAS)

        tmp_imagepro300 = '/tmp/' + 'resize' + str(key)  # create file to save resizedimage to
        temp.save(tmp_imagepro300)
        final_img = 'resizedimage300' + str(key)

        s3.upload_file(tmp_imagepro300, 's3photosfinal124', final_img)  # Upload resized image to bucket

        temp = Image.open(tmp_imgraw)

        # downsize the image with an ANTIALIAS filter (gives the highest quality)
        temp = temp.resize((600, 600), Image.ANTIALIAS)

        tmp_imagepro600 = '/tmp/' + 'resize' + str(key)  # create file to save resizedimage to
        temp.save(tmp_imagepro600)
        final_img = 'resizedimage600' + str(key)

        s3.upload_file(tmp_imagepro600, 's3photosfinal124', final_img)  # Upload resized image to bucket

        temp = Image.open(tmp_imgraw)

        # downsize the image with an ANTIALIAS filter (gives the highest quality)
        temp = temp.resize((900, 900), Image.ANTIALIAS)

        tmp_imagepro900 = '/tmp/' + 'resize' + str(key)  # create file to save resizedimage to
        temp.save(tmp_imagepro900)
        final_img = 'resizedimage900' + str(key)

        s3.upload_file(tmp_imagepro900, 's3photosfinal124', final_img)  # Upload resized image to bucket



    except Exception as e:
        print(e)