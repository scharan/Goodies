// Author: Sai Charan K.
// Depends on jQuery (currently tested with version 1.6.2)
// 
// Aims to:
// 1. Disable disqus on certain pages.
// 2. 

$(document).ready(function() {
    var nodsq = ["ask", "about"];
    if( $.inArray($(location).attr('href').split('/')[1], nodsq ) {
        $("#disqus_thread").hide();
    }
});
