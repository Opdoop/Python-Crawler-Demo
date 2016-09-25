#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
#import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"http://computer.swu.edu.cn/s/computer/szdw2\w+/\d+/\d+.html"))
        for link in links:
            
            new_url = link['href']
            if  new_url == "http://computer.swu.edu.cn/s/computer/szdw2js/20160427/913961.html":
                continue
            #new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}    
        table = soup.find('table')
        
        node = table.find("span", {"id":"U_CName_Value"})
        res_data['CName'] = node
        node = table.find("span", {"id":"U_Sex_Value"})
        res_data['Sex'] = node
        node = table.find("span", {"id":"U_GroupID_Value"})
        res_data['GroupID'] = node
        node = table.find("span", {"id":"U_searchD"})
        res_data['U_searchD'] = node
        node = table.find("span", {"id":"U_Email_Value"})
        res_data['Email'] = node
        #<td colspan="5">
        try:
            node = soup.find_all('td',colspan='5')
            res_data['Profile'] = node[1] 
            res_data['Teach'] = node[3]
            res_data['Program'] = node[5]  
            res_data['Reward'] = node[7]  
            res_data['Tip'] = node[9] 
        except:
            pass
        return res_data
