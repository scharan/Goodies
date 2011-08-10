#!/bin/bash
# Author: Sai Charan (http://saicharan.in/blog)
# Distributed without warranties or conditions of any kind, either
# express or implied except those under the CC BY-NC 3.0 license. 
# You may obtain a copy of the license at:
#
# http://creativecommons.org/licenses/by-nc/3.0/

# References: 
# http://beingkejo.wordpress.com/2008/05/28/sendmail-in-a-shell-script/

# Temporary file for containing the mail message
tmp=/tmp/mail-body-`date +%F`;
touch $tmp && chmod 600 $tmp;

# Body header seems to need two newlines to work.
NEWLINE="

";

# Some pre-processing:
# WARNING!! Not a scalable procedure in general. DONOT emulate.
# We expect first arg to be subject and second to be body (in file). If there is
# only one arg, it may be the body. So clear that upfront.
#----Assumes that if there is just one arg, it will be the body. 
# ---If two, the first has got to be the subject.
if [ "$2" ] && [ -r "$2" ]; then # File exists & is readable
    BODY=$(cat $2);
    rm -rf $2;        
fi
if [ "$1" ] && [ -r "$1" ]; then
    BODY=$(cat $1);
    rm -rf $1;
else 
    if [ "$1" ]; then
        SUBJECT=$1;
    fi
fi

#Set up the various headers for sendmail to use
TO='';
CC='';
FROM='';
if [ -z "$SUBJECT" ]; then
    SUBJECT='Task complete!';
fi
MIMEVersion='1.0';
CONTENTType='text/html; charset=us-ascii';

#Here write the content of your mail.
if [ -z "$BODY" ]; then
BODY="
Task done!
";
else 
    BODY=$NEWLINE" "$BODY" "$NEWLINE;
fi

echo Sending the mail...
echo -e "To: $TO" > $tmp;
echo -e "Cc: $CC" >> $tmp;
echo -e "From: $FROM" >> $tmp;
echo -e "Content-Type: $CONTENTType" >> $tmp;
echo -e "MIME-Version: $MIMEVersion" >> $tmp;
echo -e "Subject: $SUBJECT" >> $tmp;
echo -e "Body: $BODY" >> $tmp;

/usr/sbin/sendmail -t < $tmp;

rm -rf $tmp;
echo Done!
