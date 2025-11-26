from bs4 import BeautifulSoup
import requests
import pandas as pd 



data=[]
    
for a in range(4):
    print("aaaa page" +str(a)+ "aaaa")
    page=requests.get("https://www.etreproprio.com/annonces/thflcpo.lc75056-r0.odd.g"+str(a)+"#list")
    soup=BeautifulSoup(page.content, 'html.parser')
    
    objet=soup.find("div", class_='ep-search-list-wrapper').find_all("a")
    
    liens=[]
    for i in range(len(objet)):
        if"https://www.etreproprio.com/immobilier-" in objet[i]['href']:
            liens.append(objet[i]['href'])
    
    for e in liens:
        page1=requests.get(e)
        soup1=BeautifulSoup(page1.content, 'html.parser')
        
       
        
        
            
        
        try:
            title=soup1.find("h1", class_='annonce-immobilier').text.replace(" ", "")
        
          
        except:
            title=0
        
        try:
            ville=soup1.find("div", class_='ep-loc').text.replace(" ", "")
          
        
        except:
           ville=0
           
        try:
            prix=soup1.find("div", class_='ep-price').text.replace(" ", "")
        
          
        except:
            prix=0  
        
        try:
            area=soup1.find("div", class_='ep-area').text.replace(" ", "")
          
        
        except:
           area=0
         
          
       
    
        try:
           room=soup1.find("div", class_='ep-room').text.replace(" ", "")
        except:
            room=0
        
        print( prix,title,ville, area,  room)
        
        
        data.append({"ville": ville,
                     "title": title,
                     "price": prix,
                     "area": area,
                     "room": room
        })
        
    
for k in range(4):
    print("aaaa page" +str(k)+ "aaaa")
    page1=requests.get("https://www.etreproprio.com/annonces/thflcpo.lc69123-r0.odd.g"+str(k)+"#list")
    soup1=BeautifulSoup(page1.content, 'html.parser')
    
    objet1=soup1.find("div", class_='ep-search-list-wrapper').find_all("a")
    
    liens1=[]
    for j in range(len(objet1)):
        if"https://www.etreproprio.com/immobilier-" in objet1[j]['href']:
            liens1.append(objet1[j]['href'])
    
    for m in liens1:
        page11=requests.get(m)
        soup11=BeautifulSoup(page11.content, 'html.parser')
        
       
        
        
            
        
        try:
            title1=soup11.find("h1", class_='annonce-immobilier').text.replace(" ", "")
        
          
        except:
            title1=0
        
        try:
            ville1=soup11.find("div", class_='ep-loc').text.replace(" ", "")
          
        
        except:
           ville1=0
           
        try:
            prix1=soup11.find("div", class_='ep-price').text.replace(" ", "")
        
          
        except:
            prix1=0  
        
        try:
            area1=soup11.find("div", class_='ep-area').text.replace(" ", "")
          
        
        except:
           area1=0
         
          
       
    
        try:
           room1=soup11.find("div", class_='ep-room').text.replace(" ", "")
        except:
            room1=0
        
        print( prix1,title1,ville1, area1,  room1)
        
        data.append({"ville": ville1,
                     "title": title1,
                     "price": prix1,
                     "area": area1,
                     "room": room1
        })


for k_ in range(4):
    print("aaaa page" +str(k_)+ "aaaa")
    page1_=requests.get("https://www.etreproprio.com/annonces/thflcpo.lc13055-r0.odd.g"+str(k_)+"#list")
    soup1_=BeautifulSoup(page1_.content, 'html.parser')
    
    objet1_=soup1_.find("div", class_='ep-search-list-wrapper').find_all("a")
    
    liens1_=[]
    for j_ in range(len(objet1_)):
        if"https://www.etreproprio.com/immobilier-" in objet1_[j_]['href']:
            liens1_.append(objet1_[j_]['href'])
    
    for m_ in liens1_:
        page11_=requests.get(m_)
        soup11_=BeautifulSoup(page11_.content, 'html.parser')
        
       
        
        
            
        
        try:
            title1_=soup11_.find("h1", class_='annonce-immobilier').text.replace(" ", "")
        
          
        except:
            title1_=0
        
        try:
            ville1_=soup11_.find("div", class_='ep-loc').text.replace(" ", "")
          
        
        except:
           ville1_=0
           
        try:
            prix1_=soup11_.find("div", class_='ep-price').text.replace(" ", "")
        
          
        except:
            prix1_=0  
        
        try:
            area1_=soup11_.find("div", class_='ep-area').text.replace(" ", "")
          
        
        except:
           area1_=0
         
          
       
    
        try:
           room1_=soup11_.find("div", class_='ep-room').text.replace(" ", "")
        except:
            room1_=0
        
        print( prix1_,title1_,ville1_, area1_,  room1_)
        
        
        data.append({"ville": ville1_,
                     "title": title1_,
                     "price": prix1_,
                     "area": area1_,
                     "room": room1_
        })
        
df= pd.DataFrame(data)

df.to_csv("annoncespro.csv", index=False, encoding="utf-8")

print("Fichier CSV créé ici :annoncespro.csv")
       
        
        
      

  
            

