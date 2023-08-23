class APIKeyHandler:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def get_openai_api_key(self):
        return self.openai_api_key
