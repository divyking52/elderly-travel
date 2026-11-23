# -*- coding: utf-8 -*-
import build_site as s

def pkg(num, pid, budget, dest, duration, style, img, alt, meta, title, price, summary, highs, inc, exc, flip=False):
    h = "".join(f"<li>{x}</li>" for x in highs)
    i = "".join(f"<li>{x}</li>" for x in inc)
    e = "".join(f"<li>{x}</li>" for x in exc)
    flip_cls = " is-flip" if flip else ""
    return f'''
<article class="holi-card{flip_cls}" id="{pid}" data-item data-budget="{budget}" data-destination="{dest}" data-duration="{duration}" data-style="{style}" data-holi>
  <div class="holi-card-view wrap">
    <figure class="holi-media">
      <img src="{img}" alt="{alt}" width="1200" height="900" decoding="async">
      <figcaption class="holi-num" aria-hidden="true"><span>{num}</span></figcaption>
    </figure>
    <div class="holi-body">
      <p class="holi-meta">{meta}</p>
      <h2>{title}</h2>
      <p class="holi-price"><span>{price}</span> <small>illustrative, twin share</small></p>
      <p class="holi-summary">{summary}</p>
      <div class="holi-panels">
        <div class="holi-panel">
          <h3>Itinerary highlights</h3>
          <ul>{h}</ul>
        </div>
        <div class="holi-include">
          <div><h3>Included</h3><ul>{i}</ul></div>
          <div><h3>Not included</h3><ul>{e}</ul></div>
        </div>
      </div>
      <p class="holi-actions"><a class="btn" href="contact.html#enquire">Enquire about this holiday <span class="sq" aria-hidden="true"></span></a></p>
    </div>
  </div>
</article>'''

