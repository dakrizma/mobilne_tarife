/***************************************************
    Table of contents:

    Functions:
      1. Responsive menu navigation
      2. Change text color

    Inits:
      1. initEvents();

    **********************************************/

// jshint multistr: true
var sty = sty || {};

// Responsive menu navigation
sty.toggleNavigation = function() {

    $('#main_menu').slideToggle('slow', function() {
        $(this)
        .toggleClass('show')
        .toggleClass('hide')
        .removeAttr('style')
        .addClass('js_toggleNavigation_init')
        ;
    });
}

// Change text color
sty.colorMe = function(settings) {

    var $el = settings.el; // $(this)
    var color = settings.color; // '#f00'

    $el.addClass('js_colorMe_init')
    .css('color', color);
    // js_klasa stavljena na inicijalizirani objekt
    // stavljen color iz settings
    // pojednostavljen primjer
}



// Funkcija za inicijalizaciju svih evenata
var initEvents = function () {

  // PRIMJER 1 (ovo je specijalan slučaj)
  $('#menu_btn').click(function(e){
    e.preventDefault();
    st.toggleNavigation();
  });


  // PRIMJER 2:
  // na svakom elementu s class="js_colorMe"
  $('.js_colorMe').each(function(){

    st.colorMe({
      'el': $(this),
      'color': '#f00'
    })

  });

}






$(document).ready( function() {
    // ovdje stavljamo neke inicijalne stvari

    initEvents();
   // initFancyBox(); // TODO: napraviti primjer
});