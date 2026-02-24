import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Супер-мобильный дизайн Leviathan VPN
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body { 
            background: #020617; 
            color: white; 
            font-family: 'Inter', sans-serif; 
            -webkit-tap-highlight-color: transparent;
            overflow: hidden;
        }
        .font-logo { font-family: 'Orbitron', sans-serif; }
        .glass { 
            background: rgba(15, 23, 42, 0.6); 
            backdrop-filter: blur(12px); 
            border: 1px solid rgba(51, 65, 85, 0.5); 
        }
        .neon-border {
            box-shadow: 0 0 15px rgba(59, 130, 246, 0.5);
            border: 1px solid rgba(96, 165, 250, 0.5);
        }
        .pulse {
            animation: pulse-animation 2s infinite;
        }
        @keyframes pulse-animation {
            0% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.05); opacity: 0.7; }
            100% { transform: scale(1); opacity: 1; }
        }
    </style>
</head>
<body class="flex flex-col items-center justify-between min-h-screen p-6 pb-10">
    
    <div class="w-full flex justify-between items-center mt-4">
        <div class="flex flex-col">
            <h1 class="font-logo text-xl font-black tracking-tighter text-blue-500">LEVIATHAN</h1>
            <p class="text-[8px] tracking-[0.4em] uppercase opacity-50">Secure Protocol v2.4</p>
        </div>
        <div class="w-10 h-10 rounded-full glass flex items-center justify-center neon-border">
            <div class="w-2 h-2 rounded-full bg-blue-500 pulse"></div>
        </div>
    </div>

    <div class="relative flex items-center justify-center my-12">
        <div class="absolute w-64 h-64 bg-blue-600/10 rounded-full blur-3xl"></div>
        <div class="z-10 w-48 h-48 rounded-full border-4 border-dashed border-blue-500/30 flex items-center justify-center p-4">
            <div class="w-full h-full rounded-full glass neon-border flex items-center justify-center">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-20 w-20 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
                </svg>
            </div>
        </div>
    </div>

    <div class="w-full glass rounded-[32px] p-6 space-y-4 mb-6">
        <div class="flex justify-between items-center border-b border-slate-700/50 pb-3">
            <span class="text-slate-400 text-sm">Твой IP:</span>
            <span class="text-sm font-mono text-blue-300">188.243.12.XX</span>
        </div>
        <div class="flex justify-between items-center">
            <span class="text-slate-400 text-sm">Статус:</span>
            <span class="text-sm font-bold text-red-500 uppercase tracking-widest">Не защищен</span>
        </div>
    </div>

    <button onclick="handleConnect()" class="w-full bg-blue-600 hover:bg-blue-500 py-5 rounded-[24px] font-black text-lg shadow-2xl shadow-blue-900/40 transition-all active:scale-95">
        ПОДКЛЮЧИТЬ VPN
    </button>

    <p class="text-slate-600 text-[10px] mt-6 uppercase tracking-widest font-bold">Deep Sea Encryption Active</p>

    <script>
        const tele = window.Telegram.WebApp;
        tele.expand();
        tele.ready();
        tele.headerColor = '#020617';

        function handleConnect() {
            tele.HapticFeedback.impactOccurred('heavy');
            tele.showConfirm("Хотите активировать Leviathan VPN для этого устройства?", (ok) => {
                if(ok) tele.showAlert("Подключение к серверу в Нидерландах...");
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
