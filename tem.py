import json
import requests
import urllib
def getimgname(prompt_id,url):
      URL=url
      print(URL)
      respons = requests.get(f"{URL}/history/{prompt_id}")
      n=(respons.json()) 
      f=(respons.json()[prompt_id]["outputs"]['9']["images"])
      a=[]
      for i in f:
          filename = i["filename"]
          subfolder = i["subfolder"]
          folder_type = i["type"]
          z=(URL+"/"+"view?"+get_image(filename, subfolder, folder_type))
          a.append(URL+"/"+"view?"+get_image(filename, subfolder, folder_type))
      return a    

def get_image(filename, subfolder, folder_type):
    data = {"filename": filename, "subfolder": subfolder, "type": folder_type}
    url_values = urllib.parse.urlencode(data)
    return url_values
