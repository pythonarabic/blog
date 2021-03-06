Title: السلاسل النصية في بايثون 2
Date: 2021-06-06 12:15
Category: سلسلة مبادئ البايثون
Tags: بايثون 101
Summary: فهرسة النصوص وكيفية الوصول الى عناصرها
Author: Essa Alshammari
Slug: strings-2


## فهرسة النصوص

عادتاً في لغات البرمجة العناصر التي تكون ضمن مجموعة من البيانات مثل النصوص بأمكاننا الوصول لها من خلال مؤشر او مفتاح, وهذي العملية تسمى بالفهرسة `indexing`.

في البايثون النص هو عبارة عن سلسلة من الاحرف المرتبة, لذلك بالامكان فهرستها والوصول اليها عن طريق اتباع النص بـ `[0]` اقواس مربعة وبداخلها رقم يمثل مكان الحرف داخل النص.

والفهرسة في بايثون تبدأ من الصفر بمعنى ان الحرف الاول يتم الوصول اليه عن طريق الرقم 0 والذي يليله عن طريق الرقم 1 ... وهكذا, والحرف الاخير يساوي طول النص ناقص واحد.

توضيح:

|    	|  	|  	|  	|  	|  	|  	|  	|
|---------	|---	|---	|---	|---	|---	|---	|---	|
| الحرف   	| ! 	| n 	| o 	| h 	| t 	| y 	| p 	|
| المفتاح 	| 6 	| 5 	| 4 	| 3 	| 2 	| 1 	| 0 	|

مثال:

```python
>>> s = "python!"
>>> s[0]
'p'
>>> s[2]
't'
>>> s[len(s) - 1]
'!'
```

هنا قمنا بالوصول للحرف الاول عن طريق الرقم 0 والحرف الثالث عن طريق الرقم 2 والحرف الاخير عن طريق تعبير قمنا بكتابتة داخل الاقواس المربعة والذي استخدم الفنكشن `len`لارجاع طول النص ثم قمنا بأنقاص واحد منه والذي اعطانا رقم 6 وهو مفتاح او المؤشر الذي يشير للحرف الاخير.

واذا قمنا بكتابة مفتاح اطول من السلسلة النصية البايثون سيرجع لنا خطأً

مثال:

```python
>>> s = "python!"
>>> s[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

هنا قمنا بمحاولة الوصول للحرف الذي يكون مفتاحة رقم 7 وهو غير موجود في الاساس لذلك قام المفسر باعطاء خطأ يفيد بان المفتاح او المؤشر خارج نطاق النص.

ايضا البايثون يمكننا من الوصول الى العناصر داخل النص عن طريق استخدام الارقام السالبة, لكن في هذه الحالة يبدأ العد من الاخير, بمعنى ان الحرف الاخير مفتاحة -1 والذي يسبقة مفتاحة -2 وهكذا ... والعنصر او الحرف الاول مفتاحة يساوي طول النص سالباً.

توضيح:

|           	|    	|    	|    	|    	|    	|    	|    	|
|-----------	|----	|----	|----	|----	|----	|----	|----	|
| المفتاح - 	| -1 	| -2 	| -3 	| -4 	| -5 	| -6 	| -7 	|
| الحرف     	| !  	| n  	| o  	| h  	| t  	| y  	| p  	|
| المفتاح + 	| 6  	| 5  	| 4  	| 3  	| 2  	| 1  	| 0  	|


مثال:

```python
>>> s = "python!"
>>> s[-1]
'!'
>>> s[-5]
't'
>>> s[-len(s)]
'p'
```

هنا قمنا بالدخول للحرف الاخير عن طريق المفتاح 1- والحرف الثالث عن طريق المفتاح 5- والحرف الاول عن طريق التعبير مستخدماً الفنكشن `len` والتي تقوم بارجاع طول النص لكنها مسبوقة بعامل احادي `-` ومهمتة يقوم بعكس اشارة الرقم واعطانا المفتاح رقم 7-

نقف عند هذا الحد ونكمل في المواضيع التالية.