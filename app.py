from fastapi import FastAPI,WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Rajat's Chat Application</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <style>
    :root {
      --bg: #f4f6f8;
      --panel: #ffffff;
      --user-msg: #dcfce7;
      --other-msg: #e5e7eb;
      --border: #d1d5db;
      --text: #111827;
      --accent: #2563eb;
    }

    * {
      box-sizing: border-box;
      font-family: system-ui, sans-serif;
    }

    body {
      margin: 0;
      background: var(--bg);
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .chat-wrapper {
      width: 100%;
      max-width: 420px;
      height: 90vh;
      background: var(--panel);
      border-radius: 12px;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 25px rgba(0,0,0,0.08);
      overflow: hidden;
    }

    .chat-header {
      padding: 14px;
      border-bottom: 1px solid var(--border);
      font-weight: 600;
      text-align: center;
    }

    .chat-messages {
      flex: 1;
      padding: 14px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .message {
      max-width: 80%;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 14px;
      line-height: 1.4;
    }

    .message.me {
      align-self: flex-end;
      background: var(--user-msg);
    }

    .message.other {
      align-self: flex-start;
      background: var(--other-msg);
    }

    .username {
      font-size: 11px;
      opacity: 0.7;
      margin-bottom: 2px;
    }

    .chat-input {
      display: flex;
      gap: 8px;
      padding: 12px;
      border-top: 1px solid var(--border);
    }

    .chat-input input {
      flex: 1;
      padding: 10px;
      border-radius: 8px;
      border: 1px solid var(--border);
      font-size: 14px;
      outline: none;
    }

    .chat-input input:focus {
      border-color: var(--accent);
    }

    .chat-input button {
      padding: 10px 14px;
      border-radius: 8px;
      border: none;
      background: var(--accent);
      color: #fff;
      cursor: pointer;
    }

    .username-modal {
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.4);
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .username-box {
      background: white;
      padding: 20px;
      border-radius: 10px;
      width: 280px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
  </style>
</head>

<body>

<div class="username-modal" id="usernameModal">
  <div class="username-box">
    <strong>Enter your name</strong>
    <input id="usernameInput" placeholder="Your name" />
    <button onclick="connect()">Join Chat</button>
  </div>
</div>

<div class="chat-wrapper">
  <div class="chat-header">Rajat's Chat</div>

  <div class="chat-messages" id="messages"></div>

  <div class="chat-input">
    <input id="messageInput" placeholder="Type a message..." />
    <button onclick="sendMessage()">Send</button>
  </div>
</div>


</body>
</html>


"""

@app.get("/")
async def get():
    return HTMLResponse(html)

