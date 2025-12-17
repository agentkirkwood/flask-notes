# Bokeh - Interactive Visualization for Web Browsers

Bokeh is a Python library for creating interactive visualizations for web browsers. It's particularly well-suited for Flask applications because it generates JavaScript-based plots that can be embedded directly in HTML.

## Key Features

* **Interactive plots** - Built-in tools for panning, zooming, hovering, selecting
* **Web-native** - Renders using HTML5 Canvas or WebGL, no plugins needed
* **Large datasets** - Handles millions of data points efficiently
* **Server-side Python** - Generate plots with Python, display in browser with JavaScript

## Common Use Cases

* Dashboards and data exploration tools
* Real-time streaming data visualization
* Scientific and statistical plots
* Heatmaps, scatter plots, time series

## Flask Integration Pattern

The typical pattern for embedding Bokeh plots in Flask applications:

```python
from bokeh.embed import components
from bokeh.resources import INLINE
from bokeh.plotting import figure
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/plot')
def plot():
    # Create plot
    p = figure(title="My Plot", width=600, height=400)
    p.circle([1, 2, 3], [4, 5, 6])
    
    # Generate JavaScript/HTML components
    script, div = components(p)
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    
    # Pass to template
    return render_template('page.html', 
                           plot_script=script, 
                           plot_div=div,
                           js_resources=js_resources,
                           css_resources=css_resources)
```

### Template Integration

In your HTML template:

```html
<!DOCTYPE html>
<html>
<head>
    {{ js_resources|safe }}
    {{ css_resources|safe }}
</head>
<body>
    <h1>My Bokeh Plot</h1>
    {{ plot_div|safe }}
    {{ plot_script|safe }}
</body>
</html>
```

## Creating Different Plot Types

### Scatter Plot

```python
from bokeh.plotting import figure

p = figure(title="Scatter Plot", width=600, height=400)
p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10, color="navy", alpha=0.5)
```

### Line Plot

```python
p = figure(title="Line Plot", width=600, height=400)
p.line([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], line_width=2)
```

### Heatmap

```python
from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
from bokeh.plotting import figure

p = figure(title="Heatmap",
           x_range=x_labels, 
           y_range=y_labels,
           width=600, 
           height=400,
           toolbar_location='below',
           tools="hover,save,pan,box_zoom,reset,wheel_zoom")

mapper = LinearColorMapper(palette="Viridis256", low=0, high=100)

p.rect(x="x", y="y", width=1, height=1,
       source=source,
       fill_color={'field': 'value', 'transform': mapper},
       line_color=None)
```

## Bokeh 3.x Updates

If you're upgrading from older versions of Bokeh, note these important changes:

### Deprecated Parameters

- `plot_width` → `width`
- `plot_height` → `height`
- `bokeh.util.string.encode_utf8` → No longer needed (removed)

### Example Migration

**Old (Bokeh 2.x):**
```python
from bokeh.util.string import encode_utf8

p = figure(plot_width=600, plot_height=400)
# ... add glyphs ...
html = render_template('page.html', ...)
return encode_utf8(html)
```

**New (Bokeh 3.x):**
```python
p = figure(width=600, height=400)
# ... add glyphs ...
html = render_template('page.html', ...)
return html  # No encoding needed
```

## Interactive Tools

Bokeh plots come with built-in interactive tools:

- **Pan** - Click and drag to move around the plot
- **Box Zoom** - Select an area to zoom into
- **Wheel Zoom** - Scroll to zoom in/out
- **Reset** - Return to original view
- **Save** - Download plot as PNG
- **Hover** - Show tooltips on data points

Enable tools when creating a figure:

```python
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"
p = figure(tools=TOOLS, toolbar_location='below')
```

## HoverTool Customization

Add custom tooltips to show data on hover:

```python
from bokeh.models import HoverTool

hover = HoverTool(tooltips=[
    ("Index", "$index"),
    ("(X,Y)", "($x, $y)"),
    ("Value", "@value"),
    ("Label", "@label")
])

p.add_tools(hover)
```

## Alternatives to Bokeh

* **Matplotlib** - Static images, simpler but not interactive
* **Plotly** - Similar to Bokeh, also interactive, different API
* **D3.js** - More control but requires JavaScript expertise
* **Altair** - Declarative visualization based on Vega-Lite

## When to Use Bokeh

Bokeh is ideal when you need:
- Interactive, publication-quality visualizations
- Web-based dashboards without JavaScript knowledge
- Large dataset visualization (millions of points)
- Integration with existing Flask/Django applications
- Real-time streaming data displays

## Resources

- [Official Documentation](https://docs.bokeh.org/)
- [Gallery of Examples](https://docs.bokeh.org/en/latest/docs/gallery.html)
- [Tutorial](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb)
- [Discourse Community](https://discourse.bokeh.org/)
