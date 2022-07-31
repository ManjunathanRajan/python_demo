# Author: OMKAR PATHAK

import smtplib

fadd = 'manjublr92@gmail.com'                                      # sender's email address
tadd = 'manju.adhavan@vmscout.in'                                  # receiver's email address
msg = 'Mail sent through Python using Jenkins job!'                # Message to be sent!
username = 'manjublr92@gmail.com'                                  # Your username(email ID)
password = 'mynldzefwjerhnlv'                                      # Your password for above email ID
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fadd,tadd,msg)
