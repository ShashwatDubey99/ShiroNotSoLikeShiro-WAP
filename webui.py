from flask import Flask, jsonify, request, render_template_string
import requests
import random
import json
import tem
import time
import argparse

app = Flask(__name__, static_folder="static", template_folder="templates")

parser = argparse.ArgumentParser()
parser.add_argument('url', type=str, help="Pass The URL of the Comfy WebUI IMP-[Without the / at the end ]")
args = parser.parse_args()

@app.route("/")
def hello():
    quality = ""
    quality_prompts = {
        "High Quality": "high quality high res, 4k hdr",
        "Detailed": "Highly detailed, insane details, sharp image",
        "4k": "4k",
    }
    neg=''
    places = ""
    places_prompts = {
        "In the sky": "in the sky",
        "In classroom": "in classroom",
        "In the office": "in the office",
        "On the floor": "on the floor",
        "In the corner": "in the corner",
        "In the mountain": "In the mountain",
    }
    neg_prompts = {
        "low quality": "low quality",
        "low res": "low res",
        "worst quality": "worst quality",
        "blurry": "blurry",
        "bad anatomy": "bad anatomy",
        "bad proportions": "bad proportions",
        "extra": "extra",
        "cropped": "cropped",
        "worst quality": "worst quality",
        "bad quality": "bad quality",
        "jpeg artifacts": "jpeg artifacts",
        "watermark": "watermark",}

    for label, value in quality_prompts.items():
        quality += f'''
        <label class="container">
            <input type="checkbox" id="positive" name="option" value="({value})">{label}
        </label>
        '''
    
    for label, value in places_prompts.items():
        places += f'''
        <label class="container">
            <input type="checkbox" id="positive" name="option" value="({value})">{label}
        </label>
        '''
    for label, value in neg_prompts.items():
        neg += f'''
    <label class="container">
        <input type="checkbox" id="negetive" name="negetive" value="({value})">{label}
    </label>
    '''

    return render_template_string('''
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
        <script src="{{ url_for('static', filename='script.js') }}"></script>
    </head>
    <body>
        <form id="qualityForm" action="/text2img" method="post">
              <label class="container">
                <input type="checkbox" id="advanced" onclick="toggleTextAreas()"> Advanced
            </label>
            <div class="wrapper" id="advanced-options" style="display: none;">
                <textarea id="positive" name="positive">POSITIVE</textarea>
                <textarea id="negetive" name="negetive">NEGATIVE</textarea>
            </div>
            <div class="wrapper">
                <input type="button" value="Generate" onclick="submitForm()">
            </div>
                      
            <h1>Quality Prompt</h1>
            <div class="wrapper">''' + quality + '''</div>
            <h1>Place Prompt</h1>
            <div class="wrapper">''' + places + '''</div>
            <h1>Negative Prompt</h1>
            <div class="wrapper">''' + neg + '''</div>
            <div class="slider-container">
                <div class="slider-wrapper">
                    <label class="slider-label" for="cfg">CFG:</label>
                    <input type="range" id="cfg" name="cfg" min="1" max="20" step="0.1" value="10" class="slider" oninput="updateValue('cfg-value', this.value)">
                    <span id="cfg-value" class="slider-value">10</span>
                </div>
                <hr>
                <div class="slider-wrapper">
                    <label class="slider-label" for="steps">Steps:</label>
                    <input type="range" id="steps" name="steps" min="1" max="100" value="50" class="slider" oninput="updateValue('steps-value', this.value)">
                    <span id="steps-value" class="slider-value">50</span>
                </div>
                <div class="slider-wrapper">
                    <label class="slider-label" for="batch">Batch Size:</label>
                    <input type="range" id="batch" name="batch" min="1" max="10" value="1" class="slider" oninput="updateValue('batch-value', this.value)">
                    <span id="batch-value" class="slider-value">1</span>
                </div>
            </div>
            <label for="aspect">Aspect:</label>
            <select name="aspect" id="aspect">
                <option value="1:1 square 512x512">1:1 square 512x512</option>
                <option value="1:1 square 1024x1024">1:1 square 1024x1024</option>
                <option value="2:3 portrait 512x768">2:3 portrait 512x768</option>
                <option value="3:4 portrait 512x682">3:4 portrait 512x682</option>
                <option value="3:2 landscape 768x512">3:2 landscape 768x512</option>
                <option value="4:3 landscape 682x512">4:3 landscape 682x512</option>
                <option value="16:9 cinema 910x512">16:9 cinema 910x512</option>
                <option value="1.85:1 cinema 952x512">1.85:1 cinema 952x512</option>
                <option value="2:1 cinema 1024x512">2:1 cinema 1024x512</option>
            </select> 

        </form>
        <div id="loading-spinner" class="loading-spinner"></div>
        <div id="image-container" class="img-container"></div>
    </body>
    </html>
    ''')

URL = args.url

def queue_prompt(prompt, url):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req = requests.post(f"{url}/prompt", data=data)
    global prompt_id
    prompt_id = req.json()["prompt_id"]
    print(prompt_id)

def textimg(pos,neg, cfg, steps, aspect, batch):
  
        global data
        data = json.loads(tem.thehell())
        data["4"]["inputs"]["text"] = pos
        data["5"]["inputs"]["text"] = neg
        data["3"]["inputs"]["cfg"] = cfg
        data["2"]["inputs"]["steps"] = steps
        data["7"]["inputs"]["aspect_ratio"] = aspect
        data["7"]["inputs"]["batch_size"] = batch
        data["3"]["inputs"]["noise_seed"] = random.randint(1, 974538867544)
        queue_prompt(data, URL)

@app.route("/text2img", methods=["POST"])
def text2img():
    data = request.get_json()
    prompt = data.get('prompt', '')
    neg = data.get('negetive','')
    steps = data.get('steps', '')
    cfg = data.get('cfg', '')
    aspect = data.get('aspect', '')
    batch = data.get('batch', '')
    textimg(prompt,neg, cfg, steps, aspect, batch)
    j = requests.get(URL + "/queue")
    j = j.json()
    time.sleep(1)
    while j["queue_running"] != []:
        j = requests.get(URL + "/queue")
        j = j.json()
        time.sleep(2) 
    a = tem.getimgname(prompt_id, URL)
    print(a)
    return jsonify(a)

if __name__ == "__main__":
    app.run(debug=True)
