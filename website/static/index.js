let scrollpos = localStorage.getItem("scrollpos");
if (scrollpos) window.scrollTo(0, scrollpos); // This if statement can be modified to not scroll in some cases, but I don't know how to do it
// I may have to group all this into one function and call the fuction with a boolean parameter to determine wether or not I want to go to the beggining of the page
window.addEventListener("beforeunload", function (e) {
  let top = window.pageYOffset || document.documentElement.scrollTop;
  localStorage.setItem("scrollpos", top);
});

function edit_category(id, name) {
  $(`#text-plus-logo-${id}`).toggleClass("hidden");
  $(`#edit-${id}`).toggleClass("hidden");
  $(`#content-${id}`).focus();
  $(`#content-${id}`).val(name);
}

function edit_note(id, content) {}

function save_note_content_changes(id, content) {
  $(`#text-plus-logo-${id}`).toggleClass("hidden");
  $(`#edit-${id}`).toggleClass("hidden");
  $(`#edit-button-${id}`).toggleClass("hidden");
  $(`#modal-title-${id}`).text(content);
}

function delete_alert(index) {
  $(`#alert-${index}`).hide("slow");
}

function toggle_nav_items() {
  $("#nav-items").toggleClass("hidden");
}

function fetch_reload(url_, id_) {
  fetch(url_, {
    method: "POST",
    body: JSON.stringify({ id_: id_ }),
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
    window.location.reload();
  });
}

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

// Sección para ver/no ver la contraseña

// const togglePassword = document.querySelector("#toggle-pwd");
// const password = document.querySelector("#password");

// togglePassword.addEventListener("click", function (e) {
//   // toggle the type attribute
//   const type =
//     password.getAttribute("type") === "password" ? "text" : "password";
//   password.setAttribute("type", type);
//   // toggle the eye slash icon
//   this.classList.toggle("fa-eye-slash");
// });
