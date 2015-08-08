#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('sqlite:///catalog.db')
#engine = create_engine('sqlite:///catalog.db', assert_unicode=True)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categories = (
    {
        'id': 1,
        'name': u'Belgian-Style Ales'
    },
    {
        'id': 2,
        'name': u'Sour Beer'
    },
    {
        'id': 3,
        'name': u'Anglo-American Ales'
    },
    {
        'id': 4,
        'name': u'Stouts and Porters'
    },
    {
        'id': 5,
        'name': u'Wheat Beer'
    },
    {
        'id': 6,
        'name': u'Lager'
    },
    {
        'id': 7,
        'name': u'Abbey Dubbel',
        'description': ' '.join((
            'These are dark, malty, yeasty strong ales in the Trappist',
            'tradition, but produced (mainly) by secular brewers. Dubbels',
            'range between 6.5-8% abv, and have a dark brown, cloudy',
            'colour, and a palate mixing malt, a lush fruitiness, and',
            'yeast. They are typically bottle-conditioned.')),
        'parent_id': 1
    },
    {
        'id': 8,
        'name': u'Abbey Tripel',
        'description': 'Like other abbey ales, Tripels are strong, yeasty-malty beers. But they are also pale, and have a notable hop profile. Hop bitterness may be higher than a typical abbey ale, up to 45IBUs. But the finish is where the hops really shine, as tripels should finish fairly dry. Otherwise, maltiness is still essential to the style, and the assertive yeast note typical of all abbey ales will be more apparent in tripels, since they do not have the rich dark malts to distract the palate. Alcohol flavours feature more prominently in Tripels that in just about any other style.',
        'parent_id': 1
    },
    {
        'id': 9,
        'name': u'Abt/Quadrupel',
        'description': 'descr',
        'parent_id': 1
    },
    {
        'id': 10,
        'name': u'Belgian Ale',
        'description': 'descr',
        'parent_id': 1
    },
    {
        'id': 11,
        'name': u'Belgian Strong Ale',
        'parent_id': 1
    },
    {
        'id': 12,
        'name': u'Bière de Garde',
        'parent_id': 1
    },
    {
        'id': 13,
        'name': u'Saison',
        'parent_id': 1
    },
    {
        'id': 14,
        'name': u'Berliner Weisse',
        'parent_id': 2
    },
    {
        'id': 15,
        'name': u'Lambic Style - Faro',
        'parent_id': 2
    },
    {
        'id': 16,
        'name': u'Lambic Style - Fruit',
        'parent_id': 2
    },
    {
        'id': 17,
        'name': u'Lambic Style - Gueuze',
        'parent_id': 2
    },
    {
        'id': 18,
        'name': u'Lambic Style - Unblended',
        'parent_id': 2
    },
    {
        'id': 19,
        'name': u'Sour Red/Brown',
        'parent_id': 2
    },
    {
        'id': 20,
        'name': u'Sour/Wild Ale',
        'parent_id': 2
    },
    {
        'id': 21,
        'name': u'Altbier',
        'parent_id': 3
    },
    {
        'id': 22,
        'name': u'Amber Ale',
        'parent_id': 3
    },
    {
        'id': 23,
        'name': u'American Pale Ale',
        'parent_id': 3
    },
    {
        'id': 24,
        'name': u'American Strong Ale',
        'parent_id': 3
    },
    {
        'id': 25,
        'name': u'Barley Wine',
        'parent_id': 3
    },
    {
        'id': 26,
        'name': u'Bitter',
        'parent_id': 3
    },
    {
        'id': 27,
        'name': u'Brown Ale',
        'parent_id': 3
    },
    {
        'id': 28,
        'name': u'Cream Ale',
        'parent_id': 3
    },
    {
        'id': 29,
        'name': u'English Pale Ale',
        'parent_id': 3
    },
    {
        'id': 30,
        'name': u'English Strong Ale',
        'parent_id': 3
    },
    {
        'id': 31,
        'name': u'Golden Ale/Blond Ale',
        'parent_id': 3
    },
    {
        'id': 32,
        'name': u'Imperial IPA',
        'parent_id': 3
    },
    {
        'id': 33,
        'name': u'India Pale Ale (IPA)',
        'parent_id': 3
    },
    {
        'id': 34,
        'name': u'Irish Ale',
        'parent_id': 3
    },
    {
        'id': 35,
        'name': u'Kölsch',
        'parent_id': 3
    },
    {
        'id': 36,
        'name': u'Mild Ale',
        'parent_id': 3
    },
    {
        'id': 37,
        'name': u'Old Ale',
        'parent_id': 3
    },
    {
        'id': 38,
        'name': u'Premium Bitter/ESB',
        'parent_id': 3
    },
    {
        'id': 39,
        'name': u'Scotch Ale',
        'parent_id': 3
    },
    {
        'id': 40,
        'name': u'Scottish Ale',
        'parent_id': 3
    },
    {
        'id': 41,
        'name': u'Session IPA',
        'parent_id': 3
    },
    {
        'id': 42,
        'name': u'Baltic Porter',
        'parent_id': 4
    },
    {
        'id': 43,
        'name': u'Black IPA',
        'parent_id': 4
    },
    {
        'id': 44,
        'name': u'Dry Stout',
        'parent_id': 4
    },
    {
        'id': 45,
        'name': u'Foreign Stout',
        'parent_id': 4
    },
    {
        'id': 46,
        'name': u'Imperial Porter',
        'parent_id': 4
    },
    {
        'id': 47,
        'name': u'Imperial Stout',
        'parent_id': 4
    },
    {
        'id': 48,
        'name': u'Porter',
        'parent_id': 4
    },
    {
        'id': 49,
        'name': u'Stout',
        'parent_id': 4
    },
    {
        'id': 50,
        'name': u'Sweet Stout',
        'parent_id': 4
    },
    {
        'id': 51,
        'name': u'Dunkelweizen',
        'parent_id': 5
    },
    {
        'id': 52,
        'name': u'German Hefeweizen',
        'parent_id': 5
    },
    {
        'id': 53,
        'name': u'German Kristallweizen',
        'parent_id': 5
    },
    {
        'id': 54,
        'name': u'Grodziskie/Gose/Lichtenhainer',
        'parent_id': 5
    },
    {
        'id': 55,
        'name': u'Weizen Bock',
        'parent_id': 5
    },
    {
        'id': 56,
        'name': u'Wheat Ale',
        'parent_id': 5
    },
    {
        'id': 57,
        'name': u'Witbier',
        'parent_id': 5
    },
    {
        'id': 58,
        'name': u'Amber Lager/Vienna',
        'parent_id': 6
    },
    {
        'id': 59,
        'name': u'California Common',
        'parent_id': 6
    },
    {
        'id': 60,
        'name': u'Czech Pilsner (Světlý)',
        'parent_id': 6
    },
    {
        'id': 61,
        'name': u'Doppelbock',
        'parent_id': 6
    },
    {
        'id': 62,
        'name': u'Dortmunder/Helles',
        'parent_id': 6
    },
    {
        'id': 63,
        'name': u'Dunkel/Tmavý',
        'parent_id': 6
    },
    {
        'id': 64,
        'name': u'Dunkler Bock',
        'parent_id': 6
    },
    {
        'id': 65,
        'name': u'Eisbock',
        'parent_id': 6
    },
    {
        'id': 66,
        'name': u'Heller Bock',
        'parent_id': 6
    },
    {
        'id': 67,
        'name': u'Imperial Pils/Strong Pale Lager',
        'parent_id': 6
    },
    {
        'id': 68,
        'name': u'Malt Liquor',
        'parent_id': 6
    },
    {
        'id': 69,
        'name': u'Oktoberfest/Märzen',
        'parent_id': 6
    },
    {
        'id': 70,
        'name': u'Pale Lager',
        'parent_id': 6
    },
    {
        'id': 71,
        'name': u'Pilsener',
        'parent_id': 6
    },
    {
        'id': 72,
        'name': u'Polotmavý',
        'parent_id': 6
    },
    {
        'id': 73,
        'name': u'Premium Lager',
        'parent_id': 6
    },
    {
        'id': 74,
        'name': u'Schwarzbier',
        'parent_id': 6
    },
    {
        'id': 75,
        'name': u'Zwickel/Keller/Landbier',
        'parent_id': 6
    },
)

