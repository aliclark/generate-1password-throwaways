#!/usr/bin/env python

from argparse import ArgumentParser
from math import floor

import csv
from datetime import datetime, date
from calendar import isleap
from random import randint
import random

from sys import stdout
from glob import glob
import json
from subprocess import check_output


parser = ArgumentParser(description='Generate throwaway logins for 1password.')
parser.add_argument('--birth-year', choices=range(1900, 2005), type=int, default=1980, metavar='year',
                    help='birth year, which will be rounded down to the nearest 5 years')
parser.add_argument('--birth-year-variance', type=int, default=2, metavar='years',
                    help='number of random years to add or remove from birth year')
parser.add_argument('--email-service', default='gmail.com', metavar='domain',
                    help='which domain to use for generated email addresses in the Notes field')
parser.add_argument('--uk', action='store_true',
                    help='use United Kingdom formatting, eg. for dates')

args = parser.parse_args()

args.birth_year = floor(args.birth_year / 5) * 5


# https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/livebirths/articles/howpopularisyourbirthday/2015-12-18

with open('data/birthdays.csv', newline='') as birthdaysFile:
    reader = csv.DictReader(birthdaysFile)
    birthdays, birthdaysWeights = zip(*[(datetime.strptime('{0} 2000'.format(row['date']), '%d-%b %Y').date(), float(row['average']))
                                        for row in reader])


def generateBirthdate():
    randomYear = randint(args.birth_year - args.birth_year_variance, args.birth_year + args.birth_year_variance)
    [randomDate] = random.choices(birthdays, birthdaysWeights)

    if not isleap(randomYear) and randomDate.month == 2 and randomDate.day == 29:
        return generateBirthdate()

    return date(randomYear, randomDate.month, randomDate.day)


# https://www.randomlists.com/random-adjectives?dup=false&qty=9999
with open('data/adjectives.txt') as adjectivesFile:
    adjectives = adjectivesFile.read().splitlines()

# https://www.randomlists.com/nouns?dup=false&qty=9999
with open('data/nouns.txt') as nounsFile:
    nouns = nounsFile.read().splitlines()


writer = csv.writer(stdout, quoting=csv.QUOTE_ALL)

for fileName in glob('data/identities/*.json'):

    with open(fileName) as jsonfile:
        response = json.load(jsonfile)
        data = response['data']
        details = data['Details']

        birthDate = generateBirthdate()

        username = random.choice(adjectives) + random.choice(nouns)
        phone = details['Phone'].replace(' ', '')

        writer.writerow([username,
                        '{0}@{1}'.format(username, args.email_service),
                        check_output(['ppg']).decode('utf-8').strip(),
                        f"""{data['Name'].split(' ')[0]} {details['MothersMaidenName'][0]} {data['Name'].split(' ')[-1]}

{data['Address'].split(', ')[0]}
{data['Address'].split(', ')[1].title()}
{data['Address'].split(', ')[2]}

{phone}

{birthDate.strftime('%d / %m / %Y') if args.uk else birthDate.isoformat()}

{details['Occupation']}
{details['Company']}
"""])
