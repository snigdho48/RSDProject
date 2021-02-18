$(document).on('ready',function() {
	"use strict";
	
	/*----------------------------------------------
	 -----------Sticky Header  --------------------
	 -------------------------------------------------*/
	var navWrap = $('.mainmenu-area');
	if (navWrap.length) {
		var navWrap_Offset = $('.mainmenu-area').offset().top;
		$(window).on('scroll',function() {
			var top_scroll = $(window).scrollTop();
			if (top_scroll > navWrap_Offset) {
				navWrap.addClass('stricky');
			} else {
				navWrap.removeClass('stricky');
			}
		});
	}

	var stricky_header_top = $('.stricky-header__top');
	if (stricky_header_top.length) {
		var stricky_header_top_Offset = stricky_header_top.offset().top;
		$(window).on('scroll',function() {
			var top_scroll = $(window).scrollTop();
			if (top_scroll > stricky_header_top_Offset) {
				stricky_header_top.addClass('stricky');
			} else {
				stricky_header_top.removeClass('stricky');
			}
		});
	}
	/*----------------------------------------------
	 -----------Dropdown Function  --------------------
	 -------------------------------------------------*/
	var mobilemenuLink =  $('.mobile-menu> li >a');
	var mobilemenuLi =  $('.mobile-menu> li');
	var mobilemenuUl =  $('.mobile-menu> li >ul');
	mobilemenuLink.on('click', function() {
		if ($(window).width() <= 991) {
			mobilemenuLi.removeClass('on');
			mobilemenuUl.slideUp('normal');
			if ($(this).next().next('ul').is(':hidden') === true) {
				$(this).parent('li').addClass('on');
				$(this).next().next('ul').slideDown('normal');
			}
		}
	});
	/*----------------------------------------------
	 -----------Masonry Function  --------------------
	 -------------------------------------------------*/
	var container_masonry = $(".container-masonry");
	container_masonry.imagesLoaded(function() {
		container_masonry.isotope({
			itemSelector : '.nf-item',
			transitionDuration : '1s',
			percentPosition : true,
			masonry : {
				columnWidth : '.grid-sizer'
			}
		});
	});

	/*----------------------------------------------
	 -----------Masonry filter Function  --------------------
	 -------------------------------------------------*/
	var container_filter = $(".container-filter");
	container_filter.on("click", ".categories", function() {
		var a = $(this).attr("data-filter");
		container_masonry.isotope({
			filter : a
		});

	});
	/*----------------------------------------------
	 -----------Masonry filter Active Function  --------------------
	 -------------------------------------------------*/
	container_filter.each(function(e, a) {
		var i = $(a);
		i.on("click", ".categories", function() {
			i.find(".active").removeClass("active"), $(this).addClass("active");
		});
	});

	/*----------------------------------------------
	 -----------Masonry Grid view Function  --------------------
	 -------------------------------------------------*/
	var container_grid = $(".container-grid");
	container_grid.imagesLoaded(function() {
		container_grid.isotope({
			itemSelector : ".nf-item",
			layoutMode : "fitRows"
		});
	});

	/*----------------------------------------------
	 -----------Masonry Grid Filter Function  --------------------
	 -------------------------------------------------*/
	container_filter.on("click", ".categories", function() {
		var e = $(this).attr("data-filter");
		container_grid.isotope({
			filter : e
		});
	});

	/*----------------------------------------------
	 -----------isotope Function  --------------------
	 -------------------------------------------------*/
	var isotop_grid = $('#isotope');
	if (isotop_grid.length) {
		// init Isotope
		var $grid = isotop_grid.isotope({
			itemSelector : 'li	',
			percentPosition : true,
			layoutMode : 'fitRows',
			fitRows : {
				gutter : 0
			}
		});
	}
	/*----------------------------------------------
	 -----------Light Function  --------------------
	 -------------------------------------------------*/
	var fLight = $(".fancylight");
	if (fLight.length) {
		fLight.fancybox({
			openEffect : 'elastic',
			closeEffect : 'elastic',
			helpers : {
				media : {}
			}
		});
	}

	(function($) {
		"use strict";
		if ($("a[rel^='prettyPhoto'], a[data-rel^='prettyPhoto']").length != 0) {
			$("a[rel^='prettyPhoto'], a[data-rel^='prettyPhoto']").prettyPhoto({
				hook : 'data-rel',
				theme : "dark_square",
				social_tools : false,
				deeplinking : false
			});
		}
	})(jQuery);

	/* --------------------------------------------
	 Price Range Slier
	 -------------------------------------------- */
	var rangeJs = $(".range");
	if (rangeJs.length != 0) {
		rangeJs.nstSlider({
			"left_grip_selector" : ".leftGrip",
			"right_grip_selector" : ".rightGrip",
			"value_bar_selector" : ".bar",
			"value_changed_callback" : function(cause, leftValue, rightValue) {
				var $container = $(this).parent();
				$container.find('.leftLabel').text(leftValue);
				$container.find('.rightLabel').text(rightValue);
			},
			"highlight" : {
				"grip_class" : "gripHighlighted",
				"panel_selector" : ".highlightPanel"
			}
		});
		var highlightRangeButton = $('#highlightRangeButton');
		var nstSlider = $('.nstSlider');
		highlightRangeButton.on('click', function() {
			var highlightMin = Math.random() * 20,
			    highlightMax = highlightMin + Math.random() * 80;
			nstSlider.nstSlider('highlight_range', highlightMin, highlightMax);
		});
	}

	/* --------------------------------------------
	 Product Zoom
	 -------------------------------------------- */
	var single_product = $(".single-product");
	if (single_product.length !== 0) {
		var zoomWindowWidth;
		var zoomWindowHeight; zoomWindowWidth    :400; zoomWindowHeight   :470;
		if ($(window).width() < 992) { zoomWindowWidth    :0; zoomWindowHeight   :0;
			//zoomType = 'inner';
		}
		var zoomProduct = $("#zoom-product");
		zoomProduct.elevateZoom({
			gallery : 'zoom-product-thumb',
			cursor : 'pointer',
			galleryActiveClass : 'active',
			imageCrossfade : true,
			responsive : true,
			scrollZoom : false,
			zoomWindowWidth : zoomWindowWidth,
			zoomWindowHeight : zoomWindowHeight,
			//zoomType		: zoomType
		});

		zoomProduct.on("click", function(e) {
			var ez = zoomProduct.data('elevateZoom');
			$.fancybox(ez.getGalleryList());
			return false;
		});

	}
	var plusJs = $('.plus');
	var minusJs = $('.minus');
	plusJs.on('click', function() {
		$(this).parent('.product-regulator').find('.output').html(function(i, val) {
			return val * 1 + 1
		});
	});
	minusJs.on('click', function() {
		var ab = $(this).parent('.product-regulator').find('.output').html();
		if (1 <= ab) {
			$(this).parent('.product-regulator').find('.output').html(function(i, val) {
				return val * 1 - 1
			});
		}

	});

	/*----------------------------------------------
	 -----------Counter Function  --------------------
	 -------------------------------------------------*/
	var counter = $('.counter');
	if (counter.length) {
		counter.appear(function() {
			counter.each(function() {
				var e = $(this),
				    a = e.attr("data-count");
				$({
					countNum : e.text()
				}).animate({
					countNum : a
				}, {
					duration : 8e3,
					easing : "linear",
					step : function() {
						e.text(Math.floor(this.countNum));
					},
					complete : function() {
						e.text(this.countNum);
					}
				});
			});
		});
	}
	
//	Index_Service
	var service_slider_home = $(".service_slider_home");
	service_slider_home.owlCarousel({
		loop : true,
		nav : true,
		dots : false,
		center:true,
		margin : 30,
		responsive : {
			0 : {
				items : 1,
				center:false
			},
			767 : {
				items : 2,
				center:false
			},
			1200 : {
				items : 3
			}
		},
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"]

	});

//	index1_testimonial_slider
	var slider_testimonial = $(".home_testimonial");
	slider_testimonial.owlCarousel({
		loop : true,
		nav : true,
		dots : false,
		margin : 10,
		responsive : {
			0 : {
				items : 1
			},
			767 : {
				items : 2
			},
			992 : {
				items :2
			},
			1200 : {
				items : 2
			}
		},
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"]

	});
	


	/*----------------------------------------------
	-----------Slider Function  --------------------
	-------------------------------------------------*/
	//Blog Slider
	var itemCarousel_1 = $(".item1-carousel");
	itemCarousel_1.owlCarousel({
		loop : true,
		margin : 10,
		nav : true,
		dots : false,
		center : true,
		autoplay : true,
		autoplayTimeout : 2000,
		autoplayHoverPause : true,
		responsive : {
			0 : {
				items : 1

			},
			600 : {
				items : 1

			},
			1000 : {
				items : 1

			}
		},
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"]

	});

	//	Releted Project slider
	var relatedProject = $("#related-project");
	relatedProject.owlCarousel({
		loop : true,
		nav : true,
		dots : false,
		margin : 30,
		responsive : {
			0 : {
				items : 1
			},
			767 : {
				items : 2
			},
			992 : {
				items : 2
			},
			1200 : {
				items : 3
			}
		},
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"]

	});

	
	//	About page Carousel
	var carouselSlider = $('.abt-block__slider');
	carouselSlider.owlCarousel({
		loop : true,
		margin : 10,
		nav : false,
		dots : true,
		center : false,
		responsive : {
			0 : {
				items : 1
			},
			767 : {
				items : 1
			},
			992 : {
				items : 1
			},
			1200 : {
				items : 1
			}
		}
	});
		//About3-team
	var historyBlock = $('.team_carousel');
	historyBlock.owlCarousel({
		loop : true,
		margin : 0,
		nav : true,
		dots : false,
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"],
		responsive : {
			0 : {
				items : 1
			},
			767 : {
				items : 2
			},
			992 : {
				items : 4
			},
			1200 : {
				items : 4
			}
		}
	});
	//services-items
	var historyBlock = $('.history-block');
	historyBlock.owlCarousel({
		loop : true,
		margin : 30,
		nav : true,
		dots : false,
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"],
		responsive : {
			0 : {
				items : 1
			},
			767 : {
				items : 2
			},
			992 : {
				items : 3
			},
			1200 : {
				items : 4
			}
		}
	});

	var carouselSlider = $('.carousel-slider');
	carouselSlider.owlCarousel({
		loop : true,
		margin : 10,
		nav : true,
		dots : false,
		navText : ["<i class='ion-ios-arrow-back'></i>", "<i class='ion-ios-arrow-forward'></i>"],
		responsive : {
			0 : {
				items : 1
			},
			767 : {
				items : 2
			},
			992 : {
				items : 3
			},
			1200 : {
				items : 3
			}
		}
	});

	
	
	
	/* ---------------------
	 Owl Slider
	 /* --------------------- */
	"use strict";
	var owlCarousel = $('.owl-carousel');
	if (owlCarousel.length) {
		owlCarousel.each(function(index) {
			var effect_mode = $(this).data('effect');
			var autoplay = $(this).data('autoplay');
			var loop = $(this).data('loop');
			var margin = $(this).data('margin');
			var center = $(this).data('center');
			var autoplay = $(this).data('autoplay');
			var autoplayTimeout = $(this).data('autoplayTimeout');
			var autoplayHoverPause = $(this).data('autoplayHoverPause');
			var navigation = $(this).data('navigation');
			var prev_arrow = $(this).data('prev');
			var next_arrow = $(this).data('next');
			var pagination = $(this).data('pagination');
			var singleitem = $(this).data('singleitem');
			var items = $(this).data('items');
			var itemsdesktop = $(this).data('desktop');
			var itemsdesktopsmall = $(this).data('desktopsmall');
			var itemstablet = $(this).data('tablet');
			var itemsmobile = $(this).data('mobile');
			var nav22 = "namee";

			$(this).owlCarousel({
				loop : loop,
				margin : margin,

				nav : navigation,
				dots : pagination,
				autoplay : autoplay,
				autoplayTimeout : 2000,
				autoplayHoverPause : autoplayHoverPause,
				responsive : {
					0 : {
						items : itemsmobile
					},
					767 : {
						items : itemstablet
					},
					992 : {
						items : itemsdesktopsmall
					},
					1200 : {
						items : itemsdesktop
					}
				},

				navText : ["<i class='" + prev_arrow + "'></i>", "<i class='" + next_arrow + "'></i>"]
			});
		});
	}

	/*----------------------------------------------
	 -----------Search Input  --------------------
	 -------------------------------------------------*/
	var searchDropdown = $("#searchDropdown");
	var dropdownInput = $('.dropdown-input');
	searchDropdown.on('click', function() {
		dropdownInput.show();
	});
	var closeInput = $(".close-input");
	closeInput.on('click', function() {
		dropdownInput.hide();
	});
	/*----------------------------------------------
	 ----------- video  --------------------
	 -------------------------------------------------*/

	var videoBg = $(".bg-video");
	if (videoBg.length) {
		videoBg.mediaelementplayer({
			loop : !0,
			enableKeyboard : !1,
			iPadUseNativeControls : !1,
			pauseOtherPlayers : !1,
			iPhoneUseNativeControls : !1,
			AndroidUseNativeControls : !1,
			enableAutosize : !0,
			alwaysShowControls : !1
		});
	}
	$(window).height(function() {
		function e() {
			var e = $(window).innerHeight();
			$(".slider-hero, .full-screen-intro").css("height", e);
		}


		e(), $(window).on('resize', function() {
			e();
		});
	});
	/*----------------------------------------------
	 ----------- parallax Function  --------------------
	 -------------------------------------------------*/
	var parallaxs = $(".parallax");
	if (parallaxs.length) {
		parallaxs.parallax("50%", 0.02);
	}
	var parallaxs = $("#overlay_block");
	if (parallaxs.length) {
		parallaxs.parallax("50%", 0.02);
	}

	/*----------------------------------------------
	 ----------- Loader Function  --------------------
	 -------------------------------------------------*/
	var preloader = $("#preloader");
	preloader.delay(500).fadeOut();

	/*----------------------------------------------
	 ----------- Map Function  --------------------
	 -------------------------------------------------*/
	var mapWrap = $('#map');
	if (mapWrap.length) {
		google.maps.event.addDomListener(window, 'load', initialize);

	}
	
	/*-----------------------------------------------
	 -----------  style-switcher  --------------------
	 -------------------------------------------------*/
	//$("body").append('<div id="style-switcher"></div>');
	//$("#style-switcher").load("theme-option/swicher.html");
	
});

