"""Integrate S3 data to workflow"""

import os
from b2blaze import B2
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




class IODataB2:
	"""Read/write remote data Using B2"""
	key_id="002b76795509bd80000000002"
	application_key="K0022KfEz54NeI7MvorXXivHq0vfWqY"

	def __init__(self, bucketName):
		self.b2 = B2(key_id=self.key_id, application_key=self.application_key)
		self.bucket = b2.buckets.get(bucketName) 

	def putLocal(self, localFile, remoteFile, numThreads=2):
		"""Put local file in remote bucket"""
		fileSize = os.path.getsize(localFile)/1000000 # Mb
		if fileSize>500:
			with open(localFile, "rb") as f:
				bucket.files.upload_large_file(contents=f, file_name=remoteFile, num_threads=numThreads)
		else:
			with open(localFile, "rb") as f:
				bucket.files.upload(contents=f, file_name=remoteFile)
		print("Uploaded {} to {}/{}".format(localFile, self.bucket.bucket_name, remoteFile))


	def getRemote(self):
		pass

