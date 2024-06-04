# Function Creator

Il **Function Creator** è una classe progettata per generare funzioni matematiche che combinano polinomi e funzioni trascendenti. Le funzioni trascendenti sono quelle funzioni non algebriche che contengono espressioni logaritmiche, esponenziali o trigonometriche. Questo strumento consente di creare e manipolare funzioni complesse in modo dinamico, includendo polinomi di ordine variabile e una varietà di funzioni trascendenti. Di seguito è riportata una descrizione dettagliata delle caratteristiche e funzionalità della classe:

## Attributi:
- **__x:** Simbolo variabile utilizzato per definire le funzioni.
- **PolyOrder:** Ordine del polinomio, generato casualmente tra 1 e 5 al momento dell'inizializzazione.
- **base:** Coefficiente di base per i termini del polinomio, generato casualmente tra -5 e 5 al momento dell'inizializzazione.
- **FunList:** Lista di funzioni trascendenti predefinite che include coseno, seno, esponenziale, logaritmo e una funzione esponenziale modificata.
- **fx:** Funzione utente inizializzata a 0.
- **__min_poly e __max_poly:** Limiti minimo e massimo per l'ordine del polinomio.
- **__min_base e __max_base:** Limiti minimo e massimo per il coefficiente di base.
- **__derivate_order:** Ordine della derivata attuale, inizializzato a 1.

## Metodi:
- **set_poly_order(min_, max_):** Imposta i limiti minimo e massimo per l'ordine del polinomio e genera un ordine casuale tra questi limiti.
- **get_poly_order():** Restituisce una tupla contenente i limiti minimo e massimo per l'ordine del polinomio.
- **set_base_range(min_base, max_base):** Imposta i limiti minimo e massimo per il coefficiente di base.
- **set_base():** Genera un coefficiente di base casuale tra i limiti specificati.
- **add_function_to_list(new_function):** Aggiunge una nuova funzione alla lista di funzioni trascendenti.
- **make_numerator():** Crea il numeratore della funzione utente combinando termini polinomiali e funzioni trascendenti selezionate casualmente.
- **make_denominator():** Seleziona una funzione trascendente casuale dalla lista e la utilizza come denominatore della funzione utente.
- **next_derivate():** Incrementa l'ordine della derivata e calcola la derivata successiva della funzione utente.
- **plot_function():** Grafica la funzione utente attuale.
- **reset_function():** Reimposta la funzione utente a 0.

## Example of Usage:

### First Example:
```python
fc = FunctionCreator()
fc.set_poly_order(1, 5)
fc.set_base_range(-5, 6)
fc.set_base()

fc.make_numerator()
fc.fx     # −sin(𝑥)+cos(𝑥)

fc.make_denominator()
fc.fx    # −sin(𝑥)+cos(𝑥)/1+𝑒−𝑥

fc.plot_function()
```

### Second Example:
```python
fc = FunctionCreator()
fc.set_poly_order(1, 2)
fc.set_base_range(-2, 2)
fc.set_base()

fc.make_numerator()
fc.fx      # 𝑒𝑥−1−𝑒−𝑥

fc.make_denominator()
fc.fx     # 𝑒𝑥−1−𝑒−𝑥 / (1+𝑒−𝑥)

fc.next_derivate()
fc.fx   # too long to be posted

```

Questa classe offre un potente strumento per creare e analizzare funzioni complesse, combinando elementi polinomiali e trascendenti, e può essere utile per scopi didattici, di ricerca o di esplorazione matematica.
