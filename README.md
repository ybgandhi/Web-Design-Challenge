# Web-Design-Challenge

Use HTML, CSS and BOOTSTRAP to create a web page that displays visualizations and the data that is used to create the visualizations.

## Web Visualization Dashboard

Create a visualization dashboard website using climate visualization plots.

Create individual pages for each plot and navigate between them. These pages contain the visualizations and their corresponding explanations.

Landing page that has a comparison of all of the plots, and another page where the data displays as an html table.

* A [landing page](#landing-page) containing:
  * An explanation of the project.
  * Links to each visualizations page. There should be a sidebar containing preview images of each plot, and clicking an image should take the user to that visualization.

* Four [visualization pages](#visualization-pages), each with:
  * The plot/visualization itself for the selected comparison.
  * A paragraph describing the plot and its significance.

  * A ["Comparisons" page](#comparisons-page) that:
  * Contains all of the visualizations on the same page so it can be easily compared
  * Uses a Bootstrap grid for the visualizations.
    * The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.

  * A ["Data" page](#data-page) that:
  * Displays a responsive table containing the data used in the visualizations.
  * Data comes from csv_to_html.py using Pandas library feature `to_html`
 