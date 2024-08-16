import os
import sys
from PyQt5.QtGui import QBrush, QColor, QDesktopServices, QFont, QImage, QPainter, QPixmap#需要安装库 pip3 install PyQt5
from PyQt5.QtCore import  QObject,  QRect,  QUrl,  Qt, pyqtSignal 
from PyQt5.QtWidgets import QAbstractItemView,QHeaderView,QApplication, QTableWidgetItem, QFrame, QGridLayout, QGroupBox, QLabel,QFileDialog, QStackedWidget, QHBoxLayout, QVBoxLayout

from qfluentwidgets.components import Dialog  # 需要安装库 pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
from qfluentwidgets import ProgressRing, SegmentedWidget, TableWidget,CheckBox, DoubleSpinBox, HyperlinkButton,InfoBar, InfoBarPosition, NavigationWidget, Slider, SpinBox, ComboBox, LineEdit, PrimaryPushButton, PushButton ,StateToolTip, SwitchButton, TextEdit, Theme,  setTheme ,isDarkTheme,qrouter,NavigationInterface,NavigationItemPosition, EditableComboBox
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar


from .AI_Platform_Interface.Interface_AI import Widget_AI
from .AI_Platform_Interface.Interface_official_api import Widget_official_api
from .AI_Platform_Interface.Interface_Openai import Widget_Openai
from .AI_Platform_Interface.Interface_Proxy import Widget_Proxy
from .AI_Platform_Interface.Interface_Anthropic import Widget_Anthropic
from .AI_Platform_Interface.Interface_Google import Widget_Google
from .AI_Platform_Interface.Interface_Cohere import Widget_Cohere
from .AI_Platform_Interface.Interface_ZhiPu import Widget_ZhiPu
from .AI_Platform_Interface.Interface_Yi import Widget_Yi
from .AI_Platform_Interface.Interface_Moonshot import Widget_Moonshot
from .AI_Platform_Interface.Interface_Deepseek import Widget_Deepseek
from .AI_Platform_Interface.Interface_Dashscope import Widget_Dashscope
from .AI_Platform_Interface.Interface_Volcengine import Widget_Volcengine
from .AI_Platform_Interface.Interface_SakuraLLM import Widget_SakuraLLM


from .Translation_Settings_Interface.Interface_translation_settings import Widget_translation_settings
from .Translation_Settings_Interface.Interface_translation_settings_A import Widget_translation_settings_A
from .Translation_Settings_Interface.Interface_translation_settings_B1 import Widget_translation_settings_B1
from .Translation_Settings_Interface.Interface_translation_settings_B2 import Widget_translation_settings_B2
from .Translation_Settings_Interface.Interface_translation_settings_B3 import Widget_translation_settings_B3
from .Translation_Settings_Interface.Interface_translation_settings_C import Widget_translation_settings_C


from .Start_Translation_Interface.Interface_start_translation import Widget_start_translation

from .Prompt_Book_Interface.Interface_rulebook import Widget_rulebook
from .Prompt_Book_Interface.Interface_system_prompt import Widget_system_prompt
from .Prompt_Book_Interface.Interface_prompt_dict import Widget_prompt_dict
from .Prompt_Book_Interface.Interface_characterization import Widget_characterization
from .Prompt_Book_Interface.Interface_world_building import Widget_world_building
from .Prompt_Book_Interface.Interface_writing_style import Widget_writing_style
from .Prompt_Book_Interface.Interface_translation_example import Widget_translation_example


from .Replacement_Dictionary_Interface.Interface_replace_dict import Widget_replace_dict


from .Parameter_Adjustment_Interface.Interface_tune import Widget_tune
from .Parameter_Adjustment_Interface.Interface_tune_anthropic import Widget_tune_anthropic
from .Parameter_Adjustment_Interface.Interface_tune_google import Widget_tune_google
from .Parameter_Adjustment_Interface.Interface_tune_openai import Widget_tune_openai
from .Parameter_Adjustment_Interface.Interface_tune_sakura import Widget_tune_sakura


from .Other_Interfaces.Interface_AvatarWidget import AvatarWidget
from .Other_Interfaces.Interface_sponsor import Widget_sponsor

from .Text_Extraction_Tool_Interface.Interface_RPG import Widget_RPG
from .Text_Extraction_Tool_Interface.Interface_export_source_text import Widget_export_source_text
from .Text_Extraction_Tool_Interface.Interface_import_translated_text import Widget_import_translated_text
from .Text_Extraction_Tool_Interface.Interface_update_text import Widget_update_text


