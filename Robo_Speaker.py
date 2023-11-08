import os

if __name__ == "__main__":

    while(True):

        text = input("Enter the text you want the robo-speaker to say: ")
        os.system(f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')
        if text == "bye bye":
            break
# os.system() is a function that allows running system commands.
# The PowerShell -Command part is a command-line instruction that tells the operating system to execute the following command in PowerShell.
# Add-Type -AssemblyName System.Speech loads the necessary .NET assembly required for speech synthesis.
# (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\') creates a new SpeechSynthesizer object and uses the Speak() method to read out the text provided by the user