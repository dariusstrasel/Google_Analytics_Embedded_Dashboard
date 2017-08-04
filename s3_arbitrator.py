"""s3.arbitrator.py
Gets Google Service Account credentials from an S3 file object.
""" 

import boto3
import botocore
import os
import json

BUCKET_NAME = 'google-dashboard-service-key'
KEY = 'key.json'

def hasAWSEnviornmentalVariables():
    """Checks the presence of AWS Credentials in OS envoirnmental variables and returns a bool if True or False."""
    access_key = os.environ.get('ACCESS_KEY')
    secret_key = os.environ.get('SECRET_KEY')

    if access_key and secret_key:
        return True
    return False

def openS3Connection():
    """Returns a S3 connection object if AWS ENV tokens are found."""
    if hasAWSEnviornmentalVariables():
        return boto3.resource('s3')
    else:
        raise Exception("Could not find access tokens in OS ENV variables.")


def getJSONKeyDictionary():
    """Returns the body of S3 file "key.json" as a Python dictionary. """
    s3 = openS3Connection()
    s3_file_object = s3.Object(BUCKET_NAME, KEY) 

    response_binary = s3_file_object.get()['Body'].read() # This allows the file to be accessed without saving it the filesystem.
    response_as_dictionary = json.loads(response_binary.decode('utf-8'))

    return response_as_dictionary
