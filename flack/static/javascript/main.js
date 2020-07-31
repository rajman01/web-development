const menuBtn = document.querySelector('.menu-btn');
const sideBar = document.getElementById('sidebar');
const trans = document.querySelectorAll('.transform');


function transform(x) {
    if (trans.length != 0){
    if (x.matches) {
        trans[0].classList.remove('btn-lg');
        trans[1].classList.remove('btn-lg');
        document.querySelectorAll('.btn-div').forEach(function(div){
            div.classList.remove('col-4');
            div.classList.add('col-5');
            
        });
    } else {
        trans[0].classList.add('btn-lg')
        trans[1].classList.add('btn-lg')
        document.querySelectorAll('.btn-div').forEach(function(div){
            div.classList.remove('col-5');
            div.classList.add('col-4');
            
        });
    }
    }
};

var x = window.matchMedia("(max-width:500px)");
transform(x);
x.addListener(transform);
let menuOpen = false;
menuBtn.addEventListener('click', () => {
    if (!menuOpen) {
        menuBtn.classList.add('open');
        sideBar.classList.add('active');
        menuOpen = true;
    } else {
        menuBtn.classList.remove('open');
        sideBar.classList.remove('active');
        menuOpen = false;
    }
});
