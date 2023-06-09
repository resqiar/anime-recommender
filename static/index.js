let currentUser = null;

function getCurrentUser() {
  const user = localStorage.getItem("user");
  if (!user) return window.location = "/login";
  currentUser = JSON.parse(user);
}

getCurrentUser();

async function getAnimeData() {
  if (!currentUser) return;

  try {
    const req = await fetch("/api/anime")
    const result = await req.json();

    renderAnime(result.animes);
  } catch (error) {
    console.log(error);
  }
}

getAnimeData();

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

          <div class="flex items-center">
          ${currentUser.rated[current.title] ?
        `<svg aria-hidden="true" class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><title>Rating star</title><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path></svg> <p class="ml-2 text-sm font-bold text-gray-900 dark:text-white">${currentUser.rated[current.title]}</p>`
        : ''
      }
          </div >
        </div >
      </div >
    </a >
    `;

    container.append(child);
  }
}

