from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch a random cat image from the public API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    data = response.json()
    cat_url = data[0]['url']
    return render_template("index.html", cat_url=cat_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

