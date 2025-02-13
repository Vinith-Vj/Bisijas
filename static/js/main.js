$(function() {
    
    "use strict";
    
    //===== Prealoder
    
    $(window).on('load', function(event) {
        $('.preloader').delay(500).fadeOut(500);
    });
    
    
    //===== Sticky

    $(window).on('scroll', function (event) {
        var scroll = $(window).scrollTop();
        if (scroll < 20) {
            $(".header_navbar").removeClass("sticky");
            // $(".header_navbar img").attr("src", "assets/images/logo.svg");
        } else {
            $(".header_navbar").addClass("sticky");
            // $(".header_navbar img").attr("src", "assets/images/logo-2.svg");
        }
    });
    
    
    //===== Section Menu Active

    var scrollLink = $('.page-scroll');
    // Active link switching
    $(window).scroll(function () {
        var scrollbarLocation = $(this).scrollTop();

        scrollLink.each(function () {

            var sectionOffset = $(this.hash).offset().top - 73;

            if (sectionOffset <= scrollbarLocation) {
                $(this).parent().addClass('active');
                $(this).parent().siblings().removeClass('active');
            }
        });
    });
    
    //===== close navbar-collapse when a  clicked

    // $(".navbar-nav a").on('click', function () {
    //     $(".navbar-collapse").removeClass("show");
    // });

    // $(".navbar-toggler").on('click', function () {
    //     $(this).toggleClass("active");
    // });

    // $(".navbar-nav a").on('click', function () {
    //     $(".navbar-toggler").removeClass('active');
    // });


    $(".navbar-nav a").on('click', function (e) {
        if (!$(this).closest('.nav-item').hasClass('dropdown')) {
            $(".navbar-collapse").removeClass("show");
            $(".navbar-toggler").removeClass('active');
        }
    });
    
    $(".navbar-toggler").on('click', function () {
        $(this).toggleClass("active");
    });
    
    
    //===== Counter Up
    
    $('.counter').counterUp({
        delay: 10,
        time: 3000
    });
    
    
    
    //===== Back to top
    
    // Show or hide the sticky footer button
    $(window).on('scroll', function(event) {
        if($(this).scrollTop() > 600){
            $('.back-to-top').fadeIn(200)
        } else{
            $('.back-to-top').fadeOut(200)
        }
    });
    
    
    //Animate the scroll to yop
    $('.back-to-top').on('click', function(event) {
        event.preventDefault();
        
        $('html, body').animate({
            scrollTop: 0,
        }, 1500);
    });
    
    
    //===== Nice Select
    
    $('select').niceSelect();
    
    
    //=====  WOW active
    
    var wow = new WOW({
        boxClass: 'wow', //
        mobile: false, // 
    })
    wow.init();
    
    
     
    
});



document.addEventListener("DOMContentLoaded", function () {
    let popup = document.getElementById("imagePopup");
    let popupImage = document.getElementById("popupImage");
    let closeBtn = document.querySelector(".popup .close");

    document.querySelectorAll(".pop-image").forEach(img => {
        img.addEventListener("click", function () {
            popupImage.src = this.getAttribute("data-src");
            popup.style.display = "flex"; // Show popup
        });
    });

    closeBtn.addEventListener("click", function () {
        popup.style.display = "none"; // Hide popup
    });

    popup.addEventListener("click", function (e) {
        if (e.target !== popupImage) { 
            popup.style.display = "none"; // Close when clicking outside the image
        }
    });
});