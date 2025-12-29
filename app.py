from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Bagian ini yang diubah dan diperpanjang
    return """
    <body style="background-color: #f0f0f0; display: flex; justify-content: center; align-items: center; height: 100vh; font-family: sans-serif;">
        <div style="background: white; padding: 50px; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); text-align: center;">
            <h1 style="color: #2c3e50;">Mantap Gilang! 🔥</h1>
            <p style="color: #7f8c8d; font-size: 1.2rem;">Ini adalah website pertama saya di Codespaces.</p>
            <button onclick="alert('Halo Gilang! Semangat belajarnya!')" 
                    style="background: #3498db; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 1rem;">
                Klik Saya
            </button>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)