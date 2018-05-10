document.observe("dom:loaded",
function() {

    //     if(aImagesToLoad){
    //       var img = new Image();
    //       for (i=0; i < aImagesToLoad.length; i++) {
    // 	img.src = aImagesToLoad[i];
    //       }
    //     }
    window.setTimeout(function() {

	var toggleNextList = $$('h3.toggleNext');
	toggleNextList.each(function(elm) {
	    elm.observe('mouseover', toggleHelp);
	    elm.observe('mouseout', UnTip);
	    elm.observe('click', toggleNext);
	    toggleInit(elm);
	});

	var toggleMoreLessList = $$('span.moreLess');
	toggleMoreLessList.each(function(elm) {
	    elm.observe('click', toggleMoreLess);
	    initMoreLess(elm);
	});

	// context sensitive help
	var helpList = $$('span.help');
	helpList.each(function(elm) {
	    elm.insert({
		after: '<img class="csh" src="img/helpbubble.png" alt="Questionmark" width="16" height="16" border="0" />'
	    });
	    elm.next('img.csh').observe('mouseover', showCSH);
	    elm.next('img.csh').observe('mouseout', UnTip);
	    elm.hide();
	});

	if ($('hmmerStatusLink')) {
	    oHmmerStat = new hmmerStat('hmmerStatusLink');
	    oHmmerStat.update();
	    oHmmerStat.start();
	}

	// after all toggling is done, show it
	$$('div.toggleNice').each(function(elm) {
	    elm.show();
	});

	if ($('teaser-overlay')) $('teaser-overlay').hide();

    },
    10);

});


var hmmerStat = Class.create({
    initialize: function(divToUpdate, interval) {
	this.divToUpdate = divToUpdate;
	this.interval = typeof(interval) != 'undefined' ? interval: 2;
	this.file = "index.php";
	this.status;
    },

    start: function() {
	this.perEx = new PeriodicalExecuter(this.update.bind(this), this.interval);
    },

    update: function() {

	if (!this.status || force) {
	    var oOptions = {
		method: "GET",
		asynchronous: true,
		parameters: "ajaxId=" + "hmmerStatus" + "&sessionId=" + window.sessionId,
		onComplete: function(oXHR, Json) {
		    if (oXHR.responseText.trim() == "1" && (typeof(this.status) == 'undefined' || !this.status)) {
			$(this.divToUpdate).innerHTML = 'searching for pfam-domains done, click to see updated results';
			$(this.divToUpdate).show();
			if ($('hmmerStatusAjax')) {
			    $('hmmerStatusAjax').remove();
			}
			this.status = true;
			if (this.perEx) {
			    this.perEx.stop();
			}
		    } else if (typeof(this.status) == 'undefined' || this.status) {
			$(this.divToUpdate).hide();
			$(this.divToUpdate).insert({
			    after: '<div id="hmmerStatusAjax"><img class="csh" src="img/ajax-loader.gif" alt="Loading..." width="16" height="16" border="0" />&nbsp;&nbsp;still searching for pfam-domains, please wait.</div>'
			});
			this.status = false;
		    }
		}.bind(this)
	    }
	    var oRequest = new Ajax.Request(this.file, oOptions);
	};
    }
});

function showCSH(event) {
    var element = event.element();
    var elmPrev;
    if (element.previous('span.help')) {
	elmPrev = element.previous('span.help').identify();
	TagToTip(elmPrev);
    }
}

var toggleShowList = ['adjustToggle', 'helpToggle', 'legendToggle', 'pfamToggle', 'locToggle', 'downloadsToggle'];

function toggleInit(element) {

    if (element.id && ((toggleShowList.member(element.id) && readCookie('toggle_' + element.id) == null) || readCookie('toggle_' + element.id) == '1')) {
	element.next().show();
	element.addClassName('opened');
    } else {
	element.next().hide();
	element.addClassName('closed');
    }
}

function toggleHelp(event) {
    var element = event.element();
    Tip('click&nbsp;to&nbsp;expand/collapse');
}

function toggleNext(event) {
    var element = event.element();
    element.next().toggle();
    element.toggleClassName('opened');
    element.toggleClassName('closed');

    if (element.id) {
	// save state to show when the user visits the page again
	createCookie('toggle_' + element.id, (element.next().visible() ? '1': '0'), 1);
    }
}

function toggleMoreLess(event) {
    var element = event.element();
    var elmUpNext = element.up().next();
    elmUpNext.toggleClassName('moreLessContent');
    elmUpNext.toggle();

    if (element.innerHTML == 'More') {
	element.innerHTML = 'Less';
    } else {
	element.innerHTML = 'More';
    }
}

function initMoreLess(element) {
    if (element.innerHTML != 'Less') {
	element.innerHTML = 'More';
	element.up().next().hide();
    }
}

function createCookie(name, value, days) {
    if (days) {
	var date = new Date();
	date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
	var expires = "; expires=" + date.toGMTString();
    } else var expires = "";
    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
	var c = ca[i];
	while (c.charAt(0) == ' ') c = c.substring(1, c.length);
	if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}

String.prototype.trim = function() {
    return this.replace(/^\s+|\s+$/g, "");
}
String.prototype.ltrim = function() {
    return this.replace(/^\s+/, "");
}
String.prototype.rtrim = function() {
    return this.replace(/\s+$/, "");
}