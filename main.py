from multiprocessing.connection import wait
import os
from xml.etree.ElementTree import tostring

for filename in os.listdir(os.getcwd() + "/src/"):
	os.system("pandoc -s -f markdown --template=template --css=style.css -M title={} -o {}.html .\src\{}".format(os.path.basename(filename)[:-3], os.path.basename(filename)[:-3], format(os.path.basename(filename)))
)