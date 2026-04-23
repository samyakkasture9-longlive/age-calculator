import ipywidgets as widgets
from IPython.display import display, clear_output
from datetime import date

# Define UI elements
style = {'description_width': 'initial'}
header = widgets.HTML("<h3>Premium Age Calculator</h3>")

day_in = widgets.IntText(value=1, description='Day (DD):', style=style)
month_in = widgets.IntText(value=1, description='Month (MM):', style=style)
year_in = widgets.IntText(value=2000, description='Year (YYYY):', style=style)

calc_btn = widgets.Button(
    description='Calculate Age',
    button_style='info',
    tooltip='Click to calculate',
    icon='calculator'
)

output_area = widgets.Output()

def on_calc_clicked(b):
    with output_area:
        clear_output()
        try:
            d, m, y = day_in.value, month_in.value, year_in.value
            birth_date = date(y, m, d)
            today = date.today()

            if birth_date > today:
                print("Error: Date cannot be in the future.")
                return

            years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            # Handle leap years for the last birthday calculation
            try:
                last_bday = birth_date.replace(year=today.year)
            except ValueError:
                last_bday = birth_date.replace(year=today.year, day=28)

            if last_bday > today:
                try:
                    last_bday = birth_date.replace(year=today.year - 1)
                except ValueError:
                    last_bday = birth_date.replace(year=today.year - 1, day=28)

            days_since = (today - last_bday).days
            
            print(f"Result: {years} Years Old and {days_since} days.")
        except Exception as e:
            print(f"Error: {e}")

calc_btn.on_click(on_calc_clicked)

# Display the UI
layout = widgets.VBox([header, day_in, month_in, year_in, calc_btn, output_area])
display(layout)
