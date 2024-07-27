---
title: Audio Transcribe Translate
emoji: 🚀
colorFrom: purple
colorTo: yellow
sdk: gradio
sdk_version: 4.39.0
app_file: app.py
pinned: false
license: mit
---

<p align='center'>
  <img src="https://github.com/PhuongFX/Audio_Transcribe_Translate/blob/8ce5e3f0183d4b9b081a01c41c71d092c087acf0/Interfaces/Screenshot%202024-07-27%20230331.jpg" />
</p>




## Description 📝

    > Using OpenAI Whisper Base model to transcribe audio files into text Google Madlad model to translate transcribed texts into multiple languages. 
    > Enabling users to convert spoken words into written text. 
    > Supporting various use cases, including transcription of audio files, detection of phrases, speech-to-text generation, and translation of text.
    
## How it Works 🫶

  - Upload an audio file or record a new one directly in the app.
  - Transcribe the audio into text, allow copy and paste function for further use.
  - Or/ Translates the transcribed text into multiple languages.

## Usage 🤗

  - Transcribe audio files for note-taking, research, or content creation
  - Detect phrases or keywords in audio recordings for data analysis or market research
  - Generate text from speech for speech-to-text applications, such as subtitles, closed captions, or voice assistants
  - Use the app for language learning, by transcribing audio files in a foreign language and practicing pronunciation
  - Translate the transcribed text into multiple languages for global communication

## Features 🎉

1. Supports audio files and live recording 📻
2. Uses the OpenAI Whisper Base model for speech recognition 💬
3. Displays transcribed text in the app 📝
4. Allows you to copy and paste the transcribed text for further use 📋
5. Translates the transcribed text into multiple languages using the Google Madlad model 🌎


## Model Details 📊   
<p style='text-align: center'>"
				"🐤 <a href='https://huggingface.co/openai/whisper-small' target='_blank'>OpenAI Whisper</a> | "
				"🧑‍💻 <a href='https://huggingface.co/google/madlad400-3b-mt' target='_blank'>Google Madlad</a> |"
			"</p>

    The OpenAI Whisper Base model is a pre-trained model for automatic speech recognition (ASR) and speech translation.
    It was trained on 680k hours of labelled data and demonstrates a strong ability to generalize to many datasets and domains without fine-tuning.

| Size     | Parameters | English-only                                         | Multilingual                                        |
|----------|------------|------------------------------------------------------|-----------------------------------------------------|
| tiny     | 39 M       | [✓](https://huggingface.co/openai/whisper-tiny.en)   | [✓](https://huggingface.co/openai/whisper-tiny)     |
| base     | 74 M       | [✓](https://huggingface.co/openai/whisper-base.en)   | [✓](https://huggingface.co/openai/whisper-base)     |
| small    | 244 M      | [✓](https://huggingface.co/openai/whisper-small.en)  | [✓](https://huggingface.co/openai/whisper-small)    |
| medium   | 769 M      | [✓](https://huggingface.co/openai/whisper-medium.en) | [✓](https://huggingface.co/openai/whisper-medium)   |
| large    | 1550 M     | x                                                    | [✓](https://huggingface.co/openai/whisper-large)    |
| large-v2 | 1550 M     | x                                                    | [✓](https://huggingface.co/openai/whisper-large-v2) |
| large-v3 | 1550 M     | x                                                    | [✓](https://huggingface.co/openai/whisper-large-v3) |


	For both the machine translation and language model, MADLAD-400 (Multilingual (400+ languages)) is used. For the machine translation model, a combination of parallel datasources covering 157 languages is also used. Using a Sentence Piece Model with 256k tokens shared on both the encoder and decoder side. Each input sentence has a <2xx> token prepended to the source sentence to indicate the target language.


![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b7f632037d6452a321fa15/EzsMD1AwCuFH0S0DeD-n8.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b7f632037d6452a321fa15/CJ5zCUVy7vTU76Lc8NZcK.png)

![image/png](https://cdn-uploads.huggingface.co/production/uploads/64b7f632037d6452a321fa15/NK0S-yVeWuhKoidpLYh3m.png)

See the [research paper](https://arxiv.org/pdf/2309.04662.pdf) for further details.

    
## Disclaimer 🙅‍♂️

> This app is for personal use only and should not be used for commercial purposes.
The OpenAI Whisper Base model and Google Madlad model are pre-trained models and may not always produce accurate results.


