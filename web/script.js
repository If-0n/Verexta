function submitForm() {
    var token = document.getElementById("name").value;
    eel.processToken(token)(function(result) {
        console.log(result);
    });
}

function updateUptime() {
    eel.get_uptime()(function(response) {
        const uptimeValue = document.getElementById("uptime-value");
        const seconds = Math.floor(response);
        uptimeValue.textContent = seconds + " seconds";
    });
}

// Call the updateUptime function every second
setInterval(updateUptime, 1000);