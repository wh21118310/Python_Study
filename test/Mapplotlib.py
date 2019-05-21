from bokeh.plotting import figure,output_notebook,show
output_notebook()
p = figure(plot_width=400,plot_height=400)
nan = float('nan')
p.patch([1,3,2,1, 2, 4, nan, 4, 5, 6], [3,4,5,6, 7, 5, nan, 7, 3, 6], alpha=0.5, line_width=2)
print(show(p))
