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

