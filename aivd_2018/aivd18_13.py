from crpt import Cryptography

people = {'Dries van Agt': 0, 'Hans Andreus': 0, 'Lodewijk Asscher': 1, 'Ron Blaauw': 2, 'Herman den Blijker': 2, 'Jonnie Boer': 2, 'Eduard Bomhoff': 0, 'Louis Paul Boon': 0, 'Wouter Bos': 0, 'Maartje Boudeling': 2, 'Lourens Jan Brinkhorst': 0, 'Remco Campert': 0, 'Hugo Claus': 0, 'Lodewijk van Deyssel': 0, 'Alphons Diepenbrock': 0, 'Frederik van Eeden': 0, 'Jan Elburg': 0, 'Frans Erens': 0, 'Gaspar Fagel': 4, 'Herman Gorter': 0, 'Thom de Graaf': 0, 'Jan Hanlo': 0, 'Anthonie van der Heim': 4, 'Anthonie Heinsius': 4, 'Cees Helder': 2, 'Sergio Herman': 2, 'Isaac van Hoornbeek': 4, 'Hugo de Jonge': 0, 'Annemarie Jorritsma': 0, 'Willem Kloos': 0, 'Wim Kok': 0, 'Rudolf de Korte': 0, 'Gerrit Kouwenaar': 0, 'Robert Kranenborg': 2, 'Erik van Loo': 2, 'Lucebert': 3, 'Roelof Nelissen': 0, 'Kajsa Ollongren': 1, 'Sybren Polet': 0, 'Johan Remkes': 0, 'Margo Reuten': 2, 'Mario Ridder': 2, 'Lucas Rive': 2, 'Paul Rodenko': 0, 'Andre Rouvoet': 0, 'Bert Schierbeek': 0, 'Angelique Schmeinck': 2, 'Carola Schouten': 1, 'Simon van Slingelandt': 4, 'Paul Snoek': 0, 'Cas Spijkers': 2, 'Helene Swarth': 0, 'Jan Terlouw': 0, 'Mario Uva': 2, 'Maxime Verhagen': 0, 'Albert Verwey': 0, 'Simon Vinkenoog': 0, 'Hans Wiegel': 0, 'Johan de Witt': 4, 'Johan Witteveen': 0, 'Hans van Wolde': 2, 'Gerrit Zalm': 0}
categories = {1: 'tweedekamerleden', 2: 'chefkoks', 3: 'schrijvers', 4: 'raadpensionarissen'}

# Niet: politici, kamerleden, tweedekamerleden, raadsleden, kabinetsleden, regeringsleden, regering, kabinet, ministerspresident

crypt = Cryptography()

for person, group in people.items():
  if group in categories:
    key = categories[group]
    crypt.set_decoded_text(person)
    print(person, crypt.encode_bifid(key))
