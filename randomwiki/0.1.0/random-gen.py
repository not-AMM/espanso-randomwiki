import wikipedia
import pyperclip
import webbrowser

def new():
    pag = wikipedia.random(1)
    cont = wikipedia.page(pag)
    url = cont.url
    print(pag + " | " + url)
    pyperclip.copy(url)

new()
