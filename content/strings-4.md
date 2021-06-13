Title: السلاسل النصية في بايثون 4
Date: 2021-06-13 20:42
Category: سلسلة مبادئ البايثون
Tags: بايثون 101
Summary: تعديل النصوص وتنسيقها
Author: Essa Alshammari
Slug: strings-4

## تعديل النصوص وتنسيقها

### تعديل النصوص

بكل اختصار النصوص لا يمكن تعديلها في البايثون! لان النصوص من انواع البيانات التي تعتبرها البايثون غير قابلة للتعديل `immutable` , بالطبع هناك انواع بيانات قابلة للتعديل `mutable` لكن حتى الان جميع انواع البيانات التي سبق شرحها كلها غير قابلة للتعديل.

على سبيل المثال لا يمكن فعل التالي:

```python
>>> s = "bython!"
>>> s[0] = "p"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

طبعا هناك طرق اخرى للتعديل ولا نحتاج لمثل ما فعلناه مسبقا, ومن اشهر الطرق ان ننسخ النص المراد تعديله مع التعديل واسناده مجددا.

مثال:

```python
>>> s = "bython!"
>>> s = "p" + s[1:]
>>> s
'python!'
```

بالاضافة الى العديد من الوظائف المدمجة في كلاس النص وسنتعرف عليها لاحقاً ان شاء الله.

### تنسيق النصوص

مؤخرا اضيف للبايثون طريقة جديدة لتنسيق النصوص وهي الان الطريقة الامثل لتنسيق النصوص, وتسمى بـ `f-string`.

هناك العديد من طرق التنسيق للنصوص في البايثون لكن سنعتمد هذه الطريقة.

الا انها لا يمكن حصرها في موضوع واحد لكثرة مميزاتها فسوف نقتصر الامر على ادراج متغير داخل النص حاليا.

الـ `f-string` تعتمد على `{ }`

مثال لادراج متغير داخل النص:

```python
>>> version = 3.9
>>> s = f"the latest stable python release is {version}"
>>> s
'the latest stable python release is 3.9'
```

مثال اخر:

```python
>>> url = "https://t.me/arabipython"
>>> s = f"You can reach us at {url} and you will be welcomed :)"
>>> s
'You can reach us at https://t.me/arabipython and you will be welcomed :)'
```

> f-strings تعمل فقط من اصدار بايثون 3.6 وما فوق.
