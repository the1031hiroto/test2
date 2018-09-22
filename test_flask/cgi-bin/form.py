import cgi
 
print "Content-Type: text/html\n"
 
print "<html><body>"
 
form = cgi.FieldStorage()
form_check = 0
if form.has_key("name") and form.has_key("mail") :
  form_check = 1
if form_check == 0 :
  print "<h1>ERROR !</h1>"
else :
  print "<h2>PRINT</h2><hr>"
  print "<b>name: </b>", form["name"].value
  print "<b>mail: </b>", form["mail"].value
 
print "</body></html>"