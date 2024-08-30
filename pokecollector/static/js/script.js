document.addEventListener("DOMContentLoaded", function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // collapsible sections
  var elems = document.querySelectorAll(".collapsible");
  var instance = M.Collapsible.init(elems);

  // confirm delete function
  function confirmDelete() {
    return confirm(
      "Are you sure you want to delete your account? This action can not be undone."
    );
  }

  // attach confirmDelete to the form's submite event
  var deleteForm = document.querySelector("form[action='/remove_user']");
  if (deleteForm) {
    deleteForm.addEventListener("submit", function (event) {
      if (!confirmDelete()) {
        event.preventDefault();
      }
    });
  }
});
