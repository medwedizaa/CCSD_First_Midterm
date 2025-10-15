from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def cat():
    try:
        # Получаем случайное изображение кота
        url = requests.get("https://api.thecatapi.com/v1/images/search").json()[0]['url']
        html = f"""
        <html>
        <head><title>Random Cat</title></head>
        <body style='text-align:center; font-family:Arial'>
            <h2>Here is your random cat 😺</h2>
            <img src='{url}' width='400'>
            <p><a href='/'>Get another one</a></p>
        </body></html>
        """
        return render_template_string(html)
    except Exception as e:
        return f"<h3>Error loading cat image: {e}</h3>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

