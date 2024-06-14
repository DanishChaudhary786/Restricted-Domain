from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    # Ensure the 'static_site' directory exists
    os.makedirs('static_site', exist_ok=True)

    # Write the robots.txt file
    with open('static_site/robots.txt', 'w') as f:
        f.write("User-agent: *\nDisallow: /\n")

    # Generate the static index.html
    with open('static_site/index.html', 'w') as f:
        f.write("<h1>Welcome to my website</h1><p>Crawling is restricted here!</p>")

    print("Static site generated in the 'static_site' directory.")
