import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import requests
from bs4 import BeautifulSoup


url = 'https://www.yahoo.com/news/weather/ukraine/kyiv-city-municipality/kyiv-924938/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'lxml')
tempF = soup.find('span', class_='Va(t)').text
tempC = (int(tempF) - 32) * 5 / 9.
# print(tempF)
# print(tempC)

f = open("temprinfo.txt", "w+")
f.write("Temperature today is {} Farenheits/{} Celsius".format(tempF, round(int(tempC), 1)))
f.close()


myemail = "myfinalprojectforpython@gmail.com"
recieversemail = "kkuzmichov@gmail.com" #Поменяйте на свой почтовый ящик для проверки

msg = MIMEMultipart()

msg['From'] = 'Python Weather Website Parser'
msg['To'] = 'Testuser'
msg['Subject'] = "Open File"

body = "Hello, this is my python project. In the file you will see current temperature for Kyiv in both Farenheit and Celsius values."

msg.attach(MIMEText(body, 'plain'))

filename = "temprinfo.txt"
attachment = open("C:\\Users\\YOURuSERNAME\\PycharmProjects\\parser\\temprinfo.txt", "rb") #Поменяйте имя пользователя на свое

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myemail, "password12345678")
text = msg.as_string()
server.sendmail(myemail, recieversemail, text)
server.quit()

