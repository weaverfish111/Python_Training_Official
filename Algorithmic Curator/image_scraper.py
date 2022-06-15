# import webbrowser
# webbrowser.open(https://www.librarything.com/catalog/TheBlackArchives/yourlibrary)


import requests
from bs4 import BeautifulSoup
	
def getdata(url):
	r = requests.get(url)
	return r.text
	
htmldata = getdata("https://www.librarything.com/work/book/218041042")
soup = BeautifulSoup(htmldata, 'html.parser')

all_imgs = [img["src"] for img in soup.select(".workCoverImage")]
print(all_imgs)




# for item in soup.find("maincover", class_="mainleftimage"):
#     image = item['src']
#     print(image)
    # cover = item['src']
    # print(cover)
    
#     soup.find(div='mainCover', class_="mainleftimage")
#     # book_container = cover.nextSibling.nextSibling
#     print(cover)


# for item in soup.find_all('img'):
#     images = item['src'] + '\n'
    # print(images)
    # list_images = images.split()
    # cover_image = list_images[3]
    # cover_image = list_images[0]
    # print(cover_image)
	# print(item['src'])
    # print(item)
    # cover_image = item['src'].split()
    # print(cover_image)


# print(f"{item} is this")