from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure the Flask app for email sending
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'alternarrator@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'ywlb bzyd pinc ozcj'  # Replace with your generated App Password
app.config['MAIL_DEFAULT_SENDER'] = 'alternarrator@gmail.com'  # Default sender
app.secret_key = 'oqTd0lw9Jo'  # Required for session management

mail = Mail(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/librat')
def books():
    return render_template('librat.html')

@app.route("/sugjero", methods=['GET', 'POST'])
def suggest():
    if request.method == 'POST':
        book_name = request.form['book_name']
        author = request.form['author']
        suggestion = request.form['suggestion']
        
        # Prepare the email
        msg = Message("Book Suggestion", recipients=["krijimtar@gmail.com"])
        msg.body = f"Book Name: {book_name}\nAuthor: {author}\nSuggestion: {suggestion}"

        # Send the email
        try:
            mail.send(msg)
            flash("Sugjerimi juaj u ruajt. Faleminderit!", "success")
        except Exception as e:
            flash(f"Failed to send email: {str(e)}", "error")
        
        return redirect(url_for('suggest'))

    return render_template('sugjero.html')


@app.route('/view_pdf/<book_name>')
def view_pdf(book_name):
    return render_template('view_pdf.html', book_name=book_name)

if __name__ == '__main__':
    app.run(debug=True)