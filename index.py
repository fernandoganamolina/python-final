#import requests
import requests
from string import Template
data=requests.get("https://reqres.in/api/users")
if data.status_code==200: #cheque si conexion a api fue exitosa
    data=data.json()
    canti=data['per_page'] #cantidad de usuarios
    users=data['data'] #datos de los usuarios
    
    #crea html para insertar en template
    lista="<main class='m-2' style='display:flex;gap:10px'>\n"
    for num in range(canti):
        ide=users[num]['id']
        ema=users[num]['email']
        nom=users[num]['first_name']
        app=users[num]['last_name']
        fot=users[num]['avatar']
        lista+="<div class='card border border-primary border-2'>\n"
        lista+="<div class='card-header bg-primary text-white text-center'>\n"
        lista+="<span style='font-size:0.9em'>"+nom+" "+app+"<span></div>\n"
        lista+="<div class='card-body text-center bg-white m-0 p-0'>\n"
        lista+="<img src='"+fot+"' class='img-fluid' title='"+nom+" "+app+"'></div>\n"
        #lista+="<div class='card-footer bg-primary text-white'>&nbsp;</div>\n"
        lista+="</div>\n"
    lista+="</main>\n"
    
    html=open("index.html") #abre html base
    lineas=html.read()
    temp=Template(lineas) #crea template con contenido base
    output=temp.substitute(data=lista) #inserta html creado
    
    html2=open("lista.html","w") #crea html de salida
    html2.write(output) #escribe contenido en nuevo html
    html2.close()
    
else:
    print(f"ERROR {data.status_code}")     