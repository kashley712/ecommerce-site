/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

 // Add a click event listener to the button
 //
    // Redirect to the desired URL or template
   // window.location.href = "{% url 'shopitempage' %}";
  //});

  //
  
  // Template One (index.html) Animation
document.addEventListener('DOMContentLoaded', function () {
  // Select all product cards in template one
  const productCards = document.querySelectorAll('.col.mb-5');

  // Apply animation to each product card
  productCards.forEach(function (card, index) {
    card.style.animationDelay = index * 100 + 'ms';
    card.classList.add('animate__animated', 'animate__fadeInUp');
  });
});

// Template Two (shopitem.html) Animation
document.addEventListener('DOMContentLoaded', function () {
  // Select product details section in template two
  const productDetails = document.querySelector('.col-md-6');

  // Apply animation to product details section
  productDetails.classList.add('animate__animated', 'animate__fadeIn');

  // Select add to cart button in template two
  const addToCartBtn = document.querySelector('.btn.btn-outline-dark');

  // Apply animation to add to cart button on hover
  addToCartBtn.addEventListener('mouseenter', function () {
    addToCartBtn.classList.add('animate__animated', 'animate__shakeX');
  });

  // Remove animation from add to cart button on mouse leave
  addToCartBtn.addEventListener('mouseleave', function () {
    addToCartBtn.classList.remove('animate__animated', 'animate__shakeX');
  });
});
