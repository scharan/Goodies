// Author: Sai Charan (http://saicharan.in/blog)
// Distributed without warranties or conditions of any kind, either
// express or implied except those under the CC BY-NC 3.0 license.
// You may obtain a copy of the license at:
//
// http://creativecommons.org/licenses/by-nc/3.0/
//
// Leave comments at: 
// http://saicharan.in/blog/2009/07/12/hn-submit-button/

(function() {
var hn_link = "http://news.ycombinator.com/submitlink?u=";
if (window.hn_url) { 
	hn_link += encodeURIComponent(hn_url); 
}
else { 
	hn_link += encodeURIComponent(document.location);
}
if (window.hn_title) { 
	hn_link += "&t=" + encodeURIComponent(hn_title); 
}
else { 
	hn_link += "&t=" + encodeURIComponent(document.title);
}

var write_string = "<a href="+hn_link+"><img src='http://ycombinator.com/images/y18.gif' alt='Hacker News' width=18 height=18 style='border:1px #ffffff solid;'/></a><a href="+hn_link+" alink='#000000'; vlink='#828282' style='text-decoration:none' target='_blank'><span style='font-family:Verdana; font-size: 10pt; color:#828282;'><b>Submit</b></span></a>";
document.write(write_string);
})()
