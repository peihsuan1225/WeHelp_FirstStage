var menu=document.querySelector(".menuItems");

function popupMenu(){
    menu.style.display = "block";
}

function closeMenu(){
    menu.style.display = "none";
}

window.addEventListener('resize', function() {
    var screenWidth = window.innerWidth;
    if (screenWidth > 600) {
        menu.style.display=""; 
    }
});
