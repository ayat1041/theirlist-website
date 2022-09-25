const menuBtn = document.querySelector('.menu-btn');
const subMenu = document.querySelector('.submenu');
const movieMore = document.querySelector('.movie-more');
const movieExpand = document.querySelector('.movie-expand');
const bookMore = document.querySelector('.book-more');
const bookExpand = document.querySelector('.book-expand');
const musicMore = document.querySelector('.music-more');
const musicExpand = document.querySelector('.music-expand');
const navmovieMore = document.querySelector('.nav-movie-more');
const navmovieExpand = document.querySelector('.nav-movie-expand');
const navbookMore = document.querySelector('.nav-book-more');
const navbookExpand = document.querySelector('.nav-book-expand');
const navmusicMore = document.querySelector('.nav-music-more');
const navmusicExpand = document.querySelector('.nav-music-expand');
const userdoclogo = document.querySelector('.user-doc-logo');
const userdocmenu = document.querySelector('.login-sub-menu');
const addlist = document.querySelector('#add-list-butt');
const addlistmenu = document.querySelector('.add-list-sub-menu');
const loader = document.getElementById("preloader");

// window.addEventListener("load", function(){
//   loader.style.display = "none";
// })


let addlistclick = false;
addlist.addEventListener('click', () => {
  if(!addlistclick) {
    addlistmenu.style.left = "0px";
    addlistclick = true;
    addlistmenu.style.transition = "all 250ms ease-in-out";
  } else {
    addlistmenu.style.left = "-65px";
    addlistclick = false;
  }
});


let menuOpen = false;
let movieExpandOpen = false;
let bookExpandOpen = false;
let musicExpandOpen = false;
let navmovieExpandOpen = false;
let navmusicExpandOpen = false;
let navbookExpandOpen = false;
let userdoclogoOpen = false;

userdoclogo.addEventListener('click', () => {
  if(!userdoclogoOpen){
    userdocmenu.style.bottom = "42px";
    userdocmenu.style.left = "5px";
    userdoclogoOpen = true;
    userdocmenu.style.transition = "all 100ms ease-in-out";
  } else {
    userdocmenu.style.left = "-200px";
    userdoclogoOpen = false;
  }
});

menuBtn.addEventListener('click', () => {
  if(!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true;
    subMenu.style.bottom = "76px";
    subMenu.style.transition = "all 250ms ease-in-out";
    document.body.scrollTop = 0;
    // document.documentElement.scrollTop = 0;
  } else {
    menuBtn.classList.remove('open');
    menuOpen = false;
    subMenu.style.bottom = "-60px";
    movieMore.style.display = "none";
    musicMore.style.display = "none";
    bookMore.style.display = "none";
    subMenu.style.transition = "all 250ms ease-in-out";
  }
});
movieExpand.addEventListener('click', () =>{
  if(!movieExpandOpen){
    movieMore.style.display = "block";
    musicMore.style.display = "none";
    bookMore.style.display = "none";
    movieExpandOpen = true;
    movieMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    movieMore.style.display = "none";
    movieExpandOpen = false;
    movieMore.style.transition = "all 250ms ease-in-out";
  }
});
bookExpand.addEventListener('click', () =>{
  if(!bookExpandOpen){
    bookMore.style.display = "block";
    movieMore.style.display = "none";
    musicMore.style.display = "none";
    bookExpandOpen = true;
    bookMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    bookMore.style.display = "none";
    bookExpandOpen = false;
    bookMore.style.transition = "all 250ms ease-in-out";
  }
});
musicExpand.addEventListener('click', () =>{
  if(!musicExpandOpen){
    musicMore.style.display = "block";
    movieMore.style.display = "none";
    bookMore.style.display = "none";
    musicExpandOpen = true;
    musicMore.style.transition = "all 250ms ease-in-out";
  }
  else{
    musicMore.style.display = "none";
    musicExpandOpen = false;
    musicMore.style.transition = "all 250ms ease-in-out";
  }
});



// desktop menu functions
