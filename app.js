const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Append a message to the chat box
function appendMessage(sender, text) {
  const message = document.createElement('div');
  message.classList.add(sender);
  message.textContent = text;
  chatBox.appendChild(message);
  chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
}

// Mock chatbot response
function getBotResponse(userMessage) {
  // Add simple logic here for demo
  if (userMessage.toLowerCase().includes('dream')) {
    return "That's an interesting dream! What goal would you like to set based on it?";
  }
  return "I'm here to log your dreams or help you set reminders. Tell me more!";
}

// Handle user input
sendBtn.addEventListener('click', () => {
  const userMessage = userInput.value.trim();
  if (userMessage) {
    appendMessage('user', userMessage);
    userInput.value = '';

    // Simulate bot response
    setTimeout(() => {
      const botMessage = getBotResponse(userMessage);
      appendMessage('bot', botMessage);
    }, 500);
  }
});

// Handle Enter key
userInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    sendBtn.click();
  }
});
