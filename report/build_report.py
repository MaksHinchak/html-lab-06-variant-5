from pathlib import Path
from shutil import copy2
from html import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, Preformatted, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PIL import Image as PILImage
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'report/lab6-svg-variant5.pdf'
DESKTOP=Path('/Users/maksimginchak/Desktop/Лабораторні/HTML/Лаба 6 SVG варіант 5.pdf')
pdfmetrics.registerFont(TTFont('ArialUA','/Library/Fonts/Arial Unicode.ttf'))
pdfmetrics.registerFont(TTFont('ArialBold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('ArialUA',normal='ArialUA',bold='ArialBold')
pdfmetrics.registerFont(TTFont('CourierUA','/System/Library/Fonts/Supplemental/Courier New.ttf'))
BLUE=colors.HexColor('#174a7e'); LINE=colors.HexColor('#c9d8e2'); PALE=colors.HexColor('#f2f8fb')
body=ParagraphStyle('body',fontName='ArialUA',fontSize=10.5,leading=16,spaceAfter=8)
heading=ParagraphStyle('heading',fontName='ArialBold',fontSize=13,leading=18,textColor=BLUE,spaceBefore=5,spaceAfter=9)
example=ParagraphStyle('example',parent=heading,fontSize=14,leading=19,spaceAfter=11)
small=ParagraphStyle('small',parent=body,fontSize=10,leading=14)
cell=ParagraphStyle('cell',parent=body,fontSize=9,leading=13,spaceAfter=0)
white=ParagraphStyle('white',parent=cell,fontName='ArialBold',textColor=colors.white)
code=ParagraphStyle('code',fontName='CourierUA',fontSize=8,leading=10)
WIDTH=470.5512
story=[]
def p(s,style=body): return Paragraph(s,style)
def h(s): story.append(p(s,heading))
def paragraph(s): story.append(p(s))
def screenshot(name):
 path=ROOT/'report'/name
 w,ht=PILImage.open(path).size
 story.append(Image(str(path),width=WIDTH,height=ht*WIDTH/w))
 story.append(Spacer(1,10))
def source(text):
 block=Preformatted(text.strip(),code)
 t=Table([[block]],colWidths=[WIDTH],hAlign='LEFT')
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),.5,LINE),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
 story.append(t);story.append(Spacer(1,10))
def page(): story.append(PageBreak())
def example_start(title):
 story.append(p(title,example))
 story.append(p('Сторінка: svg.html. Скріншот реального сайту у Chrome, ширина вікна 1280 px.',small))