for c in categories:
    print 'adding category: %s' % c
    category = Category(id=c['id'], name=c['name'])
    if 'description' in c.keys():
        print '    description: %s' % c['description']
        category.description = c['description']
    if 'parent_id' in c.keys():
        parent = session.query(Category).filter_by(id=c['parent_id']).one()
        print '    parent: %s' % parent
        category.parent_id = parent.id

    session.add(category)

session.commit()

print 'added categories!'

items = (
    {
        'id': 1,
        'name': u'Westmalle Dubbel',
        'description': u'''A reddish brown trappist ale, malty and fruit, featuring a 3 week secondary fermentation. This ale has a full, pale yellow head. The bouquet is full of esters and fruitiness. Notes of ripe banana predominate. The taste is fruity and slightly bitter, with a long, dry finish.''',
        'category_id': 7
    },
    {
        'id': 2,
        'name': u'Tripel Karmeliet',
        'description': u'''First brewed 1996; claimed to be based on a recipe from 1679 which used wheat, oat and barley. Tripel Karmeliet is a very refined and complex golden-to-bronze brew with a fantastic creamy head. These characteristics derive not only from the grains used but also from restrained hopping with Styrians and the fruity nature (banana and vanilla) of the house yeast. Aroma has hints of vanilla mixed with citrus aromas. Tripel Karmeliet has not only the lightness and freshness of wheat, but also the creaminess of oats together with a spicy lemony almost quinine dryness.''',
        'category_id': 8
    },
    {
        'id': 3,
        'name': u'Westmalle Tripel',
        'description': u'''A strong, dry and spicy trappist ale. The product of a secondary fermentation lasting 5 weeks. This is a complex ale with a fruity aroma and a nice nuanced hop scent. It is soft and creamy in the mouth, with a bitter touch carried by the fruity aroma. An exceptional ale, with a great deal of finesse and elegance, and with a splendid long after taste.''',
        'category_id': 8
    },
    {
        'id': 4,
        'name': u'Orval',
        'description': u'''In contrast to all the others, the Orval Trappist brewery makes only one beer for the general public. It has an intensely aromatic and dry character. Between the first and second fermentations there is also an additional dry-hopping process. Through this the beer acquires its pronounced hoppy aroma and extra dry taste.  Bottled at 5.2% abv - can go up as high as 7.2%''',
        'category_id': 10
    },
    {
        'id': 5,
        'name': u'Westvleteren Blond',
        'description': u'''Westvleteren Blond is the basic beer for the monks’ own consumption, since 1999, when the former 6° dark ale (red cap) was finally discarded, after the 4° had already gone that path.''',
        'category_id': 10
    },
    {
        'id': 6,
        'name': u'Just a Beer',
        'description': 'Just a description for just a beer.',
        'category_id': 10
    }
)

for i in items:
    print 'adding item: %s' % i
    item = Item(id=i['id'], name=i['name'], description=i['description'], category_id=i['category_id'])

    session.add(item)

session.commit()
