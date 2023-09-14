
function openSideNav() {
    let mainSideNav = document.getElementById("main-sidenav")
    let content = document.getElementById("content")
    mainSideNav.style.width = "250px";
    content.style.marginLeft = "250px";
    content.style.filter = "brightness(75%)";
    console.log('asdas')
  }

  function closeSideNav() {
    let mainSideNav = document.getElementById("main-sidenav")
    let content = document.getElementById("content")
    mainSideNav.style.width = "0";
    content.style.marginLeft = "0";
    content.style.filter = "brightness(100%)";
  }

  console.log('hello')