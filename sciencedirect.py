import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from time import sleep
from sci_hub_pdf import download_pdf
from load_chrome_driver import load_driver

JOURNAL_BASE_URL = 'https://www.sciencedirect.com'
JOURNAL_URL = f"{JOURNAL_BASE_URL}/journal/european-journal-of-operational-research/issues"
print(JOURNAL_URL)

driver = load_driver()
# driver.get(JOURNAL_URL)
# contents = driver.page_source

contents = '''
<div id="1-accordion-panel-2" class="accordion-panel-content u-padding-xs-ver" role="tabpanel" aria-labelledby="1-accordion-tab-2"><section class="js-issue-list-content"><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/303/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 303, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 997-1506 (16 December 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/303/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 303, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 501-996 (1 December 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/303/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 303, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-500 (16 November 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/302/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 302, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 799-1294 (1 November 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/302/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 302, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 403-798 (16 October 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/302/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 302, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-402 (1 October 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/301/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 301, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 797-1194 (16 September 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/301/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 301, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 395-796 (1 September 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/301/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 301, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-394 (16 August 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/300/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 300, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 789-1194 (1 August 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/300/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 300, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 387-788 (16 July 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/300/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 300, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-386 (1 July 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/299/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 299, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 795-1192 (16 June 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/299/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 299, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 397-794 (1 June 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/299/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 299, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-396 (16 May 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/298/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 298, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 801-1192 (1 May 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/298/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 298, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 401-800 (16 April 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/298/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 298, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-400 (1 April 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/297/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 297, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 795-1192 (16 March 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/297/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 297, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 393-794 (1 March 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/297/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 297, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-392 (16 February 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/296/issue/3" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 296, Issue 3&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 749-1098 (1 February 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/296/issue/2" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 296, Issue 2&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 393-748 (16 January 2022)</h3></span></div><div class="issue-item u-margin-s-bottom"><a class="anchor js-issue-item-link text-m anchor-default" href="/journal/european-journal-of-operational-research/vol/296/issue/1" data-aa-name="Issue title" usagezone="rslt_list_item"><span class="anchor-text">Volume 296, Issue 1&nbsp;</span></a><span class="js-issue-status"><h3 class="js-issue-status text-s">Pages 1-392 (1 January 2022)</h3></span></div></section></div>
'''
# response = requests.get(JOURNAL_URL)
print("Parse is Ended")
soup = BeautifulSoup(contents, 'html.parser')

journal_name = 'European Journal of Operation Research'
# current_dir = os.getcwd()

current_dir = 'E://Book/Journals'
output_folder = current_dir + "/" + journal_name

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for link in soup.select('a.js-issue-item-link'):
    href = link['href']

    if "240" in href:
        break 

    href = JOURNAL_BASE_URL + href
    print(href)

    # response = requests.get(href)
    driver.get(href)
    contents = driver.page_source
    soup = BeautifulSoup(contents, 'html.parser')
    
    title = soup.select_one('.js-vol-issue').contents[0]
    print(title)

    output_folder = current_dir + "/" + journal_name  + "/" + title

    output_folder = output_folder.strip()
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    sleep(0.1)

    for link in soup.select('a.article-content-title'):
        href = link['href']

        title  = link.select_one('.js-article-title').contents[0]

        href = JOURNAL_BASE_URL + href

        # response = requests.get(href)
        driver.get(href)
        contents = driver.page_source
        soup = BeautifulSoup(contents, 'html.parser')

        href  = soup.select_one('a.doi').contents[0]

        # get doi
        doi = href.replace("https://doi.org/", "")
        doi = doi.strip()
        print(doi, title)

        count = 0
        while True:
            if download_pdf(doi, output_folder, title):
                break

            count = count + 1
            sleep(30)
            if count > 20:
                break

        sleep(0.5)

    # break