DEST = '''
<section class="dest-hero" data-dest-hero>
  <div class="dest-hero-media">
    <img data-parallax src="images/swiss.jpg" alt="Alpine meadows and snowy peaks" width="1600" height="1000" decoding="async">
    <div class="dest-hero-veil" aria-hidden="true"></div>
  </div>
  <div class="dest-hero-copy wrap">
    <p class="eyebrow">Places</p>
    <h1 data-dest-title>
      <span class="dest-title-line">Destinations,</span>
      <span class="dest-title-line">kept to a human pace.</span>
    </h1>
    <p class="lede" data-dest-lede>Six regions. Each one is a place to stay with, not a list to finish. Illustrative prices depend on dates, availability, and inclusions.</p>
  </div>
  <div class="dest-ticker" aria-hidden="true">
    <div class="dest-ticker-track">
      <span>Switzerland</span><span>Italy</span><span>Japan</span><span>Rajasthan</span><span>Kerala</span><span>New Zealand</span>
      <span>Switzerland</span><span>Italy</span><span>Japan</span><span>Rajasthan</span><span>Kerala</span><span>New Zealand</span>
    </div>
  </div>
</section>

<section class="dest-atlas" data-dest-atlas data-filter-root data-label="destinations">
  <div class="dest-atlas-bar">
    <div class="wrap dest-atlas-bar-inner">
      <div class="filter-block" data-filter="category">
        <p>Find a pace</p>
        <div class="filters" role="group" aria-label="Destination category">
          <button class="chip" type="button" data-value="all" aria-pressed="true">All places</button>
          <button class="chip" type="button" data-value="mountains" aria-pressed="false">Mountains</button>
          <button class="chip" type="button" data-value="heritage" aria-pressed="false">Heritage</button>
          <button class="chip" type="button" data-value="water" aria-pressed="false">Water</button>
          <button class="chip" type="button" data-value="cities" aria-pressed="false">Cities &amp; culture</button>
        </div>
      </div>
      <p class="live" id="filter-live" role="status">6 destinations shown.</p>
    </div>
  </div>

  <nav class="dest-rail" data-dest-rail aria-label="Destination index">
    <a href="#switzerland" data-dest-jump="switzerland"><b>01</b><span>Switzerland</span></a>
    <a href="#italy" data-dest-jump="italy"><b>02</b><span>Italy</span></a>
    <a href="#japan" data-dest-jump="japan"><b>03</b><span>Japan</span></a>
    <a href="#rajasthan" data-dest-jump="rajasthan"><b>04</b><span>Rajasthan</span></a>
    <a href="#kerala" data-dest-jump="kerala"><b>05</b><span>Kerala</span></a>
    <a href="#new-zealand" data-dest-jump="new-zealand"><b>06</b><span>New Zealand</span></a>
  </nav>

  <div class="dest-chapters">
    <article class="dest-chapter" id="switzerland" data-item data-category="mountains" data-dest-chapter data-place="Switzerland">
      <div class="dest-chapter-view wrap">
        <figure class="dest-media">
          <img src="images/lake.jpg" alt="Two people in a boat on an alpine lake" width="1200" height="900" decoding="async">
          <figcaption class="dest-index" aria-hidden="true"><span>01</span></figcaption>
        </figure>
        <div class="dest-copy">
          <p class="dest-tag">Mountains</p>
          <p class="meta-row">From ₹1,49,999 · 8 days / 7 nights</p>
          <h2>Switzerland</h2>
          <p>Lakes in the morning, a mountain railway when the light is kind, and a hotel you return to before the day is spent. We keep the map small: one or two valleys, not a circuit of the country.</p>
          <p>Good if you like cool air, clear timetables, and scenery that does the talking. Walks are optional and described in minutes, not in bravery.</p>
          <p class="dest-actions"><a class="btn btn-line" href="packages.html#swiss">Related holiday</a> <a class="btn" href="contact.html#enquire">Enquire</a></p>
        </div>
      </div>
    </article>

    <article class="dest-chapter is-flip" id="italy" data-item data-category="water" data-dest-chapter data-place="Italy">
      <div class="dest-chapter-view wrap">
        <figure class="dest-media">
          <img src="images/tuscany.jpg" alt="An Italian coastal village on a cliff above the sea" width="1200" height="900" decoding="async">
          <figcaption class="dest-index" aria-hidden="true"><span>02</span></figcaption>
        </figure>
        <div class="dest-copy">
          <p class="dest-tag">Water</p>
          <p class="meta-row">From ₹1,29,999 · 7 days / 6 nights</p>
          <h2>Italy</h2>
          <p>Villages, a long table, and one city if you want it — seen in the late afternoon, when the day-trippers have thinned. Cooking, courtyards, and a pace that allows a second coffee.</p>
          <p>We say which lanes are steep before you choose them. A hill town can be beautiful and still be the wrong hill.</p>
          <p class="dest-actions"><a class="btn btn-line" href="packages.html#italy">Related holiday</a> <a class="btn" href="contact.html#enquire">Enquire</a></p>
        </div>
      </div>
    </article>

    <article class="dest-chapter" id="japan" data-item data-category="cities" data-dest-chapter data-place="Japan">
      <div class="dest-chapter-view wrap">
        <figure class="dest-media">
          <img src="images/fuji.jpg" alt="Mount Fuji framed by cherry blossom" width="1200" height="900" decoding="async">
          <figcaption class="dest-index" aria-hidden="true"><span>03</span></figcaption>
        </figure>
        <div class="dest-copy">
          <p class="dest-tag">Cities &amp; culture</p>
          <p class="meta-row">From ₹1,59,999 · 9 days / 8 nights</p>
          <h2>Japan</h2>
          <p>Gardens, a train that is easy to trust, and rooms that stay quiet. Kyoto for lanes and temples. A smaller town for the nights. Tokyo only if you ask for it, and only for a piece of it.</p>
          <p>Food is discussed properly: what you love, what you avoid, and where a chair is more comfortable than a floor.</p>
          <p class="dest-actions"><a class="btn btn-line" href="packages.html#japan">Related holiday</a> <a class="btn" href="contact.html#enquire">Enquire</a></p>
        </div>
      </div>
    </article>

    <article class="dest-chapter is-flip" id="rajasthan" data-item data-category="heritage" data-dest-chapter data-place="Rajasthan">
      <div class="dest-chapter-view wrap">
        <figure class="dest-media">
          <img src="images/rajasthan.jpg" alt="Hawa Mahal in Jaipur" width="1200" height="900" decoding="async">
          <figcaption class="dest-index" aria-hidden="true"><span>04</span></figcaption>
        </figure>
        <div class="dest-copy">
          <p class="dest-tag">Heritage</p>
          <p class="meta-row">From ₹49,999 · 6 days / 5 nights</p>
          <h2>Rajasthan</h2>
          <p>Jaipur’s courtyards and Amber’s sandstone, with the heat respected. Heritage hotels, a musician if the evening calls for one, and drives that are not disguised as sightseeing.</p>
          <p>Palaces have steps. We name them. The beautiful room is the one you can actually reach after lunch.</p>
          <p class="dest-actions"><a class="btn btn-line" href="packages.html#rajasthan">Related holiday</a> <a class="btn" href="contact.html#enquire">Enquire</a></p>
        </div>
      </div>
    </article>

    <article class="dest-chapter" id="kerala" data-item data-category="water" data-dest-chapter data-place="Kerala">
      <div class="dest-chapter-view wrap">
        <figure class="dest-media">
          <img src="images/kerala.jpg" alt="A covered boat on a palm-lined backwater" width="1200" height="900" decoding="async">
          <figcaption class="dest-index" aria-hidden="true"><span>05</span></figcaption>
        </figure>
        <div class="dest-copy">
          <p class="dest-tag">Water</p>
          <p class="meta-row">From ₹39,999 · 5 days / 4 nights</p>
          <h2>Kerala</h2>
          <p>A houseboat with shade, a bank of palms, and meals that arrive without a schedule shouted from a jetty. Add a quiet garden or a short Ayurvedic hour only if you want it.</p>
          <p>This is the journey we suggest when someone says they would like to do very little, properly.</p>
          <p class="dest-actions"><a class="btn btn-line" href="packages.html#kerala">Related holiday</a> <a class="btn" href="contact.html#enquire">Enquire</a></p>
        </div>
      </div>
    </article>

    <article class="dest-chapter is-flip" id="new-zealand" data-item data-category="mountains" data-dest-chapter data-place="New Zealand">
      <div class="dest-chapter-view wrap">
        <figure class="dest-media">
          <img src="images/forest.jpg" alt="Mist over green mountain country and a quiet road" width="1200" height="900" decoding="async">
          <figcaption class="dest-index" aria-hidden="true"><span>06</span></figcaption>
        </figure>
        <div class="dest-copy">
          <p class="dest-tag">Mountains</p>
          <p class="meta-row">From ₹1,79,999 · 10 days / 9 nights</p>
          <h2>New Zealand</h2>
          <p>Lakes, short scenic drives, and nights in the same place twice. The country is long. We do not pretend you can see it in a week without living on a coach.</p>
          <p>Wildlife is watched from a distance that is decent for the animal and comfortable for you. No sprint to a viewpoint.</p>
          <p class="dest-actions"><a class="btn btn-line" href="packages.html#nz">Related holiday</a> <a class="btn" href="contact.html#enquire">Enquire</a></p>
        </div>
      </div>
    </article>
  </div>
</section>

<section class="band dest-close">
  <img class="bg" data-parallax src="images/hills.jpg" alt="Sun over open farmland" width="1600" height="1000" decoding="async">
  <div class="veil"></div>
  <div class="wrap" data-dest-close>
    <p class="eyebrow">Still choosing</p>
    <h2>Not sure which country yet?</h2>
    <p class="lede">Tell us the month, the company, and whether you want water, mountains, or a city you can leave by dinner.</p>
    <p><a class="btn" href="contact.html#enquire">Plan Your Holiday <span class="sq" aria-hidden="true"></span></a></p>
  </div>
</section>
'''

