from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('datainput.html')

@app.route('/submit', methods=['POST'])
def submit():
    classification = request.form.get('classification')
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

    with open('/Users/julianolschwang/Desktop/lockedstuff/completedata.csv', 'a', newline='') as csvfile:
        fieldnames = ['Classification', 'Pitch0', 'Roll0', 'Pitch1', 'Roll1', 'Pitch2', 'Roll2', 'Pitch3', 'Roll3', 'Pitch4', 'Roll4']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Classification': classification, 'Pitch0': pitch0, 'Roll0': roll0, 'Pitch1': pitch1, 'Roll1': roll1, 'Pitch2': pitch2, 'Roll2': roll2, 'Pitch3': pitch3, 'Roll3': roll3, 'Pitch4': pitch4, 'Roll4': roll4})
        
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)