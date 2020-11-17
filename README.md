# Generate 1password throwaways

Generates a CSV export containing rows of `Title`, `Username`, `Password`, `Notes`,
which can be imported into a 1Password vault ready to use for a throwaway account.

The `Notes` field contains suggestions for *full name*, *address*, *phone*, *birth date*, *occupation*, and *company*.

```sh
$ ./generate-1password-throwaways.py
"protectivebutton","protectivebutton@gmail.com","Nrhjxbmxpwjuev8,","Hallie L Gracia

2142 Columbia Mine Road
Monongah
WV 26554

304-534-7284

11 / 04 / 1981

Production cost estimator
Lawn N Order Garden Care
"
```

## Prerequisites

1. The `data/identities` folder should contain any number of fake identities in `.json` files,
2. as created by https://www.fakenamegenerator.com/ eg. using https://fakeid.now.sh/

3. The `ppg` command should return a fresh password, eg. by cloning https://github.com/aliclark/pragmatic-password-generator and creating a symlink `ppg` to `ppg.py` in the executable path

## Usage

```
usage: generate-1password-throwaways.py [-h] [--birth-year year] [--birth-year-variance years] [--email-service domain] [--uk]
 
Generate throwaway logins for 1password.

optional arguments:
  -h, --help            show this help message and exit
  --birth-year year     birth year, which will be rounded down to the nearest 5 years
  --birth-year-variance years
                        number of random years to add or remove from birth year
  --email-service domain
                        which domain to use for generated email addresses in the Notes field
  --uk                  use United Kingdom formatting, eg. for dates
```

* The `birth-year` default is `1980`
* The `birth-year-variance` default is `2`
* The `email-service` default is `gmail.com`.