PACKAGES = '''
<section class="holi-hero" data-holi-hero>
  <div class="holi-hero-media">
    <img data-parallax src="images/palace.jpg" alt="Amber Fort in warm evening light" width="1600" height="1000" decoding="async">
    <div class="holi-hero-veil" aria-hidden="true"></div>
  </div>
  <div class="holi-hero-copy wrap">
    <p class="eyebrow">Holidays</p>
    <h1 data-holi-title>
      <span class="holi-title-line">Handpicked holiday</span>
      <span class="holi-title-line">packages.</span>
    </h1>
    <p class="lede" data-holi-lede>Filter by budget, place, length, or style. Every price is an illustration. The figure you confirm will name the dates and the inclusions.</p>
  </div>
  <div class="holi-ticker" aria-hidden="true">
    <div class="holi-ticker-track">
      <span>Swiss Alpine Escape</span><span>Royal Rajasthan</span><span>Kerala Slow Living</span><span>Italian Countryside</span><span>Japan Gardens &amp; Rail</span><span>New Zealand Lakes</span>
      <span>Swiss Alpine Escape</span><span>Royal Rajasthan</span><span>Kerala Slow Living</span><span>Italian Countryside</span><span>Japan Gardens &amp; Rail</span><span>New Zealand Lakes</span>
    </div>
  </div>
</section>

<section class="holi-folio" data-holi-folio data-filter-root data-label="holidays">
  <div class="holi-folio-bar">
    <div class="wrap holi-folio-bar-inner">
      <div class="holi-filters">
        <div class="filter-block" data-filter="budget">
          <p>Budget</p>
          <div class="filters" role="group" aria-label="Budget">
            <button class="chip" type="button" data-value="all" aria-pressed="true">All budgets</button>
            <button class="chip" type="button" data-value="value" aria-pressed="false">Under ₹50,000</button>
            <button class="chip" type="button" data-value="premium" aria-pressed="false">₹1,00,000 and above</button>
          </div>
        </div>
        <div class="filter-block" data-filter="destination">
          <p>Destination</p>
          <div class="filters" role="group" aria-label="Destination">
            <button class="chip" type="button" data-value="all" aria-pressed="true">All destinations</button>
            <button class="chip" type="button" data-value="switzerland" aria-pressed="false">Switzerland</button>
            <button class="chip" type="button" data-value="italy" aria-pressed="false">Italy</button>
            <button class="chip" type="button" data-value="japan" aria-pressed="false">Japan</button>
            <button class="chip" type="button" data-value="rajasthan" aria-pressed="false">Rajasthan</button>
            <button class="chip" type="button" data-value="kerala" aria-pressed="false">Kerala</button>
            <button class="chip" type="button" data-value="newzealand" aria-pressed="false">New Zealand</button>
          </div>
        </div>
        <div class="filter-block" data-filter="duration">
          <p>Duration</p>
          <div class="filters" role="group" aria-label="Duration">
            <button class="chip" type="button" data-value="all" aria-pressed="true">Any length</button>
            <button class="chip" type="button" data-value="short" aria-pressed="false">Up to 5 nights</button>
            <button class="chip" type="button" data-value="long" aria-pressed="false">6 nights or more</button>
          </div>
        </div>
        <div class="filter-block" data-filter="style">
          <p>Travel style</p>
          <div class="filters" role="group" aria-label="Travel style">
            <button class="chip" type="button" data-value="all" aria-pressed="true">All styles</button>
            <button class="chip" type="button" data-value="scenic" aria-pressed="false">Scenic</button>
            <button class="chip" type="button" data-value="heritage" aria-pressed="false">Heritage</button>
            <button class="chip" type="button" data-value="wellness" aria-pressed="false">Wellness</button>
            <button class="chip" type="button" data-value="cultural" aria-pressed="false">Cultural</button>
            <button class="chip" type="button" data-value="nature" aria-pressed="false">Nature</button>
          </div>
        </div>
      </div>
      <div class="holi-folio-meta">
        <p class="live" id="filter-live" role="status">6 holidays shown.</p>
        <p class="price-note">Illustrative starting prices, per person, twin share. Flights are quoted separately unless a plan says otherwise.</p>
      </div>
    </div>
  </div>

  <div class="holi-list">
''' + pkg(
    "01","swiss","premium","switzerland","long","scenic",
    "images/swiss.jpg","Swiss alpine lake and peaks",
    "8 days / 7 nights · Scenic",
    "Swiss Alpine Escape","₹1,49,999",
    "Scenic train journeys and mountain retreats. Two bases, not six hotels.",
    ["A lake morning with the option to stay on the shore.","A scenic rail segment in daylight, with help at the platform.","One valley walk described in time and gradient, easy to decline.","Evenings back at the same hotel."],
    ["7 nights’ accommodation","Daily breakfast","Scenic rail sector as described","Local host on touring days","Private transfers listed in the plan"],
    ["International flights","Lunches and dinners unless noted","Travel insurance","Personal expenses","Entrance fees not named in the plan"]
) + pkg(
    "02","rajasthan","value","rajasthan","short","heritage",
    "images/palace.jpg","Amber Fort above still water",
    "6 days / 5 nights · Heritage",
    "Royal Rajasthan Journey","₹49,999",
    "Heritage hotels, cultural experiences, and royal hospitality with the afternoons left open.",
    ["Jaipur at a walking pace you choose.","Amber, with the step count discussed before the day.","A courtyard evening: music, or simply the courtyard.","A free morning with no group activity invented to fill it."],
    ["5 nights in heritage or equivalent hotels","Daily breakfast","Private car and driver on touring days","Entrance fees named in the plan","A local host"],
    ["Flights","Most lunches and dinners","Camera fees","Travel insurance","Tips"],
    True
) + pkg(
    "03","kerala","value","kerala","short","wellness",
    "images/backwater.jpg","Houseboat on a Kerala backwater",
    "5 days / 4 nights · Slow living",
    "Kerala Slow Living Retreat","₹39,999",
    "Backwaters, the option of a gentle wellness hour, and nature that does not require a hike.",
    ["A houseboat day with shade and meals on board.","A garden or village landing, only if you want to step off.","One unscheduled afternoon.","A quiet hotel night at either end of the water."],
    ["4 nights’ stay, including the houseboat night","Breakfasts and houseboat meals","Transfers named in the plan","A host on the water day"],
    ["Flights","Wellness treatments unless added","Alcohol","Travel insurance","Personal shopping"]
) + pkg(
    "04","italy","premium","italy","long","cultural",
    "images/tuscany.jpg","Italian coastal village above the sea",
    "7 days / 6 nights · Villages",
    "Italian Countryside Escape","₹1,29,999",
    "Beautiful villages, Italian cuisine, and cultural stops that end in time for a proper evening.",
    ["Two or three bases, so you unpack more than once.","A cooking morning or a market, your choice.","A city hour in good light, not at the opening bell.","Trains where they are simpler than a long car day."],
    ["6 nights’ accommodation","Daily breakfast","Rail or private transfers named in the plan","One hosted meal","A local host on touring days"],
    ["International flights","Most meals","Museum fees not listed","Travel insurance","City tourist taxes, which we will estimate"],
    True
) + pkg(
    "05","japan","premium","japan","long","cultural",
    "images/kyoto.jpg","Kyoto lane and pagoda at dusk",
    "9 days / 8 nights · Cultural",
    "Japan Gardens &amp; Rail","₹1,59,999",
    "Temples, gardens, and trains. Seats are reserved. Days end while you still like the day.",
    ["Kyoto lanes in a small group or privately.","A rail journey with reserved seats and platform help.","A garden with benches, not a march.","One completely free day."],
    ["8 nights’ accommodation","Daily breakfast","Rail passes or tickets named in the plan","Hosted days as listed","Airport transfers if flights are booked with us"],
    ["International flights unless added","Most lunches and dinners","Travel insurance","Personal expenses"]
) + pkg(
    "06","nz","premium","newzealand","long","nature",
    "images/nz.jpg","Auckland harbour at dusk",
    "10 days / 9 nights · Nature",
    "New Zealand Lakes","₹1,79,999",
    "Lakes, short drives, and wildlife from a respectful distance. The route stays in one island unless you ask for more.",
    ["Two nights in most stops.","Scenic drives with breaks written in.","A boat or lakeside morning.","A day with nothing booked, on purpose."],
    ["9 nights’ accommodation","Daily breakfast","Vehicle and driver or self-drive hire as agreed","Activities named in the plan"],
    ["International flights","Most meals","Travel insurance","National park fees not listed","Optional scenic flights"],
    True
) + '''
  </div>
</section>

<section class="band holi-close">
  <img class="bg" data-parallax src="images/dining.jpg" alt="A quiet table set for an unhurried meal" width="1600" height="1000" decoding="async">
  <div class="veil"></div>
  <div class="wrap" data-holi-close>
    <p class="eyebrow">Shape a plan</p>
    <h2>Ready to choose a holiday — or invent one?</h2>
    <p class="lede">Tell us which package feels close, or describe the pace you want. We answer with a written outline, not a brochure dump.</p>
    <p><a class="btn" href="contact.html#enquire">Plan Your Holiday <span class="sq" aria-hidden="true"></span></a></p>
  </div>
</section>
'''

