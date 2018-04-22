HTML = """ 
<html>
<head>
<title>Meme Prone</title>
<h1>{tool}</h1>
</head>
<body>
{body}
</body>
</html> 
"""

def generate_file(dir, tool, body):
    results = HTML.replace('{tool}', tool.upper()).replace('{body}', body)
    with open('{dir}/output.html'.replace('{dir}', dir), 'w') as out:
        out.write(results)