story.append(Spacer(1,680));page()
h('Завдання')
paragraph('Створити вебсторінку з SVG-графікою за варіантом №5. Відтворити статичний малюнок, розмістити текст уздовж кривої та додати динамічну зміну кольору, переміщення, обертання, розміру й перекосу окремих фігур. Вивчити способи вбудовування SVG у HTML.')
h('Варіант №5')
paragraph('На координатних осях X і Y розташовано 9 синіх фігур: 2 кола, 6 прямокутників та ромб. Кола мають радіус 1 і центри (-2; 1), (1; 1). Вершини ромба: (2; -1), (3; 0), (4; -1), (3; -2). Прямокутники займають області [-3; -1] × [-1; 0], [2; 3] × [1; 2], [3; 4] × [0; 1], [0; 1] × [-2; -1], [1; 3] × [-3; -2], [4; 5] × [-2; -1].')
h('Складові завдання за методичкою')
rows=[['Складова','Частка'],['Статичний малюнок варіанта','40%'],['Текст уздовж кривої','10%'],['Зміна кольору','10%'],['Переміщення','10%'],['Обертання','10%'],['Зміна розміру','10%'],['Перекіс','10%']]
t=Table([[p(s,white if i==0 else cell) for s in row] for i,row in enumerate(rows)],colWidths=[WIDTH-75,75])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('GRID',(0,0),(-1,-1),.5,LINE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('LEFTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]));story.append(t);story.append(Spacer(1,10))
h('Розв’язування та файли проєкту')
paragraph('Створено окремий проєкт ByteMarket на основі лабораторної №5. Нові матеріали містяться на svg.html, а пункт «SVG» доступний на всіх 8 сторінках. Малюнки мають viewBox і масштабуються разом із контейнером. Перехід до математичних координат задано перетворенням translate(290 245) scale(72 -72). Кольори й положення статичних фігур звірено зі схемою методички.')
for line in ['svg.html - статичний малюнок, текст по кривій, анімація та вбудовування.','assets/svg/ - три окремі SVG-файли.','assets/css/svg.css, assets/js/svg.js - оформлення й кнопки керування.','scripts/build_svgs.py - складання SVG та HTML із текстового шаблону.','report/ - звіт, скриншоти, відповідність вимогам і пам’ятка до захисту.']:
 story.append(p('• '+line,small))
page()
h('Тестові приклади')
rows=[['№','Перевірка','Отриманий результат'],['1','Порівняти фігури зі схемою','9 фігур: 2 кола, 6 прямокутників, 1 ромб. Колір синій; положення відповідає варіанту 5.'],['2','Відкрити приклад тексту','textPath посилається на path; напис повторює криву Безьє.'],['3','Перевірити стан на 0 і 1.5 с','Ліве коло змінює fill; верхній квадрат переміщується; ромб обертається; праве коло масштабується; нижній правий квадрат перекошується.'],['4','Натиснути «Пауза» та «Спочатку»','Пауза зупиняє часову шкалу; перезапуск повертає час до початку та відновлює рух.'],['5','Увімкнути зменшення руху','Анімація початково призупинена; її можна продовжити кнопкою.'],['6','Перевірити зовнішні SVG','Один файл відображається через object, embed та iframe.'],['7','Вимкнути JavaScript','Статична графіка зберігається; SVG-анімація не залежить від скрипту; кнопки керування вимкнені.'],['8','Екран шириною 390 px','Сторінка без горизонтального виходу, графіка зменшується, блоки вбудовування стають в одну колонку.']]
t=Table([[p(escape(s),white if i==0 else cell) for s in row] for i,row in enumerate(rows)],colWidths=[28,147,WIDTH-175])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),('GRID',(0,0),(-1,-1),.5,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));story.append(t);story.append(Spacer(1,12))
h('Основні засоби SVG')
paragraph('svg - контейнер і система координат; circle, rect, polygon - фігури; line - осі й поділки; defs та symbol - визначення повторюваних елементів; use - їхні копії. Path задає криву, text і textPath розміщують напис, g групує фігури й перетворення. Title та desc описують графіку. У прикладі тексту додатково використано ellipse і polyline.')
paragraph('Анімація реалізована тегами animate та animateTransform. Translate переміщує, rotate обертає, scale змінює розмір, skewX задає перекіс. Це коректні SVG-назви; записи symbols і transform як окремі теги в методичці не використано.')
page()
example_start('Приклад 1. Статичний малюнок варіанта №5')
story.append(p('Зразок із методички, сторінка 8',small))
reference=ROOT/'report/variant5-reference.png';rw,rh=PILImage.open(reference).size
story.append(Image(str(reference),width=330,height=330*rh/rw));story.append(Spacer(1,10))
story.append(p('Результат на вебсторінці',small));screenshot('static-figure.png')
paragraph('Координати фігур задаються у математичній системі. Група g переносить початок координат і перевертає вісь Y. Для повторення прямокутників використано symbol із preserveAspectRatio="none" та use; осі й підписи намальовано поверх фігур.')
page()
example_start('Приклад 2. Текст по кривій та вбудовування')
screenshot('curved-text.png')
paragraph('Відповідні блоки svg.html')
source('''<defs>
  <path id="headline-curve"
        d="M80 205 C180 25 600 25 700 205" />
</defs>
<text>
  <textPath href="#headline-curve" startOffset="50%"
            text-anchor="middle">
    SVG · ByteMarket · Варіант 5
  </textPath>
</text>''')
paragraph('Команда C задає кубічну криву Безьє. textPath пов’язує напис із контуром через href; startOffset і text-anchor центрують його вздовж кривої.')
screenshot('embedding.png')
paragraph('Зовнішній SVG підключено через object, embed та iframe. Для object є резервне посилання на файл. Застарілий param наведено на вимогу методички; переданий параметр не керує SVG. Безпосередня вставка svg у HTML використана в основних прикладах.')
page()
example_start('Приклад 3. Динамічні зміни фігур')
screenshot('animated-figure.png')
paragraph('Фрагменти анімації SVG')
source('''<animate attributeName="fill"
  values="#0000ff;#ff6b35;#0000ff" dur="4s"
  repeatCount="indefinite" />
<animateTransform attributeName="transform" type="skewX"
  values="0;25;-25;0" dur="7s" repeatCount="indefinite" />''')
