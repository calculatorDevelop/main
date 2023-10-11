import streamlit as st
from math import *

def main():
    #页面设置
    st.set_page_config(layout="wide")
    st.header('原神伤害计算器')

    #分成两列，左列选择乘区，右列是便携计算器
    col_cq,col_cal=st.columns([0.7,0.25])

    #左列开始
    with col_cq:
        #分成6页，每页放置一个乘区
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['基准*倍率+附加','增伤','抗性','防御','双爆','增幅'])

        #基准（jz）*倍率（bl）乘区,gjl攻击力，smz生命值，fyl防御力，ysjt元素精通，cs乘数
        with tab1:
            #flag_用于标记是否参与单词条提升分析
            if st.toggle('攻击力倍率'):
                flag_gjl=True
                gjlblcs=1
                gjl=st.number_input('请输入攻击力',min_value=0,value=2000,step=1)
                bl_gjl=st.number_input('请输入攻击力倍率',min_value=0.0,value=1.0,step=0.001)
                #攻击力倍率乘数
                if st.toggle('攻击力倍率乘数'):
                    gjlblcs=st.number_input('请输入攻击力倍率乘数',min_value=0.0,value=1.0,step=0.001)
                    gjlbl=gjl*bl_gjl*gjlblcs
                else:    
                    gjlbl=gjl*bl_gjl
                st.markdown('\n\n')
            else:
                flag_gjl=False
                gjlbl=0

            if st.toggle('生命值倍率'):
                flag_smz=True
                smz=st.number_input('请输入生命值',min_value=0,value=20000,step=1)
                bl_smz=st.number_input('请输入生命值倍率',min_value=0.0,value=1.0,step=0.001)
                smzbl=smz*bl_smz
            else:
                flag_smz=False
                smzbl=0

            if st.toggle('防御力倍率'):
                flag_fyl=True
                fyl=st.number_input('请输入防御力',min_value=0,value=2000,step=1)
                bl_fyl=st.number_input('请输入防御力倍率',min_value=0.0,value=1.0,step=0.001)  
                fylbl=fyl*bl_fyl
            else:
                flag_fyl=False
                fylbl=0

            if st.toggle('元素精通倍率'):
                flag_ysjt=True
                ysjt=st.number_input('请输入元素精通',min_value=0,value=200,step=1)
                bl_ysjt=st.number_input('请输入参与倍率计算的元素精通',min_value=0.0,value=1.0,step=0.001) 
                ysjtbl=ysjt*bl_ysjt
            else:
                flag_ysjt=False
                ysjtbl=0
            #基准倍率求和
            jzbl=gjlbl+smzbl+fylbl+ysjtbl

            #附加倍率，fj附加
            flag_fjgjl=False
            flag_fjsmz=False
            flag_fjfyl=False
            flag_fjysjt=False
            if st.toggle('附加倍率'):
                if st.toggle('附加攻击力倍率'):
                    flag_fjgjl=True
                    fjgjl=st.number_input('请输入附加攻击力',min_value=0,value=2000,step=1)
                    bl_fjgjl=st.number_input('请输入附加攻击力倍率',min_value=0.0,value=1.0,step=0.001)
                    fj_gjlbl=fjgjl*bl_fjgjl
                else:
                    fj_gjlbl=0

                if st.toggle('附加生命值倍率'):
                    flag_fjsmz=True
                    fjsmz=st.number_input('请输入附加生命值',min_value=0,value=20000,step=1)
                    bl_fjsmz=st.number_input('请输入附加生命值倍率',min_value=0.0,value=1.0,step=0.001)
                    fj_smzbl=fjsmz*bl_fjsmz
                else:
                    fj_smzbl=0

                if st.toggle('附加防御力倍率'):
                    flag_fjfyl=True
                    fjfyl=st.number_input('请输入附加防御力',min_value=0,value=2000,step=1)
                    bl_fjfyl=st.number_input('请输入附加防御力倍率',min_value=0.0,value=1.0,step=0.001)  
                    fj_fylbl=fjfyl*bl_fjfyl
                else:
                    fj_fylbl=0

                if st.toggle('附加元素精通倍率'):
                    flag_fjysjt=True
                    fjysjt=st.number_input('请输入附加元素精通',min_value=0,value=200,step=1)
                    bl_fjysjt=st.number_input('请输入附加元素精通倍率',min_value=0.0,value=1.0,step=0.001) 
                    fj_ysjtbl=fjysjt*bl_fjysjt
                else:
                    fj_ysjtbl=0
                #附加倍率求和
                fjbl=fj_gjlbl+fj_fylbl+fj_smzbl+fj_ysjtbl
            else:
                fjbl=0

        #增伤（zs）乘区
        with tab2:
            zs=st.number_input('请输入增伤系数',min_value=0.0,value=1.0,step=0.001)

        #抗性（kx）乘区，gwkx怪物抗性
        def get_kx(gwkx):#根据怪物抗性得到抗性系数
                if gwkx<0:
                    return 1-gwkx/2
                if gwkx>0.75:
                    return 1/(1+4*gwkx)
                else:
                    return 1-gwkx
        with tab3:     
            gwkx=st.number_input('请输入怪物抗性',value=1.0,step=0.001)
            kx=get_kx(gwkx)

        #防御（fy）乘区,jsdj角色等级，gwdj怪物等级，jf减防，wsfy无视防御    
        def get_fy(jsdj,gwdj,jf=0.0,wsfy=0.0):#计算防御系数
            return (jsdj+100)/((gwdj+100)*(1-jf)*(1-wsfy)+(jsdj+100))
        with tab4:
            jsdj=st.slider('请选择角色等级',1,90,90)
            gwdj=st.slider('请选择怪物等级',1,100,100)
            jf=st.number_input('请输入减防量',min_value=0.0,value=0.0,step=0.01)
            wsfy=st.number_input('请输入无视防御量',min_value=0.0,value=0.0,step=0.01)
            fy=get_fy(jsdj,gwdj,jf,wsfy)

        #暴击乘区，bjl暴击率，bjsh暴击伤害，qw期望
        with tab5:  
            bjl=st.number_input('请输入暴击率',min_value=0.0,max_value=1.0,value=0.05,step=0.001)
            bjsh=st.number_input('请输入暴击伤害',min_value=0.0,value=0.5,step=0.001)
            #暴击期望乘数计算
            qw=1+bjl*bjsh

        #增幅（zf）乘区，jczf基础增幅
        def get_zf(jczf,ysjt_r):  #计算增幅系数
            return jczf+2.78*ysjt_r/(ysjt_r+1400)
        with tab6:
            jczf=st.slider('请选择基础增幅系数',1.0,2.0,1.0,0.5)
            if jczf>1:
                ysjt_r=st.number_input('请输入用于反应的元素精通',min_value=0,value=200,step=1)
                zf=get_zf(jczf,ysjt_r)
    #左列结束

    #右列开始
    with col_cal:
        def calculate(expression):  
            try:  
                result = eval(expression)  
                return result  
            except:  
                st.error('等待输入')  
                return None
            
        st.markdown('**便携计算器**')    
        expression = st.text_input('请输入表达式')
        result = calculate(expression)
        if st.button('='):
            st.write(result)  

    st.markdown('\n\n')
    #单词条提升(ts)分析，额外增加一个词条，计算伤害提升百分比  
    #单个词条：5%攻击 5%生命 6.2%防御力 5%增伤 3.3%暴击 6.6%暴击伤害 20精通 *5%减抗 5%减防 5%无视防御
    if st.toggle('单词条提升分析'):
        #根据标记获取基础值jc,并计算提升ts
        #倍率区
        temp=jzbl+fjbl #记录原先的倍率区
        if flag_gjl:
            jc_gjl=st.number_input('请输入基础攻击力',min_value=1,value=300,step=1)
            ts_gjl=jc_gjl*5*bl_gjl*gjlblcs/temp
        if flag_smz:
            jc_smz=st.number_input('请输入基础生命值',min_value=1,value=10000,step=1)
            ts_smz=jc_smz*5*bl_smz/temp
        if flag_fyl:
            jc_fyl=st.number_input('请输入基础防御力',min_value=1,value=300,step=1)
            ts_fyl=jc_fyl*6.2*bl_fyl/temp
        if flag_ysjt:
            ts_ysjt=2000/ysjt
        if flag_fjgjl:
            jc_fjgjl=st.number_input('请输入附加的基础攻击力',min_value=1,value=300,step=1)
            ts_fjgjl=jc_fjgjl*5*bl_fjgjl/temp
        if flag_fjsmz:
            jc_fjsmz=st.number_input('请输入附加的基础生命值',min_value=1,value=10000,step=1)
            ts_fjsmz=jc_fjsmz*5*bl_fjsmz/temp
        if flag_fjfyl:
            jc_fjfyl=st.number_input('请输入附加的基础防御力',min_value=1,value=300,step=1)
            ts_fjfyl=jc_fjfyl*5*bl_fjfyl/temp
        if flag_fjysjt:
            ts_fjysjt=2000/fjysjt
        #倍率区结束

        ts_zs=5/zs  #增伤
        if bjl+0.033>100:  #暴击率
            ts_bjl=(1-bjl)*bjsh*100/qw
        else:
            ts_bjl=3.3*bjsh/qw
        ts_bjsh=bjl*6.6/qw  #暴击伤害
        ts_jk=(get_kx(gwkx-0.05)-kx)*100/kx  #减抗
        if jsdj>80 and jsdj<90:  #角色等级
            ts_jsdj=(get_fy(90,gwdj,jf,wsfy)-fy)*100/fy
        if jsdj<=80:
            ts_jsdj=(get_fy(jsdj+10,gwdj,jf,wsfy)-fy)*100/fy
        ts_jf=(get_fy(jsdj,gwdj,jf+0.05,wsfy)-fy)*100/fy  #减防
        ts_wsfy=(get_fy(jsdj,gwdj,jf,wsfy+0.05)-fy)*100/fy  #无视防御
        if jczf>1:  #增幅
            ts_zf=(get_zf(jczf,ysjt_r+20)-zf)*100/zf
        
    #结果展示,result伤害结果，_b暴击伤害，_qw暴击期望伤害，_r反应伤害
    #分2列展示伤害，无反应在左，反应在右
    col_res,col_res_r=st.columns(2)
    #分3列展示单词条提升分析
    col_ts_1,col_ts_2,col_ts_3=st.columns(3)
    if st.button('计算'):
        st.markdown('\n\n')
        with col_res:
            result=(jzbl+fjbl)*zs*kx*fy
            result_b=result*(1+bjsh)
            result_qw=result*qw
            st.write('无反应未暴击伤害是：',round(result))
            st.write('无反应暴击伤害是：',round(result_b))
            st.write('无反应期望伤害是：',round(result_qw))
        #反应伤害展示
        with col_res_r:
            if jczf>1:
                result_r=result*zf
                result_r_b=result_r*(1+bjsh)
                result_r_qw=result_r*qw
                st.write('反应未暴击伤害是：',round(result_r))
                st.write('反应暴击伤害是：',round(result_r_b))
                st.write('反应期望伤害是：',round(result_r_qw))

        st.markdown('\n\n') 
        #单词条提升展示
        with col_ts_1: 
            if flag_gjl:
                st.write('5%攻击力(',round(jc_gjl*0.05),')可以提升伤害：',round(ts_gjl,2),'%')
            if flag_smz:
                st.write('5%生命值(',round(jc_smz*0.05),')可以提升伤害：',round(ts_smz,2),'%') 
            if flag_fyl:
                st.write('6.2%防御力(',round(jc_fyl*0.062),')可以提升伤害：',round(ts_fyl,2),'%')
            if flag_ysjt:
                st.write('20元素精通可以提升伤害：',round(ts_ysjt,2),'%')
            if flag_fjgjl:
                st.write('5%附加攻击力(',round(jc_fjgjl*0.05),')可以提升伤害：',round(ts_fjgjl,2),'%')
            if flag_fjsmz:
                st.write('5%附加生命值(',round(jc_fjsmz*0.05),')可以提升伤害：',round(ts_fjsmz,2),'%')
            if flag_fjfyl:
                st.write('6.2%附加防御力(',round(jc_fjfyl*0.062),')可以提升伤害：',round(ts_fjfyl,2),'%')
            if flag_fjysjt:
                st.write('20附加元素精通可以提升伤害：',round(ts_fjysjt,2),'%')
        with col_ts_2:
            st.write('5%增伤可以提升伤害：',round(ts_zs,2),'%')
            st.write('3.3%暴击率可以提升伤害：',round(ts_bjl,2),'%')
            if bjl+0.033>100:
                st.write('暴击率溢出，收益有所下降')
            st.write('6.6%暴击伤害可以提升伤害：',round(ts_bjsh,2),'%')
            st.write('5%减抗可以提升伤害：',round(ts_jk,2),'%')
        with col_ts_3:
            if jsdj>80 and jsdj<90:
                st.write('将角色升至满级可以提升伤害：',round(ts_jsdj,2),'%')
            if jsdj<=80:
                st.write('提升10级角色等级可以提升伤害：',round(ts_jsdj,2),'%')
            st.write('5%减防可以提升伤害：',round(ts_jf,2),'%')
            st.write('5%无视防御可以提升伤害：',round(ts_wsfy,2),'%')
            if jczf>1:
                st.write('20元素精通用于反应可以提升伤害：',round(ts_zf,2),'%')
        
if __name__ == '__main__':  
    main()