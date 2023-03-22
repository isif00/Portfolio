document.getElementById("skills").addEventListener("click", function() {
    window.scrollBy({
        top: window.innerHeight,
        behavior: 'smooth'
    })
    
})

const sectionHeight = document.querySelector('section').clientHeight;

document.getElementById("projects").addEventListener("click", function() {
    window.scrollBy({
        top: sectionHeight * -2,
        behavior: "smooth"
    })
    
})

