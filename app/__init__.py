from app.services.blob_reader import BlobReader
from app.services.gemini_pro import GeminiPro
import app.services.storage as storage
import os

# Reading CSV needed for the project
blob = storage.read(os.getenv('BUCKET_NAME'), os.getenv('BUCKET_FILE'))
blob_reader = BlobReader(os.getenv('BUCKET_NAME'), os.getenv('BUCKET_FILE'), blob=blob)
csv_file = blob_reader.read()

# Instance gemini model
gemini = GeminiPro(project=os.getenv('PROJECT_ID'), location=os.getenv('PROJECT_LOCATION'), model=os.getenv('DEFAULT_MODEL_VERSION'))