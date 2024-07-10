import app.services.prompts as prompts
import logging
from app import gemini

class UseCase:
    def __init__(self):
        pass

    def run(data):

        try:
            categorization = prompts.prompt(data['description'])
            logging.debug("Prompt builded %s", categorization)

            categorization_response = gemini.gemini_pro(prompt=categorization).text

        except Exception as ex:
            logging.error(ex)

        return categorization_response