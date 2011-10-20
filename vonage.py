#!/usr/bin/python

# Author: Sai Charan (http://saicharan.in/blog)
# Distributed without warranties or conditions of any kind, either
# express or implied except those under the CC BY-NC 3.0 license. 
# You may obtain a copy of the license at:
#
# http://creativecommons.org/licenses/by-nc/3.0/

# For support, leave a comment at: http://saicharan.in/blog/2011/08/09/vonage-usage-python-script/

import urllib, urllib2, cookielib
import libxml2dom
import time, datetime
import string

# All variables
username = ''
password = ''
month_mins = 3000
month_days = 30
day_mins = month_mins/month_days
login_url = 'https://secure.vonage.com/vonage-web/public/login.htm'
billing_url = 'https://secure.vonage.com/webaccount/billing/index.htm'
international_mins_id = 'td_value_international_minutes'
billing_cycle_id = 'td_value_current_billing_cycle'
billing_cycle_date_format = "%b %d, %Y"
billing_cycle_date_separator = '-'

# Functionality
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'password' : password})
opener.open(login_url, login_data)
resp = opener.open(billing_url)
billing_page = resp.read()
opener.close();

doc = libxml2dom.parseString(billing_page, html=1)
mins = string.atoi(doc.getElementById(international_mins_id).childNodes[0].nodeValue.strip())
today = datetime.datetime.now()

# Billing cycle is of the form: Jul 12, 2011 - Aug 12, 2011.
# Now calculate number of days passed since start of billing cycle.
elapsed = (today - datetime.datetime.strptime( doc.getElementById(billing_cycle_id).childNodes[0].nodeValue.expandtabs().split(billing_cycle_date_separator)[0].strip(), billing_cycle_date_format) ).days
print "Your unbilled Vonage usage (%d days so far) is: %d mins; " % (elapsed, mins),
if mins/day_mins < elapsed:
    print "you are under the limit."
    exit(0)
else:
    print "You have overshot the limit!"
    exit(mins)
