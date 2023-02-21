var menuIcon = document.getElementById("menuIcon")
var sideNav = document.getElementById("sideNav")
var menu = document.getElementById("menu")

menuIcon.onclick = function(){
    if(sideNav.style.right == "-250px")
    {
        sideNav.style.right = "0";
    }
    else{
        sideNav.style.right = "-250px";
    }
}

document.getElementById("skills").addEventListener("click", function() {
    window.scrollBy({
        top: window.innerHeight,
        behavior: 'smooth'
    })
    
})