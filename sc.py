#!/usr/bin/python
import os
from collections import OrderedDict
os.chdir("<DIR PATH>")
vf = open("names.txt","w+")

directs=os.listdir('.')
dic={}
l=[]
for d in directs:
	if d != ".DS_Store":
		dic[ float(d[:d.find('. ')])]=d
dic=OrderedDict(sorted(dic.items(), key=lambda t: t[0]))
for d in dic:
	l.append(dic[d])

	
for d in l:
	if d != ".DS_Store":
		os.chdir("./"+d)
		files = [f for f in os.listdir('.') if os.path.isfile(f) and f[f.rfind('.')+1:]=='mp4']
		videos={}
		for f in files:
				k=f[:f.find(' ')]
				videos[int(k)]=str(f)
		l=[]
		keylist = videos.keys()
		print(keylist)
		keylist=sorted(keylist)
		for key in keylist:
			l.append(videos[key])		
		cwd = os.getcwd()
		for f in l:
			vf.write("file '"+cwd+'/'+f+"'\n")
		os.chdir("..")
vf.close()
