# Web Design Challenge
**Completed By:** Lauren Stein\
**Objective:** Use HTML, CSS and BOOTSTRAP to create a web page that displays the raw data file and associated graphs from the OpenWeather API analysis of latitude vs. weather metrics. 

<img src="/Resources/lms_assets/Screen Shot 2020-09-03 at 6.16.45 PM.png">
---

## Web Visualization Dashboard

Leverage HTML, CSS, and Bootstrap to create an interactive visualization dashboard website using climate visualization plots.

Each plot is linked to an individual page and allows for easy navigation between them. Each page contains the visualizations and corresponding analysis.

Two additional landing pages were created for comparison of all the plots and another page that displays the data as an html file. 

### Website Details:

* Landing Page:
  * An explanation of the project.
  * Links to each visualizations page.

* Visualization Pages:
  * A descriptive title and heading tag.
  * The plot/visualization itself for the selected comparison.
  * A paragraph describing the plot and its significance.

* Comparison Page:
  * Contains all of the visualizations on the same page so we can easily visually compare them.
  * Uses a bootstrap grid for the visualizations.
    * The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.

* Data PageL 
  * Displays a responsive table containing the data used in the visualizations.
    * The table must be a bootstrap table component.
    * The data came from converting the `.csv` file  to HTML using the pandas method `to_html`.
