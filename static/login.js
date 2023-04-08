const loginBtn = document.getElementById("login-button");
const error = document.getElementById("error");
loginBtn.addEventListener("click", login);

async function login() {
  // reset error
  error.innerHTML = "";

  const username = document.getElementById("username-input").value;
  if (!username) return;

  try {
    const req = await fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username: username
      })
    })

    const result = await req.json();

    if (result.error) {
      return error.innerHTML = `
        <div class="p-4 text-sm text-red-800 rounded-lg bg-red-50 dark:bg-gray-800 dark:text-red-400" role="alert">
          <span class="font-medium">${result.error}</div>
        </div>
      `;
    }

    localStorage.setItem("user", JSON.stringify(result));
    window.location = "/";
  } catch (error) {
    console.log(error);
  }
}
