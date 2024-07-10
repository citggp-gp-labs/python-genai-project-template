import app.services.csv as csv_services
import logging
class BlobReader:
    def __init__(self, bucket_name, bucket_file, blob):
        self.bucket_name = bucket_name
        self.bucket_file = bucket_file
        self.blob = blob
        logging.info("Object Blob Reader created")

    def read(self):
        try:
            with self.blob.open("r") as f:
                csv_mapper = csv_services.mapper_to_str(f)
            return csv_mapper
        except Exception as e:
            logging.error(e)