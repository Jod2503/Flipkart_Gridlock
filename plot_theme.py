import plotly.io as pio

# Base template
traffic_template = pio.templates["plotly_white"]

# Professional color palette
traffic_template.layout.colorway = [

    "#4F46E5",  # Indigo
    "#6366F1",  # Soft Indigo
    "#8B5CF6",  # Purple
    "#0EA5E9",  # Sky Blue
    "#10B981",  # Emerald
    "#F59E0B",  # Amber
    "#EC4899",  # Pink

]

# Layout settings
traffic_template.layout.paper_bgcolor = "#F8FAFC"
traffic_template.layout.plot_bgcolor = "#FFFFFF"

traffic_template.layout.font = dict(

    family="Inter",
    size=15,
    color="#111827"

)

traffic_template.layout.title = dict(

    font=dict(
        family="Inter",
        size=22,
        color="#111827"
    )

)

traffic_template.layout.legend = dict(

    font=dict(
        family="Inter",
        size=13
    )

)

traffic_template.layout.xaxis = dict(

    showgrid=True,
    gridcolor="#E5E7EB",
    zeroline=False

)

traffic_template.layout.yaxis = dict(

    showgrid=True,
    gridcolor="#E5E7EB",
    zeroline=False

)

traffic_template.layout.margin = dict(

    l=40,
    r=40,
    t=60,
    b=40

)

# Register template
pio.templates["traffic"] = traffic_template

# Make default
pio.templates.default = "traffic"
