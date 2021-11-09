from flask import Flask,render_template,request
from bs4 import BeautifulSoup
import requests
app=Flask(__name__,static_folder='static',template_folder='templates')
app.secret_key="viggu2205"
def clr_list(hex):
    url="https://mycolor.space/?hex=%23"+hex+"&sub=1"
    page1=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"},verify=False)
    soup1=BeautifulSoup(page1.content,"html5lib")
    soup2=soup1.find_all('div',attrs={"class":["color-palette"]})
    clrs=[]
    for j in soup2:
        li=[i['style'].split(":")[1][:-1] for i in j.find_all('div',attrs={"class":"color"})]
        clrs.append(li) 
    return clrs
def style_create(clrs):
    styles=[]
    for li in clrs:
        s="linear-gradient(to top right,"
        for i in li:
            s+=i+","
        s=s[:-1]+")"
        styles.append(s)
    return styles
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="POST":
        hex=request.form['hex'][1:]
        return render_template("new.html",s=style_create(clr_list(hex)))
    else:
        return render_template("new.html",s=None)
if __name__=="__main__":
    app.run(debug=True)