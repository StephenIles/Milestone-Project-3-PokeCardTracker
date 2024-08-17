document.addEventListener("DOMContentLoaded", function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // collapsible sections
  var elems = document.querySelectorAll(".collapsible");
  var instance = M.Collapsible.init(elems);
});
