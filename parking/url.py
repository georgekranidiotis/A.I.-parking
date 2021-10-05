import json
import urllib.request


location="shop"

def send_plate(plate):
    send_url = urllib.request.urlopen("http://ameaparking.000webhostapp.com/par.php?plate="+plate+"&location="+location)
    data=json.load(send_url)
    cert=data['certified']
    return plate,cert
