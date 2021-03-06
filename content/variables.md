Title: المتغيرات في بايثون
Date: 2021-05-17 00:18
Category: سلسلة مبادئ البايثون
Tags: بايثون 101
Summary: المتغيرات في بايثون
Author: Essa Alshammari
Slug: variables

# المتغيرات في بايثون

في المواضيع السابقة عندما تعرفنا على انواع البيانات في بايثون كنا نكتبها بشكل حرفي او ثابت لا تتغير,
وما اذا اردنا ان نتكتب شيفرة لفعل شي معين اي معقدة بشكل ما فهناك متتطلب لهذة البيانات ان تتغير مع تقدم تنفيذ الشيفرة.

هنا يأتي دور المتغيرات, فتاليا سوف نتعرف على ماهيتها وكيف نعطي البيانات في البايثون وصفاً مجرداً, والذي من خلاله يمكننا ان نتلاعب بهذه البيانات .

### اسناد القيم للمتغيرات

فكر بها كالتالي نعطي لاي نوع من انواع البيانات في البايثون اسماً.
وفي البايثون يتم ذلك من خلال  علامة = كالتالي:

```python
name = "Essa"
age = 30
```

هنا لدينا متغيرين الاول name والاخر age.

وقد قمنا باسناد القيم لها "Essa" و 30.

بالنسبة لمفسر البايثون فيقرأها كالتالي المتغير name له قيمة "Essa",  وعندما يستخدم المتغير name في اي مكان اخر مرة اخرى فسوف يستبدله بالقيمة "Essa" كالتالي:

```python
>>> print(name)
Essa
```

وعند تغيير قيمة المتغير الى شي اخر سيتغير.

```python
>>> name = "Hanan"
>>> print(name)
Hanan
```

ايضاً في البايثون نوع المتغير بأمكانة ان يتغير على خلاف العديد من اللغات الاخرى والتي يكون انشاء المتغير فيها يجب ان يصاحبة نوع البيانات الذي سيكون في القيمة ولا يتغير اطلاقاً.

في البايثون يمكننا فعل التالي:

```python
>>> n = "Essa"
>>> type(n)
<class 'str'>
>>> n = 1
>>> type(n)
<class 'int'>
```

هنا اسندنا قيمة من نوع نص الى المتغير n, وعند طباعة نوع البيانات الموجودة في المتغير قام المفسر بتأكيد ذلك.
 وبعدها قمنا بتغيير قيمة نفس المتغير n الى بيانات من نوع عدد, وعند طباعة نوعه نجد انه فعلا تغير.

### لندخل في العمق قليلاً

ما الذي يحدث عندما نسند قيمة الى متغير؟ الاجابة ستكون طويلة بعض الشئ.

قلنا في السابق ان البايثون تدعم اكثر من توجة برمجي ولعل اللغة مبنية بشكل جيد في البرمجة كائنية التوجة, ولذلك فكل قيمة في البايثون تقريبا تعتبر كائن object ينتمي الى نوع class.

> عندما نقول كائن فنعني به object.

لنأخذ المثال التالي:

```python
>>> print(1)
1
```

هنا يقوم المفسر بالخطوات التالية:

 - يقوم بأنشاء كائن من نوع `integer`.
 - يقوم بأعطاء الكائن قيمة 1.
 - يقوم بعرضة.

الان مع المتغير

المتغير هو فقط عبارة عن اسم رمزي يؤشر على الكائن الذي يحمل بداخلة القيمة والتي نقوم باعطائها نحن للمتغير.

وبمجرد ان نعطي قيمة ما لمتغيربامكاننا الرجوع للكائن نفسة عن طريق اسم المتغير, لكن البيانات او القيمة هي لا زالت في محتوى الكائن.

مثال:

```python
>>> n = 1
```

هنا عملية الاسناد تقوم بأنشاء كائن من نوع القيمة `int` في هذه الحالة, وتعطية القيمة 1 ومن ثم  تعطي اسم المتغير `n` مؤشر من خلاله يمكن الرجوع الكائن.

