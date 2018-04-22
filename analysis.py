import meme
import os
import output
import re
import subprocess

ERROR_PRONE = 'mvn -q -f {dir}/pom.xml {cmd}'
PYCODESTYLE = 'pycodestyle --first {file}'
DIR = os.path.dirname(os.path.realpath(__file__))

def parse(log):
    # print log
    errors = []
    path = num = error = msg = body = link = ""
    for line in log:
        if re.match("^\\d+\\serror[s]*$", line) or re.match("^\\d+\\swarning[s]*$", line) or line.startswith("Note:"):
            continue
        elif line.startswith(DIR):
            if error != "":
                errors.append((path, num, error, msg, link))
                path = num = error = msg = link = ""
            err = line.split(":")
            path = err[0]
            num = err[1]
            error = err[3][err[3].index("[") + 1:err[3].index("]")]
            msg = err[3][err[3].index("]") + 2:]
        elif "http://errorprone.info/bugpattern" in line:
            link = line
        else:
            if msg != "":
                msg += line
    if error != "":
        errors.append((path, num, error, msg, link))
    if len(errors) == 0:
        return "<img src=\"success.jpg\"><br>"
    for e in errors:
        body += "<h3>"+ e[0].replace(DIR+"/", "") + "- line #" + e[1] + "</h3><br>"
        body += "<img src=\"" + meme.memify(e[0], error, msg) + "\"><br>"
        url = e[4][e[4].index("http"):e[4].index(")")]
        body += e[4].replace(url, "<a href=\""+url+"\">"+url + "</a>") + "<br><br><br>"
    return body

def run(gitDir):
    with open('output.txt', 'r') as f:
        log = f.readlines()
    results = parse(log)
    # TODO: Implement other tools
    output.generate_file('Error Prone', results)
