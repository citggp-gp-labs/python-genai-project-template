from flask import Flask, request, render_template
import app.use_case.use_case as use_case
import app.config.config as config
import google.cloud.logging
import logging
import os
from app import csv_file
from app.use_case.use_case import UseCase

config.load()

client = google.cloud.logging.Client()
client.setup_logging()

# Adding logs to the project
log_level = os.environ.get('LOG_LEVEL', 'INFO').upper()

level_mapping = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}

log_level_numeric = level_mapping.get(log_level, logging.INFO)

logging.getLogger().setLevel(log_level_numeric)

use_case = UseCase()

# Create a Flask app instance

app = Flask(__name__)

@app.get("/")
def hello():
    """Return a friendly HTTP greeting."""
    return "Sou uma AI Generativa que irá te ajudar na categorização dos produtos."
    
@app.post("/v2/unified_categorization")
def unified_categorization_v2():
    data = request.json
    logging.debug("Received request: %s", data)
    return use_case.run(data, csv_file)
