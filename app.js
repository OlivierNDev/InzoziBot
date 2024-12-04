const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const API_BASE = "http://127.0.0.1:5000/api"; // Backend URL

// Append a message to the chat box
function appendMessage(sender, text) {
  const message = document.createElement('div');
  message.classList.add(sender);
  message.textContent = text;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
}

// Handle user input
sendBtn.addEventListener('click', async () => {
  const userMessage = userInput.value.trim();
  if (userMessage) {
    appendMessage('user', userMessage);
    userInput.value = '';

    try {
      // Send dream to backend and get analysis
      const response = await fetch(`${API_BASE}/analyze`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ dream: userMessage }),
      });
      const data = await response.json();

      if (response.ok) {
        appendMessage('bot', data.analysis);
      } else {
        appendMessage('bot', data.error || "Something went wrong.");
      }
    } catch (error) {
      appendMessage('bot', "Unable to connect to the server.");
    }
  }
});

// Handle Enter key
userInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    sendBtn.click();
  }
});
