let currentUser = null;

function getCurrentUser() {
  const user = localStorage.getItem("user");
  if (!user) return window.location = "/login";
  currentUser = user;
}

getCurrentUser();
