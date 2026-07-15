class ModelManager:
    AVAILABLE_MODELS = [
        "mistral",
        "llama3",
        "phi3"
    ]

    def list_models(self):
        return self.AVAILABLE_MODELS

    def validate(self, model):
        return model in self.AVAILABLE_MODELS