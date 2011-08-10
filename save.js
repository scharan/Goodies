// Author: Sai Charan (http://saicharan.in/blog)
// Distributed without warranties or conditions of any kind, either
// express or implied except those under the CC BY-NC 3.0 license.
// You may obtain a copy of the license at:
//
// http://creativecommons.org/licenses/by-nc/3.0/
//
// Adapted from Instapaper's 'Read Later' Bookmarklet.
// On Windows, this file should go into:
// %USERPROFILE%\AppData\Local\Google\Chrome\User Data\Default\Extensions\oadggleneidfmbhhedlildjnpgcggmch\1.6_0\js
//
// For comments/queries, leave a comment at: 
// http://saicharan.in/blog/2011/08/08/readability-for-chrome-save-to-instapaper/
(function(){var d=document,z=d.createElement('scr'+'ipt'),b=d.body,l=d.location;try{if(!b)throw(0);d.title='(Saving...) '+d.title;z.setAttribute('src',l.protocol+'//www.instapaper.com/j/ms9ZEqYS9JfG?u='+encodeURIComponent(l.href)+'&t='+(new Date().getTime()));b.appendChild(z);}catch(e){alert('Please wait until the page has loaded.');}}());
