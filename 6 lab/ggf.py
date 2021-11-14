




def pause(url):
    r = requests.get(url)
    soup = BeatifulSoup(r.text, 'html.parser')
    return soup
page = pause(url)
content = page.find('div', 'content-article')

def inside():
    i = 0
    for link in content.find_all('a', href = True):
        i+=1
        text = page.find('div', 'content-article').text
        words = len(text.split())
        img = len([tag.name for tag in page.find_all('img')])
        links = len([tag.name for tag in page.find_all('link')])
        tags = len([tag.name for tag in page.find_all()])
    print('Слів у тексті:')
    print('слів', words)
    print('Картинок', img)
    print('Тегів', tags)
    print('Посилань', links)
print(inside())    