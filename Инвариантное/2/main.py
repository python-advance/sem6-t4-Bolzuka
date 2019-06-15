import pyqrcode

url = pyqrcode.create('https://moodle.herzen.spb.ru/')
url.svg('uca-url.svg', scale=2, module_color='#7D007D')
url.eps('uca-url.eps', scale=2, module_color='#36C')
print(url.terminal(quiet_zone=1))