from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style='text-align:center;'>🛒 SIVA SHOP</h1>
    <div style='display:flex; flex-wrap:wrap; justify-content:center;'>
      <div style='border:1px solid #ccc; border-radius:15px; padding:10px; margin:10px; width:160px; text-align:center;'>
        <img src='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400' width='100%'>
        <h3>Headphones 🎧</h3><p>₹999</p><button style='background:orange;color:white;padding:10px;border:none;border-radius:8px;width:100%;'>BUY NOW</button>
      </div>
      <div style='border:1px solid #ccc; border-radius:15px; padding:10px; margin:10px; width:160px; text-align:center;'>
        <img src='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400' width='100%'>
        <h3>Smart Watch ⌚</h3><p>₹1999</p><button style='background:orange;color:white;padding:10px;border:none;border-radius:8px;width:100%;'>BUY NOW</button>
      </div>
    </div>
    <p style='text-align:center;'>Website is LIVE on Render!</p>
    """
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
