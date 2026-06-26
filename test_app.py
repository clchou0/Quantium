from task3 import app

def test_header_present():
    layout = str(app.layout)
    assert 'Pink Morsel Sales Visualiser' in layout

def test_chart_present():
    layout = str(app.layout)
    assert 'sales-chart' in layout

def test_region_picker_present():
    layout = str(app.layout)
    assert 'region-filter' in layout