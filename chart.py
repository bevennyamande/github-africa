import pygal

bc = pygal.Bar()

# set the title for the graph
bc.title = 'Github Users in Africa by Country'

#add the country as well as the users and percentage
bc.add()

# save the chart to a file
bc.render_to_file('chart.svg')
