import json

charName = input("Enter character name:")
print("Username is: " + charName)

charRace = input("Enter race:")
print("Character's race is: " + charRace)

charClass = input("Enter class:")
print("Character class is " + charClass)

print("Your character is: " + charName + " the " + charRace + " " + charClass + "!")

charStrength = input("Enter character strength level:")
charConstitution = input("Enter character constitution level:")
charIntelligence = input("Enter character intelligence level:")
charAgility = input("Enter character agility level:")
charStats = {
	"strength": charStrength,
	"constitution": charConstitution,
	"intelligence": charIntelligence,
	"agility": charAgility,
	
}
y = json.dumps(charStats, indent=4)

print(y)