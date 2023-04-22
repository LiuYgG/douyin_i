### 抖音达人邀约及达人资料爬取脚本

---
### 目录结构

---

```
    bases           【页面元素的封装】
    browser_install 【浏览器安装包】
    datas           【达人资料存储目录】
    drivers         【浏览器驱动】

### 脚本运行方式（界面待完善中…）

---

```
    1.安装 browser_install 文件夹下的 Chrome浏览器
    2.环境变量中添加 Chrome浏览器的文件目录路径
    3.启动方式
      a. windows 打开 cmd 窗口输入 chrome --remote-debugging-port=5247
         或直接运行目录下的【浏览器运行命令.bat】
    4.登录到抖音的达人广场
    5.选择好自己要找的达人类型后，运行 daren_sen_and_message.py 脚本进行达人信息的收集和邀约
    6.若有执行错误的情况，请自行修改脚本或联系本人进行脚本的修改…
