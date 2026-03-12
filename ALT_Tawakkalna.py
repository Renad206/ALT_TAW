import streamlit as st 

st.title ("منصة تسجيل بيانات المستخدمين")

name = st.text_input("الاسم الرباعي")

id = st.text_input("رقم الهوية/الاقامة", max_chars=10, help="أدخل 10 أرقام")

phone = st.text_input("رقم الجوال", placeholder="05XXXXXXXX", max_chars=10)

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

if st.button("تسجيل"):
    st.success("تم التسجيل بنجاح")

    st.write("البيانات المدخلة:")
    st.write("الاسم:" , name)
    st.write("رقم الهوية:" , id)
    st.write("رقم الجوال:" , phone)
    st.write("المؤهل:" , degree)
    st.write("سنوات الخبرة:" ,exp)
    st.write("المهارات:" , skills)

    
    