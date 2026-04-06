# Parent class 1
class WiFiDevice:
    def connect_wifi(self):
        print("WiFi connected")

# Parent class 2
class VoiceAssistant:
    def enable_voice(self):
        print("Voice assistant enabled")

# Child class (Multiple Inheritance)
class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def play_music(self):
        print("Playing music")

# Main function
def main():
    speaker = SmartSpeaker()

    speaker.connect_wifi()
    speaker.enable_voice()
    speaker.play_music()

# Entry point
if __name__ == "__main__":
    main()
