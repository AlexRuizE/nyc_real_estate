"""Integrate S3 data to workflow"""

import boto3

def getS3Data(bucket=None, key=None):
	"""Get a file from S3."""
	assert all(v is not None for v in [bucket, key]), "Define a bucket and a key."
	s3 = boto3.client("s3")
	try:
		rObject = s3.get_object(Bucket=bucket, Key=key)
		return rObject['Body'].read()	# Bytes, not string
	except Exception as e:
		print(e)

def putS3Data():
	pass

