import re, urllib
"""
#print(re.split(r'(s*)', 'here are some words'))
\s = space
* = 0 or more
+ = 1 or more
? = 0 or 1 of
. any caracter but newline (\n)
{5} = exact number of
{4,10} = range number of nelja numeroa vahintaan ja 10 maksimissa
\d = digits
\D = non digits
\S non-space
\w numbers or letters
flags=
re.I = ignorecase
re.M = Multiline
print (re.split(r'[a-fA-F]', 'ABCdefGH', re.I|re.M))
print(re.findall(r'\d{1,5}\s\w+\s\w+\.', 'perkele21 meri tie.luli'))
"""
try:
    import urllib.request
except:
    pass
data = str(input("Sites to scan example google or multiple sites like google.com msn.com\n"))
sites = str(data).split()
for s in sites:
    try:
        print('Searching: ' + s)
        try:
            u = urllib.urlopen('http://' + s)
        except:
            u = urllib.request.urlopen('http://' + s)

        text = u.read()
        title = re.findall(r'<title>+.*</title>+', str(text), re.I|re.M)
        print (title[0])
    except:
        print("Something went wrong with " + s)
        pass
