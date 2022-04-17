let isMenuOpened = false;
let modal_menu = document.getElementsByClassName('modal-menu')[0]
function openMenu(){
    if(!isMenuOpened){
        modal_menu.style.opacity = "100%";
        modal_menu.style.pointerEvents = "auto";
    }
    else{
        modal_menu.style.opacity = "0";
        modal_menu.style.pointerEvents = "none";
    }
    isMenuOpened = !isMenuOpened;
}
function clickLogo(){
    location.href = "/";
}