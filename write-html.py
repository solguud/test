# write-html.py

f = open('helloworld.html','w')

message = """<!DOCTYPE html>
<html>
<head>Hello World</head>
<body>
<p>Hello World</p>
</body>
</html>"""

f.write(message)
f.close()
