# -*- coding: utf-8 -*-
### v0.1
### 学学玩的，有啥改进地方多提提
import sys
import json
import base64
import time
import os
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
timer = time.perf_counter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem,QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(980, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setStyleSheet("background-color:rgb(255, 185, 185);")
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.service_choice_radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.service_choice_radioButton.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.service_choice_radioButton.setFont(font)
        self.service_choice_radioButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.service_choice_radioButton.setChecked(True)
        self.service_choice_radioButton.setObjectName("service_choice_radioButton")
        self.horizontalLayout_5.addWidget(self.service_choice_radioButton)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.apikey_label = QtWidgets.QLabel(self.groupBox)
        self.apikey_label.setObjectName("apikey_label")
        self.horizontalLayout.addWidget(self.apikey_label)
        self.apikey_edit = QtWidgets.QLineEdit(self.groupBox)
        self.apikey_edit.setObjectName("apikey_edit")
        self.horizontalLayout.addWidget(self.apikey_edit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.secretkey_label = QtWidgets.QLabel(self.groupBox)
        self.secretkey_label.setObjectName("secretkey_label")
        self.horizontalLayout_2.addWidget(self.secretkey_label)
        self.secretkey_edit = QtWidgets.QLineEdit(self.groupBox)
        self.secretkey_edit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.secretkey_edit.setInputMask("")
        self.secretkey_edit.setText("")
        self.secretkey_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.secretkey_edit.setObjectName("secretkey_edit")
        self.horizontalLayout_2.addWidget(self.secretkey_edit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.connection_button = QtWidgets.QPushButton(self.groupBox)
        self.connection_button.setMinimumSize(QtCore.QSize(0, 40))
        self.connection_button.setObjectName("connection_button")
        self.horizontalLayout_4.addWidget(self.connection_button)
        self.connection_status_label = QtWidgets.QLabel(self.groupBox)
        self.connection_status_label.setObjectName("connection_status_label")
        self.horizontalLayout_4.addWidget(self.connection_status_label)
        self.voice_language_combobox = QtWidgets.QComboBox(self.groupBox)
        self.voice_language_combobox.setMinimumSize(QtCore.QSize(0, 25))
        self.voice_language_combobox.setObjectName("voice_language_combobox")
        self.voice_language_combobox.addItem("")
        self.voice_language_combobox.addItem("")
        self.voice_language_combobox.addItem("")
        self.voice_language_combobox.addItem("")
        self.voice_language_combobox.addItem("")
        self.horizontalLayout_4.addWidget(self.voice_language_combobox)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tableView = QtWidgets.QTableView(self.splitter)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.tableView_2 = QtWidgets.QTableView(self.splitter)
        self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_input_dir_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.open_input_dir_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.open_input_dir_pushButton.setObjectName("open_input_dir_pushButton")
        self.horizontalLayout_3.addWidget(self.open_input_dir_pushButton)
        self.choose_save_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.choose_save_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.choose_save_pushButton.setObjectName("choose_save_pushButton")
        self.horizontalLayout_3.addWidget(self.choose_save_pushButton)
        self.begin_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.begin_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.begin_pushButton.setObjectName("begin_pushButton")
        self.horizontalLayout_3.addWidget(self.begin_pushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 980, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_key = QtWidgets.QAction(MainWindow)
        self.action_key.setObjectName("action_key")
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.service_choice_radioButton.setToolTip(_translate("MainWindow", "目前只支持百度智能云，看需求添加腾讯云、阿里云、华为云等等"))
        self.service_choice_radioButton.setStatusTip(_translate("MainWindow", "目前只支持百度智能云，看需求添加腾讯云、阿里云、华为云等等"))
        self.service_choice_radioButton.setText(_translate("MainWindow", "百度智能云"))
        self.apikey_label.setToolTip(_translate("MainWindow", "请填入在百度智能云里申请的应用API Key"))
        self.apikey_label.setStatusTip(_translate("MainWindow", "请填入在百度智能云里申请的应用API Key"))
        self.apikey_label.setText(_translate("MainWindow", "API Key:    "))
        self.apikey_edit.setToolTip(_translate("MainWindow", "请填入在百度智能云里申请的应用API Key"))
        self.apikey_edit.setStatusTip(_translate("MainWindow", "请填入在百度智能云里申请的应用API Key"))
        self.apikey_edit.setPlaceholderText(_translate("MainWindow", "请填入在百度智能云里申请的应用API Key"))
        self.secretkey_label.setToolTip(_translate("MainWindow", "请填入在百度智能云里申请的应用Secret Key"))
        self.secretkey_label.setStatusTip(_translate("MainWindow", "请填入在百度智能云里申请的应用Secret Key"))
        self.secretkey_label.setText(_translate("MainWindow", "Secret Key: "))
        self.secretkey_edit.setToolTip(_translate("MainWindow", "请填入在百度智能云里申请的应用Secret Key"))
        self.secretkey_edit.setStatusTip(_translate("MainWindow", "请填入在百度智能云里申请的应用Secret Key"))
        self.secretkey_edit.setPlaceholderText(_translate("MainWindow", "请填入在百度智能云里申请的应用Secret Key"))
        self.connection_button.setToolTip(_translate("MainWindow", "连接至百度智能云"))
        self.connection_button.setStatusTip(_translate("MainWindow", "连接至百度智能云"))
        self.connection_button.setText(_translate("MainWindow", "连接"))
        self.connection_status_label.setText(_translate("MainWindow", "<b>连接失败</b>"))
        self.voice_language_combobox.setToolTip(_translate("MainWindow", "默认选择普通话"))
        self.voice_language_combobox.setStatusTip(_translate("MainWindow", "默认选择普通话"))
        self.voice_language_combobox.setItemText(0, _translate("MainWindow", "普通话"))
        self.voice_language_combobox.setItemText(1, _translate("MainWindow", "英语"))
        self.voice_language_combobox.setItemText(2, _translate("MainWindow", "粤语"))
        self.voice_language_combobox.setItemText(3, _translate("MainWindow", "四川话"))
        self.voice_language_combobox.setItemText(4, _translate("MainWindow", "普通话远场"))
        self.tableView.setToolTip(_translate("MainWindow", "待转换的文件"))
        self.tableView.setStatusTip(_translate("MainWindow", "待转换的文件"))
        self.tableView_2.setToolTip(_translate("MainWindow", "转换完的文件及情况"))
        self.tableView_2.setStatusTip(_translate("MainWindow", "转换完的文件及情况"))
        self.open_input_dir_pushButton.setToolTip(_translate("MainWindow", "选择 .amr 文件"))
        self.open_input_dir_pushButton.setStatusTip(_translate("MainWindow", "选择 .amr 文件"))
        self.open_input_dir_pushButton.setText(_translate("MainWindow", "选择 .amr 文件"))
        self.choose_save_pushButton.setToolTip(_translate("MainWindow", "选择txt文件的保存位置"))
        self.choose_save_pushButton.setStatusTip(_translate("MainWindow", "选择txt文件的保存位置"))
        self.choose_save_pushButton.setText(_translate("MainWindow", "选择保存位置(默认当前目录)"))
        self.begin_pushButton.setToolTip(_translate("MainWindow", "开始识别,程序还不完善,在运行过程中可能假死,请耐心等待"))
        self.begin_pushButton.setStatusTip(_translate("MainWindow", "开始识别,程序还不完善,在运行过程中可能假死,请耐心等待"))
        self.begin_pushButton.setText(_translate("MainWindow", "开始识别"))
        self.menu_2.setTitle(_translate("MainWindow", "使用说明"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.menu.setTitle(_translate("MainWindow", "捐助"))
        self.menu_4.setTitle(_translate("MainWindow", "反馈"))
        self.menu_5.setTitle(_translate("MainWindow", "官网"))


class wechatasr(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(wechatasr, self).__init__(parent)
        self.setupUi(self)
        self.token = ''
        self.secret_key = ''
        self.api_key = ''
        self.save_file_path = ''
        self.save_pcm_path = ''
        self.files_number = 0
        self.pcm_files_number = 0
        self.todofiletable = QStandardItemModel(self.files_number, 3)
        self.changefiletable = QStandardItemModel(self.files_number, 2)

        self.connection_button.clicked.connect(self.connecttobaidu)
        self.open_input_dir_pushButton.clicked.connect(self.opendir)
        self.choose_save_pushButton.clicked.connect(self.choose_save_file)
        self.begin_pushButton.clicked.connect(self.begin)

    def connecttobaidu(self):
        self.api_key = self.apikey_edit.text()
        self.secret_key = self.secretkey_edit.text()
        if self.api_key == '' or self.secret_key == '':
            QMessageBox.warning(self, u'连接失败', u"请输入 <b>API Key</b> 和 <b>Secret Key</b>  ")
        else:
            status, self.token = self.fetch_token()  # 0是网络连接失败 1是API key错误 2 是成功并返回token
            if status == 0:
                self.groupBox.setStyleSheet('background-color:rgb(255, 185, 185);')
                QMessageBox.warning(self, u'连接失败', u"网络连接失败\n请检查网络是否连接")
            elif status == 1:
                self.groupBox.setStyleSheet('background-color:rgb(255, 185, 185);')
                QMessageBox.warning(self, u'连接失败', u"API Key或Secret Key错误，连接失败")
            elif status == 2:
                self.groupBox.setStyleSheet('background-color:rgb(222, 255, 222);')
                self.connection_status_label.setText('<b>连接成功</b>')
            else:
                self.groupBox.setStyleSheet('background-color:rgb(255, 185, 185);')
                QMessageBox.warning(self, u'连接失败', u"未知错误")
            #QMessageBox.warning(self, u'连接失败', self.voice_language_combobox.currentText())

    def fetch_token(self):
        try:
            SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有
            TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
            API_KEY = self.api_key
            SECRET_KEY = self.secret_key
            params = {'grant_type': 'client_credentials',
                      'client_id': API_KEY,
                      'client_secret': SECRET_KEY}
            post_data = urlencode(params)
            post_data = post_data.encode('utf-8')
            req = Request(TOKEN_URL, post_data)
            try:
                f = urlopen(req)
                result_str = f.read()
            except URLError as err:
                if err.code == 401:
                    return 1, ''
                else:
                    return 0, ' '  # 0是网络连接失败 1是API key错误 2 是成功并返回token
            result_str = result_str.decode()
            if len(result_str) == 0:
                return 0, ' '  # 0是网络连接失败 1是API key错误 2 是成功并返回token
            result = json.loads(result_str)
            if ('access_token' in result.keys() and 'scope' in result.keys()):
                if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
                    return 1, ' '
                return 2, result['access_token']
            else:
                return 1, ' '
                # raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')
        except:
            return -1, ' '

    def opendir(self):
        self.progressBar.setValue(0)
        timeArray = time.localtime(time.time())
        time_now = time.strftime("%Y%m%d%H%M%S", timeArray)
        self.save_file_path = './'+'result_'+time_now+'.txt'
        self.save_pcm_path='./'+'pcm_'+time_now
        files, ok1 = QFileDialog.getOpenFileNames(self, "请选择amr文件", "./", "ALL Files (*.*)")
        if len(files) != 0:
            self.files_number = len(files)
            self.todofiletable = QStandardItemModel(self.files_number, 3)
            self.todofiletable.setHorizontalHeaderLabels(['名称', '修改日期', '大小'])
            count = 0
            for todofile in files:
                finfo = os.stat(todofile)
                info = QStandardItem(todofile)
                self.todofiletable.setItem(count, 0, info)
                timeArray = time.localtime(finfo.st_mtime)
                nametime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)
                info = QStandardItem(nametime)
                self.todofiletable.setItem(count, 1, info)
                self.todofiletable.item(count, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                info = QStandardItem(str(format(finfo.st_size // 8 / 1024, '.1f')) + 'KB')
                self.todofiletable.setItem(count, 2, info)
                self.todofiletable.item(count, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                count += 1
            self.todofiletable.sort(1, 0)
            self.tableView.setModel(self.todofiletable)
            self.tableView.setColumnWidth(0, 200)
            self.tableView.resizeColumnToContents(1)
            self.tableView.resizeColumnToContents(2)

    def choose_save_file(self):
        print(self.save_file_path)
        timeArray = time.localtime(time.time())
        time_now = time.strftime("%Y%m%d%H%M%S", timeArray)
        self.save_file_path, ok2 = QFileDialog.getSaveFileName(self, "文件保存", "./" + "result_" + time_now,
                                                               "Text Files (*.txt)")
        if self.save_file_path == '':
            timeArray = time.localtime(time.time())
            time_now = time.strftime("%Y%m%d%H%M%S", timeArray)
            self.save_file_path = './'+'result_'+time_now+'.txt'

    def begin(self):
        if self.token == '':
            QMessageBox.warning(self, u'识别失败', u"还没有连接至百度智能云")
            return
        elif self.files_number == 0:
            QMessageBox.warning(self, u'识别失败', u"还没有添加文件")
            return
        try:
            os.mkdir(self.save_pcm_path)
        except:
            QMessageBox.warning(self, u'创建目录失败', u"创建目录失败")
            return
        self.changefiletable = QStandardItemModel(self.files_number, 2)
        self.changefiletable.setHorizontalHeaderLabels(['名称', '状态'])
        self.tableView_2.setModel(self.changefiletable)
        self.changefiletable.sort(0, 0)
        for i in range(0,self.files_number):

            self.progressBar.setValue(int(i/self.files_number*100))
            QApplication.processEvents()
            time.sleep(0.3)
            QApplication.processEvents()
            doing_file=self.save_pcm_path+'/'+  \
                        str(i+1).zfill(len(str(self.files_number)))+ '__' + \
                        str(self.todofiletable.item(i,1).text()).replace('/','_').replace(':','_').replace(' ','_')+'.pcm'
            commandstring= ' silk_v3_decoder.exe ' + ' "' +\
                        str(self.todofiletable.item(i,0).text()) + '" "' + \
                        doing_file + \
                        '" ' + \
                        ' -Fs_API 16000 '
            try:
                res = os.popen(commandstring)
                result = res.read()
                QApplication.processEvents()
                #print(commandstring)
                #print(result)
            except:
                QMessageBox.warning(self, u'未知错误', u"未知错误\n请检查<b>silk_v3_decoder.exe</b>\n是否在当前目录下")
                return
            if result is None:
                QMessageBox.warning(self, u'未找到程序', u"未找到程序\n请检查<b>silk_v3_decoder.exe</b>\n是否在当前目录下")
                return
            else:
                if 'Decoding Finished' not in result:
                    QMessageBox.warning(self, u'音频文件可能出现了错误', u"音频文件可能出现了错误\n请检查文件"+\
                                        str(self.todofiletable.item(i,0).text())+"\n"\
                                        "该文件将跳过"+\
                                        "\n")
                    info = QStandardItem(doing_file[(doing_file).rfind('/')+1:])
                    self.changefiletable.setItem(i, 0, info)
                    info = QStandardItem('转码失败')
                    self.changefiletable.setItem(i, 1, info)
                    self.changefiletable.item(i,0).setBackground(QColor(255, 185, 185))
                    self.changefiletable .item(i,1).setBackground(QColor(255, 185, 185))
                    self.tableView_2.resizeColumnToContents(0)
                    self.tableView_2.resizeColumnToContents(1)
                    continue
                self.tableView_2.resizeColumnToContents(0)
                self.tableView_2.resizeColumnToContents(1)
                info = QStandardItem(doing_file[(doing_file).rfind('/')+1:])
                self.changefiletable.setItem(i, 0, info)
                info = QStandardItem('正在处理')
                self.changefiletable.setItem(i, 1, info)
                status,mess=self.upload_asr(doing_file)
                if status==2:
                    info = QStandardItem('识别成功')
                    self.changefiletable.setItem(i, 1, info)
                else:
                    if status==1:
                        info = QStandardItem('http错误'+mess)
                    else:
                        info = QStandardItem('失败')
                    self.changefiletable.setItem(i, 1, info)
                    self.changefiletable.item(i,0).setBackground(QColor(255, 185, 185))
                    self.changefiletable .item(i,1).setBackground(QColor(255, 185, 185))


    def upload_asr(self,up_file):
        FORMAT = 'pcm'  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
        CUID = 'Carr0t2'
        RATE = 16000  # 固定值# 采样率
        DEV_PID = 1537  # 1537 表示识别普通话，使用输入法模型。根据文档填写PID，选择语言及识别模型
        ASR_URL = 'http://vop.baidu.com/server_api'
        AUDIO_FILE=up_file
        speech_data = []
        with open(AUDIO_FILE, 'rb') as speech_file:
            speech_data = speech_file.read()
        length = len(speech_data)
        if length == 0:
            QMessageBox.warning(self, u'未知错误', u"未知错误\n请检查"+up_file+"是否有误")
            return 0,''
        speech = base64.b64encode(speech_data)
        speech = str(speech, 'utf-8')
        params = {'dev_pid': DEV_PID,
                  'format': FORMAT,
                  'rate': RATE,
                  'token': self.token,
                  'cuid': CUID,
                  'channel': 1,
                  'speech': speech,
                  'len': length
                  }
        post_data = json.dumps(params, sort_keys=False)
        req = Request(ASR_URL, post_data.encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        QApplication.processEvents()
        try:
            begin = timer()
            f = urlopen(req)
            result_str = f.read()
            #print ("Request time cost %f" % (timer() - begin))
        except URLError as err:
            QMessageBox.warning(self, u'请求错误', u"请求错误\n请尝试重新连接，检查网络，重启软件\n"+'asr http response http code : ' + str(err.code))
            return 1,str(err.code)
        result_str = str(result_str, 'utf-8')
        QApplication.processEvents()
        with open(self.save_file_path,"a") as of:
            result_dict=eval(result_str)
            #result_dict["time"]=name
            #of.write(str(result_dict)+'\n')
            of.write('{'+up_file[(up_file).rfind('/')+1:]+'}'+'\n')
            try:
                of.write(str(result_dict["result"])[2:-2]+'\n\n')
            except:
                of.write('Error'+'\n')
            return 2,''



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = wechatasr()
    ui.show()
    sys.exit(app.exec_())
