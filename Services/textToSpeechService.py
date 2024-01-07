from google.cloud import texttospeech
from google.oauth2 import service_account
from iso639 import Lang
import pycountry

credentials = service_account.Credentials.from_service_account_file('key.json')
client = texttospeech.TextToSpeechClient(credentials=credentials)

def speak_from_text(options) -> bytes:
    input_text = texttospeech.SynthesisInput(**{"text": options['text']})
    audio_config = texttospeech.AudioConfig(**{"audio_encoding": texttospeech.AudioEncoding.MP3, "effects_profile_id": [options['device_profile']], "pitch": float(options['pitch']), "speaking_rate": float(options['speed'])})
    voice_params = texttospeech.VoiceSelectionParams(language_code=options['locale'], name=options['voice_name'])
    response = client.synthesize_speech(input=input_text, voice=voice_params, audio_config=audio_config)

    return response.audio_content

def get_supported_options() -> list:
    response = client.list_voices()
    voices = {}
    types = []
    for voice in response.voices:
        language_country_code = voice.language_codes[0].split('-')
        language = Lang(language_country_code[0]).asdict()['name']
        country = pycountry.countries.get(alpha_2=language_country_code[1])
        if country is not None:
            locale_display_name =  language + ' ( ' + country.name +' ) '
        else:
            locale_display_name =  language + ' ( Multi Region )'

        type = voice.name.split('-')[2]
        if not type in types:
            types.append(type)
        transformed_voice =  {'name' : voice.name, 'type' : voice.name.split('-')[2], 'locale_display_name': locale_display_name}
        if not voice.language_codes[0] in voices:
           voices[voice.language_codes[0]] = [transformed_voice]
        else:
            transformed_voice['locale_display_name'] = ''
            voices[voice.language_codes[0]].append(transformed_voice)

    return {'types' : types,'voices' : voices}