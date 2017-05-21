# MIPS

http://www-inst.eecs.berkeley.edu/~cs61c/resources/MIPS_help.html

## Kako testirati

Potrebno je runati hazardtest.py putem komande:
```
    python hazardtest.py
```

## Kako runati

Moguce je loadati podatkovnu memoriju koristeci file ram.txt (primjer takvog file-a vec postoji, a defaultna velicina RAM-a je 200 zamisljenih jedinica).
Ako neka adresa nije specificirana, pretpostavlja se da ona ima vrijednost 0, pri cemu prvi broj u redu predstavlja adresu, a drugi vrijednost koju ta adresa treba da posjeduje. Istom logikom je moguce ucitati vrijednost registara preko file-a reg.txt. Instrukcije je potrebno upisati u file instr.txt (primjer vec postoji u file-u instr.txt). Nakon specificiranja pocenog stanja registara, rama i instrukcija, potrebno je runati main.py file komandom:

```
    python main.py
```

