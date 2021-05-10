Title: مكتبة gazpacho
Date: 2021-05-10 06:04
Category: مكتبات بايثون
Tags: بايثون 101
Summary: تجريف, مسح, كشط الويب web scraping باستخدام مكتبة gazpacho 
Author: Essa Alshammari
Slug: gazpacho


### تجريف, مسح, كشط الويب web scraping باستخدام مكتبة gazpacho 

دائما ما نحتاج لمثل هذه المكتبات لاستخراج كمية من البيانات الموجودة على صفحات الويب
خصوصاً تلك التي لا توفر واجهة برمجية API لاخذ البيانات منها لتحليلها او تخزينها او عرضها بطرق اخرى او اياً كان الهدف.

هنا يأتي دور السكريبينق سموه ما شئتم بالعربي مثل ما ذكر في عنوان الموضوع.
هو ببساطة استخراج المعلومات من صفحات الانترنت.

> يرجى الانتباه فعملية السكريبينق غير قانونية في بعض المواقع

اليوم سنتتعلم كيفية فعل ذلك باستخدام مكتبة جميلة اسمها gazpacho.

هناك العديد من الخيارات في البايثون لفعل مثل ذلك ومنها استخدام مكتبة beautifulSoup مع requests وهذه اشهرها وغيرها الكثير.

لكن ما يميز مكتبة gazpacho بساطتها  وسرعتهاواستقرارها واصلاح الاخطاء فيها من قبل مطوريها والافضل فيها انها لا تعتمد على مكتبة اخرى اطلاقا كل ما تحتاجة فقط البايثون.

هنا [الصفحة الرسمية](https://gazpacho.xyz/){:target="_blank"}
 للمشروع مع التوثيق الرسمي 


لنبدأ

اولا نقوم بثبيت المكتبة عن طريق الامر التالي

~~~
pip install gazpacho
~~~

السيناريو كالتالي :

نريد استخراج المعلومات من هذا الموقع [http://quotes.toscrape.com/](http://quotes.toscrape.com/)

والذي يعرض مقولات مشهورة ومن قالها وهذه هي نوعية البيانات التي نريد سحبها

 - اولا نريد الاتصال بالموقع حتى نتمكن من قراءة ما يحتوية.

المكتبة توفر لنا فنكشن لعمل ذلك 
```
get(url)
```

اذا لنقوم بجلبها داخل ملفنا

~~~
#!python
from gazpacho import get
~~~

هذه الداله او الفنكشن تتطلب ان نعطيها url رابط الصفحة التي نرغب بالاطلاع على محتواها.

لنقم بذلك

~~~
#!python
from gazpacho import get

html = get("http://quotes.toscrape.com/")
~~~

هنا نقوم بتخزين المخرجات من get داخل المتغير html لانها سوف ترجع لنا بيانات الصفحة داخل نص مكتوب بـ html

لنلقي نظرة على اول 100 حرف مع نوع البيانات المخرج.

~~~
#!python
from gazpacho import get

html = get("http://quotes.toscrape.com/")
print(html[:100])
print(type(html)
~~~

الكود السابق سوف يطبع لنا التالي

~~~
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Quotes to Scrape</title>
<class 'str'> 
~~~

كما نرا فمحتويات المتغير html هي فعلا مكتوبة بــ html
ونوع بيانات المتغير html من نوع string نص

وهذه بحد ذاتها مشكلة الان كيف سنقوم بالبحث داخل النص.
يمكننا ذلك من خلال طرق كثيرة لعل اشهرها regex التعابير القياسية.

لكن مكتبة gazpacho توفر لنا كلاس Soup لتسهيل عملية البحث والتمحيص.

لنقم باستدعاء Soup

~~~
#!python
from gazpacho import get, Soup

html = get("http://quotes.toscrape.com/")
~~~

لنقم بعد ذلك باعطاء المتغير html للكلاس Soup

~~~
#!python
from gazpacho import get, Soup

html = get("http://quotes.toscrape.com/")
soup = Soup(html)
~~~

لو قمنا بطباعة محتويات المتغير soup سوف يعطينا نفس البيانات التي كان يحملها المتغير html.

لكن لو قمنا بطباعة نوع المتغير 

~~~
#!python
from gazpacho import get, Soup

html = get("http://quotes.toscrape.com/")
soup = Soup(html)
print(type(soup))
~~~
فسوف يظهر لنا
```
<class 'gazpacho.soup.Soup'>
```

وهذا هو الفائدة من المكتبة ككل الان المتغير soup هو object يحمل في طياته اهم ميثود وهو find

```
soup.find(tag, atrrs)
```

هذا الميثود ياخذ الكثير من الاشياء لكن اهما:

 - tag وهو التاق المكتوب داخل ملف html  مثل div ويجب ان نعطيه للميثود على شكل str
 - attrs وهذا الاتريبيوتز المكتوبة داخل التاق مثل ```<div class="someClass"></div>``` ويجب ان نعطيه للميثود كـ dict

 مثال اذا اردنا ان نبحث عن المقولة  الموجودة في صفحة الويب التالية

~~~
<div class="quote" itemscope itemtype="http://schema.org/CreativeWork">
        <span class="text" itemprop="text">“A day without sunshine is like, you know, night.”</span>
        <span>by <small class="author" itemprop="author">Steve Martin</small>
        <a href="/author/Steve-Martin">(about)</a>
        </span>
    </div>
~~~

فسوسف يكون الكود كالتالي

~~~
soup.find('span', attrs={'class': 'text'})
~~~

 - span هو التاق الذي نبحث عنه ولكن ليس كل التاقات التي تحمل هذا النوع
 - attrs={'class': 'text'} فقط تلك التي يكون في داخلها كلاس اسمه text


~~~
#!python
from gazpacho import get, Soup

html = get("http://quotes.toscrape.com/")
soup = Soup(html)
quotes = soup.find('span', attrs={'class': 'text'})
~~~

الكود السابق سوف يقوم بارجاع لست list فيها بيانات جميع التاقات التي تحمل الخصائص المذكورة مسبقا

بذلك يمكننا عمل لووب من نوع for حتى  نتمكن من طباعة ما بداخل التاق فقط 

لنقم بذلك

~~~
#!python
from gazpacho import get, Soup

html = get("http://quotes.toscrape.com/")
soup = Soup(html)
quotes = soup.find('span', attrs={'class': 'text'})
for quote in quotes:
    print(quote.text)
~~~

هنا استخدمنا المتغير text المعرف لنا مسبقاً من قبل الكلاسSoup.

وهذه هي المخرجات
~~~
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”

“It is our choices, Harry, that show what we truly are, far more than our abilities.”

“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”

“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”

“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”

“Try not to become a man of success. Rather become a man of value.”

“It is better to be hated for what you are than to be loved for what you are not.”

“I have not failed. I've just found 10,000 ways that won't work.”

“A day without sunshine is like, you know, night.”
~~~

هنا قمنا باستخراج بيانات الصفحة المقولات فقط بكل سهولة الان انت قم باستخراج من القائل من الصفحة واطبعه بجانب المقولة.

لمعرفة ما هو التاق والاتريبيوتز المستخدمة في الصفحة بأمكانك استخدام ادوات المطورين في كروم او اي متصفح اخر او حتى يمكنك قراءة الشيفرة المصدرية من خلال الضغط على زر الماوس الايمن داخل صفحة الويب ومن ثم الضغط على view page source او inspect.

