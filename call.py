import sys
import urllib.request
import ssl

host = 'https://47bcbb0d03324951af88848d803a8a72-us-west-1.alicloudapi.com'
path = '/query2'
method = 'GET'
appcode = 'bb9717fa2b604e51ae039d792c57f9c7'
querys = 'dept_name=Marketing'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

response = urllib.request.urlopen(request, context=ctx)
content = response.read()
if (content):
    print(content)