let rate = "0.0";
const rating = document.querySelector('.rating');
let currentRatingElem = document.getElementById(rate);
currentRatingElem.checked = true;

rating.addEventListener("click", (e) => {
  if (e.target.type === 'radio') {
    // uncheck current rating
    currentRatingElem.checked = false;

    // update to target rating
    currentRatingElem = document.getElementById(e.target.value);
    rate = e.target.value;
    currentRatingElem.checked = true;

    // show text info
    showRatingInfo();
  }
})

function showRatingInfo() {
  const text = document.getElementById("rate-info");
  text.innerText = `${rate}/5.0`;
}

showRatingInfo();
