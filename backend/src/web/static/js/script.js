var  setActive = function(){
    url = window.location.href.split('/');
    var el =  document.getElementById(url[3]);
    el.className = el.className + " active";
};

window.onload = function(){
    setActive();
}

