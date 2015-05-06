import pygal

bc = pygal.Bar()
bc.title = 'Github Users in Africa by Country'
bc.add()
bc.render_to_file('chart.svg')
