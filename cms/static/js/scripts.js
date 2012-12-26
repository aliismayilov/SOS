$(document).ready(function() {
	$('.carousel').carousel();
	
	$(".tweet").tweet({
		avatar_size: 32,
		count: 1,
		username: "sos_children",
		template: "{text}"
	});

	$('#shareme').sharrre({
		share: {
			twitter: true,
			facebook: true,
			googlePlus: true
		},
		template: '<div class="box"><div class="left">Share</div><div class="middle"><a href="#" class="facebook">f</a><a href="#" class="twitter">t</a><a href="#" class="googleplus">+1</a></div><div class="right">{total}</div></div>',
		enableHover: false,
		enableTracking: true,
		render: function (api, options) {
			$(api.element).on('click', '.twitter', function () {
				api.openPopup('twitter');
			});
			$(api.element).on('click', '.facebook', function () {
				api.openPopup('facebook');
			});
			$(api.element).on('click', '.googleplus', function () {
				api.openPopup('googlePlus');
			});
		}
	});


}).bind("loaded", function () {
	$(this).find("a.tweet_action").click(function(ev) {
		window.open(this.href, "Retweet", 'menubar=0,resizable=0,width=550,height=420,top=200,left=400');
		ev.preventDefault();
	});
});
