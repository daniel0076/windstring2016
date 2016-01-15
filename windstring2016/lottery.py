import requests
import json
import random
import os

def update_data():
	access_token="CAACEdEose0cBAFopZAZBge3AjvbYEoOHn2vEn2gmprCUtYvOKeOytbpGhdFDUndHc6fiV7WkrZAEEFY7UzrrUdNE0umXuDzvZCeADwbyZBmySPMkvvchtpZCErHFaFHmqfm0li2duMk6Krk73uVQ8e65N1rElQUANI6OoVo2UFtMTLzqqgf88CchWoGI5OvQnZAVmjZBLKlCPZB5Fq3Fe3k15"
	url="https://graph.facebook.com/106548149477723_756868187779046?fields=commentsents.limit%28200%29&access_token={0}".format(access_token)
	raw=requests.get(url)
	with open("candidates.txt","w") as f:
		f.write(raw.text)
def select():
	#get the script dir
	PATH=os.path.dirname(os.path.realpath(__file__))
	with open(PATH+"/candidates.txt","r") as f:
		raw=f.read()

	page=json.loads(raw)
	name=[]
	comments={}
	for item in page['comments']['data']:
		if item.get('message_tags') is not None:
			_n=item.get('from').get('name')
			_msg=item.get('message')
			name.append(_n)
			comments[_n]=_msg


	unique_n=list(set(name))
	candidates=list(unique_n)
	selected={}
	prizes={"萊爾富禮券200元(1名)":1,"金安德森暖心格紋抱枕(2名)":2,"安德森時尚格紋毛巾(3名)":3}
	for name,count in prizes.items():
		selected[name]=dict()
		for i in range(count):
			winner=unique_n[random.randint(0,len(unique_n)-1)]
			selected[name][winner]=comments.get(winner)
			unique_n.remove(winner)
	print(selected)

	return prizes,candidates,selected

if __name__ == '__main__':
	select()
	#update_data()
