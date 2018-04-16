from win10toast import ToastNotifier
import time
from topnews import topStories
newsitems = topStories()
for i in range(len(newsitems)):
	title = str(newsitems[i]['title']);
	description = str(newsitems[i]['description'])
	toaster = ToastNotifier()
	toaster.show_toast( title, description, duration= 10)
	while toaster.notification_active(): time.sleep(0.1)