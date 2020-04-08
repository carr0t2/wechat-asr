# -*- coding: utf-8 -*-
# 学学玩的，有啥改进地方多提提

import sys
import json
import base64
import time
import os
import traceback
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QMainWindow, QMessageBox, QFileDialog, \
    QApplication, QAbstractItemView, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor, QIcon, QDesktopServices


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 750)
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
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
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
        self.menubar = MyMenu(MainWindow)  #重载成自己的menu
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
        MainWindow.setWindowTitle(_translate("MainWindow", "微信语音批量转文字"))
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
        self.voice_language_combobox.setItemText(0, _translate("MainWindow", "普通话(有标点)"))
        self.voice_language_combobox.setItemText(1, _translate("MainWindow", "英语(无标点)"))
        self.voice_language_combobox.setItemText(2, _translate("MainWindow", "粤语(有标点)"))
        self.voice_language_combobox.setItemText(3, _translate("MainWindow", "四川话(有标点)"))
        self.voice_language_combobox.setItemText(4, _translate("MainWindow", "普通话远场(有标点)"))
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


class WechatASR(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(WechatASR, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('asr_icon.png'))
        self.token = ''  # 百度智能云的token，用两个key fetch_token方法获得
        self.secret_key = ''  # 百度智能云的token 用户输入内容
        self.api_key = ''  # 百度智能云的token 用户输入内容
        self.save_file_path = ''  # 识别结果的保存位置，默认生成在当前目录，以"result"开头，加时间的txt文件
        self.save_pcm_path = ''  # amr文件转码后文件的保存位置 在当前目录生成pcm开头，加时间的文件夹
        self.open_file_path = './'
        self.files_number = 0
        self.pcm_files_number = 0
        self.todo_file_table = QStandardItemModel(self.files_number, 3)  # 左半边的table，存放待处理的文件
        self.doing_file_table = QStandardItemModel(self.files_number, 2)  # 右边的table，显示文件的名称及状态

        self.connection_button.clicked.connect(self.connecttobaidu)
        self.open_input_dir_pushButton.clicked.connect(self.open_dir)
        self.choose_save_pushButton.clicked.connect(self.choose_save_file)
        self.begin_pushButton.clicked.connect(self.begin)
        self.website_label = QLabel("程序还不完善，可能会出现卡顿、闪退的情况，请控制识别数量(最好200以下)，并耐心等待"
                                    "  <a href='https://github.com/carr0t2/wechat-asr'>有问题请来这里反馈</a>")
        self.website_label.setOpenExternalLinks(True)
        self.statusbar.addPermanentWidget(self.website_label, stretch=0)

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
            # QMessageBox.warning(self, u'连接失败', self.voice_language_combobox.currentText())

    def fetch_token(self):
        try:
            scope = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有
            token_url = 'http://openapi.baidu.com/oauth/2.0/token'
            api_key = self.api_key
            secret_key = self.secret_key
            params = {'grant_type': 'client_credentials',
                      'client_id': api_key,
                      'client_secret': secret_key}
            post_data = urlencode(params)
            post_data = post_data.encode('utf-8')
            req = Request(token_url, post_data)
            try:
                f = urlopen(req)
                result_str = f.read()
            except URLError as err:  # 下面内容根据官方demo修改，具体不太懂，但是做返回就可以了
                if err.code == 401:
                    return 1, ''
                else:
                    return 0, ' '  # 0是网络连接失败 1是API key错误 2 是成功并返回token
            result_str = result_str.decode()
            if len(result_str) == 0:
                return 0, ' '  # 0是网络连接失败 1是API key错误 2 是成功并返回token
            result = json.loads(result_str)
            if 'access_token' in result.keys() and 'scope' in result.keys():
                if scope and (not scope in result['scope'].split(' ')):  # scope = False 忽略检查
                    return 1, ' '
                return 2, result['access_token']
            else:
                return 1, ' '
                # raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')
        except:
            return -1, ' '

    def open_dir(self):  # 将用户选择的文件显示在table上，显示修改时间，大小
        self.progressBar.setValue(0)
        time_array = time.localtime(time.time())
        time_now = time.strftime("%Y%m%d%H%M%S", time_array)
        self.save_file_path = './' + 'result_' + time_now + '.txt'
        self.save_pcm_path = './' + 'pcm_' + time_now
        files, ok1 = QFileDialog.getOpenFileNames(self, "请选择amr文件", self.open_file_path, "AMR Files (*.amr)")
        if len(files) != 0:
            self.open_file_path = files[0][:str(files[0]).rfind('/')]
            self.files_number = len(files)
            self.todo_file_table = QStandardItemModel(self.files_number, 3)
            self.todo_file_table.setHorizontalHeaderLabels(['名称', '修改日期', '大小'])
            count = 0
            for todo_file in files:
                f_info = os.stat(todo_file)
                info = QStandardItem(todo_file)
                self.todo_file_table.setItem(count, 0, info)
                time_array = time.localtime(f_info.st_mtime)
                file_mtime = time.strftime("%Y/%m/%d %H:%M:%S", time_array)
                info = QStandardItem(file_mtime)
                self.todo_file_table.setItem(count, 1, info)
                self.todo_file_table.item(count, 1).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                info = QStandardItem(str(format(f_info.st_size / 1024, '.1f')) + 'KB')
                self.todo_file_table.setItem(count, 2, info)
                self.todo_file_table.item(count, 2).setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                count += 1
            self.todo_file_table.sort(1, 0)  # 升序
            self.tableView.setModel(self.todo_file_table)
            self.tableView.setColumnWidth(0, 200)
            self.tableView.resizeColumnToContents(1)
            self.tableView.resizeColumnToContents(2)

    def choose_save_file(self):  # 用户自己选择文件保存的位置
        # print(self.save_file_path)
        time_array = time.localtime(time.time())
        time_now = time.strftime("%Y%m%d%H%M%S", time_array)
        self.save_file_path, ok2 = QFileDialog.getSaveFileName(self, "文件保存", "./" + "result_" + time_now,
                                                               "Text Files (*.txt)")
        if self.save_file_path == '':
            time_array = time.localtime(time.time())
            time_now = time.strftime("%Y%m%d%H%M%S", time_array)
            self.save_file_path = './' + 'result_' + time_now + '.txt'

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
            QMessageBox.warning(self, u'创建目录失败', u"创建目录失败\n请尝试重新添加文件再识别")
            return
        self.setDisabled(True)
        self.doing_file_table = QStandardItemModel(self.files_number, 2)
        self.doing_file_table.setHorizontalHeaderLabels(['名称', '状态'])
        self.tableView_2.setModel(self.doing_file_table)
        self.doing_file_table.sort(0, 0)  # 升序
        for i in range(0, self.files_number):
            self.progressBar.setValue(int(i / self.files_number * 100))
            doing_file = self.save_pcm_path + '/' + \
                str(i + 1).zfill(len(str(self.files_number))) + '__' + \
                str(self.todo_file_table.item(i, 1).text()).\
                replace('/', '_').replace(':', '_').replace(' ', "_") + \
                '.pcm'
            command_string = '"' + os.getcwd() + '/' \
                'silk_v3_decoder.exe"' + ' "' + \
                str(self.todo_file_table.item(i, 0).text()) + '" "' + \
                doing_file + \
                '" ' + \
                ' -Fs_API 16000 '
            try:
                res = os.popen(command_string)
                result = res.read()
                QApplication.processEvents()
                # print(command_string)
            except Exception as e:
                print(command_string)
                print('str(e):\t\t', str(e))
                print('repr(e):\t', repr(e))
                print('e.message:\t', e.message)
                print('traceback.print_exc():'+ traceback.print_exc())
                print('traceback.format_exc():\n%s' % traceback.format_exc())
                QMessageBox.warning(self, u'未知错误', u"未知错误\n请检查silk_v3_decoder.exe\n是否在当前目录下")
                self.setDisabled(False)
                return
            if result == '':
                QMessageBox.warning(self, u'未找到程序', u"未找到程序\n请检查silk_v3_decoder.exe\n是否在当前目录下")
                self.setDisabled(False)
                return
            else:
                info = QStandardItem(doing_file[doing_file.rfind('/') + 1:])
                self.doing_file_table.setItem(i, 0, info)
                if 'Decoding Finished' not in result:
                    QMessageBox.warning(self, u'音频文件可能出现了错误', u"音频文件可能出现了错误\n请检查文件" +
                                        str(self.todo_file_table.item(i, 0).text()) + "\n" +
                                        "该文件将跳过" +
                                        "\n")
                    info = QStandardItem('转码失败')
                    self.doing_file_table.setItem(i, 1, info)
                    self.doing_file_table.item(i, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.doing_file_table.item(i, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.doing_file_table.item(i, 0).setBackground(QColor(255, 185, 185))
                    self.doing_file_table.item(i, 1).setBackground(QColor(255, 185, 185))
                    continue
                info = QStandardItem('正在处理')
                self.doing_file_table.setItem(i, 1, info)
                self.doing_file_table.item(i, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.doing_file_table.item(i, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                status, mess = self.upload_asr(doing_file)  # 上传
                if status == 2:
                    info = QStandardItem('识别成功')
                    self.doing_file_table.setItem(i, 1, info)
                    print("成功"+doing_file)
                else:
                    if status == 1:
                        info = QStandardItem('http错误' + mess)
                    else:
                        info = QStandardItem('失败')
                    self.doing_file_table.setItem(i, 1, info)
                    self.doing_file_table.item(i, 0).setBackground(QColor(255, 185, 185))
                    self.doing_file_table.item(i, 1).setBackground(QColor(255, 185, 185))
            self.doing_file_table.item(i, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.doing_file_table.item(i, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            QApplication.processEvents()
            time.sleep(0.3)
            QApplication.processEvents()
            self.tableView_2.scrollToBottom()
        self.setDisabled(False)
        self.progressBar.setValue(100)
        reply = QMessageBox.question(self, '识别完成', "是否打开识别结果文件", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(self.save_file_path))

    def upload_asr(self, up_file):  # 修改了官方的demo
        dev_pid_dict = {"普通话(有标点)": 1537,
                        "英语(无标点)": 1737,
                        "粤语(有标点)": 1637,
                        "四川话(有标点)": 1837,
                        "普通话远场(有标点)": 1936
                        }
        file_format = 'pcm'  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
        cuid = self.api_key
        rate = 16000  # 固定值# 采样率
        dev_pid = dev_pid_dict[self.voice_language_combobox.currentText()]  # 1537 表示识别普通话，使用输入法模型。根据文档填写PID，选择语言及识别模型
        asr_url = 'http://vop.baidu.com/server_api'
        audio_file = up_file
        speech_data = []
        with open(audio_file, 'rb') as speech_file:
            speech_data = speech_file.read()
        length = len(speech_data)
        if length == 0:
            QMessageBox.warning(self, u'未知错误', u"未知错误\n请检查" + up_file + "是否有误")
            return 0, ''
        speech = base64.b64encode(speech_data)
        speech = str(speech, 'utf-8')
        params = {'dev_pid': dev_pid,
                  'format': file_format,
                  'rate': rate,
                  'token': self.token,
                  'cuid': cuid,
                  'channel': 1,
                  'speech': speech,
                  'len': length
                  }
        post_data = json.dumps(params, sort_keys=False)
        req = Request(asr_url, post_data.encode('utf-8'))
        req.add_header('Content-Type', 'application/json')
        QApplication.processEvents()
        try:
            # begin = timer()
            f = urlopen(req)
            result_str = f.read()
            # print ("Request time cost %f" % (timer() - begin))
        except URLError as err:
            print(result_str)
            QMessageBox.warning(self, u'请求错误',
                                u"请求错误\n请尝试重新连接，检查网络，重启软件\n" +
                                'asr http response http code : ' +
                                str(err.code))
            return 1, str(err.code)
        result_str = str(result_str, 'utf-8')
        QApplication.processEvents()
        with open(self.save_file_path, "a") as of:
            result_dict = eval(result_str)
            # result_dict["time"]=name
            # of.write(str(result_dict)+'\n')
            of.write('{' + up_file[up_file.rfind('/') + 1:] + '}' + '\n')
            try:
                of.write(str(result_dict["result"])[2:-2] + '\n\n')
            except:
                of.write('Error' + '\n')
            return 2, ''


class MyMenu(QtWidgets.QMenuBar):

    def __init__(self, parent=None):
        QtWidgets.QMenuBar.__init__(self)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        QDesktopServices.openUrl(QtCore.QUrl('https://github.com/carr0t2/wechat-asr'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = WechatASR()
    ui.show()
    sys.exit(app.exec_())
