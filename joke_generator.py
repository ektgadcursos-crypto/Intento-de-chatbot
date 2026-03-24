import requests

class JokeGenerator:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_joke(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} - {joke_data['punchline']}"  # Customize based on the API response structure
        else:
            return "Failed to retrieve joke"

if __name__ == '__main__':
    api_url = 'https://official-joke-api.appspot.com/random_joke'  # Example API
    joke_gen = JokeGenerator(api_url)
    print(joke_gen.get_joke())