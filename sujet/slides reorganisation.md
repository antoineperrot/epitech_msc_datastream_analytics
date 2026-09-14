Reorganization of the presentation
After reviewing the current presentation, I would like to reorganize and complete the slides as follows.
The main objective is to make the presentation more coherent, avoid redundancy, and create a clear progression:
Project → Data & topics → Data representation → Technologies & methodology → Evaluation criteria → Next steps

Section 1 — Project Presentation
Slide 1 — The Project
Condense the existing slides:
	•	The goal of the app
	•	Who is it for?
	•	Real questions your app answers
These should become a single, concise slide introducing the project.
Important change
Remove the slide “The question behind the data”. I don't think this framing is appropriate for the presentation.

Slide 2 — Examples of Topics
Create a new slide called:
“Examples of Topics”
Merge the content currently presented in:
	•	“Pick your destination”
	•	“One example per family”
These two slides are quite similar and can be combined into a single slide presenting examples of questions/topics that users could explore with the application.

Slide 3 — Examples of Existing Web Apps
Move the existing “Inspiration” slide here.
The objective is to show examples of existing applications/websites that can serve as references for the type of experience, visualization, or analysis we could provide.
The links should be clickable.
Real-life examples for inspiration
	•	Zillow : https://www.zillow.com/
	•	MeilleursAgents : https://www.meilleursagents.com/prix-immobilier/
	•	Mapbox : https://www.mapbox.com/industries/real-estate
	•	Gapminder : https://www.gapminder.org/tools/#$chart-type=bubbles&url=v1
	•	Villes à vivre : https://www.villesavivre.fr/
	•	Data pathologies : https://data.ameli.fr/pages/data-pathologies/
	•	Numbeo : https://www.numbeo.com/cost-of-living/

Slide 4 — Explanatory Variables & Data Sources
Merge the idea of “Examples of explanatory variables” with “Sources & APIs”.
For each example, show:
Explanatory variable → Example of data/source → URL
For example, the slide should illustrate what kinds of explanatory variables can be used and where the corresponding data can be obtained.
Important
	•	Include the relevant URLs as clickable links.
	•	Do not mention the scripts used to retrieve the data. Those are only for my personal usage and should not appear in the presentation.

Section 2 — Data Representation & Exploration
Slide 5 — Interactive Data Exploration
Create a slide based on the existing content about Interactive Visualizations.
The slide should explain that the application must provide an interactive way to explore the housing market through different forms of data representation.
Key points to communicate
	•	Present results through an interactive application.
	•	Use visualizations to provide an intuitive and comprehensive understanding of housing trends.
	•	Allow users to explore and investigate the data themselves.
	•	Provide both:
	◦	Tabular analysis
	◦	Cartographic analysis
	•	Support different types of maps, such as:
	◦	Bubble maps
	◦	Isoline maps
	◦	Choropleth maps
	◦	Heat maps
	◦	Route maps
	◦	Connection maps
	◦	etc.
	•	The application should be highly interactive and customizable.
	•	Users should be able to select what they want to explore:
	◦	Areas
	◦	Analysis results
	◦	Global indicators
	◦	etc.
	•	The analysis must cover multiple geographical scales:
	◦	City
	◦	Department
	◦	Region
Tabular data
The application should provide sortable and filterable tables containing key statistical indicators, such as:
	•	Price per m²
	•	Price evolution
	•	Demographic indicators
	•	Infrastructure indicators
	•	etc.
Users should ideally be able to cross-reference indicators and export the displayed data.
Cartographic data
Emphasize the importance of choosing an appropriate visualization for each type of data.

Slide 6 — Helping with Data Representation
Create a slide presenting useful resources for choosing appropriate visual representations.
Resources
	•	Chartjunk : https://en.wikipedia.org/wiki/Chartjunk
	•	AnyChart : https://www.anychart.com/chartopedia/usage-type/
	•	Data Viz Catalogue : https://datavizcatalogue.com/search.html
	•	From Data to Viz : https://www.data-to-viz.com/
	•	DataViz Project : https://datavizproject.com/
The purpose of this slide is to show that choosing the right visualization is an important part of the project.

Section 3 — Technologies & Methodology
Slide 7 — Big Data & Data Pipeline
Condense the following existing content into one slide:
	•	Context: Big Data 101
	•	The expected data pipeline
The slide should provide a concise overview of:
	•	What makes the project a Big Data project
	•	The different stages of the data pipeline
	•	How data moves from collection to processing and visualization

Slide 8 — Textual Data & Responsible Data Collection
Condense the existing slides:
	•	Your mandatory textual source
	•	Responsible data collection
The slide should explain both the importance of textual data and the responsible approach to collecting it.
Include the following idea about AI
While the primary focus lies in collecting and analyzing vast amounts of data, there is a crucial role for artificial intelligence to play. Textual data, such as comments describing the quality or shortcomings of a city, can be efficiently processed and analyzed using AI techniques to extract valuable information such as sentiment analysis.
The slide should therefore make clear that textual data is not simply collected and displayed. It should be processed and analyzed to extract useful information.

Slide 9 — Useful Libraries for the App & Data Visualization
Create a slide called:
“Useful Libraries for the App & Data Visualization”
Present the main Python libraries/tools used or relevant to the project.
Streamlit
https://streamlit.io/
→ Used to create the interactive application.
Leaflet
https://leafletjs.com/examples.html
→ Used to build and integrate interactive maps.
Plotly
https://plotly.com/
→ Used to create interactive data visualizations.
The links should be clickable.

Slide 10 — Data Sourcing & Processing Documentation
Create a slide explaining what should be documented regarding data sourcing and processing.
Include the following requirements
API documentation
Provide a list of the APIs used and explain:
	•	Which API was used
	•	What data was retrieved
	•	For what purpose
Data cleaning documentation
Explain the data cleaning and preparation processes applied to the collected datasets.
The slide should also mention the requirement to provide:
	•	A well-defined schema of the database(s)
	•	A clear description of the data-cleaning methodology
AI documentation
If AI algorithms are used, provide a detailed explanation of:
	•	Their implementation
	•	Their functionality
	•	How they are applied to the data

Section 4 — Evaluation Criteria
Keep the existing structure based on:
	•	“Six axes”
	•	One slide for each axis
	•	Bonuses
This section should remain focused on the evaluation criteria and expectations of the project.
Remove
Delete the slide:
“Get Started”

Final Slide — Your Next Two Hours
Keep the final slide:
“Your Next Two Hours”
It should provide a clear and practical transition from the presentation to the work to be done.

General Presentation Guidelines
Throughout the presentation:
	•	Avoid unnecessary repetition between slides.
	•	Merge slides when they cover essentially the same idea.
	•	Keep the structure clear and progressive.
	•	Make all relevant external links clickable.
	•	Do not include technical implementation details that are only useful for internal work, such as scraping/retrieval scripts.
	•	Keep the presentation informative and constructive.
Important tone adjustment
Remove comments such as:
“Get inspired — don't copy.”
I don't want the presentation to feel threatening, defensive, or menacing. The tone should remain professional, positive, and encouraging, while still clearly presenting the expectations and constraints of the project.
