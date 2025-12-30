from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <head><title>Sukses!</title></head>
        <body style="text-align: center; font-family: sans-serif; margin-top: 50px;">
            <h1>🚀 Aplikasi Flask Berhasil Jalan!</h1>
            <p>Halo Gilang, kode ini berjalan di dalam GitHub Codespaces.</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    # Host 0.0.0.0 penting agar bisa diakses di Codespaces
    app.run(host='0.0.0.0', port=5000, debug=True)