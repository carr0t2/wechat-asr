# WeChat-ASR
微信语音批量转文字  调用百度智能云短语音识别API 目前仅支持安卓手机+Windows

## 下载请前往 https://github.com/carr0t2/wechat-asr/releases
## 简介
最近线上办公，很多小会议或者讲座等也在微信群里，有时需要记录保存会议讲话内容，也可能为了节省时间，转成文字后快速浏览即可了解会议大致内容。

总之，微信自带的语音转文字虽然方便，但是面对多次的大量语音的时候一个一个点还是太麻烦了。用这个工具，第一次使用稍微有些麻烦，但是以后使用的时候还是会比较方便的。

## 原理
从手机（只写了安卓系统）找到文件夹，按时间提取需要识别的语音（还需要人工操作）

因为微信语音限制在60s，正好和百度asr限制一样，故不存在截取，准确性更高

用`silk_v3_decoder` 将微信的`.amr`文件转码`.pcm`文件

用百度智能云语音识别的API接口（需要申请账号）

生成txt，带顺序时间标志

## 运行环境
个人Windows 10+安卓手机可用
## 详细使用方法(文字版)
1. 前往页面下载最新软件 https://github.com/carr0t2/wechat-asr/releases

   (里面有图片版教程)

2. 解压

3. 从手机取出语音文件

   1. 手机连接电脑，并打开传输文件模式
   2. 依次访问`\内部存储\tencent\MicroMsg\******************************\voice2`
   3. 详细信息查看方式，并按时间排序
   4. 选中需要转码时间段的文件夹(建议从会议起始时间开始，到现在为止的文件夹全部选中)，复制粘贴到电脑

4. 连接

5. 筛选出需要的文件

   1. 在电脑上的新文件夹里，在右上的搜索为止搜索`.amr`
   2. 全选文件，复制粘贴到新文件夹

6. 申请 百度智能云 API Key 和 Secret Key

   1. 搜索打开网站 或者 https://cloud.baidu.com/
   2. 左上方 产品->人工智能->语音技术->语音识别
   3. 左边中间位  立即使用
   4. 登陆 使用百度账号即可，可能需要手机验证
   5. 左边中间位置  创建应用
   6. 应用名称 应用类型 随便选，接口不用管，语音包名 不需要，应用描述随便写  点击创建
   7. 创建完毕后 中间位置点击查看应用详情
   8. 可以看到 API Key 和 Secret Key，这两个很重要，每次使用都要填入，建议保存在程序目录里的一个txt里

7. 打开软件(不要管那个黑框框)

8. 填入5里申请的 API Key 和 Secret Key 并连接

9. 点击 '选择 .amr 文件'，打开 4.b 里保存到的文件夹，选中会议时间的文件

10. 可选 选择保存位置及名称

11. 开始识别 （因为还不会写多线程，所以程序运行中一直假死，程序运行过程中不要动软件，等到完成时会有弹窗提示）

12. 识别结束打开文件

13. 推荐到word编辑，页面布局为窄，当修订校对完成后，用查找替换删除时间点 要开启通配符模式 “\{[0123456789_.pcm]{26,31}\}” （最好保存下以免出现问题）

14. 程序如果出现闪退等情况提交issue，常见解决方法(只能先凑合)在下载的文件中有
## 已知问题
2. 菜单栏点击反胃有误
3. 没有多线程，程序假死
5. python打包程序还是有点大
6. 单元格不能复制，
7. 程序太丑，没有美化等
8. 从手机中提取出录音文件对于大部分人来说难度还是偏大，第一次上手难度高
9. 个人代码水平太低
## 后记
1. 最初是因为朋友有需求写的，但是没有做图形化界面。后来想着学学吧，就挖坑写了，不过也学了不少东西
2. 应该也有许多人会用到吧，想着慢慢也升级一下，支持从手机直接读取录音文件？支持苹果设备等等，不过还不确定，如果有需求，那我就写写
