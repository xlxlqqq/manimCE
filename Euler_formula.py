from manim import *

# Title: 为什么全体自然数平方的倒数和等于π^2/6？
# Tags:
# Desc:
# Author: 
# Date:2022-03-26 19:07:13



class CodeVideo(Scene):
    def copy_right(self):
        '''
        版权
        '''
        g = Group()
        author = Text('@123456')
        by = Text('制作方')
        g.add(author,by).scale(0.5)
        g.arrange(DOWN,buff=0.1).to_edge(DR,buff=0.2)
        g.set_color_by_gradient(RED,BLUE)
        
        self.add(g)
        # self.wait(7)
        
        
        
        
    def problem_desc(self):
        '''
        问题介绍
        全体自然数的平方的倒数和等于多少？这是著名的巴塞尔问题。
        现有的对这个问题的解答方法有很多，
        但在当时这个问题刚刚被提出的时候却难倒了一众数学家。
        直到 [欧拉] 的出现才第一次解决了这个问题，
        所以这个问题就以 [公式] 的故乡—瑞士的巴塞尔进行命名了。
        下面，我们首先来看看欧拉是如何解决这个问题的。
        '''
        # Markup 是一种标记语言
        # 参考 https://chenliangjing.me/2019/10/11/Playground-Markup-%E8%AF%AD%E6%B3%95/
        text1 = MarkupText("<big>问题介绍</big>")
        text3 = MarkupText("<small>全体自然数的平方的倒数和等于多少</small>")
        
        # 前面添加 r 是为了不要 里面的内容 转义
        f_a = ['1','2','3','4',r'\dots','n']
        f = []
        for x in f_a:
            if x == r'\dots':
                f.append(x)
            else:
                f.append(r'\frac{1}{%s^{2} } ' %(x))
            f.append("+")
        f = f[0:-1]
        f.append('=?')
        
        text2 = MathTex(*f)
        text2_anm = []
        for x in text2:
            x.set_color(random_color())
            text2_anm.append(Write(x))
          
        g = VGroup(text1, text2,text3).arrange(DOWN,buff=1)
        # self.add(g)
        self.play(*[Write(text1)])
        self.wait()
        for x in text2_anm:
            self.play(x,run_time=0.3)
        self.play(Write(text3),run_time=1)
        self.wait(3)
        self.play(FadeOut(g),run_time=1)
        
    def construct(self):
        self.copy_right()
        self.problem_desc()
        self.copy_right()
        self.setp_1()
        self.copy_right()
        self.setp_2()
        self.copy_right()
        self.oula()
        
    def gen_x3(self):
        '''
        画出 x^2+3x+2 的图像
        '''
        
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-10, 10, 1],
            x_length=config.frame_width/2,
            axis_config={"color": GREEN},
            # x_axis_config={
            #     "numbers_to_include": np.arange(-10, 10.01, 2),
            #     "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            # },
            tips=False,
            color = GRAY_E,
            fill_opacity=1
        )
        axes_labels = axes.get_axis_labels()
        
        # 函数表达式
        x3_graph = axes.plot(lambda x: np.power(x,2)+3*x+2,color = WHITE)
    

        x3_graph_lab = axes.get_graph_label(
            x3_graph, "x^2+3x+2", x_val=1
        )
        
        plot = VGroup(axes, axes_labels,x3_graph_lab)
        # 围绕一个 长方形 在函数图像上面
        sur = SurroundingRectangle(plot,color=GRAY_E,fill_opacity=1,buff=0.1,)
        
        # 定义一个 变化函数 当函数图像变化时 跟随变化
        def sur_upt(o):
            o.become(SurroundingRectangle(plot,color=GRAY_E,fill_opacity=1,buff=0.1,))
        sur.add_updater(sur_upt)
        
        self.add(sur,plot)
        # plot.add(sur)
        self.play(Create(x3_graph))
        plot.add(x3_graph)
        
        for x in range(-2,0,1):
            # 输入 x的值 得到 函数上的点的坐标
            d = Dot(axes.i2gp(x, x3_graph))
            t = Tex('$%d$' %(x))
            t.next_to(d,DOWN)
            l = Line(d.get_center(),t.get_center())
            ann = [Create(d),Create(t),Create(l)]
            self.play(*ann)
            plot.add(d,t,l)
        self.wait()
        self.play(plot.animate.scale(0.5))
        self.wait()
        # self.play(plot.animate.to_edge(UR))
        
 
        
    def setp_1(self):
        '''
        第一步
        首先，让我们来思考一个问题，如何将函数  写成一个无穷乘积的形式？
        '''
        text1 = Text('首先，让我们来思考一个问题?').scale(0.8)
        text2 = Text('如何将下面的公式，写成一个无穷乘积的形式').scale(0.8)
        text3 = Tex("$f(x)=sin(x)$").scale(2).set_color(YELLOW)
        g = Group(text1,text2,text3).arrange(DOWN,buff=0.5)
        self.play(GrowFromCenter(g))
        self.wait(4)
        self.play(g.animate.shift(UP*config.frame_height))
        self.wait()
        
        
        # 所谓因式分解就是将一个多项式写为多个因式乘积的形式，比如
        text1 = Text('所谓无穷乘积就是因式分解').scale(0.8)
        text2 = Text('就是将一个多项式写为多个因式乘积的形式，比如').scale(0.8)
        text3 = Tex('$x^2+3x+2=$','$(x+1)(x+2)$',color=RED).scale(2)
        g2 = Group(text1,text2,text3).arrange(DOWN,buff=0.5)
        self.play(*[Write(text1),Write(text2)])
        self.wait()
        self.play(Write(text3[0]))
        self.wait()
        text3[1].set_color(YELLOW)
        
        
        self.gen_x3()
        
        self.play(Write(text3[1]))
        
        text4 = Text('对于一个多项式来讲，它如果可以被分解为').scale(0.8)
        g2.add(text4)
        g2.arrange(DOWN,buff=0.5)
        self.play(Write(text4))
        text5 = Tex('$P(x)=x^n+a_1\cdot x^{n-1}+\dots+a_n=(x-x_1)\cdot(x-x_2)\cdots (x-x_n)$').scale(1).set_color(YELLOW)
        g2.add(text5)
        text3.scale(0.5)
        g2.arrange(DOWN,buff=0.5)
        self.play(Write(text5))
        self.wait()
        # self.play(g2.animate.shift(UP*config.frame_height/2))
        
        text6 = Tex('$x_1 x_2 \cdots x_n$')
        g2.add(text6)
        g2.arrange(DOWN,buff=0.5)
        self.play(Write(text6))
        
        text7 = Text('上面的x值就是在 P(x)=0 时的全体解')
        
        g2.add(text7)
        g2.arrange(DOWN,buff=0.5)
        self.play(Write(text7))
        self.wait(3)
        self.clear()
        
        # self.play(FadeOut(g2))
        
    def setp_2(self):
        '''
        现在我们回过头来看函数 ，这不是一个多项式，
        但我们仍可以将其写为无穷个多项式乘积的形式。
        首先，我们需要明确 [公式] 的零点都在哪里：
        '''
        text1= Text('现在问题变为')
        text2= Tex('$f(x)=sin(x)$',color=YELLOW).scale(2)
        text3= Text('零点在哪里？')
        g = Group(text1,text2,text3).arrange(DOWN,buff=0.5)
        self.play(GrowFromCenter(g))
        self.wait(3)
        self.play(FadeOut(g))
        
        
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            axis_config={"color": GREEN},
            # x_axis_config={
            #     "numbers_to_include": np.arange(-10, 10.01, 2),
            #     "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            # },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
    

        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=-10, direction=UP / 2
        )
        print(axes.i2gp(PI/2, sin_graph))
     
        # vert_line = axes.get_vertical_line(
        #     axes.i2gp(PI/2, sin_graph), color=YELLOW, line_func=Line
        # )
        
      
        plot = VGroup(axes,axes_labels,sin_label)
        labels = VGroup(axes_labels, sin_label)
        self.add(plot)
        self.play(Create(sin_graph))
        plot.add(sin_graph)
        self.wait()

        for x in range(-3,4,1):
            d = Dot(axes.i2gp(PI*x, sin_graph))
            if x == 0 :
                t = Tex('$0$')
            else:
                t = Tex('$%d\pi$' %(x)) 
            t.next_to(d,DOWN*5)
            l = DashedLine(d.get_center(),t.get_center())
            self.add(d,t,l)
            plot.add(d,t,l)
        self.wait(2)
        
        # 从这里往下就是公式变换了
        text_1 = Tex(
            "$sin(x)$",
            "$=$",
            "$(x-0)$",
            r"$(1-\frac{x}{\pi })$",
            r"$(1+\frac{x}{\pi })$",
            r"$(1-\frac{x}{2\pi })$",
            r"$(1+\frac{x}{2\pi })$",
            r"$\dots$"
            )
        
        g3 = Group(plot,text_1).arrange(DOWN)
        for i,x in enumerate( text_1 ):
            self.play(Create(x),run_time=0.5)
        self.wait(2)
        
        text_2 = Tex(
            "$sin(x)$",
            "$=$",
            "$x$",
            r"$(1-\frac{x^2}{\pi^2 })$",
            r"$(1-\frac{x^2}{(2\pi)^2 })$",
            r"$\dots$",
            r"$(1-\frac{x^2}{(n\pi)^2 })$",
            )
        g3.add(text_2)
        g3.arrange(DOWN,buff=0.1)
        
        for i,x in enumerate( text_2[:2] ):
            self.play(Create(x))
        self.play(TransformFromCopy(text_1[2],text_2[2]))
        self.wait()
        self.play(TransformFromCopy(text_1[3:5],text_2[3]))
        self.wait()
        self.play(TransformFromCopy(text_1[5:7],text_2[4]))
        self.wait()
        for i,x in enumerate( text_2[-2:] ):
            self.play(Create(x))
        self.wait(6)
        #  移除 函数图像
        self.play(plot.animate.shift(LEFT*15))
        g3.remove(plot)
       
        text_5 = MathTex(r'sin(x)=x\cdot \prod_{ k=1}^{+\infty} (1-\frac{x^2}{k^2x^2} )')
        g3.add(text_5)
        g3.arrange(DOWN,buff=0.5,aligned_edge=LEFT)
      
        self.play(Create(text_5))
        self.wait()
        text_6 = Text('取出连乘号里最前面的3项并记做')
        text_7 = Tex(
            "$sin_3(x)$",
            "$=$",
            "$x$",
            r"$(1-\frac{x^2}{\pi^2 })$",
            r"$(1-\frac{x^2}{(2\pi)^2 })$",
             r"$(1-\frac{x^2}{(3\pi)^2 })$",
           
            )
        g3.add(text_6,text_7)
        g3.arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        self.play(Create(text_6))
        self.wait()
        self.play(Create(text_7))
        self.wait(6)
        
        for x in g3:
            if x != text_7:
                self.play(FadeOut(x),run_time=0.2)
                g3.remove(x)
        g3.arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        self.wait()
        
        text_8 = MathTex(r'sin_3(x)=T_3(x)-\frac{x^3}{\pi ^2} -\frac{x^3}{2^2\pi ^2} -\frac{x^3}{3^2\pi ^2} ')
        g3.add(text_8)
        g3.arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        self.play(Create(text_8))
        self.wait()
        
        text_9 = MathTex(r'sin_n(x)=T_n(x)-x^3\sum_{k=1}^{n}  \frac{1}{k^2\pi ^2} ')
        g3.add(text_9)
        g3.arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        self.play(Create(text_9))
        self.wait()
        
        text_10 = MathTex(
            r'sin_n(x)\to sin(x)=T(x)-',
        r'x^3\sum_{k=1}^{n}  \frac{1}{k^2\pi ^2} ',
        r'(n\to \infty )'
        )
        g3.add(text_10)
        g3.arrange(DOWN,buff=0.5,aligned_edge=LEFT)
        self.play(Create(text_10))
        self.wait()
        
        text_11 = Text('又知道sin(x)幂级数展开式:').scale(0.5)
        text_12 = MathTex(r'sin(x) = T(x)- ',r'\frac{x^3}{3!}')
        
        g3.add(text_11,text_12)
        g3.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        self.play(Create(text_11))
        self.play(Create(text_12))
        self.wait(5)
        
    
        
        for x in g3:
            if x not in [text_10,text_12]:
                self.play(FadeOut(x),run_time=0.2)
                g3.remove(x)
        g3.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        self.wait()
        
        text_13 = MathTex(
            r'\frac{x^3}{3!}',
            '=',
            r'x^3\sum_{k=1}^{n}  \frac{1}{k^2\pi ^2} '
            )
        g3.add(text_13)
        g3.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        self.play(TransformFromCopy(text_12[1],text_13[0]))
        self.play(TransformFromCopy(text_10[1],text_13[2]))
        self.play(Create(text_13[1]))
        self.wait(3)
        
        for x in g3:
            if x not in [text_13]:
                self.play(FadeOut(x),run_time=0.2)
                g3.remove(x)
        g3.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        
        text_14 = MathTex(r'\Longrightarrow \frac{1}{6}=\frac{1}{\pi^2} \sum_{k=1}^{n}  \frac{1}{k^2} ')
        g3.add(text_14)
       

        text_15 = MathTex(r'\Longrightarrow \frac{\pi^2}{6}= \sum_{k=1}^{n}  \frac{1}{k^2} = 1+\frac{1}{2^2} +\frac{1}{3^2} +\dots +\frac{1}{n^2} ')
        g3.add(text_15)
        g3.arrange(DOWN,buff=0.2,aligned_edge=LEFT)
        
        self.play(Create(text_14))
        self.wait()
        self.play(Create(text_15))
        self.wait(5)
        self.clear()
        
        
    def oula(self):
        
        oula = ImageMobject('assets/images.jpg')
        oula.width = config.frame_width/2.5
        t = Text('欧拉 Leonhard Paul Euler').scale(0.5)
        t2 = Text('1707年4月15日－1783年9月18日').scale(0.5)
        t1 = Text('此问题由他证明').scale(0.5)
        g = Group(oula,t,t2,t1).arrange(DOWN,buff=0.5)
        self.play(FadeIn(oula))
        self.wait(6)
        self.play(Write(t))
        self.play(Write(t2))
        self.play(Write(t1))
        self.wait(6)