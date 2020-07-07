from __future__ import unicode_literals
import boto3
import os
# coding=utf-8
dir1=[]
dir2=[]
s3 = boto3.client('s3')
resp = s3.list_objects_v2(Bucket='vishnu-bucket-test')
for obj in resp['Contents']:
    if obj['Size']>0:
            dir1.append((obj['Key'].split("/"))[-1].strip())
print(dir1)
