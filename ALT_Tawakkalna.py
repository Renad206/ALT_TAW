import streamlit as st 

st.title ("منصة تسجيل بيانات المستخدمين")

name = st.text_input("الاسم الرباعي")

id = st.text_input("رقم الهوية/الاقامة", max_chars=10, help="أدخل 10 أرقام")

birth = st.date_input(
    "تاريخ الميلاد",
    value=datetime.date(2000, 1, 1),
    min_value=datetime.date(1920, 1, 1),
    max_value=datetime.date.today()
)


phone = st.text_input("رقم الجوال", placeholder="05XXXXXXXX", max_chars=10)

email = st.text_input("البريد الالكتروني")

uni = st.selectbox(
"الجامعة"
,
["جامعة الملك فيصل" , "" , "" , "" ]
)

degree = st.selectbox(
"الدرجة العلمية"
,
["دكتوراه" , "ماجستير" , "بكالوريوس" , "دبلوم" , "ثانوي"]
)

exp = st.number_input("سنوات الخبرة" , min_value = 0 , max_value = 40)

skills = st.multiselect(
"المهارات"
,
["العمل الجماعي" , "اللغة الانجليزية" , "التسويق" , "ادارة المشاريع" , "تحليل البيانات" , "البرمجة" , "كتابة تقارير"]
)

lang = st.multiselect(
"اللغات"
,
["العربية" , "" , "" , "" , "" , "" ]
)

if st.button("تسجيل"):
    if ( 
        name == "" or 
        id == "" or 
        birth == "" or
        phone == "" or 
        email == "" or
        uni == "" or
        degree == "اختر المؤهل"
    ):
        st.error("يجب تعبئة جميع البيانات") 
    elif len(phone) != 10 or not phone.startswith("05"):
        st.error("رقم الجوال غير صحيح")
        
    elif "@" not in email:
        st.error("البريد الالكتروني غير صحيح")
    
    elif len (skills) < 3:
        st.error("يجب اختيار 3 مهارات على الاقل")

    else:
        
            
        st.success("تم التسجيل بنجاح")
    
        st.write("البيانات المدخلة:")
        st.write("الاسم:" , name)
        st.write("رقم الهوية:" , id)
        st.write("رقم الجوال:" , phone)
        st.write("المؤهل:" , degree)
        st.write("سنوات الخبرة:" ,exp)
        st.write("المهارات:" , skills)

    

    

