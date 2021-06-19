import smtplib
import datetime as dt
import time

def ymd(ymd_input):
    str_ymd_input = str(ymd_input)
    year = str_ymd_input[0:4]
    month = str_ymd_input[5:7]
    date = str_ymd_input[8:10]
    y = int(year)
    m = int(month)
    d = int(date)
    return (y,m,d)
  
sender_email = input("Enter sender's email: ")
password = input("Enter sender's password: ")
print()
count = int(input("Enter the number of receivers: "))
receiver_email = []
for i in range(count):
    print("Mail id of receiver",i+1,": ",end="")
    mail = input()
    receiver_email.append(mail)
print()

time_hour = int(input("Enter the hour to send mail: "))
time_minute = int(input("Enter the minute to send mail: "))
time_second = int(input("Enter the seconds to send mail: "))
print()

file = input("Enter file path: ")
with open(file,"r") as f:
    message = f.read()
    
print()

today = dt.datetime.today()
y,m,d = ymd(today)
 
while(True):
    send_time = dt.datetime(y,m,d,time_hour,time_minute,time_second)
    if (send_time.timestamp() - time.time())<0:
        next_date = dt.datetime.today() + dt.timedelta(days=1)
        y,m,d = ymd(next_date)
        send_time = dt.datetime(y,m,d,time_hour,time_minute,time_second)
    print("Mail will be sent on ",end = "")
    print(d,m,y,sep = ".",end = "")
    print(" at ",end = "")
    if(time_hour < 10):
        str_time_hour =  '0' + str(time_hour)
    else:
        str_time_hour = str(time_hour)
    if(time_minute < 10):
        str_time_minute =  '0' + str(time_minute)
    else:
        str_time_minute = str(time_minute)
    print(str_time_hour,str_time_minute,sep = ".")
    x = time.sleep(send_time.timestamp() - time.time())
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print("Login successful")
    for i in receiver_email:
        server.sendmail(sender_email,i,message)
        print("Mail has been sent to",i)
    server.quit()
    print("Logged out")
    print()
    next_date = dt.datetime.today() + dt.timedelta(days=1)
    y,m,d = ymd(next_date)
