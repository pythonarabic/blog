Title: انواع البيانات في البايثون 1
Date: 2021-05-11 01:53
Category: سلسلة مبادئ البايثون
Tags: بايثون 101
Summary: نتعرف معاً على الارقام الصحيحة في بايثون
Author: Essa Alshammari
Slug: python-datatype-1

## انواع البيانات في البايثون 1

> هذا الموضوع سوف يكون مقسم على عدة مواضيع.

بعد ما تعلمنا كيفية التعامل مع البايثون, الان وقت تعلم البايثون الحقيقي. وسوف نبدأ بشرح انواع البيانات الموجودة مسبقاً في بايثون, لاحقا سوف تتعلم ان شاء الله كيفية انشاء نوع بيانات.

قبل ان نبدأ نريد ان نقوم بفتح الـ REPL حتى يتسنى لنا تجربة ما نتعلمه.

> ملاحظة: داخل الريبل لا نحتاج لكتابة print حتى نطبع المخرجات.

### الاعداد الصحيحة integers:

في بايثون 3 لا يوجد حد للارقام الصحيحة الا من قبل الذاكرة التي تكون في جهازك.

لاثبات ذلك نقوم بالتالي:

~~~
#!python
>>> print(999999999999999999999999999999999999999999999999999998 + 1)
999999999999999999999999999999999999999999999999999999
~~~

البايثون سيقوم بتفسير اي سلسلة من الارقام كعدد عشري شرط الا يكون مسبوقاً بشئ.

~~~
#!python
>>> print(10)
10
~~~

واذا اردنا ارقام غير العشرية فسنقوم باعطاء سابقة للرقم حتى يتمكن المفسر من تقييمة, هكذا:

الارقام الثنائية نكتب قبل الرقم 0b او 0B:

~~~
#!python
>>> print(0b111)
7
~~~

الرقم الثماني نكتب قبل الرقم 0o او 0O:

~~~
#!python
>>> print(0o11)
9
~~~

الرقم الست عشري نكتب قبل الرقم 	0x او 0X:

~~~
#!python
>>> print(0xF)
15
~~~

وكل هذه الارقام هي من نوع واحد والذي يسمى العدد الصحيح integer

حتى نتأكد نقوم بطباعة التالي في المفسر ليعطينا نوع البيانات المدخلة اليه:

~~~
#!python
>>> type(10)
<class 'int'>
>>> type(0b111)
<class 'int'>
>>> type(0o11)
<class 'int'>
>>> type(0xF)
<class 'int'>
~~~

بهذا نكون انهينا موضوع اليوم :)