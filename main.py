from selenium import webdriver
from bs4 import BeautifulSoup


urls = []
print("\nWelcome to the YouTube channel video scraper! ")
print("Enter as many YouTube channel urls as you want. Press 'q' to quit when you're done.\n")

while True:
    urls.append(input())
    if 'q' in urls:
        break
urls = urls[:-1]

def main():

    driver = webdriver.Chrome()
    for url in urls:
        print('')
        print('-'*100)
        choice = input(f"""\nHow do you want to sort {url}?
        1. Popularity - enter '1'
        2. Oldest - enter '2'
        3. Newest - enter '3'
        \n""")
        if choice == '1':
            driver.get('{}/videos?view=0&sort=p&flow=grid'.format(url))
        if choice == '2':
            driver.get('{}/videos?view=0&sort=da&flow=grid'.format(url))
        if choice == '3':
            driver.get('{}/videos?view=0&sort=dd&flow=grid'.format(url))
        
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        video_titles = soup.findAll('a',id='video-title')
        video_views = soup.findAll('span',class_='style-scope ytd-grid-video-renderer')
        video_urls = soup.findAll('a',id='video-title')

        num_of_titles = int(input(f"\nWhat is the number of videos that you want to see in {url}? \n\n"))
        print('')
        print('-'*100)
        print('\nChannel: {}'.format(url))

        i = 0 # views and time
        j = 0 # urls
        for title in video_titles[:num_of_titles]:
            print('\n{}\t{}\t{}\thttps://www.youtube.com{}'.format(title.text, video_views[i].text, video_views[i+1].text, video_urls[j].get('href')))
            i+=2
            j+=1
            
    print('')
    print('-' * 100)
    print('')
    print("Thank you for using the Youtube channel video scraper! \n")

main()

