// FUNCTIONS TO OPEN + CLOSE CONTACT FORM
function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

// FUNCTIONS TO GO TO ATTRACTION TABS FROM HEADER IMAGES
function openDining() {
    document.getElementById("dining_page").src = "dining_page.html";
}

function openAttractions() {
    document.getElementById("attractions_page")
}

function openTravel() {
    document.getElementById("attractions_page")
}

document.addEventListener("click", function(event){
    // IF CLICK HAPPENS ON CANCEL BUTTON OR ANYWHERE NOT ON THE CONTACT FORM AND THE CLICK DOESN'T HAPPEN ON ANY ELEMENT IN THE CONTACT CLASS, THEN CALL closeForm() FUNCTION
    if (event.target.matches(".cancel") || !event.target.closest(".form-popup") && !event.target.closest(".Pop_Up_Button") && !event.target.closest(".contact")){
        closeForm()
    }
}, false )