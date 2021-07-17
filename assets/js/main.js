
(function() {

	var backToTo = document.querySelector(".scroll-top");
	backToTo.style.display = "none";

	window.onscroll = function () {

        // show or hide the back-top-top button
		var backToTo = document.querySelector(".scroll-top");
		backToTo.style.display = "none";

        if (document.body.scrollTop > 350 || document.documentElement.scrollTop > 350) {
            backToTo.style.display = "flex";
        } else {
            backToTo.style.display = "none";
        }
    };


    // scroll 
    var pageLink = document.querySelectorAll('.page-scroll');
    
    pageLink.forEach(elem => {
        elem.addEventListener('click', e => {
            e.preventDefault();
            document.querySelector(elem.getAttribute('href')).scrollIntoView({
                behavior: 'smooth',
                offsetTop: 1 - 60,
            });
        });
    });


})();