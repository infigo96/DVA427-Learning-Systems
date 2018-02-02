h = plot(x,y)
legend('performance')
ax = ancestor(h, 'axes');
r = ax.YAxis;
r.Exponent = 0;
r.TickLabelFormat = '%g';
xlim([0,1002])