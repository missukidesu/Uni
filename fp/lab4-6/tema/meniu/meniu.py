def meniu_principal():
  print("                         ==Meniu==")
  print("1. Inseratii cheltuieli")
  print("2. Stergeri")
  print("3. Cautari")
  print("4. Iesire")

def meniu_inserare():
  print("                 ==Meniu Inserare==")
  print("1. Inserarea unei noi cheltuieli")
  print("2. Actualizarea unei cheltuieli")
  print("3. Revenire la meniu principal")

def meniu_stergeri():
  print("                 ==Meniu Stergeri==")
  print("1. Stergerea cheltuielilor dupa zii")
  print("2. Stergerea cheltuielilor intr un interval de 2 zile")
  print("3. Stergerea cheltuielilor dupa tip")
  print("4. Revenire la meniu principal")

def meniu_cautari():
  print("                ==Meniu Cautari==")
  print("1. Afiseaza cheltuielile mai mari decat o suma data")
  print("2. Afiseaza cheltuielile mai mici decat o suma si inainte de o zii data")
  print("3. Afiseaza cheltuielile dupa un tip")
  print("4. Revenire la meniu principal")

actiuni_meniu = {
  "1":meniu_inserare,
  "2":meniu_stergeri,
  "3":meniu_cautari,
  "4":lambda:exit()
}

def run_meniul_principal():
  meniu_principal()
  inp = input("mod: ")
  actiune = actiuni_meniu.get(inp)
  if not actiune:
    print("Optiune nevalida")
  else:
    actiune()

