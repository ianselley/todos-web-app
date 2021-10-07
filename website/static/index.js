function edit_todo(end_point, id_) {
  const content_value = document.getElementById(`text${id_}`).innerText;
  $(`#text-plus-logo${id_}`).replaceWith(`
    <div class="w-full">
        <form class="grid grid-cols-auto-min" method="POST"
        action="/${end_point}/${id_}?scroll=${window.scrollY}">
            <input id="content${id_}" name="content${id_}" onclick="event.stopPropagation()" autofocus placeholder="Note">
            <button type="submit" class="ml-2">
                <svg xmlns="http://www.w3.org/2000/svg" width="1.75rem" height="1.75rem" fill="green"
                class="bi bi-check2" viewBox="0 0 16 16">
                    <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
                </svg>
            </button>
        </form>
    </div>
    `);
  $(`#content${id_}`).focus();
  $(`#content${id_}`).val(content_value);
}

function delete_alert() {
  $("#alert").remove();
}

function toggle_nav_items() {
  $("#nav-items").toggleClass("hidden");
}

function delete_note(note_id) {
  fetch(`/delete-note/${note_id}`, {
    method: "POST",
  }).then((_res) => {
    $(`#li-${note_id}`).remove();
  });
}

function check_note(note_id) {
  fetch(`/check-note/${note_id}`, {
    method: "POST",
  }).then((_res) => {
    $(`#complete-${note_id}`).toggleClass("complete");
  });
}

function toggle_important(note_id) {
  fetch("/toggle-important", {
    method: "POST",
    body: JSON.stringify({ note_id: note_id }),
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
