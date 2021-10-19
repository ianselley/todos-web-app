document.addEventListener("DOMContentLoaded", function () {
  //The first argument are the elements to which the plugin shall be initialized
  //The second argument has to be at least a empty object or an object with your desired options
  OverlayScrollbars(document.querySelectorAll("body"), {});
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
    console.log(details);
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
