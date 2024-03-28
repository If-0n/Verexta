
function updateUptime() {
    const uptimeElement = document.querySelector('.uptime');
    const currentTime = parseTime(uptimeElement.innerText.replace('Uptime: ', ''));
    const newTime = incrementTime(currentTime);
    uptimeElement.innerText = `Uptime: ${formatTime(newTime)}`;
}

function parseTime(timeString) {
    const [hours, minutes, seconds] = timeString.split(':').map(Number);
    return { hours, minutes, seconds };
}

function incrementTime(time) {
    time.seconds++;
    if (time.seconds === 60) {
        time.seconds = 0;
        time.minutes++;
        if (time.minutes === 60) {
            time.minutes = 0;
            time.hours++;
            if (time.hours === 24) {
                time.hours = 0;
            }
        }
    }
    return time;
}

function formatTime(time) {
    const pad = (num) => num.toString().padStart(2, '0');
    return `${pad(time.hours)}:${pad(time.minutes)}:${pad(time.seconds)}`;
}

function js_update_uptime() {
    setInterval(updateUptime, 1000);
}


eel.expose(js_update_uptime, 'js_update_uptime');





function updateMotd() {
    eel.update_motd()(function(response) {
        if (response !== null) {
            const motdElement = document.getElementById('motd');
            motdElement.innerText = response;
        } else {
            console.error('Failed to fetch MOTD.');
        }
    });
}
updateMotd();





function updateDiscord() {
    eel.update_discord()(function(response) {
        if (response !== null) {
            const discordElement = document.getElementById('discord');
            discordElement.innerHTML = `<div class="discord-info">${response}</div>`;
        } else {
            console.error('Failed to fetch Discord Info.');
        }
    });
}

updateDiscord();




function updateInfo() {
    eel.update_info()(function(response) {
        if (response !== null) {
            const discordElement = document.getElementById('raid-info');
            discordElement.innerHTML = `<div class="raid-info">${response}</div>`;
        } else {
            console.error('Failed to fetch Raiding Info.');
        }
    });
}

updateInfo();




    
const homeButton = document.getElementById('homebutt');
const moduleButton = document.getElementById('modulebutt');
const settingsButton = document.getElementById('settingsbutt');
    
const homeFrame = document.getElementById('frame-1');
const moduleFrame = document.getElementById('frame-2');
const settingsFrame = document.getElementById('frame-3');

    
toggleFrame(homeFrame);

homeButton.addEventListener('click', function() {
    toggleFrame(homeFrame);
});

moduleButton.addEventListener('click', function() {
    toggleFrame(moduleFrame);
});

settingsButton.addEventListener('click', function() {
    toggleFrame(settingsFrame);
});

function toggleFrame(frame) {
    homeFrame.style.display = 'none';
    moduleFrame.style.display = 'none';
    settingsFrame.style.display = 'none';

    frame.style.display = 'block';
}

