from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
	output_file('simple_graph.html')
	fig = figure()
	
	total_values = int(input('How many values do you wanna graph?: '))
	x_values = list(range(total_values))
	y_values = []

	for x in x_values:
		val = int(input(f'Value Y for {x}: '))
		y_values.append(val)

	fig.line(x_values, y_values, line_width=2)
	show(fig)

	