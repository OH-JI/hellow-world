from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test.html')

@app.route('/test', methods=['GET'])
def listing():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg':'GET 연결되었습니다!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)