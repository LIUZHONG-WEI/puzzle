# puzzle
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # 使用環境變量 PORT，如果沒有則默認 5000
    app.run(host='0.0.0.0', port=port)