EXP = '''
<section class="page-hero">
  <img class="bg" data-parallax src="images/kyoto.jpg" alt="Two people walking a Kyoto street at dusk">
  <div class="veil"></div>
  <div class="wrap">
    <p class="eyebrow">Experiences</p>
    <h1>Ways of travelling, not a menu of stunts.</h1>
    <p class="lede">Trains, water, culture, wild country, old hotels, and a beach with nothing to prove.</p>
  </div>
</section>
<section class="section" id="trains">
  <div class="wrap split">
    <img data-anim="clip" src="images/swiss.jpg" alt="The alpine country a scenic railway crosses">
    <div data-anim="rise">
      <p class="eyebrow">Rails</p>
      <h2>Luxury train journeys</h2>
      <p>The point of a scenic railway is the window, and the fact that someone else is driving. We book daylight segments, help at the platform, and a seat you do not have to stand for.</p>
      <p>Mountain lines in Switzerland are the clearest example. In Japan, the train is simply how you move, reserved and calm. We do not sell a freight timetable dressed up as romance.</p>
      <p><a class="btn btn-line" href="packages.html#swiss">See the Swiss holiday</a></p>
    </div>
  </div>
</section>
<section class="section band-beige" id="cruises">
  <div class="wrap split">
    <div data-anim="rise">
      <p class="eyebrow">Water</p>
      <h2>Scenic cruises</h2>
      <p>We mean a lake boat, a backwater, or a small ship with time on deck — not a port day that starts in a queue. If a vessel has many stairs, you will hear that before you like the photograph.</p>
      <p>Kerala is the gentlest version. Alpine lakes are the brightest. Ask if you want something longer on the sea, and we will describe the ship in the same plain way.</p>
      <p><a class="btn btn-line" href="packages.html#kerala">See the Kerala holiday</a></p>
    </div>
    <img data-anim="clip" src="images/backwater.jpg" alt="Travellers seated on a Kerala houseboat">
  </div>
</section>
<section class="section" id="culture">
  <div class="wrap split">
    <img data-anim="clip" src="images/haveli.jpg" alt="The Taj Mahal seen through a carved gateway">
    <div data-anim="rise">
      <p class="eyebrow">Culture</p>
      <h2>Cultural experiences</h2>
      <p>A temple lane, a fort, a table, a musician in a courtyard. One of these can be the day. We hire guides who can shorten a story, and we leave before the place becomes a crowd you are trapped inside.</p>
      <p><a class="btn btn-line" href="destinations.html#japan">Explore Japan</a></p>
    </div>
  </div>
</section>
<section class="section band-beige" id="nature">
  <div class="wrap split">
    <div data-anim="rise">
      <p class="eyebrow">Outdoors</p>
      <h2>Nature &amp; wildlife</h2>
      <p>Lookouts you can reach without a scramble. Gardens with seats. Wildlife from a boat or a quiet road, not a forced march. New Zealand and the alpine valleys are where this feels most natural.</p>
      <p><a class="btn btn-line" href="destinations.html#new-zealand">Explore New Zealand</a></p>
    </div>
    <img data-anim="clip" src="images/forest.jpg" alt="Green cliffs in mist with a single road">
  </div>
</section>
<section class="section" id="heritage">
  <div class="wrap split">
    <img data-anim="clip" src="images/hotel.jpg" alt="A low hotel with a lit pool at dusk">
    <div data-anim="rise">
      <p class="eyebrow">Rooms</p>
      <h2>Heritage stays</h2>
      <p>Old buildings are a pleasure when the bed is good and the route to dinner is obvious. We ask about lifts, dinner service, and noise. A palace that looks magnificent and eats your evening in stairs is the wrong palace.</p>
      <p><a class="btn btn-line" href="packages.html#rajasthan">See Rajasthan</a></p>
    </div>
  </div>
</section>
<section class="section band-beige" id="beaches">
  <div class="wrap split">
    <div data-anim="rise">
      <p class="eyebrow">Shore</p>
      <h2>Relaxing beach holidays</h2>
      <p>A beach holiday here is shade, a comfortable room, and the sea within an easy walk or a short transfer. No beach games. No schedule pretending to be leisure.</p>
      <p><a class="btn" href="contact.html#enquire">Ask for a shore journey <span class="sq" aria-hidden="true"></span></a></p>
    </div>
    <img data-anim="clip" src="images/beach.jpg" alt="A quiet beach at sunrise">
  </div>
</section>
'''

