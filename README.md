
# Cloud Text To Speech

This is an implementation of a platform with the ability to turn text into speech. The platform makes it possible to select several text transformation options to get speech as realistic as possible. Programming language is Python


## Run BE

To Run BE Part Please do steps. (for Windows Only)

```bash
  Download And Install The Latest Python 
  https://www.python.org/downloads/
```
```bash
  In Project Root Directory Run  
  py -m venv env
```
```bash
  In Project Root Directory Run  
  env\Scripts\activate
```
```bash
  pip install Flask
```
```bash
  py -m pip install --upgrade pip
```
```bash
  set FLASK_APP=app.py
```
```bash
  pip install --upgrade google-cloud-texttospeech
```
```bash
  pip install iso639-lang
```
```bash
  pip install pycountry
```
```bash
  Get Your Google Console Credentials Json File From Your Account
  And Put It Into Project Root Directory With Name `key.json` 
```
```bash
  flask run
   or 
  flask run --debug
```

## Run FE

To Run FE Part Please do steps. (for Windows Only)

```bash
  Download And Install NODE.
  https://nodejs.org/en/download
```
```bash
  npm install -D tailwindcss
```
```bash
  npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```
## Run Locally

http://127.0.0.1:5000/

