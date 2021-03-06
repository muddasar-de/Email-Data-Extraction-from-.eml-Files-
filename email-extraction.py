# import pandas as pd
# df=pd.read_csv('./emails.txt', header=None, delimiter="\t")

# print(df)

#----------


# try:
#     print("File Found")
#     openedFile = open(fileName)
#     for line in openedFile:
#         line = line.strip()
#         to = re.findall('(To: +[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+)',line)
#         if(len(to)>0):
#             print(to)
# except:
#     print("File not found")

# try:
#     openedFile = open(fileName)
#     toEmail=""
#     pattern1 = re.compile(r'(To: +[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+)')
#     for line in openedFile:
#         line = line.strip()
#         # print(line)
#         matches = pattern1.finditer(line)
#         for match in matches:
#             toEmail= match.group(0).replace("To: ","")
#             print(toEmail)
# except:
#     print("File not opened") 


# from ast import pattern
# from operator import index
# import re
# from turtle import towards
# import pandas as pd
# from matplotlib.pyplot import get
# fileName = "./emails.txt"
# dic = {}
# def get_info ():
#     try:
#         openedFile = open(fileName)
#         for line in openedFile:
#             print("info")
#             line= line.strip()
#             get_To_Email(line)
#             get_From_Email(line)
#             get_body(line)
#         print(pd.Series(dic))
#         print(dic)
#     except:
#         print("File not found")

# def get_To_Email(line):
#     toE=""
#     patt = re.compile(r'(To: +[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+)')
#     matches = patt.finditer(line)
#     for match in matches:
#         toE = match.group(0).replace("To: ","")
#         dic["To"]=toE
#         return toE

# def get_From_Email(line):
#     fromE=""
#     patt1 = re.compile(r'(From: +[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]+)')
#     matches = patt1.finditer(line)
#     for match in matches:
#         fromE = match.group(0).replace("From: ","")
#         dic["From"]=fromE
#         return fromE
# def get_body(line):
#     patt2 = re.compile(r'(Body: +[0-9a-zA-Z]+ +)')
#     matches = patt2.finditer(line)
#     print("loop1")
#     for match in matches:
#         print("loop")
#         body = match.group(0).replace("Body: ","")
#         dic["Body"]=body
    
# # get_info()
# import pandas as pd
# # df=pd.read_csv("./output.csv")

# toEmails = []
# fromEmails = []
# openedFile = open("./emails.txt")
# print(openedFile)


# def get_info(openedFile):
#     for line in openedFile:
#         if line.startswith("To: "):
#             toEmail = line.replace("To: ","")
#             toEmails.append(toEmail) 
#         elif line.startswith("From: "):
#             print(line)
#             fromEmail= line.replace("From: ","").replace("\n","")
#             fromEmails.append(fromEmail) 
#     print(toEmails,fromEmails)

# get_info(openedFile)

# df['To']= toEmails
# df['From'] = fromEmails
# print(df)



# import email
# from re import sub

# from pyparsing import line_end

# # print(m)

# def get_subject(line):
    
#     if line.startswith("Subject: "):
#         subject = line.replace("Subject: ","")
#         print("Subject: "+ subject)
#         return (subject)

# def get_to_email(line):
    
#     if line.startswith("To: "):
#         toEmail = line.replace("To: ", "")
#         print("To: "+ toEmail)
#         return toEmail

# def get_from_email(line):
    
#     if line.startswith("From: ") :

#         toEmail = line.replace("From: ", "")
#         print("From: "+ toEmail)
#         return toEmail

# def get_body(file):
#     m = file.read()
#     mail = email.message_from_string(m)
#     print(mail)
    # if mail.is_multipart():
    #     for payload in mail.get_payload():
    #         # if payload.is_multipart(): ...
    #         print(payload.get_payload())
    #         return (payload.get_payload())
    # else:
    #     print(mail.get_payload()) 

# def get_info():
#     openFile = open("./mails.txt")
#     get_body(openFile)
    # for line in openFile :
    #     get_to_email(line)
    #     get_subject(line)
    #     get_from_email(line)
    

# get_info()

# openedFile = open("./mails.txt")
# mail = openedFile.read()
# print(mail)

# print(type(mail))


# ------------------------------------------------------------


####  Final Method ####
# Follow this 

from statistics import mode
import string 
from unicodedata import name
from numpy import busday_offset
import pandas as pd
from email import policy
from email.parser import BytesParser
import email
import textwrap
from bs4 import BeautifulSoup
import glob

# initilized the dictionary to store relavent data
dict = {
    "from": [],
    "to": [],
    "subject":[],
    "body":[],
    "date":[]
}
# Get email data using eml_parser and append them into dictionary to add them in csv. 

def get_email_info(fp):
    msg = BytesParser(policy=policy.default).parse(fp)
    print(type(msg))
    body = msg.get_body(preferencelist=('plain')).get_content()
    # print(type(body))
    soup = BeautifulSoup(body)
    # print(type(body))
    
    dict["from"].append(msg['from'])
    dict["to"].append(msg['to'])
    dict["subject"].append(msg['subject'])
    dict["body"].append(soup)
    dict["date"].append(msg['date'])
    

# def get_email_body(path):
#     openedFile = open(path)
#     msg = openedFile.read()
#     mail = email.message_from_string(msg)
#     # print(mail)
#     print(type(mail))
#     if mail.is_multipart():
#         for payload in mail.get_payload():
#             if payload.is_multipart():
#                 print("multipart")
#             else:
#                 dict["body"].append(payload.get_payload())
           
#     else:
#         dict["body"].append(mail.get_payload())


# Set CSV by passing the dictionary as a dataframe.
def set_csv(dic):
    df = pd.DataFrame(dic)
    df.to_csv("./output.csv",mode="a", index=False,  header=False)


# main Function:
path = "./mails/mail"
ext = ".eml"
list_of_files = glob.glob("./Emails/*.eml")
for file in list_of_files:
    with open(file, 'rb') as fp:
        get_email_info(fp)

set_csv(dict)
output = pd.read_csv("./output.csv")
print(output)
