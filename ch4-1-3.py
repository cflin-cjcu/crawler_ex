import requests
	
post_data = {'name': '陳會安', 'grade': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

