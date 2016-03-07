function loadData() {

    var $body = $('#body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var streetStr = $("#street").val()
    var cityStr = $("#city").val()
    var address = streetStr + ", " + cityStr;

    $greeting.text("So, you want to live at " + address + "?");

    var streetviewUrl = "https://maps.googleapis.com/maps/api/streetview?size=400x200&location=" + address + "";

    $body.append("<img class='thumbnail center-block' src='"+ streetviewUrl + "'>");

    var API = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="
    var KEY = "&sort=newest&api-key=53ac231dce440f01b73fcdda60cccc59:4:70248560"
    var URL = API + cityStr + KEY
    $.getJSON(URL, function( data ) {
        $nytHeaderElem.text("New York Times Articles About " + cityStr);
        var articles = data.response.docs;
        for (var i = 0; i < articles.length; i++ ) {
            var article = articles[i];
            $nytElem.append("<li class='thumbnail bg-thumb'>" + "<a href='"+ article.web_url +"' target='_blank'>" + article.headline.main +"</a>" + "<p>" + article.snippet + "</p></li>");
        };
    }).error(function(e) {
        $nytElem.text("Ny Times Couldn't be loaded at this time")
    });

    var wikiRequestTimeout = setTimeout(function(){
        $wikiElem.text("failed to get wikipedia resources"); 
    }, 8000);

    var wikiURL = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + cityStr + "&format=json&callback=wikiCallback";
    $.ajax({
        url: wikiURL,
        dataType: "jsonp",
        success: function ( data ) {
            var articleList = data[1]
            for (var i = 0; i < articleList.length; i++) {
                articleStr = articleList[i]
                var url = "https://en.wikipedia.org/wiki/" + articleStr;
                $wikiElem.append("<li><a href='" + url + "' target='_blank'>" + articleStr + "</a></li>");
            }; 
            clearTimeout(wikiRequestTimeout);
        }
    })
    return false;
};

$('#form-container').submit(loadData);
