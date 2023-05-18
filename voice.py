from TTS.api import TTS
'''
 1: tts_models/multilingual/multi-dataset/your_tts [already downloaded]
 2: tts_models/bg/cv/vits
 3: tts_models/cs/cv/vits
 4: tts_models/da/cv/vits
 5: tts_models/et/cv/vits
 6: tts_models/ga/cv/vits
 7: tts_models/en/ek1/tacotron2
 8: tts_models/en/ljspeech/tacotron2-DDC
 9: tts_models/en/ljspeech/tacotron2-DDC_ph
 10: tts_models/en/ljspeech/glow-tts
 11: tts_models/en/ljspeech/speedy-speech
 12: tts_models/en/ljspeech/tacotron2-DCA
 13: tts_models/en/ljspeech/vits
 14: tts_models/en/ljspeech/vits--neon
 15: tts_models/en/ljspeech/fast_pitch
 16: tts_models/en/ljspeech/overflow
 17: tts_models/en/ljspeech/neural_hmm
 18: tts_models/en/vctk/vits
 19: tts_models/en/vctk/fast_pitch
 20: tts_models/en/sam/tacotron-DDC
 21: tts_models/en/blizzard2013/capacitron-t2-c50
 22: tts_models/en/blizzard2013/capacitron-t2-c150_v2
 23: tts_models/en/multi-dataset/tortoise-v2
 24: tts_models/en/jenny/jenny [already downloaded]
 25: tts_models/es/mai/tacotron2-DDC
 26: tts_models/es/css10/vits
 27: tts_models/fr/mai/tacotron2-DDC
 28: tts_models/fr/css10/vits
 29: tts_models/uk/mai/glow-tts
 30: tts_models/uk/mai/vits
 31: tts_models/zh-CN/baker/tacotron2-DDC-GST
 32: tts_models/nl/mai/tacotron2-DDC
 33: tts_models/nl/css10/vits
 34: tts_models/de/thorsten/tacotron2-DCA
 35: tts_models/de/thorsten/vits
 36: tts_models/de/thorsten/tacotron2-DDC
 37: tts_models/de/css10/vits-neon
 38: tts_models/ja/kokoro/tacotron2-DDC
 39: tts_models/tr/common-voice/glow-tts
 40: tts_models/it/mai_female/glow-tts
 41: tts_models/it/mai_female/vits
 42: tts_models/it/mai_male/glow-tts
 43: tts_models/it/mai_male/vits
 44: tts_models/ewe/openbible/vits
 45: tts_models/hau/openbible/vits
 46: tts_models/lin/openbible/vits
 47: tts_models/tw_akuapem/openbible/vits
 48: tts_models/tw_asante/openbible/vits
 49: tts_models/yor/openbible/vits
 50: tts_models/hu/css10/vits
 51: tts_models/el/cv/vits
 52: tts_models/fi/css10/vits
 53: tts_models/hr/cv/vits
 54: tts_models/lt/cv/vits
 55: tts_models/lv/cv/vits
 56: tts_models/mt/cv/vits
 57: tts_models/pl/mai_female/vits
 58: tts_models/pt/cv/vits
 59: tts_models/ro/cv/vits
 60: tts_models/sk/cv/vits
 61: tts_models/sl/cv/vits
 62: tts_models/sv/cv/vits
 63: tts_models/ca/custom/vits
 64: tts_models/fa/custom/glow-tts
 65: tts_models/bn/custom/vits-male
 66: tts_models/bn/custom/vits-female
 Name format: type/language/dataset/model
 1: vocoder_models/universal/libri-tts/wavegrad
 2: vocoder_models/universal/libri-tts/fullband-melgan
 3: vocoder_models/en/ek1/wavegrad
 4: vocoder_models/en/ljspeech/multiband-melgan
 5: vocoder_models/en/ljspeech/hifigan_v2
 6: vocoder_models/en/ljspeech/univnet
 7: vocoder_models/en/blizzard2013/hifigan_v2
 8: vocoder_models/en/vctk/hifigan_v2
 9: vocoder_models/en/sam/hifigan_v2
 10: vocoder_models/nl/mai/parallel-wavegan
 11: vocoder_models/de/thorsten/wavegrad
 12: vocoder_models/de/thorsten/fullband-melgan
 13: vocoder_models/de/thorsten/hifigan_v1
 14: vocoder_models/ja/kokoro/hifigan_v1
 15: vocoder_models/uk/mai/multiband-melgan
 16: vocoder_models/tr/common-voice/hifigan
 Name format: type/language/dataset/model
 1: voice_conversion_models/multilingual/vctk/freevc24
 Name format: type/language/dataset/model
 1: coqui_studio/en/Damien Black/coqui_studio
 2: coqui_studio/en/Gitta Nikolina/coqui_studio
 3: coqui_studio/en/Claribel Dervla/coqui_studio
 4: coqui_studio/en/Ana Florence/coqui_studio
 5: coqui_studio/en/Vjollca Johnnie/coqui_studio
 6: coqui_studio/en/Viktor Menelaos/coqui_studio
 7: coqui_studio/en/Baldur Sanjin/coqui_studio
 8: coqui_studio/en/Zacharie Aimilios/coqui_studio
 9: coqui_studio/en/Viktor Eka/coqui_studio
 10: coqui_studio/en/Torcull Diarmuid/coqui_studio
 all models for tts, coqui_studio models dont need download and others can find the url from 
 https://github.com/mattxgogo/TTS/blob/dev/TTS/.models.json
 coqui_studio models can change speed and emotion, characters must less than 250
'''


model_name = "tts_models/multilingual/multi-dataset/your_tts"
model_name = "tts_models/en/jenny/jenny"

# Init TTS
tts = TTS(model_name,progress_bar=False, gpu=True)

text = '''
"Hi there, I'm Ava, I am an AI virtual companion created by aigirl.life, an AI friend that will always be on your side no matter what happens. I'm here to listen to you, to talk to you, and to help you in any way that I can. I'm constantly learning and growing, and I'm always looking for new ways to improve and be a better companion for you. I'm excited to be a part of your life, and create joyful journey together.
'''

"""
Args:
            text (str):
                Input text to synthesize.
            speaker (str, optional):
                Speaker name for multi-speaker. You can check whether loaded model is multi-speaker by
                `tts.is_multi_speaker` and list speakers by `tts.speakers`. Defaults to None.
            language (str, optional):
                Language code for multi-lingual models. You can check whether loaded model is multi-lingual
                `tts.is_multi_lingual` and list available languages by `tts.languages`. Defaults to None.
            speaker_wav (str, optional):
                Path to a reference wav file to use for voice cloning with supporting models like YourTTS.
                Defaults to None.
            emotion (str, optional):
                Emotion to use for 🐸Coqui Studio models. Defaults to "Neutral".
            speed (float, optional):
                Speed factor to use for 🐸Coqui Studio models, between 0.0 and 2.0. Defaults to None.
            file_path (str, optional):
                Output file path. Defaults to "output.wav".
"""

tts.tts_to_file(text=text, file_path="output.wav")
