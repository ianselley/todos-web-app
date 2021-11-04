function edit_category(id, name) {
  $(`#text-plus-logo-${id}`).toggleClass("hidden");
  $(`#edit-${id}`).toggleClass("hidden");
  $(`#content-${id}`).focus();
  $(`#content-${id}`).val(name);
}

function delete_alert(index) {
  $(`#alert-${index}`).hide("slow");
}

function toggle_nav_items() {
  $("#nav-items").toggleClass("hidden");
}

function fetch_reload(url, id) {
  fetch(url, {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.reload();
  });
}

function show_modal(id, content) {
  $(`#modal-container-${id}`).toggleClass("show-modal");
  $(`#content-${id}`).focus();
  $(`#content-${id}`).val(content);
}

function apply_changes(id, content, category_id, details, expires) {
  fetch("/edit-note", {
    method: "POST",
    body: JSON.stringify({
      id: id,
      content: content,
      category_id: category_id,
      details: details,
      expires: expires,
    }),
  }).then((_res) => {
    location.reload(true);
  });
}

// Section to handle state of mobile menu options
document.addEventListener("click", (e) => {
  const isDropdownButton = e.target.matches("[mobile-options-button]");

  if (!isDropdownButton && e.target.closest("[mobile-options]") != null) return;

  let currentMenu;
  if (isDropdownButton) {
    currentMenu = e.target.closest("[mobile-options]");
    currentMenu.classList.toggle("active");
  }

  document.querySelectorAll("[mobile-options].active").forEach((menu) => {
    if (menu === currentMenu) return;
    menu.classList.remove("active");
  });
});

// Section to handle coloring of notes relative to the expiring date and current date
let today = new Date().toLocaleDateString();

document.querySelectorAll("[note-expires]").forEach((element) => {
  let element_date = element.getAttribute("note-expires");
  if (element_date !== "None" && element.getAttribute("complete") == null) {
    let date = new Date(element_date).toLocaleDateString();
    if (today > date) {
      element.classList.add("note-expired");
    } else if (today == date) {
      element.classList.add("expires-today");
    }
  }
});

// Section to toggle password visibility
const togglePassword = document.querySelector("#toggle-pwd");
const togglePasswordConfirm = document.querySelector("#toggle-pwd-confirm");
const password = document.querySelector("#password");
const passwordConfirm = document.querySelector("#password-confirm");

function togglePwd(element, eye) {
  // toggle the type attribute
  const type =
    element.getAttribute("type") === "password" ? "text" : "password";
  element.setAttribute("type", type);
  // toggle the eye slash icon
  eye.classList.toggle("fa-eye-slash");
}

if (togglePassword) {
  togglePassword.addEventListener("click", function () {
    togglePwd(password, togglePassword);
  });
}

if (togglePasswordConfirm) {
  togglePasswordConfirm.addEventListener("click", function () {
    togglePwd(passwordConfirm, togglePasswordConfirm);
  });
}

// Section to handle the scroll
let scrollpos = localStorage.getItem("scrollpos");
let previousPath = localStorage.getItem("previousPath");
let newPath = window.location.pathname;
let alert = document.querySelector(".alert");

if (scrollpos) {
  window.scrollTo(0, scrollpos);
}

window.addEventListener("beforeunload", function () {
  let before = window.location.pathname;
  let top;
  if (alert || previousPath !== newPath) {
    top = 0;
  } else {
    top = window.pageYOffset || document.documentElement.scrollTop;
  }
  localStorage.setItem("scrollpos", top);
  localStorage.setItem("previousPath", before);
});
