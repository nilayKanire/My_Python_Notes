'''
Request Module For HTTP Requests
'''
# search about this topic on google for more information.
import requests
r = requests.get("https://financialmodelingprep.com/api/v3/actives")             # ye url link likhi hai apan ne
print(r.text)
print(r.status_code)         # search related to this on google. different types are code given for different statement.
                            # ex :-  '200 OK' status code means  The request is OK.

# url = "www.something .com"
# data = {
#     "p1":4,
#     "p2":8
# }
# #
# # r2 = requests.post(url=url, data=data)     # url hamara variable hai
# r3 = request('post', url, data=data, json=json, **kwargs)