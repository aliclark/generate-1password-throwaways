# Generate 1password throwaways

Generates a CSV export containing rows of `Title`, `Username`, `Password`, `Notes`,
which can be imported into a 1Password vault ready to use for a throwaway account.

The logins rows also include a `Notes` field containing suggested values for: *full name*, *address*, *phone*, *birth date*, *occupation*, and *company*.

## Prerequisites

1. `data/identities` folder should contain 1 or more fake identities as created by https://www.fakenamegenerator.com/ eg. using https://fakeid.now.sh/

2. The command `ppg` should return a fresh password eg. by cloning https://github.com/aliclark/pragmatic-password-generator and creating a symlink `ppg` to `ppg.py` in the executable path

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

The `birth-year` default is `1980`, `birth-year-variance` default is `2`, and `email-service` default is `gmail.com`.
