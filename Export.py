from bs4 import BeautifulSoup

with open('MapPage.html', 'r', encoding="utf8") as f:
    txt = f.read()
    soup = BeautifulSoup(txt,"html5lib")

elements = soup.find_all('tr')
elements.pop(0)

def ExtractData(msgID):
    for e in elements:
        ID = e.find('a').contents[0]
        if int(msgID)==int(ID):
            return e
    print('Failed to extract data from', msgID)
    return False

def DeleteData(msgID):
    for e in elements:
        ID = e.find('a').contents[0]
        if int(msgID)==int(ID):
            e.decompose()
            print('Successfully deleted data from', msgID)
            with open('MapPage.html', 'w', encoding="utf8") as f:
                f.write(str(soup))
            return
    print('Failed to delete data from', msgID)
    return False
    
def UpdateData(msgID, rating):
    for e in elements:
        ID = e.find('a').contents[0]
        if int(msgID)==int(ID):
            A = e.find_all('td')[-1]
            A.string = str(rating)
            print('Successfully updated data from', msgID)
            with open('MapPage.html', 'w', encoding="utf8") as f:
                f.write(str(soup))
            return
    print('Failed to update data from', msgID)
    return False

def AddData(Data): #[message-id(link), messageID, Author, Content, Thumbnail(img-link),
    print('Adding row', Data[0])
    #make the tags
    tableBody = soup.find('tbody')
    row = soup.new_tag('tr')
    msgIDparent = soup.new_tag('td')
    msgID = soup.new_tag('a', href=(str(Data[1])))
    msgID.string = str(Data[0])
    Author = soup.new_tag('td')
    Author.string = str(Data[2])
    if Data[3] == '':
        Content = soup.new_tag('td', 'empty')
    else:
        Content = soup.new_tag('td')
        Content.string = str(Data[3])
    imgParent = soup.new_tag('td')
    img = soup.new_tag('img', src=Data[4], alt='thumb', width='300',height='auto')
    downloadParent = soup.new_tag('td')
    download = soup.new_tag('a', href=str(Data[5]))
    download.string = 'Download'
    rating = soup.new_tag('td')
    rating.string = str(Data[6])
    #apply the tags
    tableBody.insert(len(tableBody)-1, row)
    row.insert(0, msgIDparent)
    msgIDparent.insert(0, msgID)
    row.insert(1, Author)
    row.insert(2, Content)
    row.insert(3, imgParent)
    imgParent.insert(0, img)
    row.insert(4, downloadParent)
    downloadParent.insert(0, download)
    row.insert(5, rating)
    print('Success!')
    with open('MapPage.html', 'w', encoding="utf8") as f:
        f.write(str(soup))
