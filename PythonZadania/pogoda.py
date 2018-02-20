import re
import urllib.request

city = input("Wprowadz nazwe miasta: ")
url = "https://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

m = re.search('span class="phrase">', data1)
start = m.end()
end = start + 200
newString = data1[start:end]

m1 = re.search("min", newString)
start1 = m1.end()
end1 = start1 + 200
newString1 = newString[start1:end1]

m = re.search("&deg", newString)
end = m.start()
m = re.search("max", newString)
start = m.end()+1
tmax = newString[start:end]

m1 = re.search("&deg", newString1)
end1 = m1.start()
tmin = newString1[1:end1]

print("Miasto: " + city)
print("Temp max: " + tmax + u'\u2103')
print("Temp min: " + tmin + u'\u2103')