# Collect user data.
name = input("Enter your name: ")
content = input("Describe yourself: ")

# Create a file object.
f = open("SMITH.html", "w")


# Adding input data to the HTML file
f.write(f"<html>\n<head>\n<title> \nOutput Data in an HTML file \
        </title>\n</head> <body><h1>{name}</h1>\
        \n<h2>{content}</h2> \n</body></html>")

# Create a string to store the html script.
data = f'''
<html>
<head>
</head>
<body>
   <center>
      <h1>{name}</h1>
   </center>
   <hr />
   {content}
   <hr />
</body>
</html>'''

            
# Saving the data into the HTML file
f.close()
