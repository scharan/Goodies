#Testing OAuth with GoogleWebServices
#Author: Sai Charan.

import httplib, urllib, hashlib, hmac, time, base64, binascii
from urlparse import parse_qs

method = "POST"
#http://code.google.com/apis/accounts/docs/OAuth_ref.html#SigningOAuth
consumerKey = "anonymous"
consumerSecret = "anonymous"
requestTokenUrl = "https://www.google.com/accounts/OAuthGetRequestToken"

#time() returns float; make it integer and then to string
#This cannot be hardcoded since Google expects that this be 'close' to
#current time.
oauthTimeStamp = `int( time.time() )`

#Hardcode nonce for testing only. Dynamically generate it in real code.
oauth_nonce = "4572616e48616d6d65724c61686176"
scope = "http://www.google.com/calendar/feeds"

#Dictionary of headers
headers = {"Content-type": "application/x-www-form-urlencoded",
		   "Accept": "text/plain", 
		   "Authorization": "OAuth"}

#Dictionary of request parameters
requestParams = {"oauth_consumer_key":consumerKey,
				 "oauth_signature_method":"HMAC-SHA1",
				 "oauth_timestamp":oauthTimeStamp,
				 "oauth_nonce":oauth_nonce, 
				 "oauth_version":"1.0", 
				 "oauth_callback":"http://saicharan.in/beta",
				 "scope":scope}

#Not 100% OAuth compatible, but works for the present example
requestkeys = requestParams.keys()
requestkeys.sort()

toBeNormalizedParamString = ''
for key in requestkeys:
	toBeNormalizedParamString += key+"="+str(requestParams[key])+"&"

#remove the trailing '&'
toBeNormalizedParamString = toBeNormalizedParamString[:-1]

#hack, hack, hack
#Google OAuth requires that the string be double escaped.
#This hack has been created from observing the base_url returned by the API
#and reading some where on the net. Unable to recall which site though.
toBeNormalizedParamString = urllib.quote(toBeNormalizedParamString, safe="~")
toBeNormalizedParamString = toBeNormalizedParamString.replace("%3A","%253A")
normalizedParamString = toBeNormalizedParamString.replace("%2F","%252F")
baseString = method+"&"+ urllib.quote(requestTokenUrl, safe="~") + "&" + normalizedParamString

hmacKey = urllib.quote(consumerSecret, safe="~")
hmacObject = hmac.new( hmacKey+"&", baseString, hashlib.sha1)
#remove the trailing newline.
signature = base64.encodestring( hmacObject.digest() )[:-1]

#Print the baseString, copy it to the text box at:
#http://hueniverse.com/2008/10/beginners-guide-to-oauth-part-iii-security-architecture/
#and use "consumerSecret&" as the secret to test if the generated signature is good.
requestParams["oauth_signature"] = signature
requestParams = sorted( requestParams.items() )
requestParamString = urllib.urlencode(requestParams)

#Another hack. See http://github.com/simplegeo/python-oauth2/blob/master/oauth2/__init__.py
requestParamString.replace("+","%20");
if(method=="GET"):
	requestParamString += "&oauth_signature=" + urllib.quote(signature, safe="~")

#All set, now make the request.
#For work environment, use this to go thru proxy
#conn = httplib.HTTPConnection("")

#For home/no proxy environments
conn = httplib.HTTPConnection("www.google.com:80")

if(method=="POST"):
	conn.request(method, "https://www.google.com/accounts/OAuthGetRequestToken", requestParamString, headers)

if(method=="GET"):
	conn.request( method, "https://www.google.com/accounts/OAuthGetRequestToken?"+requestParamString )

response = conn.getresponse()
print response.status, response.reason
data = response.read()

if (response.status != 200):
	print data
else:
	authToken = parse_qs(data)["oauth_token"][0]
	print authToken
	#authTokenRequest = "https://www.google.com/accounts/OAuthAuthorizeToken?oauth_token="+urllib.quote(authToken, safe="~")
	#print authTokenRequest
	conn.request("GET", "https://www.google.com/accounts/OAuthAuthorizeToken?"+urllib.urlencode({"oauth_token":authToken}), "", headers)
	response = conn.getresponse()
	print "Google: ", response.status, response.reason
	#if response.status != 200:
	#	data = response.read()
	#	print data
	#else:
	#	data = response.read()
	#	print data
	#requestString = "https://www.google.com/accounts/OAuthGetAccessToken"
	#print requestString
	#conn.request("GET", requestString )
	#print response.status, response.reason
	#tokenData = response.read()
	#print tokenData
	
conn.close()
