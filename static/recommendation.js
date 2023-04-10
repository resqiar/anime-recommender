let currentUser = null;

function getCurrentUser() {
  const user = localStorage.getItem("user");
  if (!user) return window.location = "/login";
  currentUser = JSON.parse(user);
}

getCurrentUser();

async function getRecommendation() {
  if (!currentUser) return;

  try {
    const req = await fetch("/api/recommendation", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: currentUser.username
      })
    })
    const result = await req.json();

    if (result.error)
      return renderError(result.error);

    renderAnime(result.data);
  } catch (error) {
    console.log(error);
  }
}

getRecommendation();

function renderAnime(anime) {
  const container = document.getElementById("anime-list");
  container.innerHTML = "";

  for (let i = 0; i < anime.length; i++) {
    const current = anime[i];
    const child = document.createElement("div");

    child.innerHTML = `
    <a href="/rate/${current.id}">
      <div
        class="max-w-sm cursor-pointer bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
        <div><img class="rounded-t-lg min-h-[300px] max-h-[300px] w-full object-cover" src="${current.image}" /></div>
        <div class="p-5 h-full">
          <div>
            <h5 class="mb-2 text-xl font-bold max-w-[200px] tracking-tight text-gray-900 dark:text-white">
              ${current.title}
            </h5>
          </div>
        </div>
      </div>
    </a>
    `;

    container.append(child);
  }
}

function renderError(message) {
  const container = document.getElementById("anime-list");
  container.innerHTML = `
    <div class="my-16 font-medium">${message}</div>
  `;
}
