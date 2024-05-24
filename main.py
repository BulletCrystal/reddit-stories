import requests
import pyttsx3
from bs4 import BeautifulSoup

def say(p):
    from gtts import gTTS

    # Text to be converted to speech 
    tts = gTTS(text=p, lang='en', tld='us')
    tts.save("Final.mp3")
    print('Audio has been Saved Succesfully At Final.mp3')


def split_into_four(text):
  n = input("enter the number of sequences to divide the paragraphe : ")
  ideal_length = len(text) // int(n)

  # Initialize the list to store the split parts
  split_parts = []

  # Iterate through the string, splitting based on ideal length
  start_index = 0
  while start_index < len(text):
    # Consider the remaining string length to avoid out-of-bounds indexing
    end_index = min(start_index + ideal_length, len(text))
    split_parts.append(text[start_index:end_index])
    start_index = end_index

  return split_parts

def coller_fichiers_audio(fichiers_sources, fichier_destination):

  with open(fichier_destination, 'wb') as destination:
    for fichier_source in fichiers_sources:
      with open(fichier_source, 'rb') as source:
        destination.write(source.read())
        
def say_eleven(p):
    
    import elevenlabs
    p = split_into_four(p)
    index = 0
    voices = []
    for i in p:
        audio = elevenlabs.generate(i)
        elevenlabs.save(audio,f'./Audios/Audio_{index}.mp3')
        voices.append(f'./Audios/Audio_{index}.mp3')
        index +=1
    coller_fichiers_audio(voices, 'Final.mp3')
    print("Audio has been Saved Succefully At Final.mp3")

def chose():
    
    try :
        while(True):
            print(f"""
        Please Select wich option you want :
        1 >> Enter a preferable link
        2 >> Select from the feed by number
        3 >> Display the list of links
        4 >> Quit
        """)
            choice = input()
            if choice == '1':
                url = input("enter the link to subreddit : ")
                if 'https' in url :
                    main(url)
                else :
                    main("https://www.reddit.com" +url)
            elif choice == '2':
                from lib.get_link import all_links
                lenght = len(all_links)
                choice = input(f"enter the index from the list from 0 to {lenght-1}: ")
                print("https://www.reddit.com" + all_links[int(choice)])
                main( "https://www.reddit.com" + all_links[int(choice)] )
            elif choice =='3':
                with open('Links.txt','r') as rb:
                    print("".join(rb.readlines()))
            elif choice =='4':
                break
            else :
                print("Error. PLease Try Again ...")
                break
    except Exception as e :
        print("Error Please Try Again !..",'\n',e)

def main(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request was successful!")
        soup = BeautifulSoup(response.content,'html.parser')
        ps = soup.find(name='div',class_="text-neutral-content")# p : All the paragraphes in the url
        ps = ps.find_all(name = 'p')
        Paragraphe = "".join([p.text.strip() for p in ps])
        print(Paragraphe)
        a = input('''enter voice choice :
1 >> eleven labs
2 >> Google voice
3 >> chose again
''')
        if a == '1':
            say_eleven(Paragraphe)
        elif a == '2':
            say(Paragraphe)
        else:
            pass
    else:
        print("Failed to get response from the website.")


if __name__ == '__main__':
    chose()
