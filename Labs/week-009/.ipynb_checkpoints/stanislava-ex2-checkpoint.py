import math
@app.route('/sqrt/<num>')
def squared_root_num(num):
    return str(math.sqrt(int(num)))

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Nice to meet you!"

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)