let currentUser = null;

function getCurrentUser() {
  const user = localStorage.getItem("user");
  if (!user) return window.location = "/login";
  currentUser = JSON.parse(user);
}

getCurrentUser();

let rate = currentUser.rated[anime.title] ? `${currentUser.rated[anime.title]}` : "0.0";
console.log(rate);
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

const rateBtn = document.getElementById("rate-btn");
rateBtn.addEventListener("click", submitRate);

async function submitRate() {
  try {
    const req = await fetch("/api/rate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: currentUser.username,
        anime_name: anime.title,
        anime_rating: rate
      })
    })

    const result = await req.json();

    if (!result.error) {
      // save updated data back to local storage
      localStorage.setItem("user", JSON.stringify(result));
      window.location.href = "/";
    }
  } catch (error) {
    console.log(error);
  }
}
