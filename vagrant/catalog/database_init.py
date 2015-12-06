#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Category, Item

engine = create_engine('postgresql+psycopg2://connoisseur:michaeljackson@localhost:5432/beercatalog')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

if len(session.query(User).all()) == 0:
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
        user = User(id=u['id'],
                    username=u['username'],
                    family_name=u['family_name'],
                    given_name=u['given_name'],
                    email=u['email'],
                    picture=u['picture'])
        session.add(user)

    session.commit()

if len(session.query(Category).all()) == 0:
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
                u'''These are dark, malty, yeasty strong ales in the '''
                u'''Trappist tradition, but produced (mainly) by secular '''
                u'''brewers. Dubbels range between 6.5-8% abv, and have a '''
                u'''dark brown, cloudy colour, and a palate mixing malt, a '''
                u'''lush fruitiness, and yeast. They are typically '''
                u'''bottle-conditioned.'''),
            'parent_id': 1
        },
        {
            'id': 8,
            'name': u'Abbey Tripel',
            'description': (
                u'''Like other abbey ales, Tripels are strong, yeasty-malty '''
                u'''beers. But they are also pale, and have a notable hop '''
                u'''profile. Hop bitterness may be higher than a typical '''
                u'''abbey ale, up to 45IBUs. But the finish is where the '''
                u'''hops really shine, as tripels should finish fairly dry. '''
                u'''Otherwise, maltiness is still essential to the style, '''
                u'''and the assertive yeast note typical of all abbey ales '''
                u'''will be more apparent in tripels, since they do not '''
                u'''have the rich dark malts to distract the palate. '''
                u'''Alcohol flavours feature more prominently in Tripels '''
                u'''that in just about any other style.'''),
            'parent_id': 1
        },
        {
            'id': 9,
            'name': u'Abt/Quadrupel',
            'description': (
                u'''Abt, or quadrupel, is the name given to ultra-strong '''
                u'''Trappist and abbey ales. The name Abt was pioneered to '''
                u'''describe Westvleteren and the beer that would become '''
                u'''St. Bernardus. Quadrupel was pioneered by La Trappe. '''
                u'''Abts are the darker of the two, with more rich, deep '''
                u'''fruity notes. Quads are paler, with corresponding '''
                u'''peachy notes. Neither have much in the way of hop, and '''
                u'''both are very strong and malty. Though both are '''
                u'''bottle-conditioned, abts trend more towards yeastiness. '''
                u'''Alcohol is very high (10+% abv) for both.'''),
            'parent_id': 1
        },
        {
            'id': 10,
            'name': u'Belgian Ale',
            'description': (
                u'''Belgian-style ales seldom fit neatly into classic beer '''
                u'''styles, but this category represents those ales under '''
                u'''approximately 7% abv that do not fit other categories. '''
                u'''Colour ranges from golden to deep amber, with the '''
                u'''occasional example coming in darker. Body tends to be '''
                u'''light to medium, with a wide range of hop and malt '''
                u'''levels. Yeastiness and acidity may also be '''
                u'''present.'''),
            'parent_id': 1
        },
        {
            'id': 11,
            'name': u'Belgian Strong Ale',
            'description': (
                u'''Belgian Strong Ales can vary from pale to dark brown in '''
                u'''color, darker ales may be colored with dark candy '''
                u'''sugar. Hop flavor can range from low to high, while hop '''
                u'''aroma is low. The beers are medium to full-bodied and '''
                u'''have a high alcoholic character. Types of beers '''
                u'''included here include tripels, dubbels and ultra-strong '''
                u'''abbey ales.'''),
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
                u'''bodied with hints of caramel or toffee. Cellared smell '''
                u'''and flavor are characteristics. The name means "beer '''
                u'''for keeping".'''),
            'parent_id': 1
        },
        {
            'id': 13,
            'name': u'Saison',
            'description': (
                u'''Fruity esters dominate the aroma. Clarity is good with '''
                u'''a large foamy head on top. The addition of several '''
                u'''spices and herbs create a complex fruity or citrusy '''
                u'''flavor. Light to medium bodied with very high '''
                u'''carbonation. Alcohol level is medium to high.'''),
            'parent_id': 1
        },
        {
            'id': 14,
            'name': u'Berliner Weisse',
            'description': (
                u'''Very wheaty, very sour style of Berlin. Berliner weisse '''
                u'''bier has a barely perceptible hop content, low alcohol, '''
                u'''and a sharp character. Often these are laced with '''
                u'''syrups to cut the intense acidity, but purists will '''
                u'''want to take them neat to enjoy the multi-faceted '''
                u'''complexity and thirst-quenching character.'''),
            'parent_id': 2
        },
        {
            'id': 15,
            'name': u'Lambic Style - Faro',
            'description': (
                u'''Faro is a lambic blend with the addition of sugar. '''
                u'''These are well-carbonated, and are sweeter and more '''
                u'''refreshing than gueuze. The flavour is often '''
                u'''straightforward and sugary, with lighter barnyard and '''
                u'''funk notes than other lambic styles. The odd variant '''
                u'''contains other spices like orange peel as flavouring.'''),
            'parent_id': 2
        },
        {
            'id': 16,
            'name': u'Lambic Style - Fruit',
            'description': (
                u'''Lambics are wheat beers made with stale hops and '''
                u'''fermented with wild yeasts and other microorganisms '''
                u'''traditionally only on the Senne Valley in and around '''
                u'''Brussels. The most traditional of the fruit lambics are '''
                u'''kriek (cherry) and framboise (raspberry). In modern '''
                u'''times peaches (peche) blackcurrants (cassis) grapes as '''
                u'''well as more exotic fruits are used. Traditional '''
                u'''lambics are commonly denoted by the term "oud" which is '''
                u'''a reference to "old-style" and these are the most sour. '''
                u'''More commonly though lambics are sweetened to cut the '''
                u'''intense acidity. Serve with sharp cheeses or pickled '''
                u'''dishes or use in the preparation of mussels.'''),
            'parent_id': 2
        },
        {
            'id': 17,
            'name': u'Lambic Style - Gueuze',
            'description': (
                u'''Gueuze is a blend of young and old lambic. The yeasts '''
                u'''are rejuvenated and carbonation ensues. The old lambic '''
                u'''is more refined in character and helps take some of the '''
                u'''edge off of the young lambic. The hops used are old, '''
                u'''and act only as a preservative, so hop character is not '''
                u'''a part of the style. The wild yeasts not only ferment '''
                u'''and sour the beer, but they bring the funky, '''
                u'''unpredictable flavours that characterize all lambic '''
                u'''beers. A quality gueuze will be blended to eliminate '''
                u'''some of the less desirable flavours. Above all else, a '''
                u'''gueuze should be sour and very complex. The best '''
                u'''examples are the most complex beers in the world, and '''
                u'''put most champagnes to shame as well. The finish should '''
                u'''be bone dry.'''),
            'parent_id': 2
        },
        {
            'id': 18,
            'name': u'Lambic Style - Unblended',
            'description': (
                u'''Unblended lambic is the purest form of lambic. This '''
                u'''rare specialty is typically only found in the '''
                u'''lambicmakers’ home region, although one bottled example '''
                u'''– Cantillon 1900 Bruocsella Grand Cru – is produced. '''
                u'''Unblended lambics will vary in character from barrel to '''
                u'''barrel, can be found in a variety of ages, and may have '''
                u'''been aged with fruit in the cask. They tend to be '''
                u'''still, with flavours whose edge has not been taken off '''
                u'''by blending.'''),
            'parent_id': 2
        },
        {
            'id': 19,
            'name': u'Sour Red/Brown',
            'description': (
                u'''The sour red/brown beers of Flanders can be considered '''
                u'''as two different styles, or two ends of a single style '''
                u'''continuum, depending on how you choose to view the '''
                u'''issue.  They are a clearly–defined sour ale subtype, '''
                u'''one with strong historical traditions. Their character '''
                u'''blends rich malt with tartness, and usually some fruity '''
                u'''character as well. Oak aging is common in the '''
                u'''traditional production of the style and therefore is '''
                u'''often evident in the character. Many examples are also '''
                u'''aged on fruit. At the red end of the style, the classic '''
                u'''is Rodenbach at the brown end it is Liefmans, and there '''
                u'''are several very good examples in between.'''),
            'parent_id': 2
        },
        {
            'id': 20,
            'name': u'Sour/Wild Ale',
            'description': (
                u'''Sour/Wild is a category encompassing a myriad of '''
                u'''non-traditional sour ales which are typically brewed '''
                u'''with an ale yeast and then inoculated with souring '''
                u'''bacteria and yeasts -- typically Lactobacillus, often '''
                u'''Brettanomyces and Pediococcus, and sometimes '''
                u'''Acetobacter.'''),
            'parent_id': 2
        },
        {
            'id': 21,
            'name': u'Altbier',
            'description': (
                u'''Well hopped and malty with copper to dark-brown color, '''
                u'''native to Dusseldorf, Germany. Alt is the German word '''
                u'''for "old" or "old style". It is more or less the German '''
                u'''equivalent to an English ale. Traditionally fermented '''
                u'''warm but aged at cold temperatures.'''),
            'parent_id': 3
        },
        {
            'id': 22,
            'name': u'Amber Ale',
            'description': (
                u'''A style without definition, amber ales range from '''
                u'''bland, vaguely caramelly beers to products with a '''
                u'''fairly healthy malt and hop balance. Often the '''
                u'''differentiation between a quality amber and an American '''
                u'''Pale is that the amber might have more dark malt '''
                u'''character, or a less assertive hop rate.'''),
            'parent_id': 3
        },
        {
            'id': 23,
            'name': u'American Pale Ale',
            'description': (
                u'''American Pale Ales are light in color, ranging from '''
                u'''golden to a light copper color. The style of this beer '''
                u'''is defined by the American hops used. American hops '''
                u'''typically have high bitterness and aroma. This is a '''
                u'''perfect beer for big fare like grilled burgers or '''
                u'''combination pizzas, as well as lighter fare like sushi '''
                u'''and green salads.'''),
            'parent_id': 3
        },
        {
            'id': 24,
            'name': u'American Strong Ale',
            'description': (
                u'''Not a style, per se, but a catch-all category to '''
                u'''incorporate the plethora of strong%2C stylistically '''
                u'''vague beers coming from American microbreweries today. '''
                u'''Some are related to English Strong Ales, but with a '''
                u'''higher hop rate, while others are ultra-strong variants '''
                u'''on the IPA or red ale themes. No matter how varied '''
                u'''their origins or characters might be, all are intense, '''
                u'''potent, with generous quantities of hops and malt.'''),
            'parent_id': 3
        },
        {
            'id': 25,
            'name': u'Barley Wine',
            'description': (
                u'''A Barley Wine is a strong, top-fermenting ale, with an '''
                u'''alcohol content of at least 9% and up to 13% (or more) '''
                u'''by volume. Hops may be hardly noticeable at all or very '''
                u'''noticeable. Sip them out of the special glass, that '''
                u'''will concentrate the aroma. They are excellent with '''
                u'''cigars or with dessert'''),
            'parent_id': 3
        },
        {
            'id': 26,
            'name': u'Bitter',
            'description': (
                u'''A gold to copper color, low carbonation and medium to '''
                u'''high bitterness. Hop flavor and aroma may be '''
                u'''non-existent to mild. Great to drink with steak and '''
                u'''lobster.'''),
            'parent_id': 3
        },
        {
            'id': 27,
            'name': u'Brown Ale',
            'description': (
                u'''Color ranges from reddish-brown to dark brown. Beers '''
                u'''termed brown ale include sweet low alcohol beers such '''
                u'''as Manns Original Brown Ale medium strength amber beers '''
                u'''of moderate bitterness such as Newcastle Brown Ale and '''
                u'''malty but hoppy beers such as Sierra Nevada Brown Ale.'''),
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
                u'''Classic English Pale Ales are not pale but rather are '''
                u'''golden to copper colored and display English variety '''
                u'''hop character. Distinguishing characteristics are '''
                u'''dryness and defined hop taste, but more malt balance '''
                u'''than what you’ll typically find in an American Pale '''
                u'''Ale. Great to drink with all sorts of meats including '''
                u'''roast beef, lamb, burgers, duck, goose, etc. Note that '''
                u'''the term ’pale ale’ is used in England to signify a '''
                u'''bottled bitter, and in that way there is no such thing '''
                u'''as ’English Pale Ale’ to the English. The style is a '''
                u'''North American construct, borne of the multitude of '''
                u'''pale ales that pay homage to these bottled bitters - '''
                u'''Bass in particular - and therefore the majority of true '''
                u'''examples of the style are found outside Britain.'''),
            'parent_id': 3
        },
        {
            'id': 30,
            'name': u'English Strong Ale',
            'description': (
                u'''Malty, with complex fruity esters. Some oxidative notes '''
                u'''are acceptable, akin to those found in port or sherry. '''
                u'''Hop aromas not usually present, due to extended age. '''
                u'''Medium amber to very dark red-amber color. Malty and '''
                u'''usually sweet. Alcoholic strength should be evident, '''
                u'''though not overwhelming. Medium to full body alcohol '''
                u'''should contribute some warmth. An ale of significant '''
                u'''alcoholic strength, though usually not as strong or '''
                u'''rich as barleywine. Usually tilted toward a sweeter, '''
                u'''more malty balance. Often regarded as winter warmers, '''
                u'''and often released as seasonal beers.'''),
            'parent_id': 3
        },
        {
            'id': 31,
            'name': u'Golden Ale/Blond Ale',
            'description': (
                u'''There are a few different types of blond ale. The first '''
                u'''is the traditional "Canadian Ale", an adjunct-laden, '''
                u'''macrobrewed, top-fermented equivalent of the American '''
                u'''Standard. The second is common in US brewpubs - a light '''
                u'''starter ale, with marginally more hop and body than a '''
                u'''macrobrew, fewer adjuncts, but still not a flavourful '''
                u'''beer by any means. The British interpretation is easily '''
                u'''the boldest, hoppiest blond ale rendition. Some of '''
                u'''these can almost be considered American Pales they are '''
                u'''so hopped up - very crisp, refreshing, with relatively '''
                u'''low alcohol compared with their North American '''
                u'''counterparts.'''),
            'parent_id': 3
        },
        {
            'id': 32,
            'name': u'Imperial IPA',
            'description': (
                u'''Imperial IPA (also called Double or Triple IPA) is a '''
                u'''strong, often sweet, intensely hoppy version of the '''
                u'''traditional India Pale Ale. Bitterness units range tend '''
                u'''to be 100 IBUs and above. The ABV level for DIPAs '''
                u'''generally begins at 7.5% but is more commonly in the '''
                u'''8.0%+ range. The flavour profile is intense all around. '''
                u'''Unlike barley wines, the balance is heavily towards the '''
                u'''hops, with crystal and other malts providing support.'''),
            'parent_id': 3
        },
        {
            'id': 33,
            'name': u'India Pale Ale (IPA)',
            'description': (
                u'''India Pale Ale, the modern version of which has largely '''
                u'''been formed in the US, has an intense hop flavor, a '''
                u'''golden to copper color, and a medium malty body. The '''
                u'''aroma is moderate to very strong. IPAs work especially '''
                u'''well at cutting the heat of chili, vindaloo or Sichuan '''
                u'''cuisine. In England, IPA is often just another name for '''
                u'''bitter although some micros are doing their own '''
                u'''versions of an American IPA as well.'''),
            'parent_id': 3
        },
        {
            'id': 34,
            'name': u'Irish Ale',
            'description': (
                u'''The red ales of Ireland have a gentle maltiness, '''
                u'''caramelly, earthy notes, and a generally restrained hop '''
                u'''character.  They are session ales, so alcohol is '''
                u'''generally at 5% abv or less, though you will find the '''
                u'''occasion stronger example. The major macrobrewed Irish '''
                u'''ales are ascribed to be in this style, but the majority '''
                u'''of examples are from New World microbreweries working '''
                u'''with Michael Jackson’s description of Irish ale.'''),
            'parent_id': 3
        },
        {
            'id': 35,
            'name': u'Kölsch',
            'description': (
                u'''Golden, top-fermented style native to Köln, Germany. '''
                u'''The style has a very narrow profile and many beers that '''
                u'''consider themselves to be kölschbiers are not. '''
                u'''Generally they have a moderate bitterness, but fairly '''
                u'''prominent hop flavour (typically Spalt, Tettnang or '''
                u'''    Hallertau). They have high effervescence, medium '''
                u'''esters, but a rounded, stylish character derived from '''
                u'''lagering.'''),
            'parent_id': 3
        },
        {
            'id': 36,
            'name': u'Mild Ale',
            'description': (
                u'''Malt accented, typically little or no hop flavour or '''
                u'''aroma. Usually medium to dark brown in colour though '''
                u'''many English examples are almost black with caramel '''
                u'''often added for colouring as well as favouring '''
                u'''purposes. Mild refers to no or limited hop '''
                u'''bitterness/ aroma. Still very popular in the '''
                u'''North- West and Midland areas of England where it is '''
                u'''usually between 3 to 4% ABV and preferred with a good '''
                u'''head. There are examples of stronger versions of the '''
                u'''style, but rarely over 5-6%.'''),
            'parent_id': 3
        },
        {
            'id': 37,
            'name': u'Old Ale',
            'description': (
                u'''Old Ale is a simple enough style to figure out. At '''
                u'''least, once you understand that there are three or four '''
                u'''beer styles called Old Ale. The first is the best known '''
                u'''- the strong dark Old Peculier style. The second type '''
                u'''of Old Ale is a blended dark ale. At least one of the '''
                u'''beers comprising the blend will be aged for a couple of '''
                u'''years in wood casks. The third version of Old Ale is a '''
                u'''form of mild – a low-gravity dark ale. Another version '''
                u'''of Old Ale is closely related to the first. For me, '''
                u'''these are robustly malty beers, akin to a top-fermented '''
                u'''version of a doppelbock.'''),
            'parent_id': 3
        },
        {
            'id': 38,
            'name': u'Premium Bitter/ESB',
            'description': (
                u'''In England, many breweries have a number of bitters in '''
                u'''their range. The style that has come to be known as '''
                u'''Premium or Special Bitter generally includes the '''
                u'''stronger (4.6%-6.0%) examples. These are mostly served '''
                u'''in the traditional way from the cask, but some are also '''
                u'''found in bottle form where the extra malt allows them '''
                u'''to stand up better than the more delicate ordinary '''
                u'''Bitter. In the US, the designation ESB is common for '''
                u'''this style, owing to the influence of Fuller’s ESB, the '''
                u'''London brew that was among the first to be exported to '''
                u'''the States. In the US, some ESBs are made with American '''
                u'''hops and a clean yeast, but the alcohol range is the '''
                u'''same, as is the range of bitterness, usually between 25 '''
                u'''and 35 but occasionally creeping higher.'''),
            'parent_id': 3
        },
        {
            'id': 39,
            'name': u'Scotch Ale',
            'description': (
                u'''Scotch Ale was the name given to a strong pale ale from '''
                u'''Edinburgh in the 19th century. This was typical of the '''
                u'''strong pale ales brewed in Britain at that time - '''
                u'''mainly pale barley malt and moderate hopping, and were '''
                u'''not that stylistically different to English Strong Ales '''
                u'''or Barley Wines. The name however became regionalised '''
                u'''so that a strong pale ale from Scotland became known as '''
                u'''a Scotch Ale or Wee Heavy. Beers using the designation '''
                u'''Scotch Ale are popular in the USA where most examples '''
                u'''are brewed locally. Examples of beers brewed in the USA '''
                u'''under the name Wee Heavy tend to be 7% abv and higher, '''
                u'''while Scottish brewed examples, such as Belhavens Wee '''
                u'''Heavy, are typically between 5.5% and 6.5% abv.'''),
            'parent_id': 3
        },
        {
            'id': 40,
            'name': u'Scottish Ale',
            'description': (
                u'''Scottish ales are generally dark, malty, full-bodied '''
                u'''brews. Many examples have a hint of smokiness derived '''
                u'''from the use of peated malt. 60, 70, and 80 shilling '''
                u'''examples are all session ales under 5% abv, but the '''
                u'''stronger "wee heavies" can range closer to 8%, with '''
                u'''the accompanying increase in alcohol flavour and '''
                u'''esters. Works well as an accompaniment to hearty meat '''
                u'''and game dishes, sharp cheddar, atholl brose and '''
                u'''shortbread.'''),
            'parent_id': 3
        },
        {
            'id': 41,
            'name': u'Session IPA',
            'description': (
                u'''he term Session IPA describes a category of beers '''
                u'''arketed for their hop-dominant flavor profiles at '''
                u'''sessionable" levels of alcohol. While this is '''
                u'''ypically 3.2 - 4.6 percent alcohol, a few have '''
                u'''tretched the definition. This class of beers arose in '''
                u'''010 out of the Craft Beer Tradition as a reaction to '''
                u'''he trend of increasingly strong beers and greater '''
                u'''ublic appreciation for hoppier profiles around the '''
                u'''lobe. It is differentiated from American Pale Ale by '''
                u'''ypically being lower in alcohol and usually having '''
                u'''ore hop-dominant profiles. While hops used are '''
                u'''ypically American Pacific Northwest and New Zealand, '''
                u'''roprietary/experimental and South African and other '''
                u'''ops may also factor into a Session IPA hop bill.'''),
            'parent_id': 3
        },
        {
            'id': 42,
            'name': u'Baltic Porter',
            'description': (
                u'''The historical remnants of the 19th c. Baltic trade in '''
                u'''imperial stouts, Baltic Porters are typically strong, '''
                u'''sweet and bottom-fermented. They lack the powerful '''
                u'''roast of an imperial stout, but have an intense malt '''
                u'''character, and moderate to strong alcohol. Though they '''
                u'''are typically lagers, there are a handful of '''
                u'''top-fermented examples.'''),
            'parent_id': 4
        },
        {
            'id': 43,
            'name': u'Black IPA',
            'description': (
                u'''An emerging beer style roughly defined as a beer with '''
                u'''IPA-level hopping relatively high alcohol and a '''
                u'''distinct toasty dark malt character. Typically lacks '''
                u'''the roastiness and body of a strong stout and is '''
                u'''hoppier than a strong porter. Expressive dry-hopping is '''
                u'''common. Also called India Dark Ale, India Black Ale, '''
                u'''Cascadian Dark Ale, Dark IPA and sometimes India Brown '''
                u'''Ale.'''),
            'parent_id': 4
        },
        {
            'id': 44,
            'name': u'Dry Stout',
            'description': (
                u'''The "Irish-style" stout is typically a low-gravity '''
                u'''stout with bitterness ranging between 30-45 IBUs. '''
                u'''Roastiness is present, but restrained, and there should '''
                u'''not be hops in either the flavour or aroma. A little '''
                u'''bit of acidity can be present. Often, this type of '''
                u'''stout is serving via nitrogen, with all the effects '''
                u'''that has on a beer - low carbonation, extra-thick head, '''
                u'''lifeless palate and muted flavour and aroma.'''),
            'parent_id': 4
        },
        {
            'id': 45,
            'name': u'Foreign Stout',
            'description': (
                u'''Foreign Stout began with the beer that would become '''
                u'''Guinness Foreign Extra Stout. This was a stronger, '''
                u'''extra-hopped version of the basic Guinness Extra Stout, '''
                u'''brewed to survive long journeys overseas. The classic '''
                u'''FES still exists in a few different forms, but many of '''
                u'''the original destination countries (Jamaica, Sri Lanka, '''
                u'''etc.) now have their own, locally-produced versions. '''
                u'''Foreign stout occupies a position between basic stout '''
                u'''and imperial stout. It is sweeter than a basic stout, '''
                u'''but not as robust as an imperial. It is less fruity and '''
                u'''less hoppy as well. Foreign stouts are sometimes made '''
                u'''with local grains and adjuncts – sugar is not uncommon. '''
                u'''Alcohol ranges from 6-8%.'''),
            'parent_id': 4
        },
        {
            'id': 46,
            'name': u'Imperial Porter',
            'description': (
                u'''Imperial (extra-strong) porters fall in between the '''
                u'''traditional porter, a Baltic porter, and an imperial '''
                u'''stout.  They range from around 7.5% upwards, with hefty '''
                u'''dark malt character, but lack the overt roastiness of '''
                u'''an imperial stout.'''),
            'parent_id': 4
        },
        {
            'id': 47,
            'name': u'Imperial Stout',
            'description': (
                u'''Imperial stouts are usually extremely dark brown to '''
                u'''black in color with flavors that are intensely malty, '''
                u'''deeply roasted and sometimes with accents of dark fruit '''
                u'''(raisin, fig) and chocolate. The bitterness is '''
                u'''typically low to moderate. Imperial stouts are strong '''
                u'''and generally exceed 8% ABV.'''),
            'parent_id': 4
        },
        {
            'id': 48,
            'name': u'Porter',
            'description': (
                u'''Black or chocolate malt gives the porter its dark brown '''
                u'''color. Porters are often well hopped and somewhat '''
                u'''heavily malted. This is a medium-bodied beer and may '''
                u'''show some sweetness usually from the light caramel to '''
                u'''light molasses range. Hoppiness can range from bitter '''
                u'''to mild. Porters, in relation to stouts of the same '''
                u'''region, are typically more mild and less aggressively '''
                u'''hopped.'''),
            'parent_id': 4
        },
        {
            'id': 49,
            'name': u'Stout',
            'description': (
                u'''A stout is made with dark roasted malts which results '''
                u'''in a dark color and a roasted malt flavor. In mainland '''
                u'''Europe they are usually termed "noir" (black). The word '''
                u'''stout means strong, and was applied to strong Porter in '''
                u'''the 18th century - most typically by Guinness, who were '''
                u'''one of the few breweries to continue making such beers '''
                u'''into the 20th century. Guinness is today the template '''
                u'''for Irish or Dry Stout. Other stout variations are '''
                u'''Imperial Stout, Foreign Stout, and Sweet or Milk Stout '''
                u'''- as well as Porter, Imperial Porter, and Baltic Porter '''
                u'''- and the related Mild and Schwarzbier.'''),
            'parent_id': 4
        },
        {
            'id': 50,
            'name': u'Sweet Stout',
            'description': (
                u'''Dark brown to black in colour. Sweet stouts come in two '''
                u'''main varieties - milk stout and oatmeal stout. Milk '''
                u'''stouts are made with the addition of lactose, and are '''
                u'''sweet and generally low in alcohol. Oatmeal lends a '''
                u'''smooth fullness of body to stouts. All of the sweet '''
                u'''stouts are noted for their restrained roastiness in '''
                u'''comparison with other stouts, and their low hop '''
                u'''levels.'''),
            'parent_id': 4
        },
        {
            'id': 51,
            'name': u'Dunkelweizen',
            'description': (
                u'''A dark take on the German wheat theme, dunkelweizens '''
                u'''have the same banana and clove notes of their pale '''
                u'''cousins, but also have earthy, toasty, chocolatey notes '''
                u'''from the addition of dark malts. They are "shoulder '''
                u'''season" wheat beers to many drinkers - something a '''
                u'''little more robust than a hefeweizen for the fall and '''
                u'''spring seasons, but not as rich as winter’s '''
                u'''weizenbocks. Alcohol is between 4.8-5.6% generally, '''
                u'''bitterness is low, and carbonation is high. '''
                u'''Occasionally, you will see dark versions of American '''
                u'''Wheats, but these are uncommon.'''),
            'parent_id': 5
        },
        {
            'id': 52,
            'name': u'German Hefeweizen',
            'description': (
                u'''Depending on the style can range from pale and light '''
                u'''body to dark brown with full body. Wheat beer is '''
                u'''characterized by its cloudy appearance and its banana '''
                u'''and sometimes vanilla aftertaste.'''),
            'parent_id': 5
        },
        {
            'id': 53,
            'name': u'German Kristallweizen',
            'description': (
                u'''Kristalweizens are the third member of the German Wheat '''
                u'''trifecta. Derided by many beer lovers as “castrated '''
                u'''hefeweizens”, kristalweizens are known for their '''
                u'''filtered, sparkling colour. They have the classic '''
                u'''spritzy carbonation of wheat beers, and the same tart '''
                u'''wheat notes and signature components of banana, '''
                u'''bubblegum and spice. The body is light, and alcohol '''
                u'''ranging around the 5% mark, give or take half a '''
                u'''point.'''),
            'parent_id': 5
        },
        {
            'id': 54,
            'name': u'Grodziskie/Gose/Lichtenhainer',
            'description': (
                u'''Sour wheat beers were common in many parts of medieval '''
                u'''and early Industrial Europe. Two styles – lambic and '''
                u'''Berliner weisse – survived, but many others did not. '''
                u'''Gose and Lichtenhainer are historic styles of sour '''
                u'''wheat beer.  Grodzisk is sometimes tart, sometimes not. '''
                u'''Gose is seasoned with salt, Grodziskie and '''
                u'''Lichtenhainer contain smoked malt. Historical sources '''
                u'''are mixed about Lichtenhainer containing wheat, so '''
                u'''modern interpretations may vary. Grätzer is an '''
                u'''alternative name for Grodziskie. All three will be '''
                u'''relatively low alcohol, with a strong wheat character, '''
                u'''but will be distinct from classic examples of Berliner '''
                u'''Weisse or lambic. As all we have are historical '''
                u'''recreations, substantial differences may exist between '''
                u'''interpretations.'''),
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
                u'''Golden to light amber in color, the body is light to '''
                u'''medium. The wheat lends a crispness to the brew, often '''
                u'''with some acidity. Some hop flavour may be present, but '''
                u'''bitterness is low.  Not as estery as German or '''
                u'''Belgian-style wheats.'''),
            'parent_id': 5
        },
        {
            'id': 57,
            'name': u'Witbier',
            'description': (
                u'''Witbier, also known as Belgian White, is a style of '''
                u'''Belgian-style wheat beers that are generally pale and '''
                u'''opaque with a crisp wheat character and citric '''
                u'''refreshment of orange peel and coriander. Ingredients '''
                u'''sometimes include oats for smoothness, and other spices '''
                u'''such as grains of paradise. Serve with light cheeses or '''
                u'''mussels.'''),
            'parent_id': 5
        },
        {
            'id': 58,
            'name': u'Amber Lager/Vienna',
            'description': (
                u'''Your typical macrobrewed Dark Lager, often rendered '''
                u'''dark with either brewer’s caramel or black patent malt, '''
                u'''but each brewery will have a different approach. Aside '''
                u'''from caramelly notes, these beers will not typically '''
                u'''resemble other dark lager styles so much as they do the '''
                u'''lighter styles, due to low amounts of hops, malt and '''
                u'''body. Vienna as a beer style was theorized by Michael '''
                u'''Jackson, but his oft-cited example was Negra Modelo, '''
                u'''which is a macro dark lager like all the others. Some '''
                u'''beers have taken on the idea of a Vienna lager as a '''
                u'''distinct style, loosely based on the 1840 Anton Dreher '''
                u'''beer, and these can be expected to be all-malt, with a '''
                u'''fuller body and more character than the average macro '''
                u'''dark.'''),
            'parent_id': 6
        },
        {
            'id': 59,
            'name': u'California Common',
            'description': (
                u'''Style originating in 18th century California, where '''
                u'''brewers with out access to refrigeration produced beers '''
                u'''using lager yeasts and warm temperatures. These still '''
                u'''retain some of the rounded character inherent in all '''
                u'''lagers, but with a dose of ale fruitiness.'''),
            'parent_id': 6
        },
        {
            'id': 60,
            'name': u'Czech Pilsner (Světlý)',
            'description': (
                u'''Hallmarked by the generous use of the Saaz hop, '''
                u'''Bohemian or Czech pilsners are also noted for their '''
                u'''rich gold color, fat maltiness and moderate to full '''
                u'''body. Generally brewed to 10-12° Plato. in Czech these '''
                u'''beers are simply called Světlý Ležák. Sometimes served '''
                u'''cloudy and unfiltered with young wort mixed in, known '''
                u'''as Kvasnicova in the Czech Republic, the same as what '''
                u'''is known as krausening in Germany. Regardless of '''
                u'''origin, to be a pilsner a beer must have at least 28 '''
                u'''units of bitterness, and preferably much more.'''),
            'parent_id': 6
        },
        {
            'id': 61,
            'name': u'Doppelbock',
            'description': (
                u'''Doppel means double and while these are stronger brews '''
                u'''than the traditional German bocks, they are typically '''
                u'''not twice the strength. Color is light amber to dark '''
                u'''brown. Very full body with a high alcoholic flavor. Low '''
                u'''hop flavor and aroma.'''),
            'parent_id': 6
        },
        {
            'id': 62,
            'name': u'Dortmunder/Helles',
            'description': (
                u'''These two styles are closely related, the former '''
                u'''hailing from Dortmund and the latter from Bavaria. Both '''
                u'''are slightly strong (5.0-5.6%), malt-accented pale '''
                u'''lagers. The cookie-like or bready maltiness should be '''
                u'''very much in evidence in a traditional example. These '''
                u'''beers are clean and easy to drink in quantity. Some '''
                u'''Dortmunders made in Denmark and the Netherlands are '''
                u'''stronger.'''),
            'parent_id': 6
        },
        {
            'id': 63,
            'name': u'Dunkel/Tmavý',
            'description': (
                u'''Copper to dark brown lager common in Germany and the '''
                u'''Czech Republic but made worldwide. Medium body. Nutty '''
                u'''toasted chocolate-like malty sweetness in aroma and '''
                u'''flavor. Medium bitterness. Low "noble-type" hop flavor '''
                u'''and aroma. In both Germany and Czech dark lagers span a '''
                u'''wide range of characters from sweet to dry forming more '''
                u'''of a category than a specific style with considerable '''
                u'''leeway for the brewer with regards to the character of '''
                u'''the beer. This is the biggest reason why they are group '''
                u'''ed together despite coming from different traditions '''
                u'''and each being made with local ingredients.'''),
            'parent_id': 6
        },
        {
            'id': 64,
            'name': u'Dunkler Bock',
            'description': (
                u'''The dark Bock has a deep copper to dark brown color. '''
                u'''Medium to full-bodied, malt sweetness and nutty or '''
                u'''light toasted flavors dominate. Hop flavor and aroma '''
                u'''can be light to non-existent.'''),
            'parent_id': 6
        },
        {
            'id': 65,
            'name': u'Eisbock',
            'description': (
                u'''A stronger version of Doppelbock. Deep copper to black. '''
                u'''Very alcoholic. Typically brewed by freezing a '''
                u'''doppelbock and removing resulting ice to increase '''
                u'''alcohol content.'''),
            'parent_id': 6
        },
        {
            'id': 66,
            'name': u'Heller Bock',
            'description': (
                u'''The Heller Bock is primarily a malty beer from the '''
                u'''German brewing tradition with little hop character - '''
                u'''neither bitter nor aromatic - though the style '''
                u'''typically has a little more hops than the standard '''
                u'''Bock. The color is golden to light brown or amber. They '''
                u'''should normally pour with a substantial white head. '''
                u'''Typical examples are pale and clear.'''),
            'parent_id': 6
        },
        {
            'id': 67,
            'name': u'Imperial Pils/Strong Pale Lager',
            'description': (
                u'''A catch-all for strong, sometimes hoppy lagers that '''
                u'''range from modern versions of "Imperial Pilsner", to '''
                u'''more traditional strong lagers which are more common in '''
                u'''Eastern Europe. These are essentially stronger versions '''
                u'''of pilsners, though the increased malt and alcohol will '''
                u'''noticeably reduce the hop accent. Because these are '''
                u'''usually all-malt, and comfortably hopped, they are '''
                u'''easily distinguishable from malt liquors. With out the '''
                u'''malt character of bocks, these are worthy of a style '''
                u'''all their own.'''),
            'parent_id': 6
        },
        {
            'id': 68,
            'name': u'Malt Liquor',
            'description': (
                u'''Strong, alcoholic-tasting, often poorly made strong '''
                u'''lagers.  Esters, fusels and other products of undiluted '''
                u'''high-gravity brewed beers are often commonplace. Proper '''
                u'''ly served in the 40oz bottle with accompanying brown '''
                u'''paper bag.'''),
            'parent_id': 6
        },
        {
            'id': 69,
            'name': u'Oktoberfest/Märzen',
            'description': (
                u'''Oktoberfest is a German festival dating from 1810, and '''
                u'''Oktoberfestbiers are the beers that have been served at '''
                u'''the festival since 1818, and are supplied by 6 '''
                u'''breweries: Spaten, Lowenbrau, Augustiner, Hofbrau, '''
                u'''Paulaner and Hacker-Pschorr. Traditionally '''
                u'''Oktoberfestbiers were the lagers of around 5.5 to 6 abv '''
                u'''called Marzen - brewed in March and allowed to ferment '''
                u'''slowly during the summer months. Originally these would '''
                u'''have been dark lagers, but from 1872 a strong March '''
                u'''brewed version of an amber-red Vienna lager made by '''
                u'''Josef Sedlmayr became the favourite Oktoberfestbier. '''
                u'''Since the 1990s European brewed versions have tended to '''
                u'''be golden in colour, while American versions have '''
                u'''remained dark or amber.'''),
            'parent_id': 6
        },
        {
            'id': 70,
            'name': u'Pale Lager',
            'description': (
                u'''The color of pale lager ranges from light bronze to '''
                u'''nearly transparent and the alcohol anywhere from 4-6%. '''
                u'''Adjunct usage may be quite high, though in some cases '''
                u'''the beer is all-malt. Carbonation is typically forced, '''
                u'''though not always. One thing that does not vary is that '''
                u'''neither the malt nor the hops make much of an '''
                u'''impression on the palate. These beers are brewed for '''
                u'''minimum character, though faint traces of hop or malt '''
                u'''may show through.  Commonly detected features and flaws '''
                u'''include fusels, oxidized malt and skunked hops. The '''
                u'''body will often be thin and/or spritzy while the finish '''
                u'''is typically mildly bitter.'''),
            'parent_id': 6
        },
        {
            'id': 71,
            'name': u'Pilsener',
            'description': (
                u'''While the definition of pilsner is open to much debate '''
                u'''in the beer community, it generally refers to pale, '''
                u'''hoppy lagers, ranging from ~30 IBU and up. From Classic '''
                u'''German Pilsners, which tend to be light-to-medium '''
                u'''bodied, semi-sweet to off-dry, hopped with German noble '''
                u'''hops, to New World artisan renditions in North America, '''
                u'''New Zealand and elsewhere, which showcase modern hop '''
                u'''strains. A separate style category is maintained for '''
                u'''Czech Pilsner (Světlý Ležák).'''),
            'parent_id': 6
        },
        {
            'id': 72,
            'name': u'Polotmavý',
            'description': (
                u'''This is the amber lager style of the Czech Republic. '''
                u'''The character that the brewery usually aims for with '''
                u'''this style is a hybrid between the dark lager and the '''
                u'''pale pilsner. The result has a richer malt character '''
                u'''than the American Dark/Amber Lager/Vienna style and '''
                u'''more hop than the Oktoberfest/Marzen style.'''),
            'parent_id': 6
        },
        {
            'id': 73,
            'name': u'Premium Lager',
            'description': (
                u'''A beer that straddles between the mainstream Pale Lager '''
                u'''and Pilsner. Not all beers that call themselves Premium '''
                u'''Lager are, but those that are will typically have a '''
                u'''deep gold to light bronze colour, and distinct '''
                u'''influence of malt and hops. They should be free of '''
                u'''adjuncts and will have a softer carbonation than Pale '''
                u'''Lager or Classic German Pilsner. IBUs will typically '''
                u'''range in the 20’s, and lagering times will typically '''
                u'''be 4-6 weeks, more in line with what pilsners have. '''
                u'''Overall accent will be malty-to-balanced, alcohol in a '''
                u'''slightly tighter range than either Pale Lager or '''
                u'''Pilsner (4.5-5.5%). Most often the product of a '''
                u'''microbrewery or brewpub, but macrobreweries can make '''
                u'''this style if they jack up the hops a bit and make it '''
                u'''all-malt.'''),
            'parent_id': 6
        },
        {
            'id': 74,
            'name': u'Radler/Shandy',
            'description': (
                u'''A mix of a sweet soft drink or juice -- typically lemon '''
                u'''or ginger but sometimes apple, grapefruit or other '''
                u'''fruit -- and beer, often in equal parts, that is '''
                u'''moderately sweet, thirst quenching, low in alcohol with '''
                u'''medium to spritzy carbonation. Often but not '''
                u'''necessarily sold as a Summer seasonal. Category '''
                u'''includes such regional styles as diesel (beer and '''
                u'''cola), cola-weizen (wheat beer and cola), and russ’n.'''),
            'parent_id': 6
        },
        {
            'id': 75,
            'name': u'Schwarzbier',
            'description': (
                u'''Dark brown to black. Medium body. Roasted malt evident. '''
                u'''Low sweetness in aroma and flavor. Low to medium '''
                u'''bitterness. Low bitterness from roast malt. Hop flavor '''
                u'''and aroma, "noble-type" OK. No fruitiness, esters.'''),
            'parent_id': 6
        },
        {
            'id': 76,
            'name': u'Zwickel/Keller/Landbier',
            'description': (
                u'''Three related lager styles most common in Franconia. '''
                u'''Essentially, these are hoppier versions of a helles, '''
                u'''served with natural carbonation and unfiltered - they '''
                u'''are the lager world’s answer to real ale. Kellerbier '''
                u'''will on average be hoppier than zwickelbier. There is '''
                u'''also Landbier, which is more malt-accented, may be '''
                u'''filtered, but is similarly lacking in carbonation. '''
                u'''Gravity is standard, low to moderate hop rates, the '''
                u'''colour from pale to reddish-amber and the palate should '''
                u'''be balanced with a hop accent. Zoiglbier, common to '''
                u'''Oberpfalz, is also included in this category.'''),
            'parent_id': 6
        },
    )

    for c in categories:
        category = Category(id=c['id'], name=c['name'])
        if 'description' in c.keys():
            category.description = c['description']
        if 'parent_id' in c.keys():
            parent = session.query(Category).filter_by(id=c['parent_id']).one()
            category.parent_id = parent.id
        session.add(category)

    session.commit()

