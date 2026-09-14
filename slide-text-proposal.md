# Slide text proposal — warmer, more descriptive paragraphs

> Goal: replace some of our terse/fragmented phrasing with the PDF's own descriptive
> paragraphs (the tone you liked — see the "Big data analysis" example you quoted),
> copied **almost verbatim**. Nothing is implemented yet — this is for your review.
>
> Source tags: `[PDF pN]` = homepedia_project.pdf, page N · `[PPTX sN]` = homepedia-kickoff.pptx, slide N.

---

## What I'm proposing to change (6 slides)

These are the slides that currently read as fragmented chips/bullets where the PDF
has real, warm prose we can lift almost as-is.

### 1. "The Project"

**Current (our own invented phrasing):**
> You're not building a real-estate listings website. You're building a decision-support
> tool for the property market that explains the territory: why prices, inequalities and
> risks vary from place to place — and what we can anticipate.

**Proposed (near-verbatim PDF intro, `[PDF p1]` + `[PDF p2]`):**
> Through data collection, processing, and analysis, you will create a platform which
> offers a user-friendly and interactive experience, empowering users to explore and sift
> through the intricate dynamics of the French real-estate landscape.
>
> Whether it's examining price trends, exploring regional variations, or delving into
> demographic factors, your app will serve as a tool for users to access the statistics
> and insights they desire.
>
> **In this project, you will be doing DataOps.** *(kept as its own emphasized line — it's
> the PDF's own framing of the whole module)*

*Keeps: the audience note ("Built for professionals & decision-makers…") and the
Collect → Cross-reference → Explain flow — those aren't in the PDF, but they're useful
scaffolding, not filler.*

** Retenu : **
In this project, you will be doing DataOps to build a powerful decision-support tool for the property market, moving far beyond a standard real-estate listings website.Through data collection, processing, and analysis, you will create a platform that explains the territory—revealing exactly why prices, inequalities, and risks vary from place to place, and what we can anticipate next. Your app will serve as a user-friendly, interactive experience that empowers users to access the statistics and insights they desire. Whether they are examining regional price trends, exploring demographic factors, or sifting through the intricate dynamics of the French real-estate landscape, your platform will turn complex data into actionable territory intelligence.

---

### 2. "Interactive Data Exploration"

**Current (chip fragments):**
> Your app must let users explore the property market themselves — an interactive,
> highly customizable experience built on tables and maps.
> [Tabular data] Sortable & filterable tables of key indicators — ideally cross-referenced and exportable.
> [chips: Price/m² · Price evolution · Demographic · Infrastructure]
> [Cartographic data] Choose the representation that fits the data you're showing.
> [chips: Bubble · Isoline · Choropleth · Heat · Route · Connection]

**Proposed (near-verbatim PDF, `[PDF p4]`):**
> Present the results through an interactive app, using visualizations to provide an
> intuitive and comprehensive understanding of housing trends.
>
> These steps are fundamental: your app effectively investigates and represents the
> data. Your outputs encompass traditional tabular presentations, showcasing statistical
> insights. Additionally, your app also incorporates cartographic analysis, allowing users
> to visualize data on bubble, isoline, choropleth, heat, route, or connection maps.
>
> You have the freedom to design the app according to your preferences, but it must be
> highly interactive and customizable: your final users are able to navigate and select
> what they want to explore — areas, analysis results, global indicators. The analysis
> must span various levels, including city, department, and region.
>
> *(Tabular Data, `[PDF p4]`):* Deliver sortable and filterable tables presenting the key
> statistical indicators of your dataset — price per m², price evolution, demographic and
> infrastructure metrics — at the various levels of granularity. Users must be able to
> cross-reference indicators and, ideally, export the displayed data.

*This is the single biggest rewrite — it turns 2 chip-cards into the PDF's actual
paragraph, which already covers tabular + cartographic + interactivity + scale in one
flowing explanation. I'd keep the map-type chips as a small visual list under the prose
(cheap visual anchor), not delete them.*

---

### 3. "Big Data & the Data Pipeline" — the slide you quoted

**Current:**
> Big Data means data whose Volume, Variety and Velocity are high enough to require
> dedicated tools and methods to turn into value.
> [flow: Collect → Organize → Process → Visualize]
> Note: For Homepedia, focus on Volume & Variety. Real-time (Velocity) is a bonus…

**Proposed — add the exact paragraph you highlighted (`[PDF p4]`, "Big data analysis"):**
> Make use of advanced tools and methods in order to extract valuable insights from the
> huge amount of data.
>
> To tackle the immense volume of data involved in this project, you have to use
> technologies for fast and efficient data processing, such as **Hadoop** and **Spark**.
>
> By creating a **cluster of machines**, you will distribute the workload across multiple
> nodes, significantly reducing processing time and enabling parallel data processing.

*I'd keep the Volume/Variety/Velocity line (from `[PPTX s2]`) as a short intro sentence,
then this paragraph as the main body, then keep the flow diagram and the real-time-bonus
note below. Net effect: same slide, but with the actual paragraph you said you liked,
almost word-for-word.*

---

### 4. "Textual Data & Responsible Collection"

**Current (already a paraphrase, fairly close):**
> Beyond tables, AI has a role to play: text such as comments describing a city's
> qualities or shortcomings can be processed — for example with sentiment analysis —
> to extract genuinely valuable information.
> [card] At least one source must be textual, and it must be turned into something
> usable — e.g. a satisfaction score per town built from reviews — not simply stored or
> listed as raw comments.
> Note: In that spirit: how often is a given word — say, "rats" — mentioned in local
> reviews of an area?

**Proposed (tightened to verbatim, `[PDF p3]` + `[PDF p2]`):**
> While the primary focus lies in collecting and analyzing vast amounts of data, there is
> a crucial role for artificial intelligence to play. Textual data, such as comments
> describing the quality or shortcomings of a city, can be efficiently processed and
> analyzed using AI techniques, to extract valuable information such as sentiment
> analysis.
>
> *(card, verbatim)* At least one of your sources should be a textual one. This type of
> data mustn't be simply mapped to its source or presented as a list of comments, but it
> should be processed in a way that makes it usable.
>
> *(note, verbatim example from the PDF)* "How many times are rats mentioned in reviews
> in the local restaurants in this region?"

*Small change, but worth it: this makes the slide word-for-word the PDF instead of our
paraphrase — including the actual example question as written, rather than our
softened version.*

---

### 5. "Helping with Data Representation" — small intro tweak

**Current:**
> Picking the right chart or map for your data is as important as building it. These
> resources can help.

**Proposed (verbatim, `[PDF p4]`, the actual warning text):**
> One of the trickiest parts of the analysis process is choosing the right way to
> represent your data — and to avoid any chartjunk.

*One sentence swap, but it's the PDF's own words and it directly motivates the resource
list that follows (chartjunk is literally the first resource linked on this slide).*

---

### 6. "Data Sourcing & Processing Documentation"

**Current (bullet fragments in 3 cards):**
> [API documentation] Which API was used / What data was retrieved / For what purpose
> [Data cleaning documentation] Cleaning & preparation steps applied / A well-defined
> database schema / A clear description of the methodology
> [AI documentation] Implementation details / How it functions / How it's applied to your data

**Proposed (near-verbatim PDF sentences replacing the fragments, `[PDF p1]` + `[PDF p2]`):**
> To provide a comprehensive understanding of your project's foundation, a well-defined
> schema of your database(s), along with a meticulous description of your data-cleaning
> methodology, must be included.
>
> If AI algorithms are utilized within the project, it is essential to provide a detailed
> account of their implementation and functionality.

*This one shrinks from 3 cards to essentially 2 real sentences — the PDF is more concise
here than our bullet version, interestingly. I'd keep a light 2-card layout (schema+cleaning
/ AI) rather than 3, since the PDF doesn't really separate "API documentation" as its own
paragraph — that bullet was something we synthesized, not sourced.*

