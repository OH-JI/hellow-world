from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/test', methods=['GET'])
def listing():
    one = request.args.get('one')
    two = request.args.get('two')
    three = request.args.get('three')

    if one == "1":
        return render_template("index1.html")
    if one == "2":
        return render_template("index2.html")

    return jsonify({'msg':'GET 연결되었습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)