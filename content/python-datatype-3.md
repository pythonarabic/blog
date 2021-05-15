Title: انواع البيانات في البايثون 3
Date: 2021-05-14 03:14
Category: سلسلة مبادئ البايثون
Tags: بايثون 101
Summary: نتعرف معاً على السلاسل النصية في بايثون
Author: Essa Alshammari
Slug: python-datatype-3

## انواع البيانات في البايثون 3

### النصوص

النصوص هي سلسلة من الاحرف ويرمز اليها في البايثون بــ str.

وهي تكون محدودة من الجهتين بعلامة التنصيص الواحدة ' او علامتي التنصيص " بذلك يصبح كل ما بينهما جزء من النص.

~~~
#!python
>>> print("I am a string.")
I am a string.
>>> print('I am too.')
I am too.
~~~

النص في البايثون بأمكانة احتواء اي حرف ترغب به وبالعدد المحدود بقدرات جهازك, كما انه ايضا يمكن ان يكون فارغاً

~~~
#!python
>>> ''
''
~~~

ربما البعض منكم يتسائل الان ماذا اذا اردت ان اضمن علامة التنصيص في محتوى النص ؟

~~~
#!python
>>> print('this is a single quote ' and this is a double quote "')
  File "<stdin>", line 1
    print('this is a single quote' and this is a double quote "'
                                                 ^
SyntaxError: invalid syntax
~~~

كما رأيتم سيضهر لنا خطأ وذلك لان البايثون قيم بداية النص بعلامة التنصيص المفردة واي علامة تنصيص  مفردة اخرى سيعتبرها نهاية للنص.

بالتالي قيم هذا المحتوى فقط

~~~
#!python
print('this is a single quote '
~~~

وبقي هذا

~~~
#!python
 and this is a double quote "')
~~~

والسطر الاخير لا يفهمة البايثون فأعتبرة خطأً بنيوياً syntax error

اذا ما الحل؟

اذا اردنا ان نستخدم علامة التنصيص الواحدة ضمن النص فيجب ان يكون حدود النص كاملا بعلامتي التنصيص, هكذا:

~~~
#!python
>>> print("This is a single quote (') character.")
This is a single quote (') character.
~~~

والعكس صحيح

~~~
#!python
>>> print('This is a double quote (") character.')
This is a double quote (") character.
~~~

جميل!

لكن ربما ايضا يتسائل بعضكم الان ماذا اذا اردنا ان نضمن كلا علامتي التنصيص الفردية والزوجية في النص؟
:)

#### تخطي النصوص escape

التخطي يستخدم لحالتين:

 - عندما تريد ايقاف البايثون من تفسير بعض الاحرف الخاصة التي لها معنى خاص في البايثون.
 - او عندما تريد من البايثون فهم وتفسير معنى خاص ان تعطية لها

الاول هو الذي واجهنا مسبقا وسنعرفة الان, اما الثاني سنشرحة بعد الاول:

في كلا الحالتين سوف نستخدم حرف الخط المائل للخلف \

وهذا الحرف خاص في البايثون وعندما يتم تقييمة يشير للمفسر ان اي حرف او اكثر بعده يجب ان يعامل معاملة خاصة.

اذا كنتم تذكرون المثال السابق

~~~
#!python
>>> print('this is a single quote ' and this is a double quote "')
  File "<stdin>", line 1
    print('this is a single quote' and this is a double quote "'
                                                 ^
SyntaxError: invalid syntax
~~~

بأمكاننا تخطية بالطريقة التالية 

~~~
#!python
>>> print('this is a single quote \' and this is a double quote "')
this is a single quote ' and this is a double quote "
~~~

وتباعاً جميع طرق التخطي والتي لها معنا خاص في بايثون

 - \\' لتخطي علامة التنصيص الواحدة.
 - \\" لتخطي علامتي التنصيص.
 - \\ لتخطي الاسطر الجديدة.
 -  \\\ لتخطي علامة التخطي اذا اردنا استخدامها في النص.


والامثلة كالتالي :

لتخطي الاسطر الجديدة

~~~
#!python
>>> print('a\
... b\
... c')
abc
~~~

لتخطي علامة التخطي

~~~
#!python
>>> print('foo\\bar')
foo\bar
~~~

> عند كتابة الموضوع استخدمت محرر markdown والذي يستخدم نفس خاصية التخطي فعند كتابة \\\  في الواقع انا كتبتها هكذا \\\\\ والاخيرة هذه التي كتبتها هنا للتوضيح في الواقع كتبت \\\\\\\\\ والاخيرة هذه في الواقع ... :) لن ننتهي 

اما الاستخدام الثاني فيطول شرحة لكن سنذكرة دون امثلة للكل:

والذي كان : عندما تريد من البايثون فهم وتفسير معنى خاص ان تعطية لها

وتكون كالتالي:
~~~
 - \a 
 - \b 
 - \f 
 - \n 
 - \N{name} 
 - \r 
 - \u
 - \U
 - \v
 - \ooo
 - \xhh
~~~

بامكانكم الاطلاع [هنا](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals){:target="_blank"}

بعض الامثلة:

لاضافة تاب داخل النص:

~~~
#!python
print("a\tb")
a    b
~~~

لاضافة سطر جديد:

~~~
#!python
>>> print("a\nb")
a
b
~~~

لاستخدام احرف بترميز يونيكود:

~~~
#!python
>>> print('\u2192')
→
~~~

~~~
#!python
print('\N{leftwards arrow}')
←
~~~

تستخدم هذه الانواع من التخطيات غالبا لادخال احرف لا تكون موجودة في الكيبوورد او عندما  تكون هذه الاحرف لا يوجد لها رموز مقروءة او مطبوعة.

#### النص الخام

والذي يشير للمفسر بان اذا كان هناك اي طريقة للتخطي داخل النص لا تقيمها بشكل خاص واطبعها كما هي.

نكتب النصوص الخام في البايثون بتضمين r او R قبل بداية النص كالتالي:

~~~
#!python
>>> print('foo\nbar')
foo
bar
>>> print(r'foo\nbar')
foo\nbar

>>> print('foo\\bar')
foo\bar
>>> print(R'foo\\bar')
foo\\bar
~~~

كما تلاحظون عندما نسبق النص بحرف r او R فيصبح التخطي لا معنى له اطلاقاً.

#### النصوص المحاطة بعلامات تنصيص ثلاثية

هناك ايضا نوع اخر من النصوص والتي يكون في النص محاطا اما بــ ''' او """ وسوف يفسرة البايثون على انه نص, جميع طرق التخطي السابقة يقيمها البايثون في هذا النوع الا علامة التنصيص الواحدة ' وعلامتي التنصيص " والسطر الجديد, بامكاننا كتابتها كما هي وسوف يتخطاها البايثون بدلا منا.

مثال:

~~~
#!python
>>> print('''this is a single quote ' and this is a double quote "''')
this is a single quote ' and this is a double quote "
~~~

مثال آخر:

~~~
#!python
>>> print("""This is a line
... and another line
... and the last line.""")
This is a line
and another line
and the last line.
~~~

كما تعتبر ايضا هذه الطريقة الاخيرة كنوع من توثيق شيفرتنا وسنأتي على هذا في دروس قادمة ان شاء الله.

ولو طلبنا من البايثون بارجاع ماهية نوع البيانات المستخدم مع جميع الامثلة السابقة سيعطينا انها من نوع str كالتالي:

~~~
#!python
>>> type("نراكم في الدرس التالي ان شاء الله :)")
<class 'str'>
~~~