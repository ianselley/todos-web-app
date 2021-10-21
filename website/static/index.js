let scrollpos = localStorage.getItem("scrollpos");
if (scrollpos) window.scrollTo(0, scrollpos); // This if statement can be modified to not scroll in some cases, but I don't know how to do it
// I may have to group all this into one function and call the fuction with a boolean parameter to determine wether or not I want to go to the beggining of the page
window.addEventListener("beforeunload", function (e) {
  localStorage.setItem("scrollpos", window.scrollY);
});

function edit_category(id, name) {
  $(`#text-plus-logo-${id}`).toggleClass("hidden");
  $(`#edit-${id}`).toggleClass("hidden");
  $(`#content-${id}`).focus();
  $(`#content-${id}`).val(name);
}

function edit_note(id, content) {
  $(`#text-plus-logo-${id}`).toggleClass("hidden");
  $(`#edit-${id}`).toggleClass("hidden");
  $(`#edit-button-${id}`).toggleClass("hidden");
  $(`#content-${id}`).focus();
  $(`#content-${id}`).val(content);
}

function change_note(id, content) {
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

function show_modal(id_) {
  $(`#modal-container-${id_}`).toggleClass("show-modal");
}

function apply_changes(id, content, details, expires) {
  fetch("/edit-note", {
    method: "POST",
    body: JSON.stringify({
      id: id,
      content: content,
      details: details,
      expires: expires,
    }),
  }).then((_res) => {
    window.location.reload();
  });
}

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

// $("#toggle-pwd").click(function () {
//   $(this).toggleClass("fa-eye fa-eye-slash");
//   var input = $($(this).attr("toggle"));
//   if (input.attr("type") == "password") {
//     input.attr("type", "text");
//   } else {
//     input.attr("type", "password");
//   }
// });