ABOUT = '''
<section class="page-hero">
  <img class="bg" data-parallax src="images/garden.jpg" alt="A flowering garden path">
  <div class="veil"></div>
  <div class="wrap">
    <p class="eyebrow">The house</p>
    <h1>We plan the journey you still want to take.</h1>
    <p class="lede">Cairn is a travel house for people who are done with being hurried, and for the families who want a plan they can trust.</p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="prose" data-anim="rise">
      <p class="eyebrow">Story</p>
      <h2>A cairn is a pile of stones that marks the path.</h2>
      <p>Someone has already walked there, noticed the turns, and left a sign that does not shout. That is the work. Not a louder brochure. A clearer way.</p>
      <p>The company began as a refusal. Too many “senior specials” were ordinary coach tours with a larger font and an earlier dinner. The travellers were not the problem. The timetable was.</p>
      <p>So the days got shorter, the groups got smaller, and the questions got more specific. How far do you like to walk? Who is coming with you? Do you want the fort, or the garden beside it?</p>
    </div>
    <img data-anim="clip" src="images/table.jpg" alt="A long outdoor table with several generations sharing a meal">
  </div>
</section>
<section class="section band-beige">
  <div class="wrap">
    <p class="eyebrow">Mission</p>
    <h2>Your pace. Your journey. Your world.</h2>
    <ol class="tenets">
      <li><span>01</span><h3>Unhurried</h3><p>One region is often enough. Rest is part of the design.</p></li>
      <li><span>02</span><h3>Plain spoken</h3><p>Stairs, prices, and limits are written in ordinary words.</p></li>
      <li><span>03</span><h3>Companionable</h3><p>Small groups, or a private plan. Never a crowd you must obey.</p></li>
      <li><span>04</span><h3>For families too</h3><p>Adult children can plan, travel, or simply read the outline and relax.</p></li>
      <li><span>05</span><h3>No theatre</h3><p>We do not dress travel up as medical care, and we do not promise what a doctor must judge.</p></li>
    </ol>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <p class="eyebrow">Why this work</p>
    <h2>Why the house specialises in senior travel</h2>
    <p>Because the industry’s default day is built for someone who can absorb a delay, a steep lane, and a 6 a.m. lobby call without it spoiling the week. Many of our travellers can do all of that. They should not have to.</p>
    <p>Specialising means the hotels are questioned, the driving hours are capped, and a solo traveller is expected — not accommodated as a favour. It also means a son or daughter in another city can understand the plan without translating a brochure.</p>
    <p>It does not mean a narrow life. Switzerland is still Switzerland. Jaipur is still vivid. The difference is that you arrive with some of the day still yours.</p>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <p class="eyebrow">Companions</p>
    <h2>The people you would meet</h2>
    <p class="note">Demonstration portraits and names, not a live team. A real company would publish the people who actually answer the phone.</p>
    <div class="people" style="margin-top:1.4rem">
      <article class="person"><img src="images/portrait-a.jpg" alt="Demonstration portrait of a journey planner"><h3>Leela Narayan</h3><p><strong>Journey planner.</strong> She writes the days so a family can read them once and know what they agreed.</p></article>
      <article class="person"><img src="images/portrait-b.jpg" alt="Demonstration portrait of a tour manager"><h3>Joseph Mathew</h3><p><strong>Tour manager.</strong> He travels with small groups and treats a change of plan as normal work.</p></article>
      <article class="person"><img src="images/portrait-c.jpg" alt="Demonstration portrait of a guest-care lead"><h3>Amina Qureshi</h3><p><strong>Guest care.</strong> She is the voice before you leave, and the number in your pocket while you are away.</p></article>
    </div>
  </div>
</section>
'''

