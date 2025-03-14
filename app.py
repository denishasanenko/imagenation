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
    semaphore = asyncio.Semaphore(3)
    tasks = [process_file(semaphore, file) for file in all_files]
    await asyncio.gather(*tasks)

async def process_file(semaphore, file):
    async with semaphore:
        sleep_time = random.randint(3,9)
        print(file)
        print(sleep_time, file.name)
        await asyncio.sleep(sleep_time)
        print('timer end for', file.name)
    pass

app.config['SECRET_KEY'] = "YOUR_SECRET_KEY_HERE"

if __name__ == "__main__":  
    app.run(debug=True)