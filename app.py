from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CONFESSION_FILE = "confessions.txt"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/write', methods=['GET', 'POST'])
def write_confession():
    if request.method == 'POST':
        confession = request.form.get('confession')
        if confession:
            with open(CONFESSION_FILE, 'a') as f:
                f.write(confession + '\n')
        return redirect(url_for('see_confessions'))
    return render_template('write.html')

@app.route('/see')
def see_confessions():
    try:
        with open(CONFESSION_FILE, 'r') as f:
            confessions = f.readlines()
    except FileNotFoundError:
        confessions = []
    return render_template('see.html', confessions=confessions)

if __name__ == '__main__':
    app.run(debug=True)
