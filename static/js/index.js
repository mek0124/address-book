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

document.addEventListener('DOMContentLoaded', function() {
  updateClock();

  const intervalId = setInterval(updateClock, 1000);
  return () => clearInterval(intervalId);
});