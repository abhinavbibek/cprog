from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route("/")
def index():
    # Get a list of all JPG files in the "pics" folder
    img_files = [f for f in os.listdir("static") if f.endswith(".jpg")]
    # Select a random JPG file from the list
    img_file = random.choice(img_files)
    # Render the "index.html" template and pass in the selected image file
    return render_template("index.html", img_file=img_file)

if __name__ == "__main__":
    app.run(debug=True)
