function updateClock() {
  let timeLabel = document.getElementById("time-display");
  let dateLabel = document.getElementById("date-display");

  const now = new Date()

  const timeOptions = {
    hour12: false,
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  };

  const dateOptions = {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  };

  const userLocation = navigator.language || 'en-US';

  const time = now.toLocaleTimeString(userLocation, timeOptions);
  const date = now.toLocaleDateString(userLocation, dateOptions);

  timeLabel.innerText = time;
  dateLabel.innerText = date;
};

function loadHeader() {
  fetch('/static/components/header.html')
    .then(response => response.text())
    .then(data => {
      document.body.insertAdjacentHTML('afterbegin', data);
      document.body.style.visibility = 'visible';
      updateClock(); // Call after header is loaded
      const intervalId = setInterval(updateClock, 1000);
    })
    .catch(error => console.error('Error loading header:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  loadHeader();
});