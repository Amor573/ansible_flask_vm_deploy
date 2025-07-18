from flask import Flask, render_template_string
import socket

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    all_servers = ["app1", "app2", "app3", "app4", "app5"]

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Load Balancer Visual</title>
        <style>
            body {
                background: #1f2937;
                color: #ffffff;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding-top: 50px;
                margin: 0;
                animation: fadeIn 1.5s ease-in;
            }

            h1 {
                color: #38bdf8;
                font-size: 3rem;
                margin-bottom: 20px;
            }

            .hostname {
                display: inline-block;
                padding: 15px 25px;
                background: #334155;
                border-radius: 15px;
                font-size: 1.3rem;
                animation: rotate 6s linear infinite;
                margin-bottom: 30px;
            }

            h2 {
                font-size: 2rem;
                color: #facc15;
                margin-top: 40px;
                margin-bottom: 20px;
            }

            ul {
                list-style: none;
                padding: 0;
                display: flex;
                justify-content: center;
                gap: 20px;
                flex-wrap: wrap;
            }

            li {
                background: #64748b;
                padding: 15px 25px;
                border-radius: 10px;
                width: 120px;
                animation: bounce 2s infinite;
                transition: transform 0.3s;
            }

            li:hover {
                transform: scale(1.1);
                background: #4ade80;
                color: #111827;
                font-weight: bold;
            }

            @keyframes rotate {
                0%   { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }

            @keyframes bounce {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-10px);
                }
            }

            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    </head>
    <body>
        <h1>⚙️ Load Balancer Status</h1>
        <div class="hostname">
            🖥️ Served by: <strong>{{ hostname }}</strong>
        </div>

        <h2>Active Servers</h2>
        <ul>
            {% for server in all_servers %}
                <li>{{ server }}</li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """

    return render_template_string(html, hostname=hostname, all_servers=all_servers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)   