from flask import Flask, request, render_template
import scanner

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        results = scanner.scan(url)
        return render_template('index.html', results=results)
    return render_template('index.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)
app.run(debug=True, host='0.0.0.0', port=5000)
