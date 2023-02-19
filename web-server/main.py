import requests

def fetch():
	r = requests.get("https://api.escuelajs.co/api/v1/categories")

	categories = r.json()
	for category in categories:
		print(category["name"])


def run():
	fetch()

if __name__ == "__main__":
	run()