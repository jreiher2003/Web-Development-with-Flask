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

    $body.append("<img class='bgimg center-block' src='"+ streetviewUrl + "'>");

    var API = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="
    var KEY = "&api-key=53ac231dce440f01b73fcdda60cccc59:4:70248560"
    var URL = API + cityStr + KEY
    $.getJSON(URL, function( data ) {
        // console.log(data)
        // console.log(data.response.docs)
        var articles = data.response.docs;
        console.log(articles.length)
        // console.log(articles[0]['web_url']);
        for (var i = 0; i < articles.length; i++ ) {
            var article = articles[i];
            $nytElem.append("<li>" + "<a href='"+ article.web_url +"' target='_blank'>" + article.headline.main +"</a>" +"</li>");
        };
        // console.log(URL)
    });
    return false;
};

$('#form-container').submit(loadData);

// loadData();