function edit_note(id_) {
  $(`#text-plus-logo${id_}`).replaceWith(`
    <form action="/edit_note/${id_}?scroll=${window.scrollY}" method="post">
        <div class="ml-3 flex items-center">
            <div class="">
                <input class="w-full" name="content${id_}" autofocus
                placeholder="Note" value="${$("#text" + id_)
                  .text()
                  .trim()}">
            </div>
            <div class="">
                <button type="submit" class="ml-2">
                    <svg xmlns="http://www.w3.org/2000/svg" width="1.75rem" height="1.75rem" fill="green"
                    class="bi bi-check2" viewBox="0 0 16 16">
                        <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0z"/>
                    </svg>
                </button>
            </div>
        </div>
    </form>`);
  $(`name=[content${id_}]`).focus();
}

window.setTimeout(function () {
  $(".alert").fadeTo(500, 0);
}, 3500);

function delete_note(note_id) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ note_id: note_id }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

// Seccion para ver/no ver la contraseña

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

$("#toggle-pwd").click(function () {
  $(this).toggleClass("fa-eye fa-eye-slash");
  var input = $($(this).attr("toggle"));
  if (input.attr("type") == "password") {
    input.attr("type", "text");
  } else {
    input.attr("type", "password");
  }
});
