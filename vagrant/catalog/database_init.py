#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('postgresql+psycopg2://vagrant:@/beercatalog')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

users = (
    {
        'id': 1,
        'username': u'Sil Westerveld',
        'family_name': u'Westerveld',
        'given_name': u'Sil',
        'email': u'g@silwesterveld.com',
        'picture': u'https://lh6.googleusercontent.com/-RR3rG2Ma6Bk/AAAAAAAAAAI/AAAAAAAAAEI/Pjmz2qSHytM/photo.jpg'
    },
)

for u in users:
    print 'adding user: %s' % u
    user = User(id=u['id'],
                username=u['username'],
                family_name=u['family_name'],
                given_name=u['given_name'],
                email=u['email'],
                picture=u['picture'])
    session.add(user)

session.commit()

print 'added users!'

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
        'description': (
            u'''These are dark, malty, yeasty strong ales in the Trappist '''
            u'''tradition, but produced (mainly) by secular brewers. Dubbels '''
            u'''range between 6.5-8% abv, and have a dark brown, cloudy '''
            u'''colour, and a palate mixing malt, a lush fruitiness, and '''
            u'''yeast. They are typically bottle-conditioned.'''),
        'parent_id': 1
    },
    {
        'id': 8,
        'name': u'Abbey Tripel',
        'description': (
            u'''Like other abbey ales, Tripels are strong, yeasty-malty '''
            u'''beers. But they are also pale, and have a notable hop '''
            u'''profile. Hop bitterness may be higher than a typical abbey '''
            u'''ale, up to 45IBUs. But the finish is where the hops really '''
            u'''shine, as tripels should finish fairly dry. Otherwise, '''
            u'''maltiness is still essential to the style, and the assertive '''
            u'''yeast note typical of all abbey ales will be more apparent '''
            u'''in tripels, since they do not have the rich dark malts to '''
            u'''distract the palate. Alcohol flavours feature more '''
            u'''prominently in Tripels that in just about any other style.'''),
        'parent_id': 1
    },
    {
        'id': 9,
        'name': u'Abt/Quadrupel',
        'description': (
            u'''Belgian-style ales seldom fit neatly into classic beer '''
            u'''styles, but this category represents those ales under '''
            u'''approximately 7% abv that do not fit other categories. '''
            u'''Colour ranges from golden to deep amber, with the occasional '''
            u'''example coming in darker. Body tends to be light to medium, '''
            u'''with a wide range of hop and malt levels. Yeastiness and '''
            u'''acidity may also be present.'''),
        'parent_id': 1
    },
    {
        'id': 10,
        'name': u'Belgian Ale',
        'description': (
            u'''Belgian-style ales seldom fit neatly into classic beer '''
            u'''styles, but this category represents those ales under '''
            u'''approximately 7% abv that do not fit other categories. '''
            u'''Colour ranges from golden to deep amber, with the occasional '''
            u'''example coming in darker. Body tends to be light to medium, '''
            u'''with a wide range of hop and malt levels. Yeastiness and '''
            u'''acidity may also be present.'''),
        'parent_id': 1
    },
    {
        'id': 11,
        'name': u'Belgian Strong Ale',
        'description': (
            u'''Belgian Strong Ales can vary from pale to dark brown in '''
            u'''color, darker ales may be colored with dark candy sugar. '''
            u'''Hop flavor can range from low to high, while hop aroma is '''
            u'''low. The beers are medium to full-bodied and have a high '''
            u'''alcoholic character. Types of beers included here include '''
            u'''tripels, dubbels and ultra-strong abbey ales.'''),
        'parent_id': 1
    },
    {
        'id': 12,
        'name': u'Bière de Garde',
        'description': (
            u'''A traditional classification for the farmhouse ales of '''
            u'''France and their sometimes-untraditional new-world '''
            u'''counterparts. Bière de Garde is today generally a warm '''
            u'''fermented strong pale ale - sometimes blonde, sometimes '''
            u'''amber, and has much in common with Belgium ales. Medium '''
            u'''bodied with hints of caramel or toffee. Cellared smell and '''
            u'''flavor are characteristics. The name means "beer for '''
            u'''keeping".'''),
        'parent_id': 1
    },
    {
        'id': 13,
        'name': u'Saison',
        'description': (
            u'''Fruity esters dominate the aroma. Clarity is good with a '''
            u'''large foamy head on top. The addition of several spices and '''
            u'''herbs create a complex fruity or citrusy flavor. Light to '''
            u'''medium bodied with very high carbonation. Alcohol level is '''
            u'''medium to high.'''),
        'parent_id': 1
    },
    {
        'id': 14,
        'name': u'Berliner Weisse',
        'description': (
            u'''Very wheaty, very sour style of Berlin. Berliner weissebier '''
            u'''has a barely perceptible hop content, low alcohol, and a '''
            u'''sharp character. Often these are laced with syrups to cut '''
            u'''the intense acidity, but purists will want to take them '''
            u'''neat to enjoy the multi-faceted complexity and '''
            u'''thirst-quenching character.'''),
        'parent_id': 2
    },
    {
        'id': 15,
        'name': u'Lambic Style - Faro',
        'description': (
            u'''Faro is a lambic blend with the addition of sugar. These '''
            u'''are well-carbonated, and are sweeter and more refreshing '''
            u'''than gueuze. The flavour is often straightforward and '''
            u'''sugary, with lighter barnyard and funk notes than other '''
            u'''lambic styles. The odd variant contains other spices like '''
            u'''orange peel as flavouring.'''),
        'parent_id': 2
    },
    {
        'id': 16,
        'name': u'Lambic Style - Fruit',
        'description': (
            u'''Lambics are wheat beers made with stale hops and fermented '''
            u'''with wild yeasts and other microorganisms traditionally '''
            u'''only on the Senne Valley in and around Brussels. The most '''
            u'''traditional of the fruit lambics are kriek (cherry) and '''
            u'''framboise (raspberry). In modern times peaches (peche) '''
            u'''blackcurrants (cassis) grapes as well as more exotic fruits '''
            u'''are used. Traditional lambics are commonly denoted by the '''
            u'''term "oud" which is a reference to "old-style" and these '''
            u'''are the most sour. More commonly though lambics are '''
            u'''sweetened to cut the intense acidity. Serve with sharp '''
            u'''cheeses or pickled dishes or use in the preparation of '''
            u'''mussels.'''),
        'parent_id': 2
    },
    {
        'id': 17,
        'name': u'Lambic Style - Gueuze',
        'description': (
            u'''Gueuze is a blend of young and old lambic. The yeasts are '''
            u'''rejuvenated and carbonation ensues. The old lambic is more '''
            u'''refined in character and helps take some of the edge off of '''
            u'''the young lambic. The hops used are old, and act only as a '''
            u'''preservative, so hop character is not a part of the style. '''
            u'''The wild yeasts not only ferment and sour the beer, but '''
            u'''they bring the funky, unpredictable flavours that '''
            u'''characterize all lambic beers. A quality gueuze will be '''
            u'''blended to eliminate some of the less desirable flavours. '''
            u'''Above all else, a gueuze should be sour and very complex. '''
            u'''The best examples are the most complex beers in the world, '''
            u'''and put most champagnes to shame as well. The finish should '''
            u'''be bone dry.'''),
        'parent_id': 2
    },
    {
        'id': 18,
        'name': u'Lambic Style - Unblended',
        'description': (
            u'''Unblended lambic is the purest form of lambic. This rare '''
            u'''specialty is typically only found in the lambicmakers’ home '''
            u'''region, although one bottled example – Cantillon 1900 '''
            u'''Bruocsella Grand Cru – is produced. Unblended lambics will '''
            u'''vary in character from barrel to barrel, can be found in a '''
            u'''variety of ages, and may have been aged with fruit in the '''
            u'''cask. They tend to be still, with flavours whose edge has '''
            u'''not been taken off by blending.'''),
        'parent_id': 2
    },
    {
        'id': 19,
        'name': u'Sour Red/Brown',
        'description': (
            u'''The sour red/brown beers of Flanders can be considered as '''
            u'''two different styles, or two ends of a single style '''
            u'''continuum, depending on how you choose to view the issue. '''
            u'''They are a clearly–defined sour ale subtype, one with strong '''
            u'''historical traditions. Their character blends rich malt with '''
            u'''tartness, and usually some fruity character as well. Oak '''
            u'''aging is common in the traditional production of the style '''
            u'''and therefore is often evident in the character. Many '''
            u'''examples are also aged on fruit. At the red end of the '''
            u'''style, the classic is Rodenbach at the brown end it is '''
            u'''Liefmans, and there are several very good examples in '''
            u'''between.'''),
        'parent_id': 2
    },
    {
        'id': 20,
        'name': u'Sour/Wild Ale',
        'description': (
            u'''Sour/Wild is a category encompassing a myriad of '''
            u'''non-traditional sour ales which are typically brewed with an '''
            u'''ale yeast and then inoculated with souring bacteria and '''
            u'''yeasts -- typically Lactobacillus, often Brettanomyces and '''
            u'''Pediococcus, and sometimes Acetobacter.'''),
        'parent_id': 2
    },
    {
        'id': 21,
        'name': u'Altbier',
        'description': (
            u'''Well hopped and malty with copper to dark-brown color, '''
            u'''native to Dusseldorf, Germany. Alt is the German word for '''
            u'''"old" or "old style". It is more or less the German '''
            u'''equivalent to an English ale. Traditionally fermented warm '''
            u'''but aged at cold temperatures.'''),
        'parent_id': 3
    },
    {
        'id': 22,
        'name': u'Amber Ale',
        'description': (
            u'''A style without definition, amber ales range from bland, '''
            u'''vaguely caramelly beers to products with a fairly healthy '''
            u'''malt and hop balance. Often the differentiation between a '''
            u'''quality amber and an American Pale is that the amber might '''
            u'''have more dark malt character, or a less assertive hop rate.'''),
        'parent_id': 3
    },
    {
        'id': 23,
        'name': u'American Pale Ale',
        'description': (
            u'''American Pale Ales are light in color, ranging from golden '''
            u'''to a light copper color. The style of this beer is defined '''
            u'''by the American hops used. American hops typically have high '''
            u'''bitterness and aroma. This is a perfect beer for big fare '''
            u'''like grilled burgers or combination pizzas, as well as '''
            u'''lighter fare like sushi and green salads.'''),
        'parent_id': 3
    },
    {
        'id': 24,
        'name': u'American Strong Ale',
        'description': (
            u'''Not a style, per se, but a catch-all category to incorporate '''
            u'''the plethora of strong%2C stylistically vague beers coming '''
            u'''from American microbreweries today. Some are related to '''
            u'''English Strong Ales, but with a higher hop rate, while '''
            u'''others are ultra-strong variants on the IPA or red ale '''
            u'''themes. No matter how varied their origins or characters '''
            u'''might be, all are intense, potent, with generous quantities '''
            u'''of hops and malt.'''),
        'parent_id': 3
    },
    {
        'id': 25,
        'name': u'Barley Wine',
        'description': (
            u'''A Barley Wine is a strong, top-fermenting ale, with an '''
            u'''alcohol content of at least 9% and up to 13% (or more) by '''
            u'''volume. Hops may be hardly noticeable at all or very '''
            u'''noticeable. Sip them out of the special glass, that will '''
            u'''concentrate the aroma. They are excellent with cigars or '''
            u'''with dessert'''),
        'parent_id': 3
    },
    {
        'id': 26,
        'name': u'Bitter',
        'description': (
            u'''A gold to copper color, low carbonation and medium to high '''
            u'''bitterness. Hop flavor and aroma may be non-existent to '''
            u'''mild. Great to drink with steak and lobster.'''),
        'parent_id': 3
    },
    {
        'id': 27,
        'name': u'Brown Ale',
        'description': (
            u'''Color ranges from reddish-brown to dark brown. Beers termed '''
            u'''brown ale include sweet low alcohol beers such as Manns '''
            u'''Original Brown Ale medium strength amber beers of moderate '''
            u'''bitterness such as Newcastle Brown Ale and malty but hoppy '''
            u'''beers such as Sierra Nevada Brown Ale.'''),
        'parent_id': 3
    },
    {
        'id': 28,
        'name': u'Cream Ale',
        'description': (
            u'''A mild, pale, light-bodied ale, made using a warm '''
            u'''fermentation (top or bottom) and cold lagering or by '''
            u'''blending top and bottom-fermented beers. Low to medium '''
            u'''bitterness. Low hop flavor and aroma.'''),
        'parent_id': 3
    },
    {
        'id': 29,
        'name': u'English Pale Ale',
        'description': (
            u'''Classic English Pale Ales are not pale but rather are golden '''
            u'''to copper colored and display English variety hop character. '''
            u'''Distinguishing characteristics are dryness and defined hop '''
            u'''taste, but more malt balance than what you’ll typically find '''
            u'''in an American Pale Ale. Great to drink with all sorts of '''
            u'''meats including roast beef, lamb, burgers, duck, goose, etc. '''
            u'''Note that the term ’pale ale’ is used in England to signify '''
            u'''a bottled bitter, and in that way there is no such thing as '''
            u'''’English Pale Ale’ to the English. The style is a North '''
            u'''American construct, borne of the multitude of pale ales that '''
            u'''pay homage to these bottled bitters - Bass in particular - '''
            u'''and therefore the majority of true examples of the style are '''
            u'''found outside Britain.'''),
        'parent_id': 3
    },
    {
        'id': 30,
        'name': u'English Strong Ale',
        'description': (
            u'''Malty, with complex fruity esters. Some oxidative notes are '''
            u'''acceptable, akin to those found in port or sherry. Hop '''
            u'''aromas not usually present, due to extended age. Medium '''
            u'''amber to very dark red-amber color. Malty and usually sweet. '''
            u'''Alcoholic strength should be evident, though not '''
            u'''overwhelming. Medium to full body alcohol should contribute '''
            u'''some warmth. An ale of significant alcoholic strength, '''
            u'''though usually not as strong or rich as barleywine. Usually '''
            u'''tilted toward a sweeter, more malty balance. Often regarded '''
            u'''as winter warmers, and often released as seasonal beers.'''),
        'parent_id': 3
    },
    {
        'id': 31,
        'name': u'Golden Ale/Blond Ale',
        'description': (
            u'''There are a few different types of blond ale. The first is '''
            u'''the traditional "Canadian Ale", an adjunct-laden, '''
            u'''macrobrewed, top-fermented equivalent of the American '''
            u'''Standard. The second is common in US brewpubs - a light '''
            u'''starter ale, with marginally more hop and body than a '''
            u'''macrobrew, fewer adjuncts, but still not a flavourful beer '''
            u'''by any means. The British interpretation is easily the '''
            u'''boldest, hoppiest blond ale rendition. Some of these can '''
            u'''almost be considered American Pales they are so hopped up - '''
            u'''very crisp, refreshing, with relatively low alcohol compared '''
            u'''with their North American counterparts.'''),
        'parent_id': 3
    },
    {
        'id': 32,
        'name': u'Imperial IPA',
        'description': (
            u'''Imperial IPA (also called Double or Triple IPA) is a strong, '''
            u'''often sweet, intensely hoppy version of the traditional '''
            u'''India Pale Ale. Bitterness units range tend to be 100 IBUs '''
            u'''and above. The ABV level for DIPAs generally begins at 7.5% '''
            u'''but is more commonly in the 8.0%+ range. The flavour profile '''
            u'''is intense all around. Unlike barley wines, the balance is '''
            u'''heavily towards the hops, with crystal and other malts '''
            u'''providing support.'''),
        'parent_id': 3
    },
    {
        'id': 33,
        'name': u'India Pale Ale (IPA)',
        'description': (
            u'''India Pale Ale, the modern version of which has largely been '''
            u'''formed in the US, has an intense hop flavor, a golden to '''
            u'''copper color, and a medium malty body. The aroma is moderate '''
            u'''to very strong. IPAs work especially well at cutting the '''
            u'''heat of chili, vindaloo or Sichuan cuisine. In England, IPA '''
            u'''is often just another name for bitter although some micros '''
            u'''are doing their own versions of an American IPA as well.'''),
        'parent_id': 3
    },
    {
        'id': 34,
        'name': u'Irish Ale',
        'description': (
            u'''The red ales of Ireland have a gentle maltiness, caramelly, '''
            u'''earthy notes, and a generally restrained hop character. '''
            u'''They are session ales, so alcohol is generally at 5% abv or '''
            u'''less, though you will find the occasion stronger example. '''
            u'''The major macrobrewed Irish ales are ascribed to be in this '''
            u'''style, but the majority of examples are from New World '''
            u'''microbreweries working with Michael Jackson’s description of '''
            u'''Irish ale.'''),
        'parent_id': 3
    },
    {
        'id': 35,
        'name': u'Kölsch',
        'description': (
            u'''Golden, top-fermented style native to Köln, Germany. The '''
            u'''style has a very narrow profile and many beers that consider '''
            u'''themselves to be kölschbiers are not. Generally they have a '''
            u'''moderate bitterness, but fairly prominent hop flavour '''
            u'''(typically Spalt, Tettnang or Hallertau). They have high '''
            u'''effervescence, medium esters, but a rounded, stylish '''
            u'''character derived from lagering.'''),
        'parent_id': 3
    },
    {
        'id': 36,
        'name': u'Mild Ale',
        'description': (
            u'''Malt accented, typically little or no hop flavour or aroma. '''
            u'''Usually medium to dark brown in colour though many English '''
            u'''examples are almost black with caramel often added for '''
            u'''colouring as well as favouring purposes. Mild refers to no '''
            u'''or limited hop bitterness/ aroma. Still very popular in the '''
            u'''North- West and Midland areas of England where it is usually '''
            u'''between 3 to 4% ABV and preferred with a good head. There '''
            u'''are examples of stronger versions of the style, but rarely '''
            u'''over 5-6%.'''),
        'parent_id': 3
    },
    {
        'id': 37,
        'name': u'Old Ale',
        'description': (
            u'''Old Ale is a simple enough style to figure out. At least, '''
            u'''once you understand that there are three or four beer styles '''
            u'''called Old Ale. The first is the best known - the strong '''
            u'''dark Old Peculier style. The second type of Old Ale is a '''
            u'''blended dark ale. At least one of the beers comprising the '''
            u'''blend will be aged for a couple of years in wood casks. The '''
            u'''third version of Old Ale is a form of mild – a low-gravity '''
            u'''dark ale. Another version of Old Ale is closely related to '''
            u'''the first. For me, these are robustly malty beers, akin to a '''
            u'''top-fermented version of a doppelbock.'''),
        'parent_id': 3
    },
    {
        'id': 38,
        'name': u'Premium Bitter/ESB',
        'description': (
            u'''In England, many breweries have a number of bitters in their '''
            u'''range. The style that has come to be known as Premium or '''
            u'''Special Bitter generally includes the stronger (4.6%-6.0%) '''
            u'''examples. These are mostly served in the traditional way '''
            u'''from the cask, but some are also found in bottle form where '''
            u'''the extra malt allows them to stand up better than the more '''
            u'''delicate ordinary Bitter. In the US, the designation ESB is '''
            u'''common for this style, owing to the influence of Fuller’s '''
            u'''ESB, the London brew that was among the first to be exported '''
            u'''to the States. In the US, some ESBs are made with American '''
            u'''hops and a clean yeast, but the alcohol range is the same, '''
            u'''as is the range of bitterness, usually between 25 and 35 but '''
            u'''occasionally creeping higher.'''),
        'parent_id': 3
    },
    {
        'id': 39,
        'name': u'Scotch Ale',
        'description': (
            u'''Scotch Ale was the name given to a strong pale ale from '''
            u'''Edinburgh in the 19th century. This was typical of the '''
            u'''strong pale ales brewed in Britain at that time - mainly '''
            u'''pale barley malt and moderate hopping, and were not that '''
            u'''stylistically different to English Strong Ales or Barley '''
            u'''Wines. The name however became regionalised so that a strong '''
            u'''pale ale from Scotland became known as a Scotch Ale or Wee '''
            u'''Heavy. Beers using the designation Scotch Ale are popular in '''
            u'''the USA where most examples are brewed locally. Examples of '''
            u'''beers brewed in the USA under the name Wee Heavy tend to be '''
            u'''7% abv and higher, while Scottish brewed examples, such as '''
            u'''Belhavens Wee Heavy, are typically between 5.5% and 6.5% '''
            u'''abv.'''),
        'parent_id': 3
    },
    {
        'id': 40,
        'name': u'Scottish Ale',
        'description': (
            u'''Scottish ales are generally dark, malty, full-bodied brews. '''
            u'''Many examples have a hint of smokiness derived from the use '''
            u'''of peated malt. 60, 70, and 80 shilling examples are all '''
            u'''session ales under 5% abv, but the stronger "wee heavies" '''
            u'''can range closer to 8%, with the accompanying increase in '''
            u'''alcohol flavour and esters. Works well as an accompaniment '''
            u'''to hearty meat and game dishes, sharp cheddar, atholl brose '''
            u'''and shortbread.'''),
        'parent_id': 3
    },
    {
        'id': 41,
        'name': u'Session IPA',
        'description': (
            u'''The term Session IPA describes a category of beers marketed '''
            u'''for their hop-dominant flavor profiles at "sessionable" '''
            u'''levels of alcohol. While this is typically 3.2 - 4.6 percent '''
            u'''alcohol, a few have stretched the definition. This class of '''
            u'''beers arose in 2010 out of the Craft Beer Tradition as a '''
            u'''reaction to the trend of increasingly strong beers and '''
            u'''greater public appreciation for hoppier profiles around the '''
            u'''globe. It is differentiated from American Pale Ale by '''
            u'''typically being lower in alcohol and usually having more '''
            u'''hop-dominant profiles. While hops used are typically '''
            u'''American Pacific Northwest and New Zealand, '''
            u'''proprietary/experimental and South African and other hops '''
            u'''may also factor into a Session IPA hop bill.'''),
        'parent_id': 3
    },
    {
        'id': 42,
        'name': u'Baltic Porter',
        'description': (
            u'''The historical remnants of the 19th c. Baltic trade in '''
            u'''imperial stouts, Baltic Porters are typically strong, sweet '''
            u'''and bottom-fermented. They lack the powerful roast of an '''
            u'''imperial stout, but have an intense malt character, and '''
            u'''moderate to strong alcohol. Though they are typically '''
            u'''lagers, there are a handful of top-fermented examples.'''),
        'parent_id': 4
    },
    {
        'id': 43,
        'name': u'Black IPA',
        'description': (
            u'''An emerging beer style roughly defined as a beer with '''
            u'''IPA-level hopping relatively high alcohol and a distinct '''
            u'''toasty dark malt character. Typically lacks the roastiness '''
            u'''and body of a strong stout and is hoppier than a strong '''
            u'''porter. Expressive dry-hopping is common. Also called India '''
            u'''Dark Ale, India Black Ale, Cascadian Dark Ale, Dark IPA and '''
            u'''sometimes India Brown Ale.'''),
        'parent_id': 4
    },
    {
        'id': 44,
        'name': u'Dry Stout',
        'description': (
            u'''The "Irish-style" stout is typically a low-gravity stout '''
            u'''with bitterness ranging between 30-45 IBUs. Roastiness is '''
            u'''present, but restrained, and there should not be hops in '''
            u'''either the flavour or aroma. A little bit of acidity can be '''
            u'''present. Often, this type of stout is serving via nitrogen, '''
            u'''with all the effects that has on a beer - low carbonation, '''
            u'''extra-thick head, lifeless palate and muted flavour and '''
            u'''aroma.'''),
        'parent_id': 4
    },
    {
        'id': 45,
        'name': u'Foreign Stout',
        'description': (
            u'''Foreign Stout began with the beer that would become Guinness '''
            u'''Foreign Extra Stout. This was a stronger, extra-hopped '''
            u'''version of the basic Guinness Extra Stout, brewed to '''
            u'''survive long journeys overseas. The classic FES still exists '''
            u'''in a few different forms, but many of the original '''
            u'''destination countries (Jamaica, Sri Lanka, etc.) now have '''
            u'''their own, locally-produced versions. Foreign stout occupies '''
            u'''a position between basic stout and imperial stout. It is '''
            u'''sweeter than a basic stout, but not as robust as an '''
            u'''imperial. It is less fruity and less hoppy as well. Foreign '''
            u'''stouts are sometimes made with local grains and adjuncts – '''
            u'''sugar is not uncommon. Alcohol ranges from 6-8%.'''),
        'parent_id': 4
    },
    {
        'id': 46,
        'name': u'Imperial Porter',
        'description': (
            u'''Imperial (extra-strong) porters fall in between the '''
            u'''traditional porter, a Baltic porter, and an imperial stout. '''
            u'''They range from around 7.5% upwards, with hefty dark malt '''
            u'''character, but lack the overt roastiness of an imperial '''
            u'''stout.'''),
        'parent_id': 4
    },
    {
        'id': 47,
        'name': u'Imperial Stout',
        'description': (
            u'''Imperial stouts are usually extremely dark brown to black in '''
            u'''color with flavors that are intensely malty, deeply roasted '''
            u'''and sometimes with accents of dark fruit (raisin, fig) and '''
            u'''chocolate. The bitterness is typically low to moderate. '''
            u'''Imperial stouts are strong and generally exceed 8% ABV.'''),
        'parent_id': 4
    },
    {
        'id': 48,
        'name': u'Porter',
        'description': (
            u'''Black or chocolate malt gives the porter its dark brown '''
            u'''color. Porters are often well hopped and somewhat heavily '''
            u'''malted. This is a medium-bodied beer and may show some '''
            u'''sweetness usually from the light caramel to light molasses '''
            u'''range. Hoppiness can range from bitter to mild. Porters, in '''
            u'''relation to stouts of the same region, are typically more '''
            u'''mild and less aggressively hopped.'''),
        'parent_id': 4
    },
    {
        'id': 49,
        'name': u'Stout',
        'description': (
            u'''A stout is made with dark roasted malts which results in a '''
            u'''dark color and a roasted malt flavor. In mainland Europe '''
            u'''they are usually termed "noir" (black). The word stout means '''
            u'''strong, and was applied to strong Porter in the 18th century '''
            u'''- most typically by Guinness, who were one of the few '''
            u'''breweries to continue making such beers into the 20th '''
            u'''century. Guinness is today the template for Irish or Dry '''
            u'''Stout. Other stout variations are Imperial Stout, Foreign '''
            u'''Stout, and Sweet or Milk Stout - as well as Porter, Imperial '''
            u'''Porter, and Baltic Porter - and the related Mild and '''
            u'''Schwarzbier.'''),
        'parent_id': 4
    },
    {
        'id': 50,
        'name': u'Sweet Stout',
        'description': (
            u'''Dark brown to black in colour. Sweet stouts come in two main '''
            u'''varieties - milk stout and oatmeal stout. Milk stouts are '''
            u'''made with the addition of lactose, and are sweet and '''
            u'''generally low in alcohol. Oatmeal lends a smooth fullness of '''
            u'''body to stouts. All of the sweet stouts are noted for their '''
            u'''restrained roastiness in comparison with other stouts, and '''
            u'''their low hop levels.'''),
        'parent_id': 4
    },
    {
        'id': 51,
        'name': u'Dunkelweizen',
        'description': (
            u'''A dark take on the German wheat theme, dunkelweizens have '''
            u'''the same banana and clove notes of their pale cousins, but '''
            u'''also have earthy, toasty, chocolatey notes from the addition '''
            u'''of dark malts. They are "shoulder season" wheat beers to '''
            u'''many drinkers - something a little more robust than a '''
            u'''hefeweizen for the fall and spring seasons, but not as rich '''
            u'''as winter’s weizenbocks. Alcohol is between 4.8-5.6% '''
            u'''generally, bitterness is low, and carbonation is high. '''
            u'''Occasionally, you will see dark versions of American Wheats, '''
            u'''but these are uncommon.'''),
        'parent_id': 5
    },
    {
        'id': 52,
        'name': u'German Hefeweizen',
        'description': (
            u'''Depending on the style can range from pale and light body to '''
            u'''dark brown with full body. Wheat beer is characterized by '''
            u'''its cloudy appearance and its banana and sometimes vanilla '''
            u'''aftertaste.'''),
        'parent_id': 5
    },
    {
        'id': 53,
        'name': u'German Kristallweizen',
        'description': (
            u'''Kristalweizens are the third member of the German Wheat '''
            u'''trifecta. Derided by many beer lovers as “castrated '''
            u'''hefeweizens”, kristalweizens are known for their filtered, '''
            u'''sparkling colour. They have the classic spritzy carbonation '''
            u'''of wheat beers, and the same tart wheat notes and signature '''
            u'''components of banana, bubblegum and spice. The body is '''
            u'''light, and alcohol ranging around the 5% mark, give or take '''
            u'''half a point.'''),
        'parent_id': 5
    },
    {
        'id': 54,
        'name': u'Grodziskie/Gose/Lichtenhainer',
        'description': (
            u'''Sour wheat beers were common in many parts of medieval and '''
            u'''early Industrial Europe. Two styles – lambic and Berliner '''
            u'''weisse – survived, but many others did not. Gose and '''
            u'''Lichtenhainer are historic styles of sour wheat beer. '''
            u'''Grodzisk is sometimes tart, sometimes not. Gose is seasoned '''
            u'''with salt, Grodziskie and Lichtenhainer contain smoked malt. '''
            u'''Historical sources are mixed about Lichtenhainer containing '''
            u'''wheat, so modern interpretations may vary. Grätzer is an '''
            u'''alter native name for Grodziskie. All three will be '''
            u'''relatively low alcohol, with a strong wheat character, but '''
            u'''will be distinct from classic examples of Berliner Weisse or '''
            u'''lambic. As all we have are historical recreations, '''
            u'''substantial differences may exist between interpretations.'''),
        'parent_id': 5
    },
    {
        'id': 55,
        'name': u'Weizen Bock',
        'description': (
            u'''Strong, dark wheat beers, typically with a high ester '''
            u'''profile and more malt and alcohol than is typically '''
            u'''associated with a wheat beer.'''),
        'parent_id': 5
    },
    {
        'id': 56,
        'name': u'Wheat Ale',
        'description': (
            u'''Golden to light amber in color, the body is light to medium. '''
            u'''The wheat lends a crispness to the brew, often with some '''
            u'''acidity. Some hop flavour may be present, but bitterness is '''
            u'''low.  Not as estery as German or Belgian-style wheats.'''),
        'parent_id': 5
    },
    {
        'id': 57,
        'name': u'Witbier',
        'description': (
            u'''Witbier, also known as Belgian White, is a style of '''
            u'''Belgian-style wheat beers that are generally pale and opaque '''
            u'''with a crisp wheat character and citric refreshment of '''
            u'''orange peel and coriander. Ingredients sometimes include '''
            u'''oats for smoothness, and other spices such as grains of '''
            u'''paradise. Serve with light cheeses or mussels.'''),
        'parent_id': 5
    },
    {
        'id': 58,
        'name': u'Amber Lager/Vienna',
        'description': (
            u'''Your typical macrobrewed Dark Lager, often rendered dark '''
            u'''with either brewer’s caramel or black patent malt, but each '''
            u'''brewery will have a different approach. Aside from caramelly '''
            u'''notes, these beers will not typically resemble other dark '''
            u'''lager styles so much as they do the lighter styles, due to '''
            u'''low amounts of hops, malt and body. Vienna as a beer style '''
            u'''was theorized by Michael Jackson, but his oft-cited example '''
            u'''was Negra Modelo, which is a macro dark lager like all the '''
            u'''others. Some beers have taken on the idea of a Vienna lager '''
            u'''as a distinct style, loosely based on the 1840 Anton Dreher '''
            u'''beer, and these can be expected to be all-malt, with a '''
            u'''fuller body and more character than the average macro dark.'''),
        'parent_id': 6
    },
    {
        'id': 59,
        'name': u'California Common',
        'description': (
            u'''Style originating in 18th century California, where brewers '''
            u'''with out access to refrigeration produced beers using lager '''
            u'''yeasts and warm temperatures. These still retain some of the '''
            u'''rounded character inherent in all lagers, but with a dose of '''
            u'''ale fruitiness.'''),
        'parent_id': 6
    },
    {
        'id': 60,
        'name': u'Czech Pilsner (Světlý)',
        'description': (
            u'''Hallmarked by the generous use of the Saaz hop, Bohemian or '''
            u'''Czech pilsners are also noted for their rich gold color, fat '''
            u'''maltiness and moderate to full body. Generally brewed to '''
            u'''10-12° Plato. in Czech these beers are simply called Světlý '''
            u'''Ležák. Sometimes served cloudy and unfiltered with young '''
            u'''wort mixed in, known as Kvasnicova in the Czech Republic, '''
            u'''the same as what is known as krausening in Germany. '''
            u'''Regardless of origin, to be a pilsner a beer must have at '''
            u'''least 28 units of bitterness, and preferably much more.'''),
        'parent_id': 6
    },
    {
        'id': 61,
        'name': u'Doppelbock',
        'description': (
            u'''Doppel means double and while these are stronger brews than '''
            u'''the traditional German bocks, they are typically not twice '''
            u'''the strength. Color is light amber to dark brown. Very full '''
            u'''body with a high alcoholic flavor. Low hop flavor and '''
            u'''aroma.'''),
        'parent_id': 6
    },
    {
        'id': 62,
        'name': u'Dortmunder/Helles',
        'description': (
            u'''These two styles are closely related, the former hailing '''
            u'''from Dortmund and the latter from Bavaria. Both are slightly '''
            u'''strong (5.0-5.6%), malt-accented pale lagers. The '''
            u'''cookie-like or bready maltiness should be very much in '''
            u'''evidence in a traditional example. These beers are clean and '''
            u'''easy to drink in quantity. Some Dortmunders made in Denmark '''
            u'''and the Netherlands are stronger.'''),
        'parent_id': 6
    },
    {
        'id': 63,
        'name': u'Dunkel/Tmavý',
        'description': (
            u'''Copper to dark brown lager common in Germany and the Czech '''
            u'''Republic but made worldwide. Medium body. Nutty toasted '''
            u'''chocolate-like malty sweetness in aroma and flavor. Medium '''
            u'''bitterness. Low "noble-type" hop flavor and aroma. In both '''
            u'''Germany and Czech dark lagers span a wide range of '''
            u'''characters from sweet to dry forming more of a category than '''
            u'''a specific style with considerable leeway for the brewer '''
            u'''with regards to the character of the beer. This is the '''
            u'''biggest reason why they are grouped together despite coming '''
            u'''from different traditions and each being made with local '''
            u'''ingredients.'''),
        'parent_id': 6
    },
    {
        'id': 64,
        'name': u'Dunkler Bock',
        'description': (
            u'''The dark Bock has a deep copper to dark brown color. Medium '''
            u'''to full-bodied, malt sweetness and nutty or light toasted '''
            u'''flavors dominate. Hop flavor and aroma can be light to '''
            u'''non-existent.'''),
        'parent_id': 6
    },
    {
        'id': 65,
        'name': u'Eisbock',
        'description': (
            u'''A stronger version of Doppelbock. Deep copper to black. Very '''
            u'''alcoholic. Typically brewed by freezing a doppelbock and '''
            u'''removing resulting ice to increase alcohol content.'''),
        'parent_id': 6
    },
    {
        'id': 66,
        'name': u'Heller Bock',
        'description': (
            u'''The Heller Bock is primarily a malty beer from the German '''
            u'''brewing tradition with little hop character - neither bitter '''
            u'''nor aromatic - though the style typically has a little more '''
            u'''hops than the standard Bock. The color is golden to light '''
            u'''brown or amber. They should normally pour with a substantial '''
            u'''white head. Typical examples are pale and clear.'''),
        'parent_id': 6
    },
    {
        'id': 67,
        'name': u'Imperial Pils/Strong Pale Lager',
        'description': (
            u'''A catch-all for strong, sometimes hoppy lagers that range '''
            u'''from modern versions of "Imperial Pilsner", to more '''
            u'''traditional strong lagers which are more common in Eastern '''
            u'''Europe. These are essentially stronger versions of pilsners, '''
            u'''though the increased malt and alcohol will noticeably '''
            u'''reduce the hop accent. Because these are usually all-malt, '''
            u'''and comfortably hopped, they are easily distinguishable from '''
            u'''malt liquors. With out the malt character of bocks, these '''
            u'''are worthy of a style all their own.'''),
        'parent_id': 6
    },
    {
        'id': 68,
        'name': u'Malt Liquor',
        'description': (
            u'''Strong, alcoholic-tasting, often poorly made strong lagers. '''
            u'''Esters, fusels and other products of undiluted high-gravity '''
            u'''brewed beers are often commonplace. Properly served in the '''
            u'''40oz bottle with accompanying brown paper bag.'''),
        'parent_id': 6
    },
    {
        'id': 69,
        'name': u'Oktoberfest/Märzen',
        'description': (
            u'''Oktoberfest is a German festival dating from 1810, and '''
            u'''Oktoberfestbiers are the beers that have been served at the '''
            u'''festival since 1818, and are supplied by 6 breweries: '''
            u'''Spaten, Lowenbrau, Augustiner, Hofbrau, Paulaner and '''
            u'''Hacker-Pschorr. Traditionally Oktoberfestbiers were the '''
            u'''lagers of around 5.5 to 6 abv called Marzen - brewed in '''
            u'''March and allowed to ferment slowly during the summer '''
            u'''months. Originally these would have been dark lagers, but '''
            u'''from 1872 a strong March brewed version of an amber-red '''
            u'''Vienna lager made by Josef Sedlmayr became the favourite '''
            u'''Oktoberfestbier. Since the 1990s European brewed versions '''
            u'''have tended to be golden in colour, while American versions '''
            u'''have remained dark or amber.'''),
        'parent_id': 6
    },
    {
        'id': 70,
        'name': u'Pale Lager',
        'description': (
            u'''The color of pale lager ranges from light bronze to nearly '''
            u'''transparent and the alcohol anywhere from 4-6%. Adjunct '''
            u'''usage may be quite high, though in some cases the beer is '''
            u'''all-malt. Carbonation is typically forced, though not '''
            u'''always. One thing that does not vary is that neither the '''
            u'''malt nor the hops make much of an impression on the palate. '''
            u'''These beers are brewed for minimum character, though faint '''
            u'''traces of hop or malt may show through.  Commonly detected '''
            u'''features and flaws include fusels, oxidized malt and skunked '''
            u'''hops. The body will often be thin and/or spritzy while the '''
            u'''finish is typically mildly bitter.'''),
        'parent_id': 6
    },
    {
        'id': 71,
        'name': u'Pilsener',
        'description': (
            u'''While the definition of pilsner is open to much debate in '''
            u'''the beer community, it generally refers to pale, hoppy '''
            u'''lagers, ranging from ~30 IBU and up. From Classic German '''
            u'''Pilsners, which tend to be light-to-medium bodied, '''
            u'''semi-sweet to off-dry, hopped with German noble hops, to New '''
            u'''World artisan renditions in North America, New Zealand and '''
            u'''elsewhere, which showcase modern hop strains. A separate '''
            u'''style category is maintained for Czech Pilsner (Světlý '''
            u'''Ležák).'''),
        'parent_id': 6
    },
    {
        'id': 72,
        'name': u'Polotmavý',
        'description': (
            u'''This is the amber lager style of the Czech Republic. The '''
            u'''character that the brewery usually aims for with this style '''
            u'''is a hybrid between the dark lager and the pale pilsner. The '''
            u'''result has a richer malt character than the American '''
            u'''Dark/Amber Lager/Vienna style and more hop than the '''
            u'''Oktoberfest/Marzen style.'''),
        'parent_id': 6
    },
    {
        'id': 73,
        'name': u'Premium Lager',
        'description': (
            u'''A beer that straddles between the mainstream Pale Lager and '''
            u'''Pilsner. Not all beers that call themselves Premium Lager '''
            u'''are, but those that are will typically have a deep gold to '''
            u'''light bronze colour, and distinct influence of malt and '''
            u'''hops. They should be free of adjuncts and will have a softer '''
            u'''carbonation than Pale Lager or Classic German Pilsner. IBUs '''
            u'''will typically range in the 20’s, and lagering times will '''
            u'''typically be 4-6 weeks, more in line with what pilsners '''
            u'''have. Overall accent will be malty-to-balanced, alcohol in a '''
            u'''slightly tighter range than either Pale Lager or Pilsner '''
            u'''(4.5-5.5%). Most often the product of a microbrewery or '''
            u'''brewpub, but macrobreweries can make this style if they jack '''
            u'''up the hops a bit and make it all-malt.'''),
        'parent_id': 6
    },
    {
        'id': 74,
        'name': u'Radler/Shandy',
        'description': (
            u'''A mix of a sweet soft drink or juice -- typically lemon or '''
            u'''ginger but sometimes apple, grapefruit or other fruit -- and '''
            u'''beer, often in equal parts, that is moderately sweet, thirst '''
            u'''quenching, low in alcohol with medium to spritzy '''
            u'''carbonation. Often but not necessarily sold as a Summer '''
            u'''seasonal. Category includes such regional styles as diesel '''
            u'''(beer and cola), cola-weizen (wheat beer and cola), and '''
            u'''russ’n.'''),
        'parent_id': 6
    },
    {
        'id': 75,
        'name': u'Schwarzbier',
        'description': (
            u'''Dark brown to black. Medium body. Roasted malt evident. Low '''
            u'''sweetness in aroma and flavor. Low to medium bitterness. Low '''
            u'''bitterness from roast malt. Hop flavor and aroma, '''
            u'''"noble-type" OK. No fruitiness, esters.'''),
        'parent_id': 6
    },
    {
        'id': 76,
        'name': u'Zwickel/Keller/Landbier',
        'description': (
            u'''Three related lager styles most common in Franconia. '''
            u'''Essentially, these are hoppier versions of a helles, served '''
            u'''with natural carbonation and unfiltered - they are the lager '''
            u'''world’s answer to real ale. Kellerbier will on average be '''
            u'''hoppier than zwickelbier. There is also Landbier, which is '''
            u'''more malt-accented, may be filtered, but is similarly '''
            u'''lacking in carbonation. Gravity is standard, low to moderate '''
            u'''hop rates, the colour from pale to reddish-amber and the '''
            u'''palate should be balanced with a hop accent. Zoiglbier, '''
            u'''common to Oberpfalz, is also included in this category.'''),
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
        'description': (
            u'''A reddish brown trappist ale, malty and fruit, featuring a 3 '''
            u'''week secondary fermentation. This ale has a full, pale '''
            u'''yellow head. The bouquet is full of esters and fruitiness. '''
            u'''Notes of ripe banana predominate. The taste is fruity and '''
            u'''slightly bitter, with a long, dry finish.'''),
        'category_id': 7,
        'user_id': 1
    },
    {
        'id': 2,
        'name': u'Tripel Karmeliet',
        'description':(
            u'''First brewed 1996; claimed to be based on a recipe from 1679 '''
            u'''which used wheat, oat and barley. Tripel Karmeliet is a very '''
            u'''refined and complex golden-to-bronze brew with a fantastic '''
            u'''creamy head. These characteristics derive not only from the '''
            u'''grains used but also from restrained hopping with Styrians '''
            u'''and the fruity nature (banana and vanilla) of the house '''
            u'''yeast. Aroma has hints of vanilla mixed with citrus aromas. '''
            u'''Tripel Karmeliet has not only the lightness and freshness of '''
            u'''wheat, but also the creaminess of oats together with a spicy '''
            u'''lemony almost quinine dryness.'''),
        'category_id': 8,
        'user_id': 1
    },
    {
        'id': 3,
        'name': u'Westmalle Tripel',
        'description': (
            u'''A strong, dry and spicy trappist ale. The product of a '''
            u'''secondary fermentation lasting 5 weeks. This is a complex '''
            u'''ale with a fruity aroma and a nice nuanced hop scent. It is '''
            u'''soft and creamy in the mouth, with a bitter touch carried by '''
            u'''the fruity aroma. An exceptional ale, with a great deal of '''
            u'''finesse and elegance, and with a splendid long after taste.'''),
        'category_id': 8,
        'user_id': 1
    },
    {
        'id': 4,
        'name': u'Orval',
        'description': (
            u'''In contrast to all the others, the Orval Trappist brewery '''
            u'''makes only one beer for the general public. It has an '''
            u'''intensely aromatic and dry character. Between the first and '''
            u'''second fermentations there is also an additional dry-hopping '''
            u'''process.  Through this the beer acquires its pronounced '''
            u'''hoppy aroma and extra dry taste.  Bottled at 5.2% abv - can '''
            u'''go up as high as 7.2%'''),
        'category_id': 10,
        'user_id': 1
    },
    {
        'id': 5,
        'name': u'Westvleteren Blond',
        'description': (
            u'''Westvleteren Blond is the basic beer for the monks' own '''
            u'''consumption, since 1999, when the former 6° dark ale (red '''
            u'''cap) was finally discarded, after the 4° had already gone '''
            u'''that path.'''),
        'category_id': 10,
        'user_id': 1
    },
    {
        'id': 6,
        'name': u'Just a Beer',
        'description': 'Just a description for just a beer.',
        'category_id': 10,
        'user_id': 1
    }
)

for i in items:
    print 'adding item: %s' % i
    item = Item(id=i['id'], name=i['name'],
                description=i['description'], category_id=i['category_id'])

    session.add(item)

session.commit()
