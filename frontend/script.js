document.getElementById('messageForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const sender = document.getElementById('sender').value;
    const message = document.getElementById('message').value;
    const recipients = document.getElementById('recipients').value.split(',');

    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ sender, message, recipients })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});