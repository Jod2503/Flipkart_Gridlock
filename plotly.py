import plotly.io as pio

pio.templates["traffic"] = pio.templates["plotly_white"]

pio.templates["traffic"].layout.colorway = [
    "#B91C1C",
    "#DC2626",
    "#EF4444",
    "#F87171",
    "#991B1B"
]

pio.templates.default = "traffic"