if len(session.query(Item).all()) == 0:
    items = (
        {
            'id': 1,
            'name': u'Westmalle Dubbel',
            'description': (
                u'''A reddish brown trappist ale, malty and fruit, '''
                u'''featuring a 3 week secondary fermentation. This ale has '''
                u'''a full, pale yellow head. The bouquet is full of esters '''
                u'''and fruitiness. Notes of ripe banana predominate. The '''
                u'''taste is fruity and slightly bitter, with a long, dry '''
                u'''finish.'''),
            'category_id': 7,
            'user_id': 1
        },
        {
            'id': 2,
            'name': u'Tripel Karmeliet',
            'description': (
                u'''First brewed 1996; claimed to be based on a recipe from '''
                u'''1679 which used wheat, oat and barley. Tripel Karmeliet '''
                u'''is a very refined and complex golden-to-bronze brew '''
                u'''with a fantastic creamy head. These characteristics '''
                u'''derive not only from the grains used but also from '''
                u'''restrained hopping with Styrians and the fruity nature '''
                u'''(banana and vanilla) of the house yeast. Aroma has '''
                u'''hints of vanilla mixed with citrus aromas. Tripel '''
                u'''Karmeliet has not only the lightness and freshness of '''
                u'''wheat, but also the creaminess of oats together with a '''
                u'''spicy lemony almost quinine dryness.'''),
            'category_id': 8,
            'user_id': 1
        },
        {
            'id': 3,
            'name': u'Westmalle Tripel',
            'description': (
                u'''A strong, dry and spicy trappist ale. The product of a '''
                u'''secondary fermentation lasting 5 weeks. This is a '''
                u'''complex ale with a fruity aroma and a nice nuanced hop '''
                u'''scent. It is soft and creamy in the mouth, with a '''
                u'''bitter touch carried by the fruity aroma. An '''
                u'''exceptional ale, with a great deal of finesse and '''
                u'''elegance, and with a splendid long after taste.'''),
            'category_id': 8,
            'user_id': 1
        },
        {
            'id': 4,
            'name': u'Orval',
            'description': (
                u'''In contrast to all the others, the Orval Trappist '''
                u'''brewery makes only one beer for the general public. It '''
                u'''has an intensely aromatic and dry character. Between '''
                u'''the first and second fermentations there is also an '''
                u'''additional dry-hopping process.  Through this the beer '''
                u'''acquires its pronounced hoppy aroma and extra dry '''
                u'''taste.  Bottled at 5.2% abv - can go up as high as '''
                u'''7.2%'''),
            'category_id': 10,
            'user_id': 1
        },
        {
            'id': 5,
            'name': u'Westvleteren Blond',
            'description': (
                u'''Westvleteren Blond is the basic beer for the monks' own '''
                u'''consumption, since 1999, when the former 6° dark ale '''
                u'''(red cap) was finally discarded, after the 4° had '''
                u'''already gone that path.'''),
            'category_id': 10,
            'user_id': 1
        },
        {
            'id': 6,
            'name': u'Toppling Goliath Kentucky Brunch',
            'description': (
                u'''This beer is the real McCoy. Barrel aged and crammed '''
                u'''with coffee, none other will stand in it’s way. Sought '''
                u'''out for being delicious, it is notoriously difficult to '''
                u'''track down. If you can find one, shoot to kill, because '''
                u'''it is definitely wanted... dead or alive.'''),
            'category_id': 47,
            'user_id': 1
        },
        {
            'id': 7,
            'name': u'''Toppling Goliath Mornin' Delight''',
            'description': (
                u'''A huge Imperial Stout with an explosive espresso aroma '''
                u'''followed by strong notes of maple syrup and vanilla.'''),
            'category_id': 47,
            'user_id': 1
        },
        {
            'id': 8,
            'name': (
                u'''Cigar City Hunahpu's Imperial Stout - Double Barrel '''
                u'''Aged'''),
            'description': (
                u'''50% aged in Rum barrels, 50% aged in Apple Brandy '''
                u'''barrels'''),
            'category_id': 47,
            'user_id': 1
        },
        {
            'id': 9,
            'name': (
                u'''Three Floyds Dark Lord Russian Imperial Stout (Bourbon '''
                u'''Barrel Aged)'''),
            'description': (
                u'''Dark Lord aged in a variety of Bourbon barrels '''
                u'''including Woodford Reserve and Heaven Hill. This '''
                u'''listing is specifically for Bourbon barrel aged '''
                u'''variants of Dark Lord. NOT Brandy.'''),
            'category_id': 47,
            'user_id': 1
        },
        {
            'id': 10,
            'name': u'''Emelisse White Label Barley Wine (Heaven Hill BA)''',
            'description': '',
            'category_id': 25,
            'user_id': 1
        },
        {
            'id': 11,
            'name': u'''De Molen Hel & Verdoemenis 666''',
            'description': (
                u'''Batch 666 was H&V with added wood chips soaked in a 40 '''
                u'''year old cognac.'''),
            'category_id': 47,
            'user_id': 1
        },
    )

    for i in items:
        item = Item(id=i['id'], name=i['name'],
                    description=i['description'], category_id=i['category_id'])
        session.add(item)

    session.commit()
