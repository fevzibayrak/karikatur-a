from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/kar1')
def kar1(): 
    return render_template('index.html')

@app.route('/kar2')
def kar2(): 
    return render_template('index1.html')

@app.route('/kar3')
def kar3(): 
    return render_template('index2.html')

@app.route('/kar4')
def kar4(): 
    return render_template('index3.html')

@app.route('/kar5')
def kar5(): 
    return render_template('index4.html')

@app.route('/kar6')
def kar6(): 
    return render_template('index5.html')

@app.route('/kar7')
def kar7(): 
    return render_template('index6.html')

@app.route('/kar8')
def kar8(): 
    return render_template('index7.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)