SAFETY = '''
<section class="page-hero">
  <img class="bg" data-parallax src="images/hotel.jpg" alt="A calm hotel courtyard at dusk">
  <div class="veil"></div>
  <div class="wrap">
    <p class="eyebrow">Care, without the clinic</p>
    <h1>Safety and comfort, said plainly.</h1>
    <p class="lede">We design for ease and we name the limits. This page is not a medical guarantee, and a holiday is not a promise that nothing can go wrong.</p>
  </div>
</section>
<section class="section">
  <div class="wrap prose">
    <h2>How a journey is planned</h2>
    <p>Every outline starts with questions: who is travelling, how you like a morning to begin, how long you want to be away from the room, and what would make a day feel like a waste. The timetable is written after those answers, not before.</p>
    <p>Driving and rail time are capped in the plan you approve. If a famous sight would break that cap, we offer it as a choice, not a surprise.</p>
  </div>
</section>
<section class="section band-beige">
  <div class="wrap trust-grid">
    <div>
      <h2>What we look at</h2>
      <p>These are standards of selection and communication. They are not a certificate, and they are not the same in every building or every country.</p>
    </div>
    <ol class="trust-list">
      <li><b>01</b><span><strong>Accommodation.</strong> Quiet, a comfortable bed, dinner that can be served at a civilised hour, and a true description of stairs or a lift.</span></li>
      <li><b>02</b><span><strong>Transport.</strong> The vehicle or carriage, the length of the ride, and where you will be met. Step-free access is stated when it is real, and not implied when it is not.</span></li>
      <li><b>03</b><span><strong>The day itself.</strong> Walking time, shade, seats, and a return that is not an afterthought.</span></li>
      <li><b>04</b><span><strong>People.</strong> A named host on the ground and a planner you can call. They coordinate. They do not provide medical care.</span></li>
      <li><b>05</b><span><strong>Food.</strong> Diets are passed on in writing. We also tell you what to reconfirm, because a kitchen can still miss a note.</span></li>
      <li><b>06</b><span><strong>If something changes.</strong> Weather, a closure, or a tired afternoon. The plan says who decides, and how you hear about it.</span></li>
    </ol>
  </div>
</section>
<section class="section">
  <div class="wrap" style="max-width:860px">
    <h2>Questions people ask before they book</h2>
    <div class="acc">
      <div class="acc-item"><button class="acc-btn" type="button" aria-expanded="false">Do you guarantee a safe trip?</button><div class="acc-panel"><div><p>No. Travel has ordinary risks: roads, weather, uneven stone, other people. We reduce hurry and confusion. We do not insure you against the world, and we do not make medical promises. Take out travel insurance that matches your needs, and speak with your doctor about your own health.</p></div></div></div>
      <div class="acc-item"><button class="acc-btn" type="button" aria-expanded="false">What assistance is arranged?</button><div class="acc-panel"><div><p>A tour manager on small-group journeys, or a local host and an on-call planner for private ones. They help with timing, hotels, and changes of plan. They are not nurses or doctors. If you want a travelling companion with a clinical role, tell us, and we will say whether that sits outside what we arrange.</p></div></div></div>
      <div class="acc-item"><button class="acc-btn" type="button" aria-expanded="false">What if a place is not step-free?</button><div class="acc-panel"><div><p>We say so before you pay. Some forts, gardens, trains, and boats have steps that cannot be removed. You can skip them, see them from another point, or choose a different journey. We would rather lose a photograph than surprise you at the door.</p></div></div></div>
      <div class="acc-item"><button class="acc-btn" type="button" aria-expanded="false">Who do we call during the trip?</button><div class="acc-panel"><div><p>You receive names and numbers before departure: the host with you, the planner at the house, and the hotel. Families at home can have the same note, if the travellers want them to.</p></div></div></div>
      <div class="acc-item"><button class="acc-btn" type="button" aria-expanded="false">What should we tell you about mobility or diet?</button><div class="acc-panel"><div><p>As much as you want the plan to reflect. Walking distance, a stick or wheelchair, stairs you prefer to avoid, foods you do not eat, and the hour you like to stop. The more specific the note, the more honest the itinerary.</p></div></div></div>
    </div>
    <p style="margin-top:1.5rem"><a class="btn" href="contact.html#enquire">Talk it through <span class="sq" aria-hidden="true"></span></a></p>
  </div>
</section>
'''

