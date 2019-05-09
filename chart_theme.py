headlineFontSize = 22
headlineFontWeight = 'normal'
labelFont = 'Arial'
labelFontSize = 11.5
labelFontWeight = 'normal'
markColor = '#82c6df'
markHighlight = '#006d8f'
markDemocrat = '#5789b8'
markRepublican = '#d94f54'
titleFont = 'Benton Gothic Bold, sans-serif'
titleFontWeight = 'normal'
titleFontSize = 13
colorSchemes = {
  'category-6': [
    '#ec8431',
    '#829eb1',
    '#c89d29',
    '#3580b1',
    '#adc839',
    '#ab7fb4',
  ],
  'fire-7': [
    '#fbf2c7',
    '#f9e39c',
    '#f8d36e',
    '#f4bb6a',
    '#e68a4f',
    '#d15a40',
    '#ab4232',
  ],
  'fireandice-6': [
    '#e68a4f',
    '#f4bb6a',
    '#f9e39c',
    '#dadfe2',
    '#a6b7c6',
    '#849eae',
  ],
  'ice-7': [
    '#edefee',
    '#dadfe2',
    '#c4ccd2',
    '#a6b7c6',
    '#849eae',
    '#607785',
    '#47525d',
  ],
}
def data_theme():

  latimesTheme = {'config':{
  'background': '#ffffff',

  'title': {
    'anchor': 'start',
    'font': titleFont,
    'fontColor': '#000000',
    'fontSize': headlineFontSize,
    'fontWeight': headlineFontWeight,
  },

  'arc': { 'fill': markColor },
  'area': { 'fill': markColor },
  'line': { 'stroke': markColor, 'strokeWidth': 2 },
  'path': { 'stroke': markColor },
  'rect': { 'fill': markColor },
  'shape': { 'stroke': markColor },
  'symbol': { 'fill': markColor, 'size': 30 },

  'axis': {
    'labelFont': labelFont,
    'labelFontSize': labelFontSize,
    'labelFontWeight': labelFontWeight,
    'titleFont':titleFont,
    'titleFontSize':titleFontSize,
    'titleFontWeight':titleFontWeight,
  },

  'axisX': {
    # 'labelAngle': 0,
    'labelPadding': 4,
    'tickSize': 3,
  },

  'axisY': {
    'labelBaseline': 'middle',
    'maxExtent': 45,
    'minExtent': 45,
    'tickSize': 2,
    # 'titleAlign': 'left',
    # 'titleAngle': 0,
    # 'titleX': -45,
    # 'titleY': -11,
  },
  'facet': {
    'spacing':5
  },

  'legend': {
    'labelFont':labelFont,
    'labelFontSize': labelFontSize,
    'titleFont': titleFont,
    'titleFontSize':titleFontSize,
    'titleFontWeight': titleFontWeight,
  },

  'range': {
    'category': colorSchemes['category-6'],
    'diverging': colorSchemes['fireandice-6'],
    'heatmap': colorSchemes['fire-7'],
    'ordinal': colorSchemes['fire-7'],
    'ramp': colorSchemes['fire-7'],
  },
}
  }
  return latimesTheme
