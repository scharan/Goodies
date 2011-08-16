// Author: Sai Charan K.
// Depends on jQuery (currently tested with version 1.6.2)
// 
// Aims to:
// 1. Disable disqus on certain pages.
// 2. 

$(document).ready(function() {
    var nodsq = ["ask", "about"];
    if( $.inArray($(location).attr('href').split('/').reverse()[0], nodsq) >= 0 ) {
        $("#disqus_thread").hide();
    }
});