CONTACT = '''
<section class="page-hero">
  <img class="bg" data-parallax src="images/hills.jpg" alt="Late sun over open fields">
  <div class="veil"></div>
  <div class="wrap">
    <p class="eyebrow">Begin</p>
    <h1>Plan your holiday.</h1>
    <p class="lede">Write with a month, a place, and the people who are going. If you are booking for your parents, say so. The questions are the same, and the plan can be read by all of you.</p>
  </div>
</section>
<section class="desk" id="enquire">
  <div class="desk-shell">
    <figure class="desk-media">
      <img src="images/table.jpg" alt="A quiet table set for a slow meal by the window">
      <figcaption>
        <p class="eyebrow">Contact</p>
        <p>Write with a month, a place, and the people who are going.</p>
      </figcaption>
    </figure>
    <div class="desk-letter">
      <header class="desk-intro">
        <p class="eyebrow">Enquiry</p>
        <h2>Tell us the journey you want.</h2>
        <p>This form stores your note in this browser only. It does not reach a live desk. On a working site it would go to a planner.</p>
        <p><a href="mailto:hello@cairn.example">hello@cairn.example</a> · <a href="tel:+918040002100">+91 80 4000 2100</a></p>
      </header>
      ''' + s.form("contact-enquire") + '''
    </div>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap">
    <div class="map-note">
      <p><strong>Map unavailable on purpose.</strong><br>A Google map will be embedded here when Cairn has a public studio address. Until then, write or call, and we will say where to meet.</p>
    </div>
  </div>
</section>
'''

