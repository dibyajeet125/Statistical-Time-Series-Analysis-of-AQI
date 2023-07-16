import requests
import matplotlib.pyplot as plt
import webbrowser

#Search
Country = input("Enter Country Name: ")
State = input("Enter State Name: ")
City = input("Enter City Name: ")

url = 'http://api.waqi.info/feed/' + City + '/?token='
api_key = '00e5f4250d2e3dcc9112dae398489457f33d6b61'
#main url of api
main_url = url + api_key
#how go to this api for that
#get method which can acess api
r = requests.get(main_url)
#above api will retun with a json file
#javascript object notification
#extract json from api with json method
#data = r.json()
#r.json() is the dictionary
#'data' is the key name
data = r.json()['data']
#for a dictionary to appear
#print(data)

#city's unique index no.
idx = data['idx']
print('Index No. of ' + City + ': ', idx)
#organisations from where the results are collected
attributions = data['attributions']
print('Organisations name & its Url: ', attributions)
city = data['city']
#print(city)
#location of the city
geo = city['geo']
print('Latitude & Longitude respectively: ', geo)
name = city['name']
print('Pollution Station: ', name)

aqi = data['aqi']
print(f'{City} AQI: ', aqi)
#Presently the most Dominent Pollutant in the Air
dominentpol = data['dominentpol']
print('Dominent Pollutant: ', dominentpol)
iaqi = data['iaqi']
#print('iaqi')
#print only pollutants name & its value
for i in iaqi.items():
    #0th index polluntant name
    #1st index there is a dictionary(value)
    #v(value) is the key name
    print(i[0], ':', i[1]['v'])

#store the key names of pollutants
pollutants = [i for i in iaqi]
#store the values of pollutants
values = [i['v'] for i in iaqi.values()]

# Plot a pie chart
#adjust the size of pie chart
plt.figure(figsize=(10, 8))
#keep pollutants as lebel
#autopct is to show the % of the pollutants
plt.pie(values, labels=pollutants, autopct='%1.1f%%')

#title for pie chart
plt.title('Air pollutants and their % in Air in ' + City)

plt.show()

webbrowser.open("https://aqicn.org/map/" + City + "/")
webbrowser.open("https://www.iqair.com/in-en/air-quality-map/" + Country + "/" + State + "/" + City)
webbrowser.open("https://www.iqair.com/in-en/" + Country + "/" + State + "/" + City)




url2 = "https://aqicn.org/map/" + City + "/?token="
api_key = '00e5f4250d2e3dcc9112dae398489457f33d6b61'

main_url2 = url2 + api_key
r2 = requests.get(main_url2)

f = open('C:\\Users\\Hp\\Documents\\5th Sem\\CS 591 Project-1(A)\\map.html', 'wb')

f.write(r2.content)
f.close()

