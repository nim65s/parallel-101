# parallel-101

Ceci est un support de cours sur la parallélisation.


## Dépendances

- python
- numpy

## `task.py`

Ce programme affiche le temps nécessaire à la résolution d’un problème linéaire de taille 6000:

```
$ ./task.py
22.890031676000035
```

## `sub.py`

Ce programme lance 4 sous process de `./task.py` et affiche le résultat:

```
$ ./sub.py
30.569570345000102
30.684381426000073
30.7306182479997
30.97802341299939
total: 31.334230673000093
```

## `pool.py`

Ce programme lance 20 sous process dans un pool:

```
$ ./pool.py
100.63667821000035
47.19717385599961
111.27389448000031
91.91384233100052
[…]
total: 112.40665133400034
```

## `multi.py`

Ce programme lance 6 sous-process dans un pool, et affiche les résultats les plus rapides en premier:

```
$ ./multi.py
callback: 20.27123352700005
callback: 20.33557166599985
callback: 20.341369764000092
callback: 20.344183653000073
20.344183653000073
20.341369764000092
20.27123352700005
callback: 20.48627573800013
callback: 20.488327484000138
20.488327484000138
20.48627573800013
20.33557166599985
total: 20.79609276799988
```

## `async_web.py`

Télécharge de manière asynchrone toutes les ressources sur la page `https://www.upssitech.eu/`:

```
$ ./async_web.py
total: 5.230209101000128
```
