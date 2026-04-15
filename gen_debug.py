import sys

html = '''<html>
<body style=\"background:#555;\">
  <div style=\"width:594px; height:604px; background:url('car.png'); border:1px solid red; position:relative;\">
'''
boxes = [
    (12,  105, 187, 85),
    (207, 105, 80, 85),
    (294, 105, 80, 85),
    (405, 105, 92, 85),
    (12,  204, 187, 75),
    (205, 210, 185, 69),
    (396, 210, 185, 69),
    (12,  293, 185, 77),
    (202, 301, 185, 69),
    (392, 301, 185, 69),
    (12,  382, 182, 57),
    (201, 394, 144, 45),
    (393, 387, 189, 98) 
]
for i,b in enumerate(boxes):
    html += f'    <div style=\"position:absolute; left:{b[0]}px; top:{b[1]}px; width:{b[2]}px; height:{b[3]}px; border:2px solid cyan;\"><span style=\"color:magenta;font-weight:bold;font-size:20px;\">{i}</span></div>\n'
html += '  </div>\n</body></html>'

with open('debug.html', 'w') as f:
    f.write(html)
