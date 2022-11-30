# Secret Santa - TIPE

The purpose of this project is simple, to automate the famous tradition of the secret Santa according to the following rules:

- Data extracted from a .csv file
- Sending emails
- Data protection
- Exception management (no draws within the same group)
- Possibility to store the draw
- Zero-knowledge proof

The principle and a demonstration can be found here : [research paper](/research%20paper/research_paper.pdf) | [presentation](presentation/presentation.pdf)

#### Contributor(s) : [@StanislasMzx](https://github.com/StanislasMzx) (Stanislas MEZUREUX) [@alicelaboss](https://github.com/alicelaboss) (Alice ESPINOSA)

## Licence

[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

This code source is published under GPLv3 licence.

    Copyright (C) 2021  Stanislas MEZUREUX - Alice ESPINOSA

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Usage

### 1 - Clone the project

Clone this project on your laptop by executing the following command in your terminal :

```
git clone https://github.com/StanislasMzx/Secret-Santa-TIPE
```

### 2 - Configure email

Modify the following lines in <code>SecretSanta.py</code>

```python
AMOUNT = 10
NAME = 'MPSI1 227/228'
DATE = '03/01/2022'
GMAIL_ADDRESS = 'secret.santa.tipe@gmail.com'
GMAIL_PASSWORD = '***secret(santa)'
```

### 3 - Check the data input format

**The list of participants must be a [csv file](https://fr.wikipedia.org/wiki/Comma-separated_values) stored in <code>/draw_files</code> and must have the following format :**

```csv
Prenom,NOM,Team,email
Stanislas,MEZUREUX,BlueTeam,stanmzx@gmail.com
Alice,ESPINOSA,RedTeam,stanmzx@gmail.com
```

> Remark : if no conditions are set, give each participant the same team name (e.g. noTeam).
>
> Remark : do not delete the first line, it is part of the csv format.

### 4 - Make a draw

```python
from SecretSanta import *

input_file = 'draw_files/data.csv' # path of data

Secret_Santa(input_file) # will export the ciphered print to /draw_files
```

#### ⚠️ WARNING : Remember to store the public key and the private key.

They are required for zero-knowledge proof and resend of draw.

### 5 - Zero-knowledge proof

**Draw path must be /draw_file/secret_santa_draw.py**

```python
from SecretSanta import *

zero_knowledge_proof(secret_key, public_key) # keys returned by step 4
```

### 6 - Resend the draw

**Draw path must be /draw_file/secret_santa_draw.py**

```python
from SecretSanta import *

resend(secret_key, public_key, draw_file) # keys returned by step 4
```

## Contact

Stanislas MEZUREUX - [stanmzx@gmail.com](mailto:stanmzx@gmail.com)

Alice ESPINOSA - [alice.espinosa29@gmail.com](mailto:alice.espinosa29@gmail.com)