paragraph('На скриншоті часову шкалу зупинено на 1 с. Кожен ефект має власний цикл: колір - 4 с, переміщення й масштаб - 5 с, обертання - 6 с, перекіс - 7 с. Кнопки JavaScript викликають pauseAnimations, unpauseAnimations та setCurrentTime; сам рух задається SVG-анімацією.')
story.append(KeepTogether([
p('Висновки',heading),
p('Створено SVG-сторінку за варіантом №5: статичну композицію, текст уздовж кривої та п’ять видів анімації. Перевірено координати, зміну властивостей із часом, керування відтворенням, вбудовування та мобільний вигляд у Chrome. Порівняно з №5 новою є векторна графіка; форми й інші сторінки попередньої роботи збережено.'),
p('Репозиторій',heading),
p('<link href="https://github.com/MaksHinchak/html-lab-06-variant-5" color="#174a7e">https://github.com/MaksHinchak/html-lab-06-variant-5</link>')
]))

def decorate(c,doc):
 c.setFont('ArialUA',9); c.setFillColor(colors.HexColor('#587083'))
 c.drawRightString(538.9134,34,str(doc.page))
 if doc.page==1:
  c.setFillColor(colors.black);c.setFont('ArialUA',12)
  for y,line in [(688.89,'Чернівецький національний університет'),(669.89,'імені Юрія Федьковича'),(650.89,'Навчально-науковий інститут фізико-технічних'),(631.89,'та комп’ютерних наук')]: c.drawCentredString(A4[0]/2,y,line)
  c.setFont('ArialUA',17)
  for y,line in [(495.89,'ЗВІТ'),(470.89,'про виконання лабораторної роботи №6'),(445.89,'з дисципліни «Веб-програмування»')]: c.drawCentredString(A4[0]/2,y,line)
  c.setFont('ArialUA',12);c.drawCentredString(A4[0]/2,423.89,'Тема: Основи SVG. Графічні об’єкти')
  author_lines=[(303.39,'Виконав: студент групи 241-А'),(284.39,'Гінчак Максим Богданович'),(265.39,'Перевірив:'),(246.39,'асистент Нестеренко Володимир Васильович')]
  for y,line in author_lines: c.drawRightString(538.9134,y,line)
  c.drawCentredString(A4[0]/2,48,'Чернівці · 2026')

SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=62.3622,rightMargin=50.3622,topMargin=56,bottomMargin=46,title='Лабораторна робота №6. SVG. Варіант 5',author='Гінчак Максим Богданович').build(story,onFirstPage=decorate,onLaterPages=decorate)
r=PdfReader(OUT)
assert len(r.pages)==6,len(r.pages)
assert 'Висновки' in r.pages[-1].extract_text()
assert 'Репозиторій' in r.pages[-1].extract_text()
assert all('Висновки' not in p.extract_text() and 'Репозиторій' not in p.extract_text() for p in r.pages[:-1])
for index,page_obj in enumerate(r.pages):
 assert len(page_obj.extract_text())>50
 assert abs(float(page_obj.mediabox.width)-A4[0])<1
links=[a.get_object().get('/A',{}).get('/URI') for pg in r.pages for a in pg.get('/Annots',[])]
assert 'https://github.com/MaksHinchak/html-lab-06-variant-5' in links
copy2(OUT,DESKTOP)
assert OUT.read_bytes()==DESKTOP.read_bytes()
print(f'Created {len(r.pages)}-page A4 report:',DESKTOP)
