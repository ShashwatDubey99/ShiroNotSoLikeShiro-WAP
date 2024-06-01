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
def thehell():
     return '''
     {
  "1": {
    "inputs": {
      "ckpt_name": "AILTM.safetensors"
    },
    "class_type": "CheckpointLoaderSimple",
    "_meta": {
      "title": "Load Checkpoint"
    }
  },
  "2": {
    "inputs": {
      "model_type": "SD1",
      "steps": 10,
      "denoise": 1
    },
    "class_type": "AlignYourStepsScheduler",
    "_meta": {
      "title": "AlignYourStepsScheduler"
    }
  },
  "3": {
    "inputs": {
      "add_noise": true,
      "noise_seed": 1030581476638208,
      "cfg": 8,
      "model": [
        "1",
        0
      ],
      "positive": [
        "4",
        0
      ],
      "negative": [
        "5",
        0
      ],
      "sampler": [
        "6",
        0
      ],
      "sigmas": [
        "2",
        0
      ],
      "latent_image": [
        "7",
        4
      ]
    },
    "class_type": "SamplerCustom",
    "_meta": {
      "title": "SamplerCustom"
    }
  },
  "4": {
    "inputs": {
      "text": "positive",
      "clip": [
        "1",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "5": {
    "inputs": {
      "text": "negetive",
      "clip": [
        "1",
        1
      ]
    },
    "class_type": "CLIPTextEncode",
    "_meta": {
      "title": "CLIP Text Encode (Prompt)"
    }
  },
  "6": {
    "inputs": {
      "eta": 1,
      "s_noise": 1,
      "noise_device": "gpu"
    },
    "class_type": "SamplerDPMPP_3M_SDE",
    "_meta": {
      "title": "SamplerDPMPP_3M_SDE"
    }
  },
  "7": {
    "inputs": {
      "width": 512,
      "height": 512,
      "aspect_ratio": "custom",
      "swap_dimensions": "Off",
      "upscale_factor": 1,
      "batch_size": 1
    },
    "class_type": "CR SD1.5 Aspect Ratio",
    "_meta": {
      "title": "🔳 CR SD1.5 Aspect Ratio"
    }
  },
  "8": {
    "inputs": {
      "samples": [
        "3",
        0
      ],
      "vae": [
        "1",
        2
      ]
    },
    "class_type": "VAEDecode",
    "_meta": {
      "title": "VAE Decode"
    }
  },
  "9": {
    "inputs": {
      "filename_prefix": "ComfyUI",
      "images": [
        "8",
        0
      ]
    },
    "class_type": "SaveImage",
    "_meta": {
      "title": "Save Image"
    }
  }
}
     '''