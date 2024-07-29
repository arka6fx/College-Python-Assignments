#replace <|Name|> & <|Date|> using str function

letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Arka").replace("<|Date|>","24 september 2050"))