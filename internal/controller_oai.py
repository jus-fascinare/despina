import openai

class OpenAI_API_Controller:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def oai_prompt(self, model_name, prompt, max_tokens=None, temperature=None, n=None):
        """
        Send a prompt to the OpenAI API using the specified parameters.

        Args:
            model_name (str): The name of the model to use.
            prompt (str): The input prompt to send to the model (mandatory).
            max_tokens (int, optional): Maximum number of tokens in the response.
            temperature (float, optional): Temperature for controlling randomness.
            n (int, optional): Number of completions to request.

        Returns:
            list of str: List of generated completions.
        """
        params = {
            "model": model_name,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "n": n,
        }

        response = openai.Completion.create(**params)

        generated_texts = [choice.text for choice in response.choices]
        return generated_texts

# Example usage:
# Replace 'YOUR_API_KEY_HERE' with your actual API key
api_key = "YOUR_API_KEY_HERE"
controller = OpenAI_API_Controller(api_key)

model_name = "legal-text-converter"
prompt = "Translate this text to French: 'Legal document'"
max_tokens = 50
temperature = 0.7
n = 3

generated_completions = controller.oai_prompt(model_name, prompt, max_tokens=max_tokens, temperature=temperature, n=n)

for i, text in enumerate(generated_completions):
    print(f"Completion {i+1}: {text}")
