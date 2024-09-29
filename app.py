from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store confessions in a list for simplicity (or use a file or database)
confessions = []

@app.route('/')
def home():
    return render_template('index.html')

# Route for the Write Confession page (GET to view form, POST to submit confession)
@app.route('/write', methods=['GET', 'POST'])
def write_confession():
    if request.method == 'POST':
        # Get confession from the form
        confession = request.form.get('confession')
        
        # Save the confession to the list (or you can save it to a file)
        if confession:
            confessions.append(confession)

        # Redirect to see confessions page after submission
        return redirect(url_for('see_confessions'))
    
    # Render the write confession form if it's a GET request
    return render_template('write.html')

# Route for the See Confessions page
@app.route('/see')
def see_confessions():
    return render_template('see.html', confessions=confessions)

# Optional: if you want a separate route to handle form submission explicitly
@app.route('/save_confession', methods=['POST'])
def save_confession():
    confession = request.form.get('confession')
    if confession:
        confessions.append(confession)
    return redirect(url_for('see_confessions'))

if __name__ == '__main__':
    app.run(debug=True)

  