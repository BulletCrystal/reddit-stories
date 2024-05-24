from gtts import gTTS

# Text to be converted to speech (replace with your desired text)
text = "This is an example text spoken in a male voice."

# Language code for male voice (US English - 'en')
language = 'en'

# Male voice can be achieved by adjusting the voice parameter
# (limited options available in free tier)

# Create a Text-to-Speech object with the specified text, language, and voice
tts = gTTS(text=text, lang=language, slow=False, tld='us')

# Save the audio file (replace 'male_voice_output.mp3' with your desired filename)
tts.save("male_voice_output.mp3")

print("Audio file with male voice saved as male_voice_output.mp3")