# contact form is injected - but s.form returns a form that should sit in the grid. The enquire-grid is 2 columns. The form is the second column. Good. But I closed the first div and then the form and then the section. The form function returns a form element, not wrapped. The grid expects two children. First div and form. Good.

PRIVACY = '''
<section class="section legal">
  <div class="wrap prose">
    <p class="eyebrow">Demonstration text</p>
    <h1>Privacy policy</h1>
    <p>This is sample policy language for a demonstration website. It is not legal advice and it does not describe a live company. Replace it with a policy written for the real business before collecting anyone’s information.</p>
    <h2>What a working version would collect</h2>
    <p>An enquiry form would collect the name, phone, email, destination, travel dates, number of travellers, and any note you choose to add about pace, diet, or mobility. That note can be sensitive. A real company should say why it is needed, who sees it, and how long it is kept.</p>
    <h2>What this demonstration does</h2>
    <p>The forms on this site do not send data to a server. If your browser allows it, the note is saved in local storage on your own device so the interaction can be tried. You can clear it by clearing site data for this page. The newsletter box behaves the same way.</p>
    <h2>What we do not do here</h2>
    <p>We do not run advertising trackers, we do not sell a list, and we do not embed a map that would hand your visit to another service. Fonts are requested from Google Fonts, and animation scripts from a public CDN, which means those providers may see a request for the file.</p>
    <h2>Your choices</h2>
    <p>You can use the pages without sending a form. You can switch off motion. You can decide not to describe health or mobility at all until you are speaking with a real planner under a real policy.</p>
    <p><a href="contact.html">Back to contact</a></p>
  </div>
</section>
'''

TERMS = '''
<section class="section legal">
  <div class="wrap prose">
    <p class="eyebrow">Demonstration text</p>
    <h1>Terms &amp; conditions</h1>
    <p>These terms are sample copy for a design demonstration. They are not a contract, not legal advice, and not the terms of a company you can book with today.</p>
    <h2>Prices</h2>
    <p>Figures on this website are illustrative starting points in Indian rupees. They are not quotations. A real booking price would depend on travel dates, availability, room type, group size, and the inclusions you agree in writing.</p>
    <h2>What a plan would need to say</h2>
    <p>Before any money changed hands, a working company would set out what is included, what is excluded, when a deposit is due, how a cancellation is treated, and what happens if a hotel or route must change. None of that machinery exists on this demonstration site.</p>
    <h2>Travel itself</h2>
    <p>Holidays involve ordinary risks. Nothing on this website promises a medical outcome, a risk-free journey, or that every building will be step-free. Insurance and medical advice sit with you and the professionals you choose.</p>
    <h2>Stories and portraits</h2>
    <p>Testimonials, star ratings, and staff portraits are invented for the layout. They are not customer reviews and not a claim about real employees.</p>
    <h2>Using the pages</h2>
    <p>You may look through this demonstration freely. Do not treat the phone number, email, or WhatsApp draft as a channel to a real desk.</p>
    <p><a href="index.html">Return home</a></p>
  </div>
</section>
'''

if __name__ == "__main__":
    s.page("destinations.html", "Destinations — Cairn", "Slow journeys in Switzerland, Italy, Japan, Rajasthan, Kerala, and New Zealand.", "destinations", DEST)
    s.page("packages.html", "Holiday packages — Cairn", "Filter illustrative senior-friendly holidays by budget, destination, duration, and style.", "packages", PACKAGES)
    s.page("experiences.html", "Travel experiences — Cairn", "Trains, scenic water, culture, nature, heritage stays, and quiet beaches.", "experiences", EXP)
    s.page("about.html", "About Cairn", "Why Cairn plans unhurried holidays for senior travellers and their families.", "about", ABOUT)
    s.page("safety.html", "Safety and comfort — Cairn", "How Cairn plans pace, hotels, transport, and assistance, without medical guarantees.", "safety", SAFETY)
    s.page("contact.html", "Contact Cairn", "Send a holiday enquiry. Demonstration contact details and a planning form.", "contact", CONTACT)
    s.page("privacy.html", "Privacy policy — Cairn", "Sample privacy note for the Cairn demonstration website.", "privacy", PRIVACY)
    s.page("terms.html", "Terms and conditions — Cairn", "Sample terms for the Cairn demonstration website.", "terms", TERMS)
