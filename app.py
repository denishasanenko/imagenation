from flask import Flask, render_template, request
from itertools import batched
import asyncio
import random


app = Flask(__name__, static_folder="./static", template_folder="./templates")  

@app.route('/')  
def hello():  
    return render_template("index.html")

@app.route('/upload', methods=["POST"])
def upload():
    all_files = request.files.getlist("files")
    asyncio.run(process_files(all_files))
    return "uploading"

async def process_files(all_files):
    chunks = batched(all_files, 3)
    print(chunks)
    for chunk in chunks:
        for file in chunk:
            await process_file(file)
            print(file)

async def process_file(file):
    sleep_time = random.randint(3,9)
    print(sleep_time, file.name)
    await asyncio.sleep(sleep_time)
    print('timer end for', file.name)
    pass

app.config['SECRET_KEY'] = "YOUR_SECRET_KEY_HERE"

if __name__ == "__main__":  
    app.run(debug=True)