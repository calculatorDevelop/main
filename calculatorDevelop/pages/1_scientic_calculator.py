import streamlit as st
from math import *
from math import factorial as f

def calculate(expression):  
    try:  
        result = eval(expression)  
        return result  
    except:  
        st.error('等待输入')  
        return None
  
def main():
    st.header('科学计算器')  
    expression = st.text_input('请输入表达式')

    #计算说明
    with st.expander('对计算有疑惑？'):
        explain_for_cal='''
                  **注意：**\n
                    1.暂不支持解析中文括号（），请使用英文括号()\n
                    2.自然对数请用e，圆周率请用pi\n
                    3.:red[乘号是不可以忽略的]，需要用 * 号  例如：2*3=6\n
                    4.计算余数请用 % ，百分号 % 不再有效  例如：3%2=1\n
                    5.计算幂请用 ** 符号  例如：2**3=8\n
                    6.计算阶乘请用符号 f ，并用括号明确数字  例如：f(5)=120\n
                    7.计算对数请用括号明确真数和对数的底，:red[且真数在前，对数的底在后]  例如：log(100,10)=2\n
                    8.计算三角函数请用括号明确数字，反三角函数同理  例如：sin(pi/2)=1\n
                    :red[最终计算结果保留10位小数]
                    '''
        st.markdown(explain_for_cal)
        
    result = calculate(expression)
    if st.button(' **计算** '):
        st.write('结果是：',result)  
       
if __name__ == '__main__':  
    main()