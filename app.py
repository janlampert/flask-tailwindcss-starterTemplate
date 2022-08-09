from flask import Flask, render_template, url_for

# Run the following command at the beginning of every session:
# npm run watch-css
# Then just normally start your flask server.

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)