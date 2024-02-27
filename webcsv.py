from flask import Flask, render_template, request, redirect
from flask import render_template_string
import csv

app = Flask('__name__')

data = []

@app.route('/create')
def create():
    
    return render_template_string('''
        <form action="{{ url_for('submit')}}"method="post">
        <input type="text" name="Classification" placeholder="Classification" required="required" /><br>
        <input type="text" name="Pitch0" placeholder="Pitch 0" required="required" /><br>
    	<input type="text" name="Roll0" placeholder="Roll 0" required="required" /><br>
    	<input type="text" name="Pitch1" placeholder="Pitch 1" required="required" /><br>
    	<input type="text" name="Roll1" placeholder="Roll 1" required="required" /><br>
    	<input type="text" name="Pitch2" placeholder="Pitch 2" required="required" /><br>
    	<input type="text" name="Roll2" placeholder="Roll 2" required="required" /><br>
    	<input type="text" name="Pitch3" placeholder="Pitch 3" required="required" /><br>
    	<input type="text" name="Roll3" placeholder="Roll 3" required="required" /><br>
    	<input type="text" name="Pitch4" placeholder="Pitch 4" required="required" /><br>
    	<input type="text" name="Roll4" placeholder="Roll 4" required="required" /><br> 
        <button type="submit">Submit</button>

    ''')
    
@app.route('/submit', methods=['POST'])
def submit():
    classification = request.form.get('Classification')
    pitch0 = request.form.get('Pitch0')
    roll0 = request.form.get('Roll0')
    pitch1 = request.form.get('Pitch1')
    roll1 = request.form.get('Roll1')
    pitch2 = request.form.get('Pitch2')
    roll2 = request.form.get('Roll2')
    pitch3 = request.form.get('Pitch3')
    roll3 = request.form.get('Roll3')
    pitch4 = request.form.get('Pitch4')
    roll4 = request.form.get('Roll4')
    
    with open('completedata.csv', 'a') as f:
        f.write(f"{classification},{pitch0},{roll0},{pitch1},{roll1},{pitch2},{roll2},{pitch3},{roll3},{pitch4},{roll4}\n")
        
    return redirect('/')

@app.route('/')
def read():
    data = []
    with open('completedata.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(dict(row))
     return render_template_string('''
        <html>
            <head>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
            </head>
            <body>
                {{data}}
            </body>
        </html>
    ''', data = str(data))

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
