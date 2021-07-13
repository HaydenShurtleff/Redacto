import fitz

doc = fitz.open("test.pdf")


page = doc[0]

text = "result"

text_instances = page.searchFor(text)

for inst in text_instances:
    highlight = page.addHighlightAnnot(inst)
    highlight.setColors({"stroke":(0, 0, 1), "fill":(0.75, 0.8, 0.95)})
    highlight.update()


doc.save("output.pdf")