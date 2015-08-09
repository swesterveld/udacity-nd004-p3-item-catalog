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
        'description': u'''These are dark, malty, yeasty strong ales in the Trappist tradition, but produced (mainly) by secular brewers. Dubbels range between 6.5-8% abv, and have a dark brown, cloudy colour, and a palate mixing malt, a lush fruitiness, and yeast. They are typically bottle-conditioned.''',
        'parent_id': 1
    },
    {
        'id': 8,
        'name': u'Abbey Tripel',
        'description': u'''Like other abbey ales, Tripels are strong, yeasty-malty beers. But they are also pale, and have a notable hop profile. Hop bitterness may be higher than a typical abbey ale, up to 45IBUs. But the finish is where the hops really shine, as tripels should finish fairly dry. Otherwise, maltiness is still essential to the style, and the assertive yeast note typical of all abbey ales will be more apparent in tripels, since they do not have the rich dark malts to distract the palate. Alcohol flavours feature more prominently in Tripels that in just about any other style.''',
        'parent_id': 1
    },
    {
        'id': 9,
        'name': u'Abt/Quadrupel',
        'description': u'''Belgian-style ales seldom fit neatly into classic beer styles, but this category represents those ales under approximately 7% abv that do not fit other categories. Colour ranges from golden to deep amber, with the occasional example coming in darker. Body tends to be light to medium, with a wide range of hop and malt levels. Yeastiness and acidity may also be present.''',
        'parent_id': 1
    },
    {
        'id': 10,
        'name': u'Belgian Ale',
        'description': u'''Belgian Strong Ales can vary from pale to dark brown in color, darker ales may be colored with dark candy sugar. Hop flavor can range from low to high, while hop aroma is low. The beers are medium to full-bodied and have a high alcoholic character. Types of beers included here include tripels, dubbels and ultra-strong abbey ales.''',
        'parent_id': 1
    },
    {
        'id': 11,
        'name': u'Belgian Strong Ale',
        'description': u'''Belgian Strong Ales can vary from pale to dark brown in color, darker ales may be colored with dark candy sugar. Hop flavor can range from low to high, while hop aroma is low. The beers are medium to full-bodied and have a high alcoholic character. Types of beers included here include tripels, dubbels and ultra-strong abbey ales.''',
        'parent_id': 1
    },
    {
        'id': 12,
        'name': u'Bière de Garde',
        'description': u'''A traditional classification for the farmhouse ales of France and their sometimes-untraditional new-world counterparts. Bière de Garde is today generally a warm fermented strong pale ale - sometimes blonde, sometimes amber, and has much in common with Belgium ales. Medium bodied with hints of caramel or toffee. Cellared smell and flavor are characteristics. The name means "beer for keeping".''',
        'parent_id': 1
    },
    {
        'id': 13,
        'name': u'Saison',
        'description': u'''Fruity esters dominate the aroma. Clarity is good with a large foamy head on top. The addition of several spices and herbs create a complex fruity or citrusy flavor. Light to medium bodied with very high carbonation. Alcohol level is medium to high.''',
        'parent_id': 1
    },
    {
        'id': 14,
        'name': u'Berliner Weisse',
        'description': u'''Very wheaty, very sour style of Berlin. Berliner weissebier has a barely perceptible hop content, low alcohol, and a sharp character. Often these are laced with syrups to cut the intense acidity, but purists will want to take them neat to enjoy the multi-faceted complexity and thirst-quenching character.''',
        'parent_id': 2
    },
    {
        'id': 15,
        'name': u'Lambic Style - Faro',
        'description': u'''Faro is a lambic blend with the addition of sugar. These are well-carbonated, and are sweeter and more refreshing than gueuze. The flavour is often straightforward and sugary, with lighter barnyard and funk notes than other lambic styles. The odd variant contains other spices like orange peel as flavouring.''',
        'parent_id': 2
    },
    {
        'id': 16,
        'name': u'Lambic Style - Fruit',
        'description': u'''Lambics are wheat beers made with stale hops and fermented with wild yeasts and other microorganisms traditionally only on the Senne Valley in and around Brussels. The most traditional of the fruit lambics are kriek (cherry) and framboise (raspberry). In modern times peaches (peche) blackcurrants (cassis) grapes as well as more exotic fruits are used. Traditional lambics are commonly denoted by the term "oud" which is a reference to "old-style" and these are the most sour. More commonly though lambics are sweetened to cut the intense acidity. Serve with sharp cheeses or pickled dishes or use in the preparation of mussels.''',
        'parent_id': 2
    },
    {
        'id': 17,
        'name': u'Lambic Style - Gueuze',
        'description': u'''Gueuze is a blend of young and old lambic. The yeasts are rejuvenated and carbonation ensues. The old lambic is more refined in character and helps take some of the edge off of the young lambic. The hops used are old, and act only as a preservative, so hop character is not a part of the style. The wild yeasts not only ferment and sour the beer, but they bring the funky, unpredictable flavours that characterize all lambic beers. A quality gueuze will be blended to eliminate some of the less desirable flavours. Above all else, a gueuze should be sour and very complex. The best examples are the most complex beers in the world, and put most champagnes to shame as well. The finish should be bone dry.''',
        'parent_id': 2
    },
    {
        'id': 18,
        'name': u'Lambic Style - Unblended',
        'description': u'''Unblended lambic is the purest form of lambic. This rare specialty is typically only found in the lambicmakers’ home region, although one bottled example – Cantillon 1900 Bruocsella Grand Cru – is produced. Unblended lambics will vary in character from barrel to barrel, can be found in a variety of ages, and may have been aged with fruit in the cask. They tend to be still, with flavours whose edge has not been taken off by blending.''',
        'parent_id': 2
    },
    {
        'id': 19,
        'name': u'Sour Red/Brown',
        'description': u'''The sour red/brown beers of Flanders can be considered as two different styles, or two ends of a single style continuum, depending on how you choose to view the issue. They are a clearly–defined sour ale subtype, one with strong historical traditions. Their character blends rich malt with tartness, and usually some fruity character as well. Oak aging is common in the traditional production of the style and therefore is often evident in the character. Many examples are also aged on fruit. At the red end of the style, the classic is Rodenbach at the brown end it is Liefmans, and there are several very good examples in between.''',
        'parent_id': 2
    },
    {
        'id': 20,
        'name': u'Sour/Wild Ale',
        'description': u'''Sour/Wild is a category encompassing a myriad of non-traditional sour ales which are typically brewed with an ale yeast and then inoculated with souring bacteria and yeasts -- typically Lactobacillus, often Brettanomyces and Pediococcus, and sometimes Acetobacter.''',
        'parent_id': 2
    },
    {
        'id': 21,
        'name': u'Altbier',
        'description': u'''Well hopped and malty with copper to dark-brown color, native to Dusseldorf, Germany. Alt is the German word for "old" or "old style". It is more or less the German equivalent to an English ale. Traditionally fermented warm but aged at cold temperatures.''',
        'parent_id': 3
    },
    {
        'id': 22,
        'name': u'Amber Ale',
        'description': u'''A style without definition, amber ales range from bland, vaguely caramelly beers to products with a fairly healthy malt and hop balance. Often the differentiation between a quality amber and an American Pale is that the amber might have more dark malt character, or a less assertive hop rate.''',
        'parent_id': 3
    },
    {
        'id': 23,
        'name': u'American Pale Ale',
        'description': u'''American Pale Ales are light in color, ranging from golden to a light copper color. The style of this beer is defined by the American hops used. American hops typically have high bitterness and aroma. This is a perfect beer for big fare like grilled burgers or combination pizzas, as well as lighter fare like sushi and green salads.''',
        'parent_id': 3
    },
    {
        'id': 24,
        'name': u'American Strong Ale',
        'description': u'''Not a style%2C per se%2C but a catch-all category to incorporate the plethora of strong%2C stylistically vague beers coming from American microbreweries today. Some are related to English Strong Ales%2C but with a higher hop rate%2C while others are ultra-strong variants on the IPA or red ale themes. No matter how varied their origins or characters might be%2C all are intense%2C potent%2C with generous quantities of hops and malt.''',
        'parent_id': 3
    },
    {
        'id': 25,
        'name': u'Barley Wine',
        'description': u'''A Barley Wine is a strong, top-fermenting ale, with an alcohol content of at least 9% and up to 13% (or more) by volume. Hops may be hardly noticeable at all or very noticeable. Sip them out of the special glass, that will concentrate the aroma. They are excellent with cigars or with dessert''',
        'parent_id': 3
    },
    {
        'id': 26,
        'name': u'Bitter',
        'description': u'''A gold to copper color, low carbonation and medium to high bitterness. Hop flavor and aroma may be non-existent to mild. Great to drink with steak and lobster.''',
        'parent_id': 3
    },
    {
        'id': 27,
        'name': u'Brown Ale',
        'description': u'''Color ranges from reddish-brown to dark brown. Beers termed brown ale include sweet low alcohol beers such as Manns Original Brown Ale medium strength amber beers of moderate bitterness such as Newcastle Brown Ale and malty but hoppy beers such as Sierra Nevada Brown Ale.''',
        'parent_id': 3
    },
    {
        'id': 28,
        'name': u'Cream Ale',
        'description': u'''A mild, pale, light-bodied ale, made using a warm fermentation (top or bottom) and cold lagering or by blending top and bottom-fermented beers. Low to medium bitterness. Low hop flavor and aroma.''',
        'parent_id': 3
    },
    {
        'id': 29,
        'name': u'English Pale Ale',
        'description': u'''Classic English Pale Ales are not pale but rather are golden to copper colored and display English variety hop character. Distinguishing characteristics are dryness and defined hop taste, but more malt balance than what you’ll typically find in an American Pale Ale. Great to drink with all sorts of meats including roast beef, lamb, burgers, duck, goose, etc. Note that the term ’pale ale’ is used in England to signify a bottled bitter, and in that way there is no such thing as ’English Pale Ale’ to the English. The style is a North American construct, borne of the multitude of pale ales that pay homage to these bottled bitters - Bass in particular - and therefore the majority of true examples of the style are found outside Britain.''',
        'parent_id': 3
    },
    {
        'id': 30,
        'name': u'English Strong Ale',
        'description': u'''Malty, with complex fruity esters. Some oxidative notes are acceptable, akin to those found in port or sherry. Hop aromas not usually present, due to extended age. Medium amber to very dark red-amber color. Malty and usually sweet. Alcoholic strength should be evident, though not overwhelming. Medium to full body alcohol should contribute some warmth. An ale of significant alcoholic strength, though usually not as strong or rich as barleywine. Usually tilted toward a sweeter, more malty balance. Often regarded as winter warmers, and often released as seasonal beers.''',
        'parent_id': 3
    },
    {
        'id': 31,
        'name': u'Golden Ale/Blond Ale',
        'description': u'''There are a few different types of blond ale. The first is the traditional "Canadian Ale", an adjunct-laden, macrobrewed, top-fermented equivalent of the American Standard. The second is common in US brewpubs - a light starter ale, with marginally more hop and body than a macrobrew, fewer adjuncts, but still not a flavourful beer by any means. The British interpretation is easily the boldest, hoppiest blond ale rendition. Some of these can almost be considered American Pales they are so hopped up - very crisp, refreshing, with relatively low alcohol compared with their North American counterparts.''',
        'parent_id': 3
    },
    {
        'id': 32,
        'name': u'Imperial IPA',
        'description': u'''Imperial IPA (also called Double or Triple IPA) is a strong, often sweet, intensely hoppy version of the traditional India Pale Ale. Bitterness units range tend to be 100 IBUs and above. The ABV level for DIPAs generally begins at 7.5% but is more commonly in the 8.0%+ range. The flavour profile is intense all around. Unlike barley wines, the balance is heavily towards the hops, with crystal and other malts providing support.''',
        'parent_id': 3
    },
    {
        'id': 33,
        'name': u'India Pale Ale (IPA)',
        'description': u'''India Pale Ale, the modern version of which has largely been formed in the US, has an intense hop flavor, a golden to copper color, and a medium malty body. The aroma is moderate to very strong. IPAs work especially well at cutting the heat of chili, vindaloo or Sichuan cuisine. In England, IPA is often just another name for bitter although some micros are doing their own versions of an American IPA as well.''',
        'parent_id': 3
    },
    {
        'id': 34,
        'name': u'Irish Ale',
        'description': u'''The red ales of Ireland have a gentle maltiness, caramelly, earthy notes, and a generally restrained hop character. They are session ales, so alcohol is generally at 5% abv or less, though you will find the occasion stronger example. The major macrobrewed Irish ales are ascribed to be in this style, but the majority of examples are from New World microbreweries working with Michael Jackson’s description of Irish ale.''',
        'parent_id': 3
    },
    {
        'id': 35,
        'name': u'Kölsch',
        'description': u'''Golden, top-fermented style native to Köln, Germany. The style has a very narrow profile and many beers that consider themselves to be kölschbiers are not. Generally they have a moderate bitterness, but fairly prominent hop flavour (typically Spalt, Tettnang or Hallertau). They have high effervescence, medium esters, but a rounded, stylish character derived from lagering.''',
        'parent_id': 3
    },
    {
        'id': 36,
        'name': u'Mild Ale',
        'description': u'''Malt accented, typically little or no hop flavour or aroma. Usually medium to dark brown in colour though many English examples are almost black with caramel often added for colouring as well as favouring purposes. Mild refers to no or limited hop bitterness/ aroma. Still very popular in the North- West and Midland areas of England where it is usually between 3 to 4% ABV and preferred with a good head. There are examples of stronger versions of the style, but rarely over 5-6%.''',
        'parent_id': 3
    },
    {
        'id': 37,
        'name': u'Old Ale',
        'description': u'''Old Ale is a simple enough style to figure out. At least, once you understand that there are three or four beer styles called Old Ale. The first is the best known - the strong dark Old Peculier style. The second type of Old Ale is a blended dark ale. At least one of the beers comprising the blend will be aged for a couple of years in wood casks. The third version of Old Ale is a form of mild – a low-gravity dark ale. Another version of Old Ale is closely related to the first. For me, these are robustly malty beers, akin to a top-fermented version of a doppelbock.''',
        'parent_id': 3
    },
    {
        'id': 38,
        'name': u'Premium Bitter/ESB',
        'description': u'''In England, many breweries have a number of bitters in their range. The style that has come to be known as Premium or Special Bitter generally includes the stronger ( 4.6%-6.0%) examples. These are mostly served in the traditional way from the cask, but some are also found in bottle form where the extra malt allows them to stand up better than the more delicate ordinary Bitter. In the US, the designation ESB is common for this style, owing to the influence of Fuller’s ESB, the London brew that was among the first to be exported to the States. In the US, some ESBs are made with American hops and a clean yeast, but the alcohol range is the same, as is the range of bitterness, usually between 25 and 35 but occasionally creeping higher.''',
        'parent_id': 3
    },
    {
        'id': 39,
        'name': u'Scotch Ale',
        'description': u'''Scotch Ale was the name given to a strong pale ale from Edinburgh in the 19th century. This was typical of the strong pale ales brewed in Britain at that time - mainly pale barley malt and moderate hopping, and were not that stylistically different to English Strong Ales or Barley Wines. The name however became regionalised so that a strong pale ale from Scotland became known as a Scotch Ale or Wee Heavy. Beers using the designation Scotch Ale are popular in the USA where most examples are brewed locally. Examples of beers brewed in the USA under the name Wee Heavy tend to be 7% abv and higher, while Scottish brewed examples, such as Belhavens Wee Heavy, are typically between 5.5% and 6.5% abv.''',
        'parent_id': 3
    },
    {
        'id': 40,
        'name': u'Scottish Ale',
        'description': u'''Scottish ales are generally dark, malty, full-bodied brews. Many examples have a hint of smokiness derived from the use of peated malt. 60, 70, and 80 shilling examples are all session ales under 5% abv, but the stronger "wee heavies" can range closer to 8%, with the accompanying increase in alcohol flavour and esters. Works well as an accompaniment to hearty meat and game dishes, sharp cheddar, atholl brose and shortbread.''',
        'parent_id': 3
    },
    {
        'id': 41,
        'name': u'Session IPA',
        'description': u'''The term Session IPA describes a category of beers marketed for their hop-dominant flavor profiles at "sessionable" levels of alcohol. While this is typically 3.2 - 4.6 percent alcohol, a few have stretched the definition. This class of beers arose in 2010 out of the Craft Beer Tradition as a reaction to the trend of increasingly strong beers and greater public appreciation for hoppier profiles around the globe. It is differentiated from American Pale Ale by typically being lower in alcohol and usually having more hop-dominant profiles. While hops used are typically American Pacific Northwest and New Zealand, proprietary/experimental and South African and other hops may also factor into a Session IPA hop bill.''',
        'parent_id': 3
    },
    {
        'id': 42,
        'name': u'Baltic Porter',
        'description': u'''The historical remnants of the 19th c. Baltic trade in imperial stouts, Baltic Porters are typically strong, sweet and bottom-fermented. They lack the powerful roast of an imperial stout, but have an intense malt character, and moderate to strong alcohol. Though they are typically lagers, there are a handful of top-fermented examples.''',
        'parent_id': 4
    },
    {
        'id': 43,
        'name': u'Black IPA',
        'description': u'''An emerging beer style roughly defined as a beer with IPA-level hopping relatively high alcohol and a distinct toasty dark malt character. Typically lacks the roastiness and body of a strong stout and is hoppier than a strong porter. Expressive dry-hopping is common. Also called India Dark Ale, India Black Ale, Cascadian Dark Ale, Dark IPA and sometimes India Brown Ale.''',
        'parent_id': 4
    },
    {
        'id': 44,
        'name': u'Dry Stout',
        'description': u'''The "Irish-style" stout is typically a low-gravity stout with bitterness ranging between 30-45 IBUs. Roastiness is present, but restrained, and there should not be hops in either the flavour or aroma. A little bit of acidity can be present. Often, this type of stout is serving via nitrogen, with all the effects that has on a beer - low carbonation, extra-thick head, lifeless palate and muted flavour and aroma.''',
        'parent_id': 4
    },
    {
        'id': 45,
        'name': u'Foreign Stout',
        'description': u'''Foreign Stout began with the beer that would become Guinness Foreign Extra Stout. This was a stronger, extra-hopped version of the basic Guinness Extra Stout, brewed to survive long journeys overseas. The classic FES still exists in a few different forms, but many of the original destination countries (Jamaica, Sri Lanka, etc.) now have their own, locally-produced versions. Foreign stout occupies a position between basic stout and imperial stout. It is sweeter than a basic stout, but not as robust as an imperial. It is less fruity and less hoppy as well. Foreign stouts are sometimes made with local grains and adjuncts – sugar is not uncommon. Alcohol ranges from 6-8%.''',
        'parent_id': 4
    },
    {
        'id': 46,
        'name': u'Imperial Porter',
        'description': u'''Imperial (extra-strong) porters fall in between the traditional porter, a Baltic porter, and an imperial stout. They range from around 7.5% upwards, with hefty dark malt character, but lack the overt roastiness of an imperial stout.''',
        'parent_id': 4
    },
    {
        'id': 47,
        'name': u'Imperial Stout',
        'description': u'''Imperial stouts are usually extremely dark brown to black in color with flavors that are intensely malty, deeply roasted and sometimes with accents of dark fruit (raisin, fig) and chocolate. The bitterness is typically low to moderate. Imperial stouts are strong and generally exceed 8% ABV.''',
        'parent_id': 4
    },
    {
        'id': 48,
        'name': u'Porter',
        'description': u'''Black or chocolate malt gives the porter its dark brown color. Porters are often well hopped and somewhat heavily malted. This is a medium-bodied beer and may show some sweetness usually from the light caramel to light molasses range. Hoppiness can range from bitter to mild. Porters, in relation to stouts of the same region, are typically more mild and less aggressively hopped.''',
        'parent_id': 4
    },
    {
        'id': 49,
        'name': u'Stout',
        'description': u'''A stout is made with dark roasted malts which results in a dark color and a roasted malt flavor. In mainland Europe they are usually termed "noir" (black). The word stout means strong, and was applied to strong Porter in the 18th century - most typically by Guinness, who were one of the few breweries to continue making such beers into the 20th century. Guinness is today the template for Irish or Dry Stout. Other stout variations are Imperial Stout, Foreign Stout, and Sweet or Milk Stout - as well as Porter, Imperial Porter, and Baltic Porter - and the related Mild and Schwarzbier.''',
        'parent_id': 4
    },
    {
        'id': 50,
        'name': u'Sweet Stout',
        'description': u'''Dark brown to black in colour. Sweet stouts come in two main varieties - milk stout and oatmeal stout. Milk stouts are made with the addition of lactose, and are sweet and generally low in alcohol. Oatmeal lends a smooth fullness of body to stouts. All of the sweet stouts are noted for their restrained roastiness in comparison with other stouts, and their low hop levels.''',
        'parent_id': 4
    },
    {
        'id': 51,
        'name': u'Dunkelweizen',
        'description': u'''A dark take on the German wheat theme, dunkelweizens have the same banana and clove notes of their pale cousins, but also have earthy, toasty, chocolatey notes from the addition of dark malts. They are "shoulder season" wheat beers to many drinkers - something a little more robust than a hefeweizen for the fall and spring seasons, but not as rich as winter’s weizenbocks. Alcohol is between 4.8-5.6% generally, bitterness is low, and carbonation is high. Occasionally, you will see dark versions of American Wheats, but these are uncommon.''',
        'parent_id': 5
    },
    {
        'id': 52,
        'name': u'German Hefeweizen',
        'description': u'''Depending on the style can range from pale and light body to dark brown with full body. Wheat beer is characterized by its cloudy appearance and its banana and sometimes vanilla aftertaste.''',
        'parent_id': 5
    },
    {
        'id': 53,
        'name': u'German Kristallweizen',
        'description': u'''Kristalweizens are the third member of the German Wheat trifecta. Derided by many beer lovers as “castrated hefeweizens”, kristalweizens are known for their filtered, sparkling colour. They have the classic spritzy carbonation of wheat beers, and the same tart wheat notes and signature components of banana, bubblegum and spice. The body is light, and alcohol ranging around the 5% mark, give or take half a point.''',
        'parent_id': 5
    },
    {
        'id': 54,
        'name': u'Grodziskie/Gose/Lichtenhainer',
        'description': u'''Sour wheat beers were common in many parts of medieval and early Industrial Europe. Two styles – lambic and Berliner weisse – survived, but many others did not. Gose and Lichtenhainer are historic styles of sour wheat beer. Grodzisk is sometimes tart, sometimes not. Gose is seasoned with salt, Grodziskie and Lichtenhainer contain smoked malt. Historical sources are mixed about Lichtenhainer containing wheat, so modern interpretations may vary. Grätzer is an alternative name for Grodziskie. All three will be relatively low alcohol, with a strong wheat character, but will be distinct from classic examples of Berliner Weisse or lambic. As all we have are historical recreations, substantial differences may exist between interpretations.''',
        'parent_id': 5
    },
    {
        'id': 55,
        'name': u'Weizen Bock',
        'description': u'''Strong, dark wheat beers, typically with a high ester profile and more malt and alcohol than is typically associated with a wheat beer.''',
        'parent_id': 5
    },
    {
        'id': 56,
        'name': u'Wheat Ale',
        'description': u'''Golden to light amber in color, the body is light to medium. The wheat lends a crispness to the brew, often with some acidity. Some hop flavour may be present, but bitterness is low. Not as estery as German or Belgian-style wheats.''',
        'parent_id': 5
    },
    {
        'id': 57,
        'name': u'Witbier',
        'description': u'''Witbier, also known as Belgian White, is a style of Belgian-style wheat beers that are generally pale and opaque with a crisp wheat character and citric refreshment of orange peel and coriander. Ingredients sometimes include oats for smoothness, and other spices such as grains of paradise. Serve with light cheeses or mussels.''',
        'parent_id': 5
    },
    {
        'id': 58,
        'name': u'Amber Lager/Vienna',
        'description': u'''Your typical macrobrewed Dark Lager, often rendered dark with either brewer’s caramel or black patent malt, but each brewery will have a different approach. Aside from caramelly notes, these beers will not typically resemble other dark lager styles so much as they do the lighter styles, due to low amounts of hops, malt and body. Vienna as a beer style was theorized by Michael Jackson, but his oft-cited example was Negra Modelo, which is a macro dark lager like all the others. Some beers have taken on the idea of a Vienna lager as a distinct style, loosely based on the 1840 Anton Dreher beer, and these can be expected to be all-malt, with a fuller body and more character than the average macro dark.''',
        'parent_id': 6
    },
    {
        'id': 59,
        'name': u'California Common',
        'description': u'''Style originating in 18th century California, where brewers without access to refrigeration produced beers using lager yeasts and warm temperatures. These still retain some of the rounded character inherent in all lagers, but with a dose of ale fruitiness.''',
        'parent_id': 6
    },
    {
        'id': 60,
        'name': u'Czech Pilsner (Světlý)',
        'description': u'''Hallmarked by the generous use of the Saaz hop, Bohemian or Czech pilsners are also noted for their rich gold color, fat maltiness and moderate to full body. Generally brewed to 10-12° Plato. in Czech these beers are simply called Světlý Ležák. Sometimes served cloudy and unfiltered with young wort mixed in, known as Kvasnicova in the Czech Republic, the same as what is known as krausening in Germany. Regardless of origin, to be a pilsner a beer must have at least 28 units of bitterness, and preferably much more.''',
        'parent_id': 6
    },
    {
        'id': 61,
        'name': u'Doppelbock',
        'description': u'''Doppel means double and while these are stronger brews than the traditional German bocks, they are typically not twice the strength. Color is light amber to dark brown. Very full body with a high alcoholic flavor. Low hop flavor and aroma.''',
        'parent_id': 6
    },
    {
        'id': 62,
        'name': u'Dortmunder/Helles',
        'description': u'''These two styles are closely related, the former hailing from Dortmund and the latter from Bavaria. Both are slightly strong (5.0-5.6%), malt-accented pale lagers. The cookie-like or bready maltiness should be very much in evidence in a traditional example. These beers are clean and easy to drink in quantity. Some Dortmunders made in Denmark and the Netherlands are stronger.''',
        'parent_id': 6
    },
    {
        'id': 63,
        'name': u'Dunkel/Tmavý',
        'description': u'''Copper to dark brown lager common in Germany and the Czech Republic but made worldwide. Medium body. Nutty toasted chocolate-like malty sweetness in aroma and flavor. Medium bitterness. Low "noble-type" hop flavor and aroma. In both Germany and Czech dark lagers span a wide range of characters from sweet to dry forming more of a category than a specific style with considerable leeway for the brewer with regards to the character of the beer. This is the biggest reason why they are grouped together despite coming from different traditions and each being made with local ingredients.''',
        'parent_id': 6
    },
    {
        'id': 64,
        'name': u'Dunkler Bock',
        'description': u'''The dark Bock has a deep copper to dark brown color. Medium to full-bodied, malt sweetness and nutty or light toasted flavors dominate. Hop flavor and aroma can be light to non-existent.''',
        'parent_id': 6
    },
    {
        'id': 65,
        'name': u'Eisbock',
        'description': u'''A stronger version of Doppelbock. Deep copper to black. Very alcoholic. Typically brewed by freezing a doppelbock and removing resulting ice to increase alcohol content.''',
        'parent_id': 6
    },
    {
        'id': 66,
        'name': u'Heller Bock',
        'description': u'''The Heller Bock is primarily a malty beer from the German brewing tradition with little hop character - neither bitter nor aromatic - though the style typically has a little more hops than the standard Bock. The color is golden to light brown or amber. They should normally pour with a substantial white head. Typical examples are pale and clear.''',
        'parent_id': 6
    },
    {
        'id': 67,
        'name': u'Imperial Pils/Strong Pale Lager',
        'description': u'''A catch-all for strong, sometimes hoppy lagers that range from modern versions of "Imperial Pilsner", to more traditional strong lagers which are more common in Eastern Europe. These are essentially stronger versions of pilsners, though the increased malt and alcohol will noticeably reduce the hop accent. Because these are usually all-malt, and comfortably hopped, they are easily distinguishable from malt liquors. Without the malt character of bocks, these are worthy of a style all their own.''',
        'parent_id': 6
    },
    {
        'id': 68,
        'name': u'Malt Liquor',
        'description': u'''Strong, alcoholic-tasting, often poorly made strong lagers. Esters, fusels and other products of undiluted high-gravity brewed beers are often commonplace. Properly served in the 40oz bottle with accompanying brown paper bag.''',
        'parent_id': 6
    },
    {
        'id': 69,
        'name': u'Oktoberfest/Märzen',
        'description': u'''Oktoberfest is a German festival dating from 1810, and Oktoberfestbiers are the beers that have been served at the festival since 1818, and are supplied by 6 breweries: Spaten, Lowenbrau, Augustiner, Hofbrau, Paulaner and Hacker-Pschorr. Traditionally Oktoberfestbiers were the lagers of around 5.5 to 6 abv called Marzen - brewed in March and allowed to ferment slowly during the summer months. Originally these would have been dark lagers, but from 1872 a strong March brewed version of an amber-red Vienna lager made by Josef Sedlmayr became the favourite Oktoberfestbier. Since the 1990s European brewed versions have tended to be golden in colour, while American versions have remained dark or amber.''',
        'parent_id': 6
    },
    {
        'id': 70,
        'name': u'Pale Lager',
        'description': u'''The color of pale lager ranges from light bronze to nearly transparent and the alcohol anywhere from 4-6%. Adjunct usage may be quite high, though in some cases the beer is all-malt. Carbonation is typically forced, though not always. One thing that does not vary is that neither the malt nor the hops make much of an impression on the palate. These beers are brewed for minimum character, though faint traces of hop or malt may show through. Commonly detected features and flaws include fusels, oxidized malt and skunked hops. The body will often be thin and/or spritzy while the finish is typically mildly bitter.''',
        'parent_id': 6
    },
    {
        'id': 71,
        'name': u'Pilsener',
        'description': u'''While the definition of pilsner is open to much debate in the beer community, it generally refers to pale, hoppy lagers, ranging from ~30 IBU and up. From Classic German Pilsners, which tend to be light-to-medium bodied, semi-sweet to off-dry, hopped with German noble hops, to New World artisan renditions in North America, New Zealand and elsewhere, which showcase modern hop strains. A separate style category is maintained for Czech Pilsner (Světlý Ležák).''',
        'parent_id': 6
    },
    {
        'id': 72,
        'name': u'Polotmavý',
        'description': u'''This is the amber lager style of the Czech Republic. The character that the brewery usually aims for with this style is a hybrid between the dark lager and the pale pilsner. The result has a richer malt character than the American Dark/Amber Lager/Vienna style and more hop than the Oktoberfest/Marzen style.''',
        'parent_id': 6
    },
    {
        'id': 73,
        'name': u'Premium Lager',
        'description': u'''A beer that straddles between the mainstream Pale Lager and Pilsner. Not all beers that call themselves Premium Lager are, but those that are will typically have a deep gold to light bronze colour, and distinct influence of malt and hops. They should be free of adjuncts and will have a softer carbonation than Pale Lager or Classic German Pilsner. IBUs will typically range in the 20’s, and lagering times will typically be 4-6 weeks, more in line with what pilsners have. Overall accent will be malty-to-balanced, alcohol in a slightly tighter range than either Pale Lager or Pilsner (4.5-5.5%). Most often the product of a microbrewery or brewpub, but macrobreweries can make this style if they jack up the hops a bit and make it all-malt.''',
        'parent_id': 6
    },
    {
        'id': 74,
        'name': u'Radler/Shandy',
        'description': u'''A mix of a sweet soft drink or juice -- typically lemon or ginger but sometimes apple, grapefruit or other fruit -- and beer, often in equal parts, that is moderately sweet, thirst quenching, low in alcohol with medium to spritzy carbonation. Often but not necessarily sold as a Summer seasonal. Category includes such regional styles as diesel (beer and cola), cola-weizen (wheat beer and cola), and russ’n.''',
        'parent_id': 6
    },
    {
        'id': 75,
        'name': u'Schwarzbier',
        'description': u'''Dark brown to black. Medium body. Roasted malt evident. Low sweetness in aroma and flavor. Low to medium bitterness. Low bitterness from roast malt. Hop flavor and aroma, "noble-type" OK. No fruitiness, esters.''',
        'parent_id': 6
    },
    {
        'id': 76,
        'name': u'Zwickel/Keller/Landbier',
        'description': u'''Three related lager styles most common in Franconia. Essentially, these are hoppier versions of a helles, served with natural carbonation and unfiltered - they are the lager world’s answer to real ale. Kellerbier will on average be hoppier than zwickelbier. There is also Landbier, which is more malt-accented, may be filtered, but is similarly lacking in carbonation. Gravity is standard, low to moderate hop rates, the colour from pale to reddish-amber and the palate should be balanced with a hop accent. Zoiglbier, common to Oberpfalz, is also included in this category.''',
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
