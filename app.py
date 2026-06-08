from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template_string(
        "<h1>Python Webapp (AI-assisted)</h1><p>This simple Flask app was scaffolded with AI assistance.</p>"
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
