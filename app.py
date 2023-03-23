import requests
import json

firstname = input("Firstname ? : ")
imgUrl = input("imgURL ? : ")
compagnyName = input("compagnyName ? : ")
poste = input("poste ? : ")
logo = input("logo ? : ")
ecole = input("ecole ? : ")
domaine = input("domaine ? : ")
skills = input("skills ? : ")
nbrelation = input("nbrelation ? : ")

webhook_url = 'Your_Zapier URL'

data = [{
	
	"firstName": firstname,
	"imgUrl": imgUrl,
	"companyName": compagnyName,
	"poste": poste,
	"logo": logo,
	"ecole": ecole,
	"domaine": domaine,
	"skills": skills,
	"nbrelation": nbrelation
}]


r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})