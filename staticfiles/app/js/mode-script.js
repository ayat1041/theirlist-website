const body = document.getElementById("body");
const darklight = document.getElementById("dark-switch");
const nav_dark = document.getElementById("nav");
const doc_dark = document.getElementById("doc-bar");
const searchterm = document.getElementById("query");
const searchbtn = document.getElementById("query-btn");
const login_menu = document.getElementById("login-sub-menu");
const addlist_menu = document.getElementById("add-list-sub-menu");
const ele_tit = document.getElementById("contain-sec");
const ele_tit2 = document.getElementById("contain-sec2");
const ele_tit3 = document.getElementById("contain-sec3");
const ele_tit4 = document.getElementById("contain-sec4");
const ele_tit5 = document.getElementById("contain-sec5");
const ele_tit6 = document.getElementById("contain-sec6");
const ele_tit7 = document.getElementById("contain-sec7");
const ele_tit8 = document.getElementById("contain-sec8");
const ele_tit9 = document.getElementById("contain-sec9");
const ele_tit10 = document.getElementById("contain-sec10");
const head_top = document.getElementById("headlline-top");
const head_middle = document.getElementById("headline-middle");
const head_bottom = document.getElementById("headline-bottom");
const fout = document.getElementById("fout");
const poster = document.getElementById("poster");

function darkmode() {
    body.classList.toggle("body-dark-mode");
    nav_dark.classList.toggle("nav-dark-mode");
    doc_dark.classList.toggle("doc-bar-dark-mode");
    searchterm.classList.toggle("searchTerm-dark-mode");
    searchbtn.classList.toggle("searchButton-dark-mode");
    login_menu.classList.toggle("login-sub-menu-dark-mode");
    addlist_menu.classList.toggle("add-list-sub-menu-dark-mode");
    head_top.classList.toggle("headline-top-dark-mode");
    head_middle.classList.toggle("headline-middle-dark-mode");
    head_bottom.classList.toggle("headline-bottom-dark-mode");
    fout.classList.toggle("fout-dark-mode");
    ele_tit.classList.toggle("contain-sec-dark-mode");
    ele_tit2.classList.toggle("contain-sec-dark-mode");
    ele_tit3.classList.toggle("contain-sec-dark-mode");
    ele_tit4.classList.toggle("contain-sec-dark-mode");
    ele_tit5.classList.toggle("contain-sec-dark-mode");
    ele_tit6.classList.toggle("contain-sec-dark-mode");
    ele_tit7.classList.toggle("contain-sec-dark-mode");
    ele_tit8.classList.toggle("contain-sec-dark-mode");
    ele_tit9.classList.toggle("contain-sec-dark-mode");
    ele_tit10.classList.toggle("contain-sec-dark-mode");
}

