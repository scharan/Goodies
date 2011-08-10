// Author: Sai Charan (http://saicharan.in/blog)
// Distributed without warranties or conditions of any kind, either
// express or implied except those under the CC BY-NC 3.0 license.
// You may obtain a copy of the license at:
//
// http://creativecommons.org/licenses/by-nc/3.0/
//
// Leave comments at: 
// http://saicharan.in/blog/2011/08/08/indian-almanac-bookmarklet/
//
// Bookmarklet to display South Indian Almanac for Riverside, CA. 
// See blog post for adapting to other Cities.
javascript: function panchangam(){var d = new Date(); var day=d.getDate(); var month=d.getMonth(); var year = d.getFullYear();location.href='http://www.mypanchang.com/phppanchang.php?cityhead=Riverside,%20California&cityname=Riverside-California'+'&yr='+year+'&monthtype=0&mn='+month+'#'+day};panchangam();