---

## What I'm deliberately leaving as-is (and why)

- **The six grading-criteria slides** (Data Gathering & Sourcing, Database Organization,
  etc.) — these are quoting `homepedia-grading_scale.md` almost verbatim already, and
  that document is *itself* written as "1 point per valid statement" — a checklist by
  design. Converting it to prose would misrepresent how you'll actually grade.
- **Logistics, Timeline, Six-axes overview, Bonuses, Your Next Two Hours** — these are
  our own scaffolding (dates, team size, action steps), not sourced from the PDF/PPTX, and
  a list is the right format for them.
- **Examples of Topics, Examples of Existing Web Apps, Explanatory Variables & Data
  Sources, Useful Libraries** — reference/example material where short cards, a table, or
  a link list are more useful to a student than prose would be.

## One trade-off to flag before we implement

Several of these paragraphs are noticeably longer than our current chip/card text —
that's the whole point, but it means those slides will carry more text than the rest of
the deck. On a 1280×720 slide this should still fit comfortably (the PDF paragraphs are
short enough), but a couple of slides (especially #2, "Interactive Data Exploration")
will look denser than their neighbors. I think that's fine — variety in slide density
isn't a bad thing — but flagging it so it's not a surprise.

---

Let me know which of the 6 you want as proposed, which need tweaking, and whether you'd
like anything reworded before I touch the HTML.
