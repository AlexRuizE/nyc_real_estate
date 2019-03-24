"""I/O data local/remote. Wrapper for b2blaze packages (https://github.com/sibblegp/b2blaze)."""

import os
from b2blaze import B2

class IODataB2:
	"""
	Read/write remote data Using B2.
	# Example:

	from nycreml.dataio import IODataB2
	b=IODataB2('trendcast')
	files=b.listFiles()
	data=b.getRemote('geospatial/nyc/rollingsales_manhattan.xls')
	with open('rollingsales_manhattan.xls', 'wb') as f:
		f.write(data)
	"""
	default_bucket='trendcast'
	key_id="002b76795509bd80000000002"
	application_key="K0022KfEz54NeI7MvorXXivHq0vfWqY"

	def __init__(self, bucketName):
		self.b2 = B2(key_id=self.key_id, application_key=self.application_key)
		self.bucket = self.b2.buckets.get(bucketName) 

	def listFiles(self, names=True):
		"""List files. If <names> is true, return actual filenames, otherwise return file objects."""
		files = self.bucket.files.all()
		if names:
			return [f.file_name	 for f in files]
		else:
			return files

	def getRemote(self, name):
		"""Get remote file from remote bucket. As bytes."""
		f_obj=self.bucket.files.get(name)
		return  f_obj.download().read()

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


def getS3Data(bucket=None, key=None):
	"""Get a file from S3. DEPRECATED"""
	assert all(v is not None for v in [bucket, key]), "Define a bucket and a key."
	s3 = boto3.client("s3")
	try:
		rObject = s3.get_object(Bucket=bucket, Key=key)
		return rObject['Body'].read()	# Bytes, not string
	except Exception as e:
		print(e)

