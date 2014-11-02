from selenium import webdriver

br=webdriver.Firefox()

def whatupwhelans(page):
	br.get("http://www.whelanslive.com/index.php/page/"+str(page)+"/")
	li=br.find_elements_by_class_name("event-listing") #list of events cut down li[0]

	for i in range(1, len(li)):
		print "="*10
		if page == 0:
			print "[",i,"]"
		else:
			count = (page-1)*10+i
			print "[",count,"]"

		print li[i].find_element_by_tag_name("a").get_attribute("href") #link to full description
		print li[i].find_element_by_tag_name("a").get_attribute("title") #name of band
		print li[i].find_element_by_tag_name("img").get_attribute("src") #image
		print li[i].find_element_by_class_name("event-title").find_element_by_css_selector('h3').text #date
		print li[i].find_elements_by_css_selector('p')[1].text #short description
		#http://www.whelanslive.com/index.php/wav-tickets/paper-aeroplanes-tickets/ #buy now

		footer = li[i].find_element_by_class_name("event-footer")
		try:
			print footer.find_element_by_css_selector("span").text #location
		except:
			pass	
		print footer.find_elements_by_css_selector("b")[0].text #time
		print footer.find_elements_by_css_selector("b")[1].text #price

try:
	for page in range(1,11):
		whatupwhelans(page)
except:
	pass


