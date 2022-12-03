from flask import Flask, render_template

import requests


app=Flask(__name__)



def get_pokemon():
    poke_dict=[]
    for i in range(1,51,1):
        url="https://pokeapi.co/api/v2/pokemon/"+str(i)
        response=requests.request("GET",url).json()
        poke_pic_front=response['sprites']['front_default']
        poke_pic_back=response['sprites']['back_default']
        poke_name=response['name']
        print(poke_pic_front,poke_pic_back,poke_name)
        poke_dict.append({'poke_pic_front':poke_pic_front,' poke_pic_back': poke_pic_back,'poke_name':poke_name})

    # for dt in arr:
    #     print(dt)
    # # print("**************",poke_name)
    return poke_dict

@app.route("/poke")
def home():
    response=get_pokemon()
    print("%%%%%%%%%%%%%%",response)
    return render_template("index.html",response=response)













if(__name__)=="__main__":
    app.run(debug=True)