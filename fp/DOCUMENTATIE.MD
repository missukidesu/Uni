# 🧾 Aplicație Gestionare Cheltuieli Familiale

## 📘 Descriere
Aplicația gestionează cheltuielile de familie efectuate într-o lună.  
Pentru fiecare cheltuială se rețin următoarele informații:
- **Ziua** (1–31)
- **Suma** cheltuită
- **Tipul cheltuielii**: mâncare, întreținere, îmbrăcăminte, telefon, altele

Aplicația permite adăugarea, modificarea, ștergerea, căutarea, raportarea și filtrarea cheltuielilor, precum și funcția **Undo** pentru revenirea la starea anterioară.

---

## 🧠 Cerințe
Aplicația trebuie să permită utilizatorului să:
1. **Adauge** sau **actualizeze** o cheltuială  
2. **Șteargă** cheltuieli (după zi, interval de zile sau tip)  
3. **Caută** cheltuieli (după sumă, zi, tip)  
4. **Genereze rapoarte** (sume totale, ziua cu cheltuiala maximă, sortări)  
5. **Filtreze** cheltuieli (după tip sau sumă)  
6. **Refacă ultima operație (Undo)** asupra listei

---

## ⚙️ Funcționalități

| Cod | Funcționalitate | Descriere |
|-----|-----------------|------------|
| **F1**  | Adaugă / Actualizează cheltuială | Permite introducerea sau modificarea unei cheltuieli existente |
| **F2**  | Șterge după zi | Elimină toate cheltuielile dintr-o anumită zi |
| **F3**  | Șterge după interval | Elimină cheltuielile dintr-un interval de zile |
| **F4**  | Șterge după tip | Elimină toate cheltuielile de un anumit tip |
| **F5**  | Căutare > sumă | Afișează cheltuielile mai mari decât o sumă dată |
| **F6**  | Căutare < sumă și înainte de zi | Afișează cheltuielile mai mici decât o sumă și efectuate înainte de o zi |
| **F7**  | Căutare după tip | Afișează cheltuielile unui anumit tip |
| **F8**  | Raport sumă totală după tip | Calculează suma totală pentru un tip de cheltuială |
| **F9**  | Zi cu suma maximă | Afișează ziua în care s-a cheltuit cel mai mult |
| **F10** | Cheltuieli cu sumă fixă | Afișează cheltuielile care au o sumă dată |
| **F11** | Sortare după tip | Afișează cheltuielile ordonate după tip |
| **F12** | Filtrare după tip | Elimină toate cheltuielile de un anumit tip |
| **F13** | Filtrare după sumă | Elimină cheltuielile mai mici decât o sumă dată |
| **F14** | Undo | Reface ultima modificare efectuată asupra listei |

---

## 🕒 Plan de dezvoltare (3 săptămâni)

### 🔹 **Săptămâna 1 – Funcționalități de bază**
- Definirea structurii de date pentru cheltuieli (zi, sumă, tip)  
- Implementarea funcționalității **F1 – Adaugă / Actualizează cheltuială**  
- Crearea unei interfețe text simple pentru introducerea datelor  
- Testarea adăugării și actualizării cheltuielilor  

**🎯 Rezultat:** aplicație funcțională pentru adăugarea și afișarea cheltuielilor.

---

### 🔹 **Săptămâna 2 – Ștergere și căutări**
- Implementarea funcțiilor de **ștergere**:  
  - F2 – Șterge după zi  
  - F3 – Șterge după interval  
  - F4 – Șterge după tip  
- Implementarea funcțiilor de **căutare**:  
  - F5 – Cheltuieli mai mari decât o sumă  
  - F6 – Cheltuieli mai mici decât o sumă și efectuate înainte de o zi  
  - F7 – Cheltuieli de un anumit tip  
- Integrarea acestor funcționalități în interfața utilizator  
- Testarea completă a operațiilor de ștergere și căutare  

**🎯 Rezultat:** aplicație care permite gestionarea completă a listei de cheltuieli.

---

### 🔹 **Săptămâna 3 – Rapoarte, filtrări și Undo**
- Implementarea funcțiilor de **rapoarte**:  
  - F8 – Suma totală pentru un tip de cheltuială  
  - F9 – Ziua cu suma maximă  
  - F10 – Cheltuieli cu o anumită sumă  
  - F11 – Sortare după tip  
- Implementarea funcțiilor de **filtrare**:  
  - F12 – Elimină cheltuielile de un anumit tip  
  - F13 – Elimină cheltuielile mai mici decât o sumă dată  
- Implementarea funcției **F14 – Undo** (refacerea ultimei modificări)  
- Integrarea completă și testarea finală  

**🎯 Rezultat:** aplicație completă, stabilă și ușor de utilizat.

---

## 📊 Plan vizual al funcționalităților

| Funcționalitate | Săptămâna de implementare |
|-----------------|----------------------------|
| F1 – Adaugă/Actualizează | ✅ Săptămâna 1 |
| F2 – F4 (Ștergere) | ✅ Săptămâna 2 |
| F5 – F7 (Căutări) | ✅ Săptămâna 2 |
| F8 – F11 (Rapoarte) | ✅ Săptămâna 3 |
| F12 – F13 (Filtrări) | ✅ Săptămâna 3 |
| F14 – Undo | ✅ Săptămâna 3 |

---

## 🧩 Scenariu de rulare
## Scenariu pentru funcționalitatea aplicației de gestionare a cheltuielilor

| Utilizator | Program | Descriere |
|-------------|----------|-----------|
| a | `python meniu.py` | Pornește aplicația și inițializează lista de cheltuieli goală |
| b | `insereaza_cheltuiala_noua 5 150 mancare` | Adaugă o cheltuială de 150 lei pentru mâncare în ziua 5 |
| c | `insereaza_cheltuiala_noua 10 200 intretinere` | Adaugă o cheltuială de 200 lei pentru întreținere în ziua 10 |
| d | `insereaza_cheltuiala_noua 10 80 telefon` | Adaugă o cheltuială de 80 lei pentru telefon în ziua 10 |
| e | `insereaza_cheltuiala_noua 15 300 imbracaminte` | Adaugă o cheltuială de 300 lei pentru îmbrăcăminte în ziua 15 |
| f | `afiseaza_cheltuielile_mai_mari_decat_o_suma 100` | Afișează toate cheltuielile mai mari de 100 lei |
| g | `sterge_o_cheltuiala_dintro_zi 10` | Șterge toate cheltuielile efectuate în ziua 10 |
| h | `undo` | Reface lista de cheltuieli anterioară ștergerii |
| i | `afiseaza_suma_totala_a_cheltuielilor_cu_tipul_dat mancare` | Calculează și afișează suma totală pentru tipul *mâncare* |
| j | `afiseaza_ziua_cu_suma_maxima` | Afișează ziua cu cheltuiala totală maximă |
| k | `filtrarea_cheltuielilor_cu_suma_mai_mica_decat_o_suma 100` | Elimină cheltuielile cu sumă mai mică de 100 lei |
| l | `sorteaza_lista_dupa_tip` | Afișează cheltuielile ordonate după tip |
| m | `exit` | Închide aplicația |



