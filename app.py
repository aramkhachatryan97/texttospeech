from flask import Flask, render_template, jsonify, request
from Services.textToSpeechService import get_supported_options, speak_from_text
import json
import shutil
import os
import random
import string

app = Flask(__name__)

@app.route("/", methods=['GET'])
def text_to_speech_options():
    options = get_supported_options()

    return render_template('index.html', options = options)

@app.route("/test", methods=['POST'])
def run_text_to_speech():
    audio_content = speak_from_text(request.get_json())

#   need to be done by devops (this is not a correct way)
    shutil.rmtree('static/player')
    os.mkdir('static/player')
#   end devops part
#   generating random file name to handle browser file caching, no need when  devops part will be done
    filename = "output-"+''.join(random.choices(string.ascii_lowercase, k=10))+".mp3"
    with open("static/player/"+filename, "wb") as out:
        out.write(audio_content)
    player_html = render_template('player.html', filename = filename)

    return jsonify({'html': player_html})

if __name__ == '__main__':
	app.run(debug=True)
