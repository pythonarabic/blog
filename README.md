<div dir="auto">

# للمشاركة في المدونة يرجى اتباع الاتي

   ### اولا \ يجب ان نقوم بعمل fork للمدونة كالاتي:


   ![fork](/images/fork.png)


   ### ثانيا \ تصدير الحزمة محلياً من الحساب الخاص بنا:


   ![clone](/images/clone.png)

   بعد ذلك نقوم بفتح terminal او powershell في الوندوز ونقوم بكتابة الامر التالي.

<div dir="ltr">

    git clone https://github.com/EssaAlshammri/blog.git 

</div>

   > يجب ان يكون git مثبت مسبقاً


   ### ثالثاً \ نقوم بانشاء branch  جديد ونعطية اسم والدخول لمجلد التدوينات كالتالي:

<div dir="ltr">

    git checkout -b python-list-comprehension

    cd blog/_posts

</div>

   ### رابعا \ انشاء التدوينة:

   تعليمات يجب اتباعها:
   
   - اسم الملف يجب ان يتبع التنسيف التالي YEAR-MONTH-DAY-title.md
 
   يجب ان يكون YEAR اربعة ارقام تمثل العام.

   يجب ان يكون MONTH رقمان يمثلان الشهر.

   يجب ان يكون DAY رقمان يمثلان اليوم.

   يجب ان يكون title نصاً مكونا من احرف وارقام وتستبدل المسافات بـ -

   كالتالي:

<div dir="ltr">

    2021-04-28-list-comprehensions.md

</div>

 - الملف من الداخل يجب ان يتبع هذا التنسيق

<div dir="ltr">

~~~
--- 
layout: post
title: "مفهوم list comprehension"  
date: 2021-04-28  
categories: tutorial   
author: "Essa Alshammari"  
---
# مرحبا بالجميع
هنا يكون الموضوع وتنسيقة يتم عن طريق markdown
~~~

</div>


   - اكتب اسمك مكان author
 
   - اكتب اسم الموضوع مكان title

   - غير التاريخ الى تاريخ كتابة الموضوع مكان date

   - صنف الموضوع مكان categories

</div>