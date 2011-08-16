// Author: Sai Charan K.
// Distributed without warranties or conditions of any kind, either
// express or implied except those under the CC BY-NC 3.0 license.
// You may obtain a copy of the license at:
//
// http://creativecommons.org/licenses/by-nc/3.0/

// Depends on jQuery (currently tested with version 1.6.2)
// 
// Aims to:
// 1. Disable disqus on certain pages.

$(document).ready(function() {
    var nodsq = ["ask", "about"];
    if( $.inArray($(location).attr('href').split('/').reverse()[0], nodsq) >= 0 ) {
        $("#disqus_thread").hide();
    }
});
