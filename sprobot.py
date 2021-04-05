#!/usr/bin/env python3
#  -*- coding: UTF-8 -*-
#
# sprobot.py
#   -- a fake robot reviews fake coffees
#
# Usage:
#
# sprobot.py [options]
#
# Options:
# --post     post the review to mastodon
#

__author__ = 'Greg Boyington (evilchili@mastodon.social)'
__copyright__ = 'Copyleft (k) YOLD 3180. All Fail Disfnordia'
__license__ = 'FNORD'
__version__ = '1.2.3'

from mastodon import Mastodon
import string
import random
import vocab
import sys
import re
import os

sprobot_re = re.compile('sprobot', re.IGNORECASE)


def cointoss(percent=50):
    """
    Return True percent percent of the time.
    """
    return random.choice(range(0, int(100 / percent))) == 1


def farm(key):
    """
    Return a randomly-generated name of a coffee farm, for a given region key.
    """

    # we use fictitous farmers' names by default
    name = ' '.join([vocab.first_name(key), vocab.surname(key)])

    # if we're creating a farm in Latin America, create a 'Finca SomeName'
    if key == 'latin':
        name = 'Finca ' + vocab.surname(key)

    # 20% of the time, create a SomeName Cooperative or Collective
    if cointoss(20):
        name = ' '.join([
            vocab.first_name(key),
            'Cooperative' if cointoss() else 'Collective'
        ]).strip()

    # If it's not a collective, it's either a Farm or an Estate (unless it's a
    # Finca).
    else:
        name = ' '.join(
            [name, ('Estate' if cointoss() else 'Farm') if key != 'latin' else ''])

    return ' '.join(name.split())


def rating():
    """
    Return a coffee rating, out of 100.
    """

    # 10% of the time, score the coffee between 70 and 80, since 90% of the time
    # every actual coffee review scores between 80 and 100.
    if cointoss(10):
        a = 70
        b = 80
    else:
        a = 81
        b = 99
    return "{}pts".format(random.choice(range(a, b)))


def compose():
    """
    Compose a coffee review in 140 characters or less.
    """

    review = ''

    # start with a random region
    key = random.choice(vocab.REGION.keys())

    # build a review out of multiple phrase templates, a coffee variety and a score, and keep doing
    # it until we have one that doesn't go over 140 characters.
    while review == '':

        # if we're at 80 chars or less, add another template.
        while len(review) < 80:
            t = vocab.template()

            # manually parse the string template and do the substitions via the lambdas in the
            # vocab.word dict. This allows for multiple substitutions of each {modifier}, {taste},
            # and so on.
            phrase = ''.join(
                [(x[0] + (vocab.word[x[1]]() if x[1] else ''))
                 for x in string.Formatter().parse(t)]
            )

            # fix up the capitalization and punctuation of the review, allowing for some
            # random sentence breaks.
            if review == '':
                review = phrase.capitalize()
            elif cointoss():
                review = review + (', ' if cointoss() else '; ') + phrase
            else:
                review = review + \
                    ('! ' if cointoss(10) else '. ') + phrase.capitalize()

        # choose a random coffee variety
        variety = vocab.variety()

        # 10% of the time, add a modifier
        if cointoss(10):
            variety = variety + ' ' + vocab.variety_modifier()

        # construct the review out of the region, farm, variety, and joined
        # phrases
        review = "{} {}, {}: {}".format(
            vocab.region(key), farm(key), variety, review)

        # if we have enough room, occasionally add an exclamation.
        if len(review) < 124 and cointoss():
            review = "{review}. {extra}{punc}".format(
                review=review,
                extra=vocab.extra(),
                punc=vocab.punctuation()
            )

        # replace the final comma in the review with 'and'.
        if cointoss(30) and review.count(',') > 2:
            comma = review.rfind(',')
            if comma != -1:
                review = review[:comma] + ' and' + review[comma + 1:]

        # make 'a' 'an' when preceeding a word starting with a vowel
        for l in 'aeiouAEIOU':
            review = review.replace(' a ' + l, ' an ' + l)
            review = review.replace(' A ' + l, ' An ' + l)

        # if the review doen't end in punctiation, append a period.
        if review[-1] not in vocab.PUNCTUATION:
            review = review + '.'

        # finally, add the rating.
        review = review + ' ' + rating()

        # always camelcase SproBot
        review = sprobot_re.sub('SproBot', review)

        # if the whole review is too long, wipe it out and try again.
        if len(review) >= 140:
            review = ''

    return review


if __name__ == '__main__':

    # compose a review
    review = compose()
    print(review)

    # optionally, tweet the review.
    if '--post' in sys.argv:
        client = Mastodon(
            access_token=os.environ.get('MASTODON_TOKEN'),
            api_base='https://botsin.space/'
        )
        client.toot(review)