/*accordion*/
var accordion_select = $('.accordion');
if (accordion_select) {
	accordion_select.each(function() {
		$(this).accordion({
			"transitionSpeed" : 400,
			transitionEasing : 'ease-in-out'
		});
	});
}
/*MatchHeight*/
var matchHeigh = $('.matchHeigh');
if (matchHeigh.length) {
	if (matchHeigh) {
		matchHeigh.matchHeight();
	}
}
/*-----------------------------------------------
 -----------  Map Color Theme Function  ----------
 -------------------------------------------------*/
var mapWrap = $('#map');
if (mapWrap.length) {
	var myCenter = new google.maps.LatLng(51.538308, -0.3817765);
	function initialize() {
		var mapProp = {
			center : myCenter,
			zoom : 15,
			mapTypeId : google.maps.MapTypeId.ROADMAP,
			scrollwheel : false,
			styles : [{
				elementType : 'geometry',
				stylers : [{
					color : '#242f3e'
				}]
			}, {
				elementType : 'labels.text.stroke',
				stylers : [{
					color : '#242f3e'
				}]
			}, {
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#746855'
				}]
			}, {
				featureType : 'administrative.locality',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#d59563'
				}]
			}, {
				featureType : 'poi',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#d59563'
				}]
			}, {
				featureType : 'poi.park',
				elementType : 'geometry',
				stylers : [{
					color : '#263c3f'
				}]
			}, {
				featureType : 'poi.park',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#6b9a76'
				}]
			}, {
				featureType : 'road',
				elementType : 'geometry',
				stylers : [{
					color : '#38414e'
				}]
			}, {
				featureType : 'road',
				elementType : 'geometry.stroke',
				stylers : [{
					color : '#212a37'
				}]
			}, {
				featureType : 'road',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#9ca5b3'
				}]
			}, {
				featureType : 'road.highway',
				elementType : 'geometry',
				stylers : [{
					color : '#746855'
				}]
			}, {
				featureType : 'road.highway',
				elementType : 'geometry.stroke',
				stylers : [{
					color : '#1f2835'
				}]
			}, {
				featureType : 'road.highway',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#f3d19c'
				}]
			}, {
				featureType : 'transit',
				elementType : 'geometry',
				stylers : [{
					color : '#2f3948'
				}]
			}, {
				featureType : 'transit.station',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#d59563'
				}]
			}, {
				featureType : 'water',
				elementType : 'geometry',
				stylers : [{
					color : '#17263c'
				}]
			}, {
				featureType : 'water',
				elementType : 'labels.text.fill',
				stylers : [{
					color : '#515c6d'
				}]
			}, {
				featureType : 'water',
				elementType : 'labels.text.stroke',
				stylers : [{
					color : '#17263c'
				}]
			}]
		};
		var map = new google.maps.Map(document.getElementById("map"), mapProp);

		var marker = new google.maps.Marker({
			position : myCenter,
			icon : {
				url : 'assets/images/map-pin.png',
				size : new google.maps.Size(90, 111), //marker image size
				origin : new google.maps.Point(0, 0), // marker origin
				anchor : new google.maps.Point(35, 86) // X-axis value (35, half of marker width) and 86 is Y-axis value (height of the marker).
			}
		});

		marker.setMap(map);

	}

	function reloadStylesheets() {
		var queryString = 'reload=' + new Date().getTime();
		$('link[rel="stylesheet"]').each(function() {
			if (this.href.indexOf('?') === -1) {
				this.href = this.href + '&' + queryString;
			} else {
				this.href = this.href + '?' + queryString;
			}
		});
	}

}