نتأكد من ذلك كالتالي:

```python
>>> type(n)
<class 'int'>
```

هنا عملية التأكيد ان المتغير `n` يشير الى الكائن `int`.

وبما ان المتغير يمكن ان نفعل به مثل ما نفعل بقيمتة! انظر للمثال التالي:

```python
>>> m = n
```

هنا اسندنا المتغير `n` الى متغير جديد `m`.

هل سيقوم مفسر البايثون باعادة جميع الخطوات السابقة ؟ لا

لن يقوم بأنشاء كائن جديد! فقط سيقوم بأنشاء مرجع او مؤشر بالاسم الجديد `m` ويقوم بالتأشير على الكائن الموجود مسبقا في `n`.

كيف نتأكد من ذلك؟

هناك فنكشن اسمه `id` مهمتة ان يقوم بأرجاع رقم المعرف المعطى للكائن عند عملية انشائة:

```python
>>> id(n)
9784896
>>> id(m)
9784896
```

هنا يتضح ذلك جلياً ان كلا المتغيرين يشيران الى نفس الكائن.

اذا ماذا لو قمنا بتغيير قيمة المتغير الجديد؟

```python
>>> m = 2
```

هنا المفسر سيقوم بأنشاء كائن جديد ويعطية القيمة الجديدة ومن ثم يقوم بتغيير الموشر الى الكائن الجديد.

الان ماذا لو قمنا بتغير قيمة احدى المتغيرات الى قيمة من نوع اخر؟

```python
>>> n = "Essa"
```

سيقوم المفسر بأنشاء كائن جديد من نوع القيمة المسندة الى المتغير ويقوم بتغيير الموشر الى الكائن الجديد.
اما القيمة السابقة ستصبح الان دون مؤشر ولا يمكننا الرجوع اليها وستصبح يتيمة., وسيقوم البايثون بحذفها.

### تسمية المتغيرات 

هناك بعض الشروط لتسميتها

يجب ان يبدأ الاسم اما بحرف او _ ويتبعه احرف صغيرةً كانت او كبيرة وارقام 

مثال:

```python
>>> name = "Essa"
>>> _Age = 30
>>> Loves_Python = True
```

كل ما سبق صحيح

لكن التالي غير صحيح:

```python
>>> 1991_something = 1
  File "<stdin>", line 1
    1991_something = 1
        ^
SyntaxError: invalid decimal literal
```

غير صحيح لانه بدأ برقم.

ويجب الانتباه ايضا الى حاله الاحرف فـ `age` مختلف تماما عن `Age`:

```python
>>> age = 1
>>> Age = 2
>>> aGe = 3
>>> AGE = 4
>>> a_g_e = 5
>>> _age = 6
>>> age_ = 7
>>> _AGE_ = 8

>>> print(age, Age, aGe, AGE, a_g_e, _age, age_, _AGE_)
1 2 3 4 5 6 7 8
```

لا يوجد شي يمنعنا من استخدام نفس الاسم لمتغيرين تختلف فيهما حالة الاحرف مثل `age` و `Age`, لكن ذلك سيخلق بعضاً من التشويش لنا. 

هناك ايضا بعض الاعراف المستخدمة بين المطورين عندما نأتي لتسمية المتغيرات وفي البايثون هناك ورقة توضح ذلك واسمها pep8.

وببساطة يقول لنا اذا اردنا تسمية متغير يجب اتباع الاتي على مثلا هذا المتغير `Number of Friends`

طبعا البايثون لا يقبل المسافات في اسماء المتغيرات لذلك سنقوم بأستبدالها بـ _ .

وحالة الاحرف يجب ان تكون صغيرة عندما نريد تسمية متغير 

اذا فسيكون كالتالي:

```python
>>> number_of_friends = 1
```

في اخر اصدارات البايثون هناك دعم للاحرف بترميز يونيكود عند استخدامها كأسماء متغيرات, وبذلك يمكننا أستخدام الاحرف العربية والايموجي كأسماء متغيرات

```python
>>> متغير = 1
>>> متغير
1
```

