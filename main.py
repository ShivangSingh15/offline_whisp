# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import streamlit as st
import whisper

 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 10

st.title("Live Voice to Text Conversion")
 
record_button = st.button(label="Record Audio")
# Start recorder with the given values
# of duration and sample frequency
if record_button:
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=1)
 
# Record audio for the given number of seconds
    sd.wait()
 
# This will convert the NumPy array to an audio
# file with the given sampling frequency
    write("recording0.wav", freq, recording)

    audio_file = "recording0.wav"

    model = whisper.load_model("medium")
    st.text("Whisper Model Loaded")

# transcribe_button = st.button(label="Transcribe Audio")

# if transcribe_button:
    if audio_file is not None:
        
        st.success("Transcribing Audio")
        transcription = model.transcribe(audio_file)
        st.success("Transcription Complete")
        
        st.write(transcription["text"])
        #st.text(end_time-start_time)
    else:
        st.error("Upload audio file")
# Convert the NumPy array to audio file
#wv.write("recording1.wav", recording, freq, sampwidth=2)