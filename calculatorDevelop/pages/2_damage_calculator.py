import streamlit as st
from math import *

def main():
    #页面设置
    st.set_page_config(layout="wide")
    st.header('原神伤害计算器')
    st.markdown('\n')
    with st.expander(' **使用说明** '):
        st.markdown('''**关于原神伤害计算你需要了解的：**\n
原神的伤害计算结果是由七大乘区相乘所得。\n
其中不同来源的\t**基准x倍率**\t互为加算关系，最终被简化成\t**(基准x倍率+附加)**\t乘区。\n
**我该如何操作？**\n
第一步：根据自身游戏内情况，在每个选项卡中输入相应的值，其中默认值即数值的精确度，如有疑惑可以查看对应说明。\n
第二步：根据需要，选择是否计算单词条提升分析。\n
第三步：点击计算按钮查看结果。
                    ''')

    #分成两列，左列选择乘区，右列是便携计算器
    col_cq,col_cal=st.columns([0.7,0.25])

    #左列开始
    with col_cq:
        #分成6页，每页放置一个乘区
        tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(['基准*倍率+附加','增伤','抗性','防御','双爆','增幅'])

        #基准（jz）*倍率（bl）乘区,gjl攻击力，smz生命值，fyl防御力，ysjt元素精通，cs乘数
        with tab1:
            with st.expander('对倍率区有疑惑？'):
                st.markdown('''**为什么有这么多选项？我该如何选择？**\n
**·** 倍率区是由不同来源的基准*倍率所得，其中基准就如选项展示，而倍率由技能说明决定。\n
**·** 打开角色详情，选择需要计算的技能，查看详细信息，可以看到精确的技能倍率。\n
**·** 技能倍率默认为攻击力倍率，显示为不加说明的百分数，而除攻击力以外的生命值倍率，防御力倍率等则会有明确说明。\n
**什么是附加倍率？我从哪里可以看到？**\n
**·** 附加倍率是除角色技能之外的，其他来源的的倍率，可以来自角色天赋，角色命座，队伍中其他角色。\n
**·\t例如：** 钟离天赋可以为自己额外增加基于自身的生命值倍率。申鹤可以给予队伍中所有角色基于自身攻击力的额外倍率。\n
**·** 原神中附加倍率的来源有许多，留意角色自身天赋、命座，队友天赋及命座即可。\n
**攻击力倍率里为什么会有攻击力倍率乘数？我可以从哪里看到？**\n
**·** 倍率乘数是目前游戏中极其稀少的部分，其可以直接与倍率乘算提升伤害。\n
**·** 倍率乘数来源极少， **例如：** 宵宫e技能天赋，提升普通攻击的倍率。行秋第4命座提升e技能倍率等。\n
**·** :red[在多数情况下你可以完全忽略它。]
                            ''')
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
            with st.expander('对增伤区有疑惑？'):
                st.markdown('''**什么是增伤？我可以从哪里看到？**\n
**·** 增伤是原神文本说明中 :red[绝大多数] **伤害增加** 和 **伤害提升** 简略描述，这些都归属于增伤乘区。\n
**·** 增伤在原神中很常见， **例如：** 角色详情页面中的 **XX元素伤害提升** ，角色命座， :red[元素共鸣]等。\n
**·** :red[注意：] 请留意面板增伤，非面板增伤，非全伤害增加\n
**·** **例如：** 枫原万叶的天赋会实时显示在角色详情。\n
而夜兰的天赋取决于召唤物的留存时间，不会显示在角色详情中。\n
丘丘霜铠王的护盾期间可以减少我方80%物理/元素伤害加成，为减算关系。\n
圣遗物绝缘之旗印的套装效果只作用于元素爆发，因此也不会显示在角色详情中。
''')
            zs=st.number_input('请输入增伤系数',min_value=0.0,value=1.0,step=0.001)

        #抗性（kx）乘区，gwkx怪物抗性
        def get_kx(gwkx):  #根据怪物抗性得到抗性系数
                if gwkx<0:
                    return 1-gwkx/2
                if gwkx>0.75:
                    return 1/(1+4*gwkx)
                else:
                    return 1-gwkx
        with tab3: 
            with st.expander('对抗性区有疑惑？'):
                st.markdown('''**什么是抗性？我可以从哪里看到？**\n
**·** 抗性是专属于怪物的减免伤害的一种乘区。\n
**·** 不同的怪物具有不同的抗性，:red[一般情况下抗性为10%]，而专精某一元素的怪物可以有70%的对应元素抗性。\n
人形怪物的物理抗性普遍较低，而发条机械类的怪物物理抗性普遍较高。\n
同时怪物的状态也影响着自身抗性，一般情况下，具有护盾则具有高额抗性，而被击倒或虚弱状态抗性较低。\n
**·** 具体怪物抗性图可以在原神wiki上找到。\n
**·** 值得注意的是，角色拥有多种减抗手段， **例如：** 圣遗物翠绿之影的套装效果，角色技能、天赋、命座等。                           
''')      
                if st.toggle('对抗性计算感到好奇？'):
                    st.markdown(''' **怪物抗性为k，怪物的最终承伤系数为x**\n 
**当 k < 0时**\n
**x = 1-k/2**\n
**当 0 <= k <= 0.75时**\n
**x = 1-k**\n
**当k > 0时**\n
**x = 1/(1+4k)**\n
''')
                    st.markdown('\n')
            gwkx=st.number_input('请输入怪物抗性',value=0.1,step=0.001)
            kx=get_kx(gwkx)

        #防御（fy）乘区,jsdj角色等级，gwdj怪物等级，jf减防，wsfy无视防御    
        def get_fy(jsdj,gwdj,jf=0.0,wsfy=0.0):#计算防御系数
            return (jsdj+100)/((gwdj+100)*(1-jf)*(1-wsfy)+(jsdj+100))
        with tab4:
            with st.expander('对防御区有疑惑？'):
                st.markdown('''**什么是防御区？和防御力有关系吗？我能在哪里看到？**\n
**·** 防御是一种基于防御力的伤害减免乘区，同时作用于角色和怪物。\n
**·** 对怪物造成伤害时，防御的计算只和角色等级和怪物等级有关，这是由于怪物的防御力由怪物等级唯一决定。\n
**·** 防御力对应伤害减免系数无法直接看到，但可以通过公式计算得出。
''')
                if st.toggle('对防御系数的计算感到好奇？'):
                    st.markdown(''' **怪物防御=怪物等级*5+500**\n
**防御系数=(角色等级+100)/(角色等级+怪物等级+200)**
''')
                    st.markdown('\n')
                st.markdown('''**什么是减防和无视防御？有什么区别吗？我能在哪里看到？**\n
**·** 减防和无视防御是在原神中较为少见，一般情况下，没有明确的文本说明保持默认值即可。\n
**·** 减防和无视防御都可以影响防御系数的计算，并最终提升伤害，但二者并不是一个概念，二者互为乘算关系。\n
**·** 减防可以在角色天赋和角色命座中找到， **例如：** 丽莎的天赋、神里绫华的第4命座等。\n
无视防御目前只能在角色命座中找到，是极为稀有的属性， **例如：** 雷电将军的第2命座，八重神子的第6命座等。
''')
                if st.toggle('对计算感到好奇？'):
                    st.markdown(' **防御系数=(角色等级+100)/(角色等级+100+(怪物等级+100)(1-减防)(1-无视防御))** ')
                    st.markdown('\n')
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
            with st.expander('对增幅区有疑惑？'):
                st.markdown(''' **什么是基础增幅系数？我在哪里可以看到元素精通影响后增幅系数？** \n
**·** 基础增幅系数即除去元素精通后的增幅反应系数， **即：** :gray[冰]接触:red[火]、:red[火]接触:blue[水]为\t1.5\n
:red[火]接触:gray[冰]、:blue[水]接触:red[火]为\t2.0\n
**·** 你可以在角色详情中直接看到元素精通影响后增幅系数。\n
''')
                if st.toggle('对增幅系数的计算感到好奇？'):
                    st.markdown(''' **元素精通值为m**\n 
**增幅系数=基础增幅系数+2.78*m/(m+1400)**                                
''')
                st.markdown(' **·** :red[在目前环境中，可以认为参与倍率计算的元素精通和参与反应的元素精通一致]')
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

    #单词条提升(ts)分析，额外增加一个词条，计算伤害提升百分比  
    #单个词条：5%攻击 5%生命 6.2%防御力 5%增伤 3.3%暴击 6.6%暴击伤害 20精通 *5%减抗 5%减防 5%无视防御
    st.markdown('\n')
    st.markdown('\n')
    flag_ts=False  #记录是否展示提升分析
    if st.toggle('单词条提升分析'):  #根据标记获取基础值jc,并计算提升ts
        with st.expander(' **什么是单词条提升分析？** '):
            st.markdown('''简单来说，就是提升单个词条能带来的伤害提升，意在为旅行者的角色培养提供一定的参考。\n
**什么是词条？**\n
**·** 原神中以圣遗物为基础的，用于提升伤害的，各种可分配资源就是词条。\n
**·** 从圣遗物词条强化的平均值出发，一条平均词条为 **5%攻击 5%生命 6.2%防御力 5%增伤 3.3%暴击 6.6%暴击伤害 20元素精通**\n
**·** 为了便于比较，约定\t**10角色等级 5%减抗 5%减防 5%无视防御**\t也是一条平均词条。
''')
        flag_ts=True
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
        with st.expander('什么是基础XX？'):
            st.markdown('显示在来源角色的角色详情中，以白色数字显示  **例如：** 基础攻击力是显示在攻击力后的白色数字，而非绿色数字。')
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
    if st.button(' **计算** '):
        with st.expander(' **计算有误？** '):
            st.markdown('''**可能是以下原因：**\n
**1.** 受浮点数精度影响，伤害值在±3以内浮动都在合理范围内。\n
**2.** 怪物抗性有误，具体可查怪物抗性表。\n
**3.** 未计算非面板增伤，非全伤害增加。留意不显示在角色详情的增伤和只作用于某个范围伤害增加效果。 
''')
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

        #单词条提升展示
        if flag_ts:
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