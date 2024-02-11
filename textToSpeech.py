import elevenlabs
import elevenLabsApiKey

#make a python file with KEY = "Insert api key here"
elevenlabs.set_api_key(elevenLabsApiKey.KEY)

text = "Hi, i'm Damiano and this is my text to speech."

#here to change the voice
voice_id = "bVMeCyTHy58xNoL34h3p"

#voice settings
voice = elevenlabs.Voice(
    voice_id = voice_id,
    settings = elevenlabs.VoiceSettings(
        stability = 0.3, 
        similarity_boost = 0.75
    )
)
        
audio = elevenlabs.generate(
    text = text,
    voice = voice
)

mp3_name = voice_id[0] + "audio" + voice_id[-1]
elevenlabs.save(audio, f"{mp3_name}.mp3")