class window(FramelessWindow): #主窗口 v


    def __init__(self,Software_Version,configurator,user_interface_prompter,background_executor,jtpp):
        super().__init__()
        # use dark theme mode
        self.setTitleBar(StandardTitleBar(self))

        self.hBoxLayout = QHBoxLayout(self)
        self.navigationInterface = NavigationInterface(self, showMenuButton=True)
        self.stackWidget = QStackedWidget(self)

        # 版本号
        self.Software_Version = Software_Version
        self.configurator = configurator
        self.user_interface_prompter = user_interface_prompter

        # 创建子界面控件，传入参数为对象名和parent
        self.Widget_AI = Widget_AI('Widget_AI', self)
        self.Widget_official_api = Widget_official_api('Widget_official_api', self)
        self.Widget_Openai = Widget_Openai('Widget_Openai', self,configurator,user_interface_prompter,background_executor)   
        self.Widget_Proxy = Widget_Proxy('Widget_Proxy', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Anthropic = Widget_Anthropic('Widget_Anthropic', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Google = Widget_Google('Widget_Google', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Cohere = Widget_Cohere('Widget_Cohere', self,configurator,user_interface_prompter,background_executor)
        self.Widget_ZhiPu = Widget_ZhiPu('Widget_ZhiPu', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Yi = Widget_Yi('Widget_Yi', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Moonshot = Widget_Moonshot('Widget_Moonshot', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Deepseek = Widget_Deepseek('Widget_Deepseek', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Dashscope = Widget_Dashscope('Widget_Dashscope', self,configurator,user_interface_prompter,background_executor)
        self.Widget_Volcengine = Widget_Volcengine('Widget_Volcengine', self,configurator,user_interface_prompter,background_executor)
        self.Widget_SakuraLLM = Widget_SakuraLLM('Widget_SakuraLLM', self,configurator,user_interface_prompter,background_executor)

        self.Widget_translation_settings = Widget_translation_settings('Widget_translation_settings', self)
        self.Widget_translation_settings_A = Widget_translation_settings_A('Widget_translation_settings_A', self,configurator,user_interface_prompter) 
        self.Widget_translation_settings_B1 = Widget_translation_settings_B1('Widget_translation_settings_B1', self,user_interface_prompter) 
        self.Widget_translation_settings_B2 = Widget_translation_settings_B2('Widget_translation_settings_B2', self,user_interface_prompter) 
        self.Widget_translation_settings_B3 = Widget_translation_settings_B3('Widget_translation_settings_B3', self,user_interface_prompter) 
        self.Widget_translation_settings_C = Widget_translation_settings_C('Widget_translation_settings_C', self,user_interface_prompter)  

        self.Widget_start_translation = Widget_start_translation('Widget_start_translation', self,configurator,user_interface_prompter,background_executor)  


        self.Widget_rulebook = Widget_rulebook('Widget_rulebook', self)
        self.Widget_system_prompt = Widget_system_prompt('Widget_system_prompt', self)  
        self.Widget_prompt_dict = Widget_prompt_dict('Widget_prompt_dict', self,configurator,user_interface_prompter)
        self.Widget_characterization = Widget_characterization('Widget_characterization', self) 
        self.Widget_world_building = Widget_world_building('Widget_world_building', self) 
        self.Widget_writing_style = Widget_writing_style('Widget_writing_style', self) 
        self.Widget_translation_example = Widget_translation_example('Widget_translation_example', self)  




        self.Widget_tune = Widget_tune('Widget_tune', self)
        self.Widget_tune_openai = Widget_tune_openai('Widget_tune_openai', self)
        self.Widget_tune_sakura = Widget_tune_sakura('Widget_tune_sakura', self)
        self.Widget_tune_anthropic = Widget_tune_anthropic('Widget_tune_anthropic', self)
        self.Widget_tune_google = Widget_tune_google('Widget_tune_google', self)

        self.Widget_sponsor = Widget_sponsor('Widget_sponsor', self,configurator = self.configurator)


        self.Widget_replace_dict = Widget_replace_dict('Widget_replace_dict', self,configurator,user_interface_prompter)


        self.Widget_RPG = Widget_RPG('Widget_RPG', self)  
        self.Widget_export_source_text = Widget_export_source_text('Widget_export_source_text', self,configurator,user_interface_prompter,jtpp)  
        self.Widget_import_translated_text = Widget_import_translated_text('Widget_import_translated_text', self,configurator,user_interface_prompter,jtpp)  
        self.Widget_update_text = Widget_update_text('Widget_update_text', self,configurator,user_interface_prompter,jtpp)   


        self.initLayout() #调用初始化布局函数 

        self.initNavigation()   #调用初始化导航栏函数

        self.initWindow()  #调用初始化窗口函数


    # 初始化布局的函数
    def initLayout(self):   
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)
        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    # 初始化导航栏的函数
    def initNavigation(self): # 详细介绍：https://pyqt-fluent-widgets.readthedocs.io/zh_CN/latest/navigation.html


 

        # 添加账号设置界面
        self.addSubInterface(self.Widget_AI, FIF.IOT, '账号设置',NavigationItemPosition.SCROLL) # NavigationItemPosition.SCROLL表示在可滚动伸缩区域
        # 添加官方接口界面
        self.addSubInterface(self.Widget_official_api, FIF.PEOPLE, '官方接口',parent=self.Widget_AI) # NavigationItemPosition.SCROLL表示在可滚动伸缩区域
        # 添加closeai官方账号界面
        self.addSubInterface(self.Widget_Openai, FIF.FEEDBACK, 'OpenAI官方',parent=self.Widget_official_api) 
        # 添加谷歌官方账号界面
        self.addSubInterface(self.Widget_Google, FIF.FEEDBACK, 'Google官方',parent=self.Widget_official_api)
        # 添加Cohere官方账号界面
        self.addSubInterface(self.Widget_Cohere, FIF.FEEDBACK, 'Cohere官方',parent=self.Widget_official_api)
        # 添加anthropic官方账号界面
        self.addSubInterface(self.Widget_Anthropic, FIF.FEEDBACK, 'Anthropic官方',parent=self.Widget_official_api)
        # 添加Moonshot官方账号界面
        self.addSubInterface(self.Widget_Moonshot, FIF.FEEDBACK, 'Moonshot官方',parent=self.Widget_official_api) 
        # 添加Deepseek官方账号界面
        self.addSubInterface(self.Widget_Deepseek, FIF.FEEDBACK, 'Deepseek官方',parent=self.Widget_official_api) 
        # 添加Dashscope官方账号界面
        self.addSubInterface(self.Widget_Dashscope, FIF.FEEDBACK, 'Dashscope官方',parent=self.Widget_official_api) 
        # 添加Volcengine官方账号界面
        self.addSubInterface(self.Widget_Volcengine, FIF.FEEDBACK, 'Volcengine官方',parent=self.Widget_official_api) 
        # 添加Yi官方账号界面
        self.addSubInterface(self.Widget_Yi, FIF.FEEDBACK, '零一万物官方',parent=self.Widget_official_api) 
        # 添加智谱官方账号界面
        self.addSubInterface(self.Widget_ZhiPu, FIF.FEEDBACK, '智谱官方',parent=self.Widget_official_api) 

        # 添加代理账号界面
        self.addSubInterface(self.Widget_Proxy, FIF.CLOUD, '代理平台',parent=self.Widget_AI) 
        # 添加sakura界面
        self.addSubInterface(self.Widget_SakuraLLM, FIF.CONNECT, 'SakuraLLM',parent=self.Widget_AI) 

        self.navigationInterface.addSeparator(NavigationItemPosition.SCROLL) # 添加分隔符

        # 添加翻译设置相关页面
        self.addSubInterface(self.Widget_translation_settings, FIF.APPLICATION, '翻译设置',NavigationItemPosition.SCROLL) 
        self.addSubInterface(self.Widget_translation_settings_A, FIF.REMOVE, '基础设置',parent=self.Widget_translation_settings) 
        self.addSubInterface(self.Widget_translation_settings_B1, FIF.ALIGNMENT, '发送设置',parent=self.Widget_translation_settings) 
        self.addSubInterface(self.Widget_translation_settings_B2, FIF.ALBUM, '专项设置',parent=self.Widget_translation_settings) 
        self.addSubInterface(self.Widget_translation_settings_B3, FIF.CHECKBOX, '检查设置',parent=self.Widget_translation_settings) 
        self.addSubInterface(self.Widget_translation_settings_C, FIF.EMOJI_TAB_SYMBOLS, '混合翻译设置',parent=self.Widget_translation_settings) 

        # 添加开始翻译页面
        self.addSubInterface(self.Widget_start_translation, FIF.ROBOT, '开始翻译',NavigationItemPosition.SCROLL)  

        self.navigationInterface.addSeparator(NavigationItemPosition.SCROLL) # 添加分隔符

        # 添加翻译设置相关页面
        self.addSubInterface(self.Widget_rulebook, FIF.BOOK_SHELF, '提示书',NavigationItemPosition.SCROLL) 
        self.addSubInterface(self.Widget_system_prompt, FIF.LABEL, '基础提示',parent=self.Widget_rulebook)
        self.addSubInterface(self.Widget_prompt_dict, FIF.DICTIONARY, '提示字典',parent=self.Widget_rulebook)   
        self.addSubInterface(self.Widget_characterization, FIF.EXPRESSIVE_INPUT_ENTRY, '角色介绍',parent=self.Widget_rulebook) 
        self.addSubInterface(self.Widget_world_building, FIF.QUICK_NOTE, '背景设定',parent=self.Widget_rulebook) 
        self.addSubInterface(self.Widget_writing_style, FIF.PENCIL_INK, '文风要求',parent=self.Widget_rulebook) 
        self.addSubInterface(self.Widget_translation_example, FIF.ZOOM, '翻译示例',parent=self.Widget_rulebook) 

        # 添加替换字典页面
        self.addSubInterface(self.Widget_replace_dict, FIF.DICTIONARY, '替换字典',NavigationItemPosition.SCROLL)  

        # 添加参数调整页面
        self.addSubInterface(self.Widget_tune, FIF.MIX_VOLUMES, '参数调整',NavigationItemPosition.SCROLL)  
        self.addSubInterface(self.Widget_tune_openai, FIF.SPEED_OFF, 'OpenAI',parent=self.Widget_tune)
        self.addSubInterface(self.Widget_tune_anthropic, FIF.SPEED_OFF, 'Anthropic',parent=self.Widget_tune)    
        self.addSubInterface(self.Widget_tune_sakura, FIF.SPEED_OFF, 'Sakura',parent=self.Widget_tune)  
        self.addSubInterface(self.Widget_tune_google, FIF.SPEED_OFF, 'Google',parent=self.Widget_tune)  

        self.navigationInterface.addSeparator(NavigationItemPosition.SCROLL)

        # 添加RPG界面
        self.addSubInterface(self.Widget_RPG, FIF.TILES, 'StevExtraction',NavigationItemPosition.SCROLL)
        self.addSubInterface(self.Widget_export_source_text, FIF.SHARE, '提取原文',parent=self.Widget_RPG)
        self.addSubInterface(self.Widget_import_translated_text, FIF.LABEL, '导入译文',parent=self.Widget_RPG)
        self.addSubInterface(self.Widget_update_text, FIF.PIE_SINGLE, '提取增量文本',parent=self.Widget_RPG)

        self.navigationInterface.addSeparator(NavigationItemPosition.SCROLL) 

        # 添加赞助页面
        self.addSubInterface(self.Widget_sponsor, FIF.CAFE, '赞助一下', NavigationItemPosition.BOTTOM) 

       # 添加头像导航项
        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=AvatarWidget(configurator = self.configurator),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM
        )

        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        self.stackWidget.setCurrentIndex(1)

    #初始化父窗口的函数
    def initWindow(self): 
        self.resize(1200 , 700)
        #self.setWindowIcon(QIcon('resource/logo.png'))
        self.setWindowTitle(self.Software_Version)
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        dir1 = os.path.join(self.configurator.resource_dir, "light")
        dir2 = os.path.join(dir1, "demo.qss")
        with open(dir2, encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    # 添加界面到导航栏布局函数
    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP, parent=None):
        """ add sub interface """
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text,
            parentRouteKey=parent.objectName() if parent else None
        )

    #切换到某个窗口的函数
    def switchTo(self, widget): 
        self.stackWidget.setCurrentWidget(widget) #设置堆栈窗口的当前窗口为widget

    #堆栈窗口的当前窗口改变时，调用的函数
    def onCurrentInterfaceChanged(self, index):    
        widget = self.stackWidget.widget(index)
        self.navigationInterface.setCurrentItem(widget.objectName())

    #头像导航项的函数调用的函数
    def showMessageBox(self):
        url = QUrl('https://github.com/NEKOparapa/AiNiee-chatgpt')
        QDesktopServices.openUrl(url)

    #窗口关闭函数，放在最后面，解决界面空白与窗口退出后子线程还在运行的问题
    def closeEvent(self, event):
        title = '确定是否退出程序?'
        content = """如果正在进行翻译任务，当前任务会停止。"""
        w = Dialog(title, content, self)

        if w.exec() :
            print("[INFO] 主窗口已经退出！")
            self.configurator.Running_status = 11
            event.accept()
        else:
            event.ignore()