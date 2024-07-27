import torch
import spaces
import gradio as gr

from transformers import pipeline
from huggingface_hub import model_info

MODEL_NAME = "openai/whisper-small"

device = 0 if torch.cuda.is_available() else "cpu"
pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL_NAME,
    chunk_length_s=30,
    device=device,
)

pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids( task="transcribe")

@spaces.GPU(duration=240)
def transcribe(mic, file_upload):

    file = mic if mic is not None else file_upload

    text = pipe(file)["text"]
    return text


#---------------------------------------------------------------
import ctranslate2
import gradio as gr
from huggingface_hub import snapshot_download
from sentencepiece import SentencePieceProcessor

model_name = "santhosh/madlad400-3b-ct2"
model_path = snapshot_download(model_name)

tokenizer = SentencePieceProcessor()
tokenizer.load(f"{model_path}/sentencepiece.model")
translator = ctranslate2.Translator(model_path)
tokens = [tokenizer.decode(i) for i in range(460)]
lang_codes = [token[2:-1] for token in tokens if token.startswith("<2")]


@spaces.GPU(duration=240)
def translate(input_text, target_language):
    input_tokens = tokenizer.encode(f"<2{target_language}> {input_text}", out_type=str)
    results = translator.translate_batch(
        [input_tokens],
        batch_type="tokens",
        beam_size=1,
        no_repeat_ngram_size=1,
    )
    translated_sentence = tokenizer.decode(results[0].hypotheses[0])
    return translated_sentence


@spaces.GPU(duration=240)
def translate_interface(input_text, target_language):
    translated_text = translate(input_text, target_language)
    return translated_text


with gr.Blocks() as demo:
    with gr.Column():
        gr.Markdown(
        """
       
        <div style="text-align: left;">
            <a href='https://huggingface.co/PhuongPhan'><img style='display: inline-block; margin: 0; padding: 0;' src='https://huggingface.co/datasets/huggingface/badges/resolve/main/follow-me-on-HF-sm-dark.svg' alt='Follow me on HF'></a>
            <a href='https://huggingface.co/Chunte'><img style='display: inline-block; margin: 0; padding: 0;' src='https://img.shields.io/badge/GitHub%20Pages-121013?logo=github&logoColor=white' alt='GitHub Pages'></a>
        </div>

        """ )

        gr.Markdown("<h1 style='text-align: center;'>🎤 Speech to Text & Translation 🗣️</h1>")

        gr.HTML(
            "<p style='text-align: center'>"
                "🐤 <a href='https://huggingface.co/openai/whisper-small' target='_blank'>OpenAI Whisper</a>  | "
                "🧑‍💻 <a href='https://huggingface.co/google/madlad400-3b-mt' target='_blank'>Google Madlad</a>"
            "</p>")
        
        gr.Markdown("<p style='text-align: center;'><i>Upload an audio file or use your microphone to transcribe speech and then translate it to different languages.</i></p>")    


    gr.Examples(
            examples=[
                "Speech_samples/consumer4.wav", 
                "Speech_samples/samples_audio-files_05-gettysburg-address-2min.wav"
                "Speech_samples/samples_audio-files_12-jfk-speech-12sec.wav"
                "Speech_samples/harvard.wav"
            ],
            inputs=audio_input,
            label="Try these examples"
        )

    
    with gr.Row():
        # First interface for transcription
        gr.Markdown("## 🎙️ Transcribe Audio ") 
        gr.Markdown("---")
        audio_input = gr.Audio(sources=["upload", "microphone"], type="filepath")
        transcribe_button = gr.Button("Transcribe")
        transcribed_output = gr.Textbox(label="Transcribed Text")
        transcribe_button.click(transcribe, inputs=audio_input, outputs=transcribed_output)

    with gr.Row():
        # Second interface for translation
        gr.Markdown("## 🌐 Translate Text 🌐")
        gr.Markdown("---") 
        lang_dropdown = gr.Dropdown(lang_codes, value="en", label="Target Language")
        translate_button = gr.Button("Translate")
        translated_output = gr.Textbox(label="Translated Text")
        translate_button.click(translate_interface, inputs=[transcribed_output, lang_dropdown], outputs=translated_output)

    gr.Markdown("---")
    with gr.Accordion("See Details", open = False):

        gr.Markdown("---")
        gr.Markdown('''

## Description 📝

    > Using OpenAI Whisper Base model to transcribe audio files into text Google Madlad model to translate transcribed texts into multiple languages. 
    > Enabling users to convert spoken words into written text. 
    > Supporting various use cases, including transcription of audio files, detection of phrases, speech-to-text generation, and translation of text.
    
## How it Works 🫶

    - Upload an audio file or record a new one directly in the app.
    - Transcribe the audio into text, allow copy and paste function for further use.
    - Or/ Translates the transcribed text into multiple languages.

## Usage 🤗

    1. Transcribe audio files for note-taking, research, or content creation
    2. Detect phrases or keywords in audio recordings for data analysis or market research
    3. Generate text from speech for speech-to-text applications, such as subtitles, closed captions, or voice assistants
    4. Use the app for language learning, by transcribing audio files in a foreign language and practicing pronunciation
    5. Translate the transcribed text into multiple languages for global communication

## Disclaimer 🙅‍♂️

> This app is for personal use only and should not be used for commercial purposes.
The OpenAI Whisper Base model and Google Madlad model are pre-trained models and may not always produce accurate results.   ''')

    demo.queue(max_size=20)
    demo.launch()
