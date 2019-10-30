from tkinter import Tk, Label, Button, Entry, Frame, messagebox
from bs4 import BeautifulSoup
import requests, json, fileinput
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart

def send_mail(url):
    with open("user_mail.zxt", 'r') as f:
        usr_mail = f.read()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sasta.hua.maal@gmail.com','Oldprice123')

    subject = "Price Fell Down, Ja ke Dekho"
    body = "the products price has decreased, follow the link given below \nRegards,\nmiri's and Yash's Price Checker"

    msg = f"Subject: {subject}\n\n{body}\n\n{url}"

    server.sendmail(
        'sasta.hua.maal@gmail.com', '{}'.format(usr_mail), msg)

    print('Hey Email Gaya, check kar jaldi')

def convert(price_str):
    temp = price_str
    temp2 = temp.replace('₹', '')
    temp3 = temp2.replace(',', '')
    float(temp3)
    # i m so dumb    
    return temp3

def prompt():
    for i in range(0,5):
            file = Path("info_{}".format(i))
            if file.exists():
                with open("info_{}".format(i), 'r') as r_data:
                    data = r_data.read()
                data = json.loads(data)
                title = data['title']
                price = data['price_float']
                file_price = float(price)
                product_url = data['url']
                
                page = requests.get(product_url)
                soup = BeautifulSoup(page.content,'html.parser')
                title = soup.find("span",{"class":"_35KyD6"})
                title = title.get_text()
                price = soup.find("div",{"class":"_1vC4OE _3qQ9m1"})
                fetched_price_float = convert(price.get_text()) 
                fetched_price_float = float(fetched_price_float)
                
                print("file price : ",file_price)
                print("fetched price : ", fetched_price_float)
                
                if file_price < fetched_price_float:
                    messagebox.showinfo("YAYYYYYYY!!!!!", "{} is cheap".format(title))
                    send_mail(product_url)
                
            else:
                continue

def make_labels(root):
    counter = 0
    for i in range(0,5):
        file = Path("info_{}".format(i))
        if file.exists():
            with open("info_{}".format(i), 'r') as r_data:
                data = r_data.read()
            data = json.loads(data)
            title = data['title']
            price = data['price_string']
            l = Label(root, text="[{}]  Product : {}".format((i+1),title), font=("arial", 12),fg="#2df0a0", bg="#090b10")
            l.place(x=50,y=50+counter)
            l2 = Label(root, text="      Old Price : {}".format(price), font=("arial", 11),fg="#1cb99d", bg="#090b10")
            l2.place(x=50,y=75+counter)
            #print(title)
        else:
            continue
        counter += 50

def get_link(link_to_site,root):
    #headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
    #print(link_to_site)
    url = link_to_site
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    title = soup.find("span",{"class":"_35KyD6"})
    title = title.get_text()
    price = soup.find("div",{"class":"_1vC4OE _3qQ9m1"})
    price_string = price.get_text()
    price_float = convert(price.get_text())
        
    info = {}
    info['url'] = url
    info['title'] = title
    info['price_string'] = price_string
    info['price_float'] = price_float
 
    json_info = json.dumps(info)
 
    #json_labels = json.loads(json_info)
 
    for i in range(0,5):
        file = Path("info_{}".format(i))
        if file.exists():
            continue
        else:
            with open(file, 'w') as f:
                f.write("{}".format(json_info))
                break
     
    make_labels(root)
    
def create_window():
    t = Tk()
    make_labels(t)
    t.geometry('1000x600')
    t.config(bg="#090b10")

    frame_insert = Frame(t, height="15", width="80", bd=2,
                        bg="cyan", highlightbackground="#090b10")
    insert_new = Entry(frame_insert, width="80", font=("arial", 13), bg="#090b10",
                    fg="#2df0a0", bd="4", relief="flat", insertbackground="cyan")
    insert_new.grid(column=2)
    frame_insert.place(x=40, y=520)

    submit = Button(t, text="A D D", width="10", height="1",font=("Helvetica", 8, "bold"), fg="#090b10", bg="#2df0a0", activebackground="#1a1a1a",
                    activeforeground="#8fdcdf", pady="2", command=lambda:get_link(insert_new.get(),t))
    submit.config(highlightbackground="#8fdcdf",
                highlightcolor="#2df0a0", highlightthickness=10, relief="solid")
    submit.place(x=810, y=515)
    
    submit2 = Button(t, text="refresh", width="10", height="1",font=("Helvetica", 8, "bold"), fg="#090b10", bg="#2df0a0", activebackground="#1a1a1a",
                    activeforeground="#8fdcdf", pady="2", command=lambda:make_labels(t))
    submit2.config(highlightbackground="#8fdcdf",
                highlightcolor="#2df0a0", highlightthickness=10, relief="solid")
    submit2.place(x=810, y=450)


    prompt()
    t.mainloop()

create_